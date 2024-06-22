#!/bin/bash

# Management and deployment script for returnsuite-website.
# Each environment must be setup as defined in `returnsuite_app/docs/hosting`.
# Running the command without arguments will output the usage.
# All stage and prod commands will only operate connected to the VPN.

# The following entries must exist in `~/.ssh/config`.
# Host returnsuite-prod-app-1
#  HostName <internal_ip>
#  User ubuntu
#  IdentityFile ~/.ssh/returnsuite-prod-app.pem
#
# Host returnsuite-stage-app
#  HostName <internal_ip>
#  User ubuntu
#  IdentityFile ~/.ssh/returnsuite-stage-app.pem
#

# The following entries must exist in `~/.my.cnf`.
# [client-returnsuite-stage-website]
# user=<user>
# password=<password>
# host=<host>
#
# [client-returnsuite-prod-website]
# user=<user>
# password=<password>
# host=<host>
#

# Calculate the directory of the script, even if called from another script.
# Reference: https://stackoverflow.com/questions/59895/
SOURCE="${BASH_SOURCE[0]}"
while [[ -h "$SOURCE" ]]; do
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ ${SOURCE} != /* ]] && SOURCE="$DIR/$SOURCE"
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

dump_date=$(date +"%Y-%m-%d_%H-%M-%S")
backup_dir="${DIR}/backup"

# Optionally override the backup directory.
if [[ -n ${RETURNSUITE_BACKUP_DIR} ]]; then
  backup_dir=${RETURNSUITE_BACKUP_DIR}
fi

# Test for the VPN connection by attempting to connect to an instance.
function test_reachability {
  if ! ssh -o PubkeyAuthentication=no \
      -o PasswordAuthentication=no \
      -o KbdInteractiveAuthentication=no \
      -o ChallengeResponseAuthentication=no \
      -o BatchMode=yes \
      -o ConnectTimeout=2 \
      "$1" 2>&1 | grep -q "Permission denied"; then
    echo "You must connect to the VPN prior to issuing this command."
    exit 101
  fi
}

function help_message {
cat << EOF
usage:
  $0 help
  $0 format
  $0 lint
  $0 test
  $0 build
  $0 clean
  $0 cloc

  $0 local server
  $0 local tailwind
  $0 local livereload
  $0 local smtpd
  $0 local ngrok

  $0 stage backup
  $0 stage deploy
  $0 stage tail

  $0 prod backup
  $0 prod deploy
  $0 prod tail

EOF
}

case "$*" in
  "help")
    help_message
    ;;

  "format")
    cd "${DIR}" || exit 2
    poetry run isort .
    poetry run black .
    ;;

  "lint")
    cd "${DIR}" || exit 2
    poetry run flake8
    ;;

  "test")
    cd "${DIR}" || exit 2
    poetry run pytest
    ;;

  "build")
    poetry --directory="${DIR}" build -f wheel
    ;;

  "clean")
    rm -rf "${DIR}/dist"
    rm -rf "${DIR}/.pytest_cache"
    ;;

  "cloc")
    cloc "${DIR}/src" --exclude-ext=css,csv,svg,yml --exclude-dir=lib,migration
    ;;

  "local server")
    cd "${DIR}" || exit 2
    poetry run server
    ;;

  "local tailwind")
    cd "${DIR}" || exit 2
    # Install with `npm install -g tailwindcss`.
    npx tailwindcss \
      -c ./docs/development/css/tailwind.config.js \
      -i ./docs/development/css/input.css \
      -o ./src/returnsuite/resources/css/styles.css \
      --watch
    ;;

  "local livereload")
    cd "${DIR}" || exit 2
    poetry run livereload --host=0.0.0.0
    ;;

  "local smtpd")
    cd "${DIR}" || exit 2
    poetry run aiosmtpd -n -d -l localhost:1025
    ;;

  "local ngrok")
    ngrok http localhost:8000
    ;;

  "stage backup")
    test_reachability "returnsuite-stage-app"
    mkdir -p "${backup_dir}"
    source="returnsuite-stage-app:/srv/project/stage.returnsuite.com/stage.env"
    destination="${backup_dir}/${dump_date}_returnsuite_stage.env"
    if [[ ! $(scp "$source" "${destination}") ]]; then
      echo "Backed up stage env to '${destination}'."
    fi
    destination="${backup_dir}/${dump_date}_returnsuite_stage.sql.gz"
    if [[ ! $(mysqldump --defaults-group-suffix=-returnsuite-stage --single-transaction -q -v returnsuite-stage | gzip > "${destination}") ]]; then
      echo "Backed up stage database to '${destination}'."
    fi
    ;;

  "stage deploy")
    test_reachability "returnsuite-stage-app"
    poetry --directory="${DIR}" build -f wheel
    latest_version=$(poetry version -s)
    latest_file="returnsuite-${latest_version}-py3-none-any.whl"
    from="${DIR}/dist/${latest_file}"
    rsync "$from" returnsuite-stage-app:/srv/project/stage.returnsuite.com/
    echo "The deployment ends in a tail command. Press 'control+c' to exit."
    # shellcheck disable=SC2029  # Expansion must occur on the client side.
    ssh returnsuite-stage-app \
      "cd /srv/project/stage.returnsuite.com/ &&
       source /srv/venv/stage.returnsuite.com/bin/activate &&
       pip install ${latest_file} --force-reinstall &&
       deactivate &&
       sudo systemctl reload gunicorn &&
       journalctl -xefu gunicorn"
    ;;

  "stage tail")
    test_reachability "returnsuite-stage-app"
    ssh returnsuite-stage-app "journalctl -xefu gunicorn"
    ;;

  "prod backup")
    test_reachability "returnsuite-prod-app-1"
    mkdir -p "${backup_dir}"
    source="returnsuite-prod-app-1:/srv/project/returnsuite.com/prod.env"
    destination="${backup_dir}/${dump_date}_returnsuite_prod_1.env"
    if [[ ! $(scp "${source}" "${destination}") ]]; then
      echo "Backed up prod env to '${destination}'."
    fi
    destination="${backup_dir}/${dump_date}_returnsuite_prod.sql.gz"
    if [[ ! $(mysqldump --defaults-group-suffix=-returnsuite-prod --single-transaction -q -v returnsuite-prod | gzip > "${destination}") ]]; then
      echo "Backed up prod database to '${destination}'."
    fi
    ;;

  "prod deploy")
    read -r -p "Are you sure you want to proceed? (yes/no) " yn
    case $yn in
      yes) ;;
      *) echo "Exiting..."; exit ;;
    esac
    test_reachability "returnsuite-prod-app-1"
    poetry --directory="${DIR}" build -f wheel
    latest_version=$(poetry version -s)
    latest_file="returnsuite-${latest_version}-py3-none-any.whl"
    from="${DIR}/dist/${latest_file}"
    rsync "$from" returnsuite-prod-app-1:/srv/project/returnsuite.com/
    echo "The deployment ends in a tail command. Press 'control+c' to exit."
    # shellcheck disable=SC2029  # Expansion must occur on the client side.
    ssh returnsuite-prod-app-1 \
      "cd /srv/project/returnsuite.com/ &&
       source /srv/venv/returnsuite.com/bin/activate &&
       pip install ${latest_file} --force-reinstall &&
       deactivate &&
       sudo systemctl reload gunicorn &&
       journalctl -xefu gunicorn"
    ;;

  "prod tail")
    test_reachability "returnsuite-prod-app-1"
    ssh returnsuite-prod-app-1 "journalctl -xefu gunicorn"
    ;;

  *)
    help_message
    exit 22
esac

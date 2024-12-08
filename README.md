# returnsuite-website

The landing website for [ReturnSuite](https://returnsuite.com). Contains product
information, contact, terms, privacy, blog, course and documentation.


## Getting started

The application supports development on all operating systems where Python,
Poetry and the system's dependencies will run. The deployment and management
scripts run on Linux and macOS.

Install the equivalent prerequisites below. On macOS, installing with
[Homebrew](https://brew.sh) is recommended.

- mariadb (Optional)
- poetry


Install the system dependencies on macOS.

```shell
brew install mariadb poetry
# (Optional) Run as a service.
brew services start mariadb
# (Optional) Run directly.
/opt/homebrew/opt/mariadb/bin/mariadbd-safe --datadir\=/opt/homebrew/var/mysql
```

(Optional) Create a database where records are stored. (Defaults to sqlite if not present)

```shell
mysql -e 'CREATE DATABASE `returnsuite-website-local` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;'
```

Install the dependencies.

```shell
poetry update
```

Install the current project so poetry can find the module.

```shell
poetry install
```

Write the local config file. Add any secret key-values as necessary.

```shell
cat <<'EOF'>> ./.env
app_env=dev
signup_enabled=true

# (Optional) Database connector if not using sqlite.
database_url=mysql+mysqlconnector://root:<password>>@127.0.0.1:3306/returnsuite-website-local
EOF
```

Run the local development server. In development mode, sample data will be
loaded into the system for testing on the initial run.

```shell
poetry run server
```

(Optional) In a separate shell, enable the livereload server to reload the page
as changes are made to the source.

```shell
poetry run livereload
```

(Optional) In a separate shell, enable the tailwind server to update the css as
changes are made to the source.

```shell
./website.sh local tailwind
```

Open a browser to the landing page.

```shell
open localhost:8000
```


## Development

### Adding a blog post

1) Preparing the assets
   1) Create an image directory for the post at `resources/img/yyyy-MM-dd`.
   2) Copy the images and related assets as lossless files to the directory.
      Suffix them as `-original`.
   3) Run the images through a compression tool to webm unless they are a `.gif`
      or `.svg`. A great tool is [Squoosh.app](https://squoosh.app/editor). Set
      compression to `WebP`, effort to max (6) and quality to 75%. The
      compressed images should not have the `-original` suffix.
2) Creating the post
   1) Copy a similar post from `templates/blog` to a new file and name
      accordingly.
   2) Update the content and image urls to the added files.
3) Create the post metadata
   1) Add a new record to `routes/posts.json` for the new blog post.
4) Check the website and content by running the `main` python file.
5) Run all tests to ensure the images load. Right click `tests` and press run.
6) If everything passes, commit the changes to the main branch in version
   control.

Note*: Be careful using third party widgets (iframes) as they may break GDPR
compliance.


### Updating landing page images

The landing page images are generated via html+css at `/landing-images`. Editing
the javascript allows screenshots to be downloaded for use on the landing page.


### SEO, accessibility, security and performance checks

Test the pages using [PageSpeed Insights](https://pagespeed.web.dev). The
website should pass with minimal warnings and a high performance score in all
categories (green).


### GDPR Compliance check

Perform a site wide GDPR compliance check using [2GDPR](https://2gdpr.com/).
This should pass cleanly if the site isin accordance with the EU's General Data
Protection Regulation. This is required because the site offers its services
to EU members.

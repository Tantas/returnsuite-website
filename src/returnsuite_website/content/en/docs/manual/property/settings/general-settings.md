---
title: General Property Settings
description: Configure settings and run actions to tailor the experience to your needs
nav-title: General Settings
nav-group: Configure property settings
---

# General Property Settings

## Configure settings and run actions to tailor the experience to your needs

General property settings include the modules activated on the property and any
rarely used actions. Changes made here will configure many user experience
settings and some components behind the scenes. All changes can be reverted
unless otherwise noted.


### Change history preferences

Change history preferences control how the system will record the paper-trail of
changes. These settings start with reasonable defaults but can be overridden to
your preferences.

<figure>
  <div class="flex place-items-center justify-center p-2 md:p-6 bg-gray-100 rounded-md max-w-prose border border-gray-200 shadow-sm">
    <img src="/img/docs/property-settings-change-history.png" alt="Screenshot of property change history settings">
  </div>
  <figcaption>Screenshot of property change history settings</figcaption>
</figure>


#### Note-taking preferences

Adding notes when saving a property creates a paper trail that can be referred
to. While this is useful for team members and when returning to a project after
a break, it can be annoying.

Options allow for the notes to be disabled, made option or required. By default,
the save note will default to the last change when it was performed by the same
user in a short period of time to save time.


#### Merge consecutive changes

Changes made in a short period of time by the sae user will be merged to create
an easier to follow change history. This will limit the ability to revert
changes and is disabled by default.


#### Allow saving from a previous version

To prevent changes from being clobbered, by default, ReturnSuite only allows
changes to be saved on the latest version of a property. This restriction can be
lifted by enabling this feature. Be warned that this may cause unintended side
effects when two people are working on the same property simultaneously. It may
create change history challenging to follow.


### Enable features

Enabling features turns on various modules for the property, such as actuals,
insights and change history. These can be disabled to reduce unused component
clutter and increase privacy as needed.

<figure>
  <div class="flex place-items-center justify-center p-2 md:p-6 bg-gray-100 rounded-md max-w-prose border border-gray-200 shadow-sm">
    <div class="bg-white p-4 border border-gray-300 rounded-md">
      <img src="/img/docs/property-settings-enable-features.png" alt="Screenshot of property enable features">
    </div>
  </div>
  <figcaption>Screenshot of property enable features</figcaption>
</figure>


#### Maps integration

Enabling the maps integration allows geocoding the property when entering the
property location and allowing some reports to place the property on a map.

This integration makes third-party API calls. Only the minimum information
required to operate is sent (address, latitude, longitude). This is enabled by
default but can be disabled for privacy concerns.


### Actions

Most property actions cannot be reverted. Please be certain before confirming
any operation. The records are immediately deleted from the system and cannot be
recovered by the ReturnSuite team.

<figure>
  <div class="flex place-items-center justify-center p-2 md:p-6 bg-gray-100 rounded-md max-w-prose border border-gray-200 shadow-sm">
    <div class="bg-white p-4 border border-gray-300 rounded-md">
      <img src="/img/docs/property-settings-actions.png" alt="Screenshot of property actions">
    </div>
  </div>
  <figcaption>Screenshot of property actions</figcaption>
</figure>

#### Unlock sample to a paid property

Sample properties have restrictions preventing their repurposing. Unlocking the
sample to a paid property will remove these restrictions. This may be useful
when repurposing a sample that is similar to a property you are trying to model.

Only the property owner and team members with sufficient permissions can perform
this action. Billing will start on the property. Billing information is required
and will be prompted if not already on file.

This option is only shown when viewing a sample property.


#### Flatten change history

Flattening the change history will remove all previous versions of the model,
preventing viewing old changes.

Only the property owner and team members with sufficient permissions can perform
this action. A confirmation dialog will require you to enter the full name of
the property to ensure this action was intended.


#### Archive the property

Archiving the property will halt new billing on the property but leave the
records in the system. Archived properties cannot be searched, viewed or edited
until they have unarchived.

Once an account has created a non-sample property, the account will be billed
for at least one property each billing cycle. To stop billing completely, you
must delete your user account, no questions asked.

Only the property owner and team members with sufficient permissions can perform
this action. A confirmation dialog will require you to enter the full name of
the property to ensure this action was intended.


#### Delete the property

Deleting the property will halt new billing on the property. The records are
immediately deleted from the system and cannot be recovered by the ReturnSuite
team.

Once an account has created a non-sample property, the account will be billed
for at least one property each billing cycle. To stop billing completely, you
must delete your user account, no questions asked.

Only the property owner and team members with sufficient permissions can perform
this action. A confirmation dialog will require you to enter the full name of
the property to ensure this action was intended.

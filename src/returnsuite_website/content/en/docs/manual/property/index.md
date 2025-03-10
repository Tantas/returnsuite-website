---
title: TODO - ReturnSuite Docs
description: TODO - Add a description
nav-title: Overview
nav-group: Property
---

# Property Overview

## Navigating around the property and viewing the property dashboard

When first navigating to a property in ReturnSuite, the property overview will
be displayed showing its identification information, listing details and
high-level cash flow information.

Everytime you navigate to a property, it will be added to the top of your
recently viewed properties on the recent activity page.

<figure>
  <div class="flex place-items-center justify-center p-2 bg-gray-100 rounded-md border border-gray-200">
    <img src="/img/docs/property-overview.png" alt="Screenshot showing the property overview">
  </div>
  <figcaption>Screenshot showing the property overview</figcaption>
</figure>


### Navigating around the property

A menu bar at the top of the overview allows for quick navigation to each of the
property's components. Hovering on a menu item will expand to show a submenu of
its contents.


#### Changing property details

The property details section contains identification information, the property's
location, and listing details. No information in this section contributes to
any calculated report results.

#### Updating the model

All model inputs are added in this section. All options found using the quick
start when creating a model will be found here along with many more options to
fine-tune. The majority of time in the property will likely be spent in this
section.

#### Running reports

Provides a list of all reports that can be viewed for the property. Reports that
have been added to your favorite list will be added to the top of the menu items
for quick access.

#### Configure property settings

This menu option provides access to general settings, administrative actions and
integrations for the property.

#### Duplicating

Duplicating the property will clone the property and all of its information,
including version history to a new property. Selecting duplicate will open a
modal view before performing the operation. Duplicating a property will update
the number of properties on file to be billed on each billing period.

<figure>
  <div class="flex place-items-center justify-center p-6 bg-gray-100 max-w-prose rounded-md border border-gray-200">
    <img src="/img/docs/property-overview-duplicate-modal.png" alt="Screenshot showing the property duplicate modal">
  </div>
  <figcaption>Screenshot showing the property duplicate modal</figcaption>
</figure>


##### Modal options:

Account
:   The account the property will be cloned into. Only your personal account and
    organization accounts in which you have permission are selectable options.

Duplicate property name:
:   A required, new name of the duplicated property. This name can be the same
    if it is being moved to a different account.

Include property change history
:   Selected by default, this copies all change history from the source
    property. Deselecting will only copy the latest version.

Sample properties have some restrictions to prevent repurposing. This option is
not present on sample properties until it has been unlocked to a paid property
in property settings.


#### Bookmarking

Bookmarking a property will make it appear in a special search filter on the
property list view for the user who bookmarked, allowing quick navigation.
Bookmarks are private to your account and are useful when you are routinely
navigating between many properties.


### Viewing the dashboard

The dashboard contains a high-level overview of the property, with various cards
of information depending on available property information and the user and
property's configuration.


#### Property listing details

The card on the left of the screenshot contains the property location, listing
information and the calculated occupancy data from the model at the time of
viewing. The listing details they were saved in the listing details form.


#### High-level cash flow report

This card displays a column chart of either the property's net operating income
or cash available for distribution by the selected period. Hovering on a column
will display relevant details for the period.

The NOI statement to the right is the operating activity calculated from market
for a year from the start of the viewing period.


#### Changing the viewing period

Controls on the bottom of the overview page display what overview report's
analysis period and viewing window. The analysis period is configured in the
model -> analysis period.  When an analysis period has not been configured, the
analysis will start at the start of the next month and run for ten years.

The viewing period controls the viewing start, the duration of the viewing
window and the currency presentation scale. These controls change display
elements on the report if they apply to the sections. All card dates will be
updated on change to reflect the selected viewing period.

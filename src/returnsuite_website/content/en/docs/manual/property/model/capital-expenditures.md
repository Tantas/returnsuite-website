---
title: Capital Expenditures
description: Adding expenditures to improve the property and combat depreciation
nav-title: Capital expenditures
nav-group: Updating the model
---

# Capital Expenditures

## Adding expenditures to improve the property and combat depreciation

Capital expenditures (CapEx) are major cash outlays used to improve or maintain
properties that are expected to generate value over an extended period,
typically more than one year. In real estate, CapEx not only includes physical
upgrades to the property but also investments that enhance its economic value
and revenue-generating capacity.


### Adding an expenditure

Add expenditures that exist for the property by selecting the "Add capital
expenditure" button at the bottom of the expenditure list. It is possible to
stack expenditures and use a similar naming convention to represent
complex cash flows that cannot be described using the provided fields.

Collapsing an expenditure will show a high-level description of its attributes.
Expenditures must be expanded to edit.

Capital expenditures can be removed using the trash icon on the top right of
each entry and can be reordered using the scrubber on the top left. The order of
expenditures is the order they will appear in reports.


#### Expenditure name

The name as it will appear for selection in the model and reports. It must be
unique and should be short and descriptive, ideally describing its function.


#### Vendor identification

An optional identifier that can be used to group cash flows when reporting.


#### Expenditure description

An optional, longer description of the expenditure providing further identification
or the source of information.


#### Expenditure type

Determines how the expenditures should be input. Any amount or rate should be
entered as the maximum expected amount.

An inflation schedule should be selected to adjust the expenditure to reflect
the value of the currency in the future.

##### Expenditure types:

One-Time Amount
:   The expenditure will be collected only once. Variability cannot be chosen.
    The amount will be paid on a specific date or over a period of time.

Amount per Recurrence
:   The specified amount will be paid on each occurrence of the payment
    frequency.

Amount per Month / Year
:   The specified amount will be prorated to the payment frequency. The rate
    will be prorated by the payment frequency using the Actual/Actual day count
    convention.

Amount per Rentable Area per Month / Year
:   The specified rate will be calculated against the property's rentable area
    and prorated to the payment frequency. The rate will be prorated by the
    payment frequency using the Actual/Actual day count convention.

---


### One-time expenditure

Expenditures input as one-time events are not affected by any variability. While
the event occurs only once, payments can be spread over a schedule as is common
for large outflows.


#### Paid on

The date or dates a one-time expenditure is paid.

##### Paid on options:

Specific Date
:   The date the full amount is paid.

Payment Schedule
:   A schedule of partial payments and their dates specific to the one-time
    event.

Property Acquisition
:   The date the property is acquired. If the purchase date is not specified in
    the model, then the analysis start is used.

Property Disposal
:   The date the property is disposed. If the disposal date is not specified in
    the model, then the analysis end is used as it is implicitly assumed to be
    the reversion date.

Analysis Start
:   The first day of the analysis period. This is not recommended because it is
    possible to unintentionally move the expected date when overriding the
    analysis period in reports and portfolios.

Analysis End
:   The last day of the analysis period. This is not recommended because it is
    possible to unintentionally move the expected date when overriding the
    analysis period in reports and portfolios.


#### Recoverability

Expenditures when recovered, are generally agreed upon separately in a leasing
agreement via a one-time contribution. Despite this, it could be possible that
an ongoing capital improvement is considered recoverable similar to operating
expenses.

This could have an unintended effect on leases with base-year-stop recovery
agreements by inflating or hiding the true leasing holding fees. This option
should only be used with a great deal of caution and understanding.

---


### Recurring expenditures

Capital expenditures input as recurring events require a duration and payment
frequency. Variability can adjust a percentage of the expense in relation to the
occupancy of the property.


#### Variability

Determines how the expenditure source should vary to the property's occupancy.
Any amount or rate should be entered as the maximum expected amount.

##### Variability options:

Fixed
:   The amount will not vary.

Percentage Occupied
:   A percentage of the amount will correlate directly with the property's
    occupancy percentage.

Percentage Unoccupied
:   A percentage of the amount will correlate directly with one minus the
    property's occupancy percentage.


#### Recoverability

Expenditures when recovered, are generally agreed upon separately in a leasing
agreement via a one-time contribution. Despite this, it could be possible that
an ongoing capital improvement is considered recoverable similar to operating
expenses.

This could have an unintended effect on leases with base-year-stop recovery
agreements by inflating or hiding the true leasing holding fees. This option
should only be used with a great deal of caution and understanding.


#### Expenditure start

The date the expenditure begins. The first payment will be made on the selected
payment frequency after the expenditure start date. No proration will occur in
regard to the initial period.

##### Start options:

Specific Date
:   Begins on the specified date. This anchors the expense to a specific point
    in time. Changing your analysis period or acquisition date will not change
    the start of the expense.

Property Acquisition
:   Begins on the property acquisition date of the analysis start date when a
    purchase date has not been specified.

Analysis Start
:   Begins on the analysis start date.


#### Expenditure end

Defines when the expenditure will stop. No proration will occur in regard to the
duration of the end period.

##### End options:

Specific Date
:   Ends on the specified date. Changing your analysis period or disposal date
    will not change the end of the expense.

Property Disposal
:   Ends on the property disposal date or analysis end when it has not been
    specified.

Analysis End
:   Ends on the analysis end date.


#### Payment frequency

The frequency that the expenditure is paid to the vendor.

##### Frequency options:

Yearly / Semiyearly / Quarterly
:   The payments will be aligned to the selected month and day of month.

Every Two Months / Monthly
:   The payments will be aligned to the selected day of the month.

Semimonthly
:   The payments will recur on the two dates of the month. Both payments will be
    equal amounts regardless of the span between them (ex. 1st and 15th in a
    month with 31 days.)

Every Two Weeks / Weekly
:   The payments will be aligned to the selected day of the week. Amounts
    entered as rates will be prorated using the Actual/Actual day-count
    convention. This means that a yearly rate will produce differing payment
    amounts when weekly frequency is selected and the number of weeks in the
    year is either 52 or 53. If this does not reflect the agreement, it is
    recommended that amounts paid weekly or every two weeks are entered as
    amount per recurrence.

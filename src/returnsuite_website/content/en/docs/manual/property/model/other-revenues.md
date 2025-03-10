---
title: Other Revenues - ReturnSuite Docs
description: Modeling revenues that are not directly associated with leased spaces.
nav-title: Other revenues
nav-group: Updating the model
---

# Other Revenues

## Modeling revenues that are not directly associated with leased spaces

Other revenues include all the other sources of property income such as parking,
signage, vending machines and events. These revenues are not part of the main
lease but may be indirectly driven by tenants. As a result, other revenues are
part of the calculation making up potential gross income.


### Adding other revenues

Add sources of revenue for that exist in the property. Add a revenue source by
selecting the "Add other revenue" button. It is possible to stack revenue
sources and use a similar naming convention to represent complex revenues that
cannot be described using the provided fields.

Collapsing a revenue will show a high-level description of its attributes.
Revenues must be expanded to edit.

Other revenues can be removed using the trash icon on the top right of each
entry and can be reordered using the scrubber on the top left. The order of the
revenues is the order they will appear in reports.

#### Revenue name

The name as it will appear for selection in the model and reports. It must be
unique and should be short and descriptive, ideally describing its source.


#### Customer identification

An optional identifier that can be used to group cash flows when reporting.


#### Revenue description

An optional, longer description of the revenue providing further identification
or the source of information.


#### Revenue type

The revenue type determines how the revenues should be recorded. It must be
input assuming the property is fully occupied to variate correctly with the
occupancy of the property.

An inflation schedule should be selected to adjust the revenues to reflect the
value of the currency in the future.

##### Type options:

One-Time Amount
:   The revenue will be collected only once. Variability cannot be chosen.
    The amount will be paid on a specific date or over a period of time.

Amount per Year
:   The specified amount will be prorated to the payment frequency. The rate
    will be prorated by the payment frequency using the Actual/Actual day
    count convention.

Amount per Month
:   The specified amount will be prorated to the payment frequency. The rate
    will be annualized by the calculation engine and prorated by the payment
    frequency using the Actual/Actual day count convention.

Amount per Recurrence
:   The specified amount will be collected for each occurrence of the payment
    frequency.

---


### One-time amount

Revenues input as one-time events are not affected by any variability. While the
event occurs only once, payment can be spread over a schedule.


#### Paid on

The date or dates a one-time revenue is paid.

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

---


### Recurring amounts

Revenues input as recurring events require a duration and payment frequency.
Variability can adjust a percentage of the expense in relation to the occupancy
of the property.


#### Variability

Determines how the revenue source should vary to the property's occupancy.
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


#### Revenue start

The date the revenue begins. The first payment will be made on the selected
payment frequency after the revenue start date. No proration will occur in
regard to the initial period.

##### Start options:

Specific Date
:   Begins on the specified date. This anchors the revenue to a specific point
    in time. Changing your analysis period or acquisition date will not change
    the start of the revenue.

Property Acquisition
:   Begins on the property acquisition date of the analysis start date when a
    purchase date has not been specified.

Analysis Start
:   Begins on the analysis start date.


#### Revenue end

Defines when the revenue will stop. No proration will occur in regard to the
duration of the end period.

##### End options:

Specific Date
:   Ends on the specified date. Changing your analysis period or disposal date
    will not change the end of the revenue.

Property Disposal
:   Ends on the property disposal date or analysis end when it has not been
    specified.

Analysis End
:   Ends on the analysis end date.


#### Payment frequency

The frequency that the revenue is received from the customer.

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

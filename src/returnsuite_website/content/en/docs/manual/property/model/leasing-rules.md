---
title: Leasing Rules - ReturnSuite Docs
description: How to input spaces and uses into a ReturnSuite property model.
nav-title: Leasing rules
nav-group: Updating the model
---

# Leasing Rules

## How to forecast how spaces are used when uses end

Leasing rules are the expected rates, terms and conditions that future
leasing activity is expected to follow. As tenant turnover creates
vacancies, the leasing rules forcast replacement uses like the popular
video game Tetris – with projected leases dropping down from the top of
the screen to fill in the gaps caused by vacancies.

In any given period of time, the existing and forecasted lease revenues
can be summed together to create the projected cashflows of a property.

<figure>
  <div class="flex place-items-center justify-center p-6 bg-gray-100 rounded-md border border-gray-200">
    <img src="/img/docs/property-model-leasing-rules.png" alt="Screenshot showing the property leasing rules input">
  </div>
  <figcaption>Screenshot showing the property leasing rules input</figcaption>
</figure>

Leasing rules are a key element to building a financial model. Without
them, once contracted leases expire, they will remain vacant for the
remainder of the analysis period.

### Defining a leasing rule

A leasing rule should be defined to represent the market use of each area you
earn revenue. They should reflect the types of revenues found in the property's
current lease agreements and reflect the market rents for the area assuming the
space was leased immediately.

#### Leasing rule name

The name as it will appear for selection in the model and reports. It must
be unique and should be short and descriptive, ideally describing its
use case.

Examples include "Market Conditions," "Small Offices" or "Exterior Access."

#### Leasing rule type

Defines the type of use that will be forecast into a space during periods it is
contractually unoccupied.

Traditional Lease
: Commercial leases typical in the office and industrial subsector.

Retail Lease
: Similar to commercial leases with the addition of percentage rent
  paid on a percentage of the tenant's sales.

#### Leasing rule description

An optional, longer description of the leasing rule to further clarify its
use or the reference of its parameters.

For example, "Smaller offices that share common elements with
other offices on their floor and carry higher rent."

### Market parameters

A leasing rule is made up market parameters that are used to forecast a lease
agreement's details when a space becomes unoccupied. These parameters are used
to determine the performance of a usage compared to the market. These values are
used to calculate the market rent, potential base rent and absorption and
turnover vacancy, appearing on many reports.

These parameters may be the same or unique depending on if the forecasted tenant
renews their lease or a new lease is forecast. This is commonly used to apply
reduced rates and leasing costs to renewals, reflecting the property owner's
savings. Selecting 'Use distinct market parameters' when enable both to be input
separately. The new lease parameters are always chosen for market calculations
when distinct parameters are input for both new and renewed leases.

#### Time to lease

The amount of time the space will remain vacant before a new lease
will be forecasted. It is recommended to align the lease start to the
first of a period to produce more realistic cashflows.

Years / Months
: The duration in years or months as a decimal. A non-integer value will cause
  the calculated date to be divided using the Actual/Actual day-count
  convention.

Weeks / Days
: The duration in weeks or days as an integer.

Immediately
: There is no vacant period. The new lease begins the day after the previous
  ends.

##### Starts on

A forecasted lease can begin immediately after the time to lease has elapsed or
be rounded to the beginning of a month. This is used to better reflect reality
and simplify reports by aligning rents to the start of a reporting period.

First of Next Month (rounded forward)
: The new lease begins on the first day of the following month. This is selected
  by default and is recommended.

Exact Date
: The new lease begins the day after the time to lease.

First of Month (rounded back)
: The new lease begins on the first day of the month that the new lease is
  scheduled to start.

#### Lease duration

The length of time the lease will be active before the next leasing event caused
by the tenant moving out or renewing for a second term.

Years / Months
: The duration in years or months as a decimal. A non-integer value will cause
  the calculated date to be divided using the Actual/Actual day-count
  convention.

Weeks / Days
: The duration in weeks or days as an integer.

#### Upon expiry

This defines what is expected to happen after the end date of a forecasted
lease. The forecasting engine will use this to determine if a new lease should
be forecast, renewed or do nothing when remain vacant is chosen.

Market
: The forecasted tenant will not be renewing their lease. A replacement lease
  will be forecast using the same leasing rules when the time to lease has
  elapsed.

Renew
: The forecasted tenant will have some likelihood of renewing their lease. The
  likelihood of renewal must be entered as the percentage chance they will sign
  a new lease. 100% signifies that a renewal is guaranteed. The lease renewal
  will have its duration prorated by the likelihood percentage, and its
  parameters prorated by the renewal parameters during traditional analysis.

Remain Vacant
: The forecasted tenant will not be renewing their lease. No lease will be
  forecast when the lease ends. This option might be chosen if the property
  owner intends to repurpose or combine the space with another and therefore
  doesn’t want to model a new long-term lease. Effectively, a lease will be
  forecast only once.


#### Renewal duration

The renewal duration is required when the forecasted lease is set to renew and
defines the length of the new term. The model will prorate the lease duration
and parameters by the likelihood of renewal when performing a traditional
analysis.

It is recommended that the renewal duration type match the lease duration type.

Years / Months
: The duration in years or months as a decimal. A non-integer value will cause
  the calculated date to be divided using the Actual/Actual day-count
  convention.

Weeks / Days
: The duration in weeks or days as an integer.


### Base rent

#### Fixed base rent

#### Step base rent

### Concessions

#### Free rent period

### Additional rent

#### CPI increases

#### Expense recoveries

### Leasing costs

#### Leasing commissions

#### TI allowance

#### Incentives

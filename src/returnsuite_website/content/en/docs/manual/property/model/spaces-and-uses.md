---
title: Spaces and Uses - ReturnSuite Docs
description: How to input spaces and uses into a ReturnSuite property model.
nav-title: Spaces and Uses
nav-group: Model
---

# Spaces and Uses

## Spaces

Spaces define the different physical areas of a property depending on the
structural use of the property. These could be by unit, floor, building,
lot, etc.

- Space name
  : The name as it will appear for selection in the model and reports.
    The name should be short, descriptive and unique, ideally matching the
    name of the space as it appears in reality.<br><br>
    For example, "100," "Suite 100," "Floor 100" or "Building 3A."

- Leasable area
  : The size of the space in the area unit of the model. All uses will be the
    size of the space unless manually overridden.<br><br>
    This value must be accurate for expenses, capital expenditures and other
    revenues to be correctly calculated and for recoverable amounts to be
    allocated.

- Availability scope
  : The period of time the space is available and exists in its current form.
    Restricting the scope is used to describe physical changes to the
    property, such as adding an addition or merging and dividing spaces.
    <br><br>
    The gross leasable area at any given point in time is calculated as
    the sum of all leasable areas with available scope.

    - Always Available (None)
    : The space exists for the entire duration the property is owned.

    - Until Date (end)
    : The space is available from property acquisition until the specified
      date. Any use exceeding this date will automatically be cut short
      during calculations.

    - After Date (start)
    : The space is available as of the specified date until the property
      disposal. A forecasting rule's time to lease begins on this date.

    - Date Range (start) (end)
    : The space is available during the specified date range. A forecasting
      rule's time to lease begins on this date. Any lease ending outside the
      period will automatically be cut short during calculations.


- Leasing rule
: Determines the market rent rate and how leases are forecast. A leasing
  rule is strongly recommended on all spaces for the most complete reporting
  data, even when the space is used for non-traditional lease types.
  <br><br>
  When a lease rule is selected, adding a use to the space will copy the lease
  parameters automatically to speed entry since they should reflect the going
  market rate
  <br><br>
  Leases will not be forecast when a leasing rule is not selected. The
  market rate will be the same as the occupied use rate and go to zero
  when the space becomes unoccupied.


## Uses

Several usage types exist for traditional leases:

Traditional Lease
:   Commercial leases typical in the office and industrial subsector.

Retail Lease
:   Similar to commercial leases with the addition of percentage rent
    paid on a percentage of the tenant's sales.

Vacant Period
:   A known period when the space is unavailable for use. The space is
    still included in all calculations impacted by the gross leasable area
    such as occupancy and recovery allocation but will prevent leases
    from being forecast into the space. The leasing rule's forecasted
    time to lease will begin from the date the space becomes available.

### Traditional Lease

#### Tenant Identification

  - Source
  : The source of the lease agreement that is shown in reports. This is
    important for lenders, so they can understand what revenues have been
    contracted and what revenues are being speculated. Additionally, a source of
    <b>Forecasted</b> may be seen in reports
    signifying a lease was forcast via the space's associated leasing rule.

    - Contracted
    : A lease has been signed. The details entered match the exact terms of
      the lease agreement.

    - Speculated
    : A lease has not been signed, but is expected to be soon.
      All lease details are known with a relatively high level of certainty.

    - Forecasted
    : A lease added by from the space's leasing rule by the forecasting engine
      when the model is executed. This is not selectable but will likely appear
      in reports.


    - Tenant name
    : The name of the tenant as it appears on the lease agreement.
      Reports aggregated by usage and tenant specific reports will show these
      names.

#### Lease timing

  - Use start
  : The inclusive date the use begins. If the use is defined by an agreement,
  it should be entered as it appears on the agreement, regardless of the
  model's analysis period.

  - Use end
  : The inclusive date the use ends. If the use is defined by an agreement,
    it should be entered as it appears on the agreement, regardless of the
    model's analysis period. A lease renewal should be entered as a new lease
    to signify both the renewal and to allow the terms to be updated.

  - Upon expiry
  : Defines what is expected to happen when the lease terminates. If this is
    the final usage, the forecasting engine will use this value to decide if
    a new lease should be forecast, renewed or do nothing when remain vacant
    is chosen.

    - Market
    : The tenant will not be renewing their lease. A replacement lease will
      be forecast using the space's associated leasing rule parameters
      after the time to lease has elapsed.

    - Renew
    : The tenant will have some likelihood of renewing their lease. The
      likelihood of renewal must be entered as the percentage chance they
      will sign a new lease. 100% signifies that a renewal is guaranteed.
      The lease renewal will have its duration prorated by the likelihood
      percentage, and its parameters prorated to the space's leasing rule's
      parameters.

      - Likelihood
      : ...

      - Renewal duration
      : The renewal duration is required when the lease is set to renew
        and defines the length of the new term. The model will prorate
        the lease duration and parameters by the likelihood of renewal when
        performing a traditional analysis.

        - Years
        : The duration in years as a decimal. A non-integer value will cause the
          decimal component to be prorated using the Actual/Actual day-count
          convention.

        - Months
        : The duration in months as a decimal. A non-integer value will cause
          the decimal component to be prorated using the Actual/Actual day-count
          convention.

        - Weeks
        : The duration in weeks as an integer.

        - Days
        : The duration in days as an integer.

        - Until
        : The lease will renew until the specified inclusive date.

- Remain Vacant
  : The tenant will not be renewing their lease. No lease will be forecast
    when the lease ends. This option might be chosen if the property owner
    intends to repurpose the space or combine the space with another.

#### Base Rent

Base rent is the rent amount explicitly specified in the lease.

  - ##### Fixed base rent
  : The minimum amount of rent that a tenant is required to pay, excluding any
    additional rent such as operating expenses recoveries or percentage rent.

    Base rents are often quoted as rates but can be entered as an amount
    per payment.

      - Amount per Month
      : A fixed amount expressed as a monthly rate.

      - Amount per Year
      : A fixed amount expressed as a yearly rate.

      - Amount per Area per Month
      : The monthly rate per unit of the leased area.

      - Amount per Area per Year
      : The yearly rate per unit of leased area.

      - Percentage of Market
      : An amount expressed as a percentage of the market rent at the time the
        lease starts as defined by the space's associated leasing rule.

  - ##### Step base rent
  : Step rent increases are an optional type of rent agreed upon in advance
    and written into the lease agreement. They are a lease structure where
    the base rent increases by predetermined amounts at specified intervals
    throughout the term.

    - Amount per Year
    : The base rent increases by a fixed amount each year on the anniversary
      of the lease start.

    - Amount per Area per Year
    : The base rent increases by a fixed amount per area each year on the
      anniversary of the lease start.

    - Percentage of Base per Year
    : The base rent increases by a percentage of the base rent amount each
      year on the anniversary of the lease start. These increases compound.


#### Concessions

  - ##### Free rent period
  : A pre-agreed period of time when the tenant can occupy the space but does
    not have to pay rent. This is a common incentive for a tenant to sign a
    long-term lease. The tenant may or may not be responsible for their share
    of the property's expenses during this period. This is signified by a
    checkbox below the period input.<br><br>
    Occasionally, free rent may not refer to a period of free rent but instead
    as an ongoing financial adjustment. In these cases, the free rent deal
    terms should be input as a concession.

    - Years
    : The duration in years as a decimal. A non-integer value will cause the
      decimal component to be prorated using the Actual/Actual day-count
      convention.

    - Months
    : The duration in months as a decimal. A non-integer value will cause the
      decimal component to be prorated using the Actual/Actual day-count
      convention.

    - Weeks
    : The duration in weeks as an integer.

    - Days
    : The duration in days as an integer.

    - Until
    : The lease will renew until the specified inclusive date.


#### Leasing Costs

  ...

  - ##### Leasing commissions
  : Fees paid to real estate brokers or agents for successfully arranging a
    lease agreement between the property owner and tenant.

    - Amount
    : A fixed amount regardless of the revenues received.

    - Amount per Area
    : The product of the supplied amount and the area being leased.

    - Amount per Area per Year
    : The product of the supplied amount, leased area and duration
      of the lease in years.

    - Percentage of Total Lease Value
    : A percentage of the total base rent paid over the entire duration of
      the lease.

  - ##### Tenant improvement allowance
  : Also known as TI contribution, is the financial offering by
    the property owner towards the tenant's costs to customize or
    renovate the leased space to fit the tenant's specific needs.

    - Amount
    : A fixed amount contributed to improvements.

    - Amount per Area
    : The product of the supplied amount and the area being leased.

    - Amount per Area per Year
    : The product of the supplied amount, leased area and duration of the
      lease in years.

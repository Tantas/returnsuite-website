---
title: Reversion Information - ReturnSuite Docs
description: Project the return of a real estate investment.
nav-title: Reversion information
nav-group: Updating the model
---

# Reversion Information

## Project the return of a real estate investment

Because NPV is valuing cash flows, we need to calculate the Net
Realizable Reversionary Value (cash that the investor expects to
receive upon sale, exclusive of any debt repayment).

### NOI to capitalize

Determines the NOI snapshot period at the disposal date or analysis end when a
sale date is not speculated. This period will be adjusted and capitalized to
calculate the reversionary value.

##### NOI capitalization period options:

Forward 12 Months
:   The total forecasted NOI in the year after the valuation date. This is most
    common.

Trailing 12 Months
:   The total forecasted NOI in the year leading up to the valuation date.

Average 24 Months
:   The one-year average NOI for 12 months before and after the valuation date.


### Gross up occupancy

A common issue using the NOI snapshot without any adjustments is occupancy
levels at the reversion date could be higher or lower than historical norms.
Valuers often adjust the occupancy to historical levels using an occupancy
adjustment.

Adding an occupancy gross up adjustment will adjust the NOI by the difference
between the forcast occupancy and the percentage input.


### NOI adjustments

Operational NOI adjustments are modifications made to the net operating income
to provide a more accurate forecast of a property's typical financial
performance. These adjustments can be both positive and negative, in the
seller's or purchaser's favor.

The adjustments ensure that the reversionary value calculation is based on a
realistic and sustainable income stream, rather than temporary or anomalous
conditions. This is important because the NOI will be capitalized like a
perpetuity. Perpetuities are based on the assumption that the income will
continue far into the future.


#### Adjustment name

The name of the NOI adjustment as it will appear in reports that
reflects its nature. Each adjustment must have a unique name.


#### Adjustment type

Determines if the adjustment should be an inflation adjusted amount or
percentage of the net operating income snapshot.

Amount
:   A fixed, positive, inflation adjusted amount to be added (seller's favor) or
    subtracted (buyer's favor) from the NOI snapshot.

Percentage
:   A positive percentage to be applied to the NOI snapshot and added
    (seller's favor) or subtracted (buyer's favor) from the NOI snapshot.


### Reversion capitalization rate

Also known as exit cap rate is the estimated capitalization rate at the
time of reversion. The capitalization rate is a percentage that estimates
an investor's potential return on investment. Rates reflect the risk of
return and are effected by a variety of factors in the market.

Market rates can be found in market sales data and aggregated reports
from appraisers. They can vary significantly between markets.


### Value adjustments

Value adjustments account for factors beyond the property's operational
performance, including market conditions, transaction-related expenses and
seller-specific costs.

These 'below the line' adjustments refine the initial reversionary value to the
actual amount a seller can expect to receive from the property sale.


#### Adjustment name

The type of adjustment corresponding order of application to the initial
reversionary value to calculate the net realizable reversionary value.


#### Adjustment type

The type of adjustment corresponding order of application to the initial
reversionary value to calculate the net realizable reversionary value.

##### Adjustment type options:

Sale Price
:   An adjustment that is added (seller's favor) or subtracted (purchaser's
    favor) from the initial reversionary value. These types of adjustments
    account for market conditions, property features not accounted for the
    Adjusted NOI or adjustments expected in negotiations, ex. Upcoming capital
    expenditures, deferred maintenance or excess land value. The application of
    sale price adjustments results in the adjusted reversionary value.

Transaction Cost
:   Cost adjustments including all the direct fees associated with completing a
    sale, ex. Brokerage fees, legal expenses and marketing spend. These costs
    are subtracted from the result of sale price adjustments. The application of
    transaction cost adjustments results in the net reversionary value.

Vendor Cost
:   Vendor costs are specific to the seller and would not necessarily be
    incurred by other buyers or sellers, ex. Management contract termination
    fees. Vendor costs are subtracted from the result of transaction cost
    adjustments. The application of vendor costs results in the net realizable
    reversionary value.


#### Adjustment description

A longer, optional description of the adjustment providing further
identification or the source of information. Visible as a tooltip in some
reports on the reporting row title.


#### Applied to

Determines the input type and value to apply the value adjustment.
Adjustment types further down in the order of application will have more
options to choose.

##### Applied to options:

Amount
:   A fixed, positive, inflation adjusted amount to be added (seller's favor) or
    subtracted (buyer's favor).

Percentage of Initial Reversionary Value
:   A positive percentage to be applied to the initial reversionary value
    and added (seller's favor) or subtracted (buyer's favor).

Percentage of Adjusted Reversionary Value
:   A positive percentage to be applied to the adjusted reversionary
    value and subtracted.

Percentage of Net Reversionary Value
:   A positive percentage to be applied to the net reversionary value and
    subtracted.

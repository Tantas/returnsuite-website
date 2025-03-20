---
title: Analysis Period
description: Specify the time frame to evaluate the model
nav-title: Analysis period
nav-group: Updating the model
---

# Analysis Period

## Specify the time frame to evaluate the model

Financial models are an analysis of the future benefits of owning a property
within a set time horizon, which requires both an Analysis start and an Analysis
term, which is defined either as a specific Analysis end date or a Duration.
The Analysis start will often coincide with a Purchase date, but it doesn’t
necessarily have to. Similarly, the Analysis end doesn’t need to coincide with
the intended Sale date.

### Setting the analysis period

Add the analysis period to the model by selecting "Add analysis period" and
complete the associated form. The analysis period can be overridden in both
reports and at the portfolio level. It is recommended financial events are not
tagged to these dates. An empty analysis period will default to the first of the
following month from the time the model is run and will proceed for a period of
ten years.

#### Analysis start

The first day of the analysis period, inclusive. This will often coincide with
the purchase date of a property. It is recommended that this date be the start
of a reporting period, ex. January 1st.

The analysis start can be overridden in reports and is often overridden at the
portfolio level. When modifying the analysis start date, it is important to
check the impact of cashflows that may be tied to the timing of this event or
to decouple the timing.

#### Analysis term

Defines how the analysis duration should be input.

Date
:   Allows the inclusive end date of the analysis to be entered.
    It is recommended this date ends on a standard reporting period end.
    Example: December 31st.

Duration
:   The duration of the financing term in years and months. The calculated end
    date will be inclusive to the period. Example: two years from January 1st,
    2400 will end December 31st, 2401.

#### Duration

The last day of the analysis period. It must be at least one year after the
start of the analysis period and ideally terminate on the last day of a standard
reporting period.

#### End date

The number of years and months included in the analysis period.

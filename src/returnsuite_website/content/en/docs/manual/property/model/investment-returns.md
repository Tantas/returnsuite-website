---
title: Investment Returns - ReturnSuite Docs
description: How to input spaces and uses into a ReturnSuite property model.
nav-title: Investment returns
nav-group: Updating the model
---

# Investment Returns

## Apply discount rates to compare opportunities

The final step of building a financial model is choosing a Discount
Rate–the Cost of Capital or Hurdle Rate that an investor requires to
earn on similar types of investments when factoring in all the forms
of risk.

Discount Rates are applied to the entire set of cash flows over the
life of the investment–and are not just applied to the Reversionary
Value.

Before choosing a discount rate, it is important to keep in mind
the purpose of the financial model. Is the model an Investment
Valuation for a specific investor or is it a Market Valuation for
the general market? The answer to this question will determine who’s
Discount Rate your analysis will be using.

Determining the Discount Rate requires two pieces of information–the
Nominal Annual Discount Rates and the Compounding Frequency.


### Adding return information

#### Compounding frequency

The compounding frequency converting the nominal discount rates to real
rates, factoring in the effect of compounding.

##### Compounding options:

Annual
:   The discount rates compound once per year on the analysis start anniversary.

Semiannual
:   The discount rates compound twice per year, every six months after the start
    of analysis.

Quarterly
:   The discount rates compound four times per year, every three months after
    the start of analysis.

Monthly
:   The discount rates compound twelve times per year, every month after the
    start of analysis.

#### Unlevered discount rate

Input as a percentage, the nominal discount rate the investors would expect
without the use of debt financing.

#### Levered discount rate

Input as a percentage, the nominal discount rate the investors would expect when
factoring in the additional risk from the use of debt financing.

The levered discount rate should always be equal of higher than the unlevered
discount rate since adding leverage to an investment can add a meaningful amount
of risk.

---
title: Financing - ReturnSuite Docs
description: How to input spaces and uses into a ReturnSuite property model.
nav-title: Financing
nav-group: Updating the model
---

# Financing

## Add loans to finance the purchase, capital improvements and operating shortfalls

The data entered into the Financing section of ReturnSuite is used to determine
the timing and amounts in the Loan Report(s) section of the Financing Activities
and Cash Flow Statements. It is also needed to calculate important financial
indicators such as Debt Service ratios, NPV and IRR.

Financing is independent of a property’s operations and is therefore an
“independent module” in a ReturnSuite model–any financing details only affect
cash flows after the NOI line in the Cash Flow Statement.

For potential purchases where the exact financing details are unknown, estimates
can be used–the exact financing details can be edited later once the financing
arrangements are finalized.

If you are modeling a property you have owned for a long time, enter the most
recent financing details and ReturnSuite will automatically adjust your loan
balances.

### Adding a loan

TODO some copy here explaining how to add a loan.

#### Financing name

The name of the financing agreement as it will appear in reports, often
describing the nature of the arrangement.


#### Lender identification

An optional identifier used to group cash flows in some reports.


#### Financing description

An optional, longer description of the loan providing further identification or
the source of information.


#### Financing types

The structure of the loan agreement along with the amount of amount that will be
borrowed at the start of the financing agreement.

##### Financing type options:

Amortizing Loan
:   The borrower makes regular blended payments that cover both interest and a
    portion of the principal amount. This structure ensures that the balance
    owed is reduced with each payment until the loan is completely paid off at
    the end of the amortization term. With each additional payment, the
    proportion of the payment going towards the principal increases and the
    proportion going towards interest decreases assuming a steady interest rate
    over the amortization term.

Simple Interest Loan
:   The borrower makes regular payments against with the interest calculated
    against the remaining principal.

Interest-Only Loan
:   The borrower is required to pay only the interest on the principal balance
    for a set period, with no repayment of the principal during that time.

Bullet Loan
:   The borrow is required to pay both all accrued interest and the principal
    at the end of the term with no regular payments.

---


### Amortizing loans

#### Principal amount

#### Nominal interest rate

The nominal interest rate, also known as the annual percentage rate (APR), is
the quoted interest rate for a financing agreement. This rate along with the
compounding frequency is used to calculate the periodic rate of the loan used to
calculate the amortized payments.


#### Compounding frequency

The frequency the nominal interest rate is compounded to produce the effective
annual rate.

##### Compound frequency options:

Annual
:   Interest compounds once per year on the anniversary of the loan begins.

Semiannual
:   Interest compounds twice per year, every six months after the loan begins.

Quarterly
:   Interest compounds four times per year, every three months after the loan
    begins.

Monthly
:   Interest compounds twelve times per year, every month after the loan begins.


#### Financing start

The date that funds from the loan are advanced and interest begins accumulating.

##### Start options:

Specific Date
:   A specific date that funds were or will be advanced.

Property Acquisition
:   The loan begins on the same date as the property purchase date. This is a
    useful option when the property has not yet been purchased or when a
    property was purchased outside the analysis period but is still financed by
    the original loan. This will default to the analysis start when there is no
    purchase date for the property.

Analysis Start
:   The loan will begin on the analysis start date. This option is not
    recommended and may cause unexpected behavior when changing overriding the
    analysis period in reports and portfolios.

#### Payment frequency

The frequency of payments that will be made against the loan from the loan start
date.

##### Frequency options:

Yearly:
:   A payment is made once per year on the anniversary of the financing start.

Semiyearly
:   Payments are made twice a year, every six months after the loan starts.

Quarterly
:   Payments are made four times a year, every three months after the loan
    starts.

Monthly
:   Payments are made twelve times a year, every month after the loan starts.


#### Financing term

The length of the lending arrangement. When the term ends, any remaining
balance must be paid in full, either in cash or refinanced. The term can be
entered in any unit equal or greater than the payment frequency.

##### Term options:

Years
:   The duration of the financing term in years.

Months
:   The duration of the financing term in months.


#### Amortization term

The length of amortization. The term must be input with the same unit as the
financing term and be at least as long.

Years
:   The duration of the amortization term in years.

Months
:   The duration of the amortization term in months.

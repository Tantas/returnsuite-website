---
title: Purchase Information
description: Add purchase information to link start dates and calculate the IRR
nav-title: Purchase information
nav-group: Updating the model
---

# Purchase Information

## Add purchase information to link start dates and calculate the IRR

The property purchase information is made of the date, amounts and closing
costs used to acquire the property. It is necessary to calculate important
financial indicators such as the Net Present Value (NPV) and the Internal
Rate of Return (IRR).

Often you may be creating a model for a potential purchase where the
exact purchase amount and date are unknown. For potential purchases,
estimates can be used. You can update the exact purchase price and date
at a later time once the sale is complete.

If you are modeling a property you have owned for a long time, input the
original purchase information, even if it falls outside the analysis
period.


### Adding the purchase information

#### Purchase date

The date the title of the property was or will be transferred. This must be
specified as a date and may be referenced elsewhere in the model. References to
this date will be linked to the analysis start date when this is not present.


#### Purchase price

The amount paid **before** closing costs. This is the price the buyer and seller
have agreed upon. Must be entered in the currency the property is modeled.


#### Purchase description

Optional, additional details or reference sources that would be helpful to
model viewers.

### Adding closing costs


#### Closing cost name

The unique name of the closing cost, often describing the nature of the cost.

Examples include 'Appraisal Fee,' 'Legal Fees,' 'Recording Fees,' 'Escrow Fees,'
'Title Insurance' and 'Transfer Taxes.'


#### Closing cost vendor

The optional name of the closing cost supplier.

This is used by reports to display additional information to the viewer and
group sources of costs and revenues.


#### Closing cost description

Optional additional details or reference sources that would be helpful model
viewers.


#### Closing cost type

Determines how costs will be input.

##### Type options:

Amount on Closing
:   A fixed amount paid on the closing day independent of the purchase price.

Percentage on Closing
:   A percentage of the purchase price due on the closing day.

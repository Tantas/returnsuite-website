---
title: Overview - Key Math Concepts used in Finance - ReturnSuite Docs
description: TODO - Add a description
nav-title: Vacancy and credit loss
nav-group: NOI and cash flow
---

# Vacancy and Credit Loss

## How vacancy and credit loss fit into the NOI statement

Vacancy & Credit Losses are reserves for unexpected losses in a
future-looking NOI Statement–they are generalized contingencies rather
than a known or expected vacancy / shortfall. They are the lines in the
NOI Statement that accounts for *“I don’t know which tenant will leave
unexpectedly, but every year it seems to happen.”*

There are two subcomponents to this line in the Net Operating Income Statement:

### Vacancy loss

Accounts for unexpected or unforeseeable vacancies not captured in
specific space projections and provides a buffer for differences in
the projected leasing rules and the actual market fluctuations.

### Credit loss

An estimate of the potential uncollectible rent from existing or
future tenants from potential tenant defaults or negotiated rent
reductions.

Both types of Vacancy Losses and Credit Losses are typically calculated
as a percentage of Potential Gross Income.

Vacancy & Credit Losses are only used in projected NOI Statements, not
in NOI Statements that display actual financial results. They are
subtracted from Potential Gross Income, we arrive at the Effective Gross
Income.

### How vacancy & credit losses are handle actuals

When creating a NOI Statement that includes actuals rather than
projections, the Vacancy & Credit Loss lines are no longer applicable
since any unexpected vacancy or collection issue would be reflected in
the corresponding revenues lines.

For example, let’s say a tenant suddenly defaulted on their lease, which
created a month of lost rental revenue for a landlord. If the tenant was
scheduled to pay $1,000, comprising $800 in Base Rent and $200 in
Additional Rent (Operating Expense Recoveries), each of those lines
would be reduced by the corresponding amount.

While the NOI Statement wouldn’t specific highlight the adjustments in
this way, here is a snapshot of what is happening to the specific lines
behind the scenes:

<figure>
  <div class="rounded-md shadow-sm border border-gray-300 overflow-auto max-w-fit pt-3">
    <table class="table-auto border-collapse font-medium">
      <thead>
        <tr>
          <th class="border-b border-gray-300 pb-3 font-semibold text-left px-8 whitespace-nowrap">Line Items</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Pre-Default</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Adjustments</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Post-Default</th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white">
          <th class="border-b py-3 font-semibold text-left px-8 whitespace-nowrap">Actual Base Rent</th>
          <td class="border-b py-3 text-right px-8 font-semibold">$1,450</td>
          <td class="border-b py-3 text-right px-8 font-semibold text-red-500">-$800</td>
          <td class="border-b py-3 text-right px-8 font-semibold">$650</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Additional Rent</th>
          <td class="border-b py-3 text-right px-8">$550</td>
          <td class="border-b py-3 text-right px-8 text-red-500">-$200</td>
          <td class="border-b py-3 text-right px-8">$350</td>
        </tr>
        <tr class="bg-white">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Other Tenant Revenue</th>
          <td class="border-b py-3 text-right px-8">$350</td>
          <td class="border-b py-3 text-right px-8">-</td>
          <td class="border-b py-3 text-right px-8">$350</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Other Revenue</th>
          <td class="border-b py-3 text-right px-8">$625</td>
          <td class="border-b py-3 text-right px-8">-</td>
          <td class="border-b py-3 text-right px-8">$625</td>
        </tr>
        <tr class="bg-white">
          <th class="py-3 font-semibold text-left px-8 whitespace-nowrap">Potential Gross Income</th>
          <td class="py-3 text-right px-8 font-semibold">$2,975</td>
          <td class="py-3 text-right px-8 font-semibold text-red-500">-$1,000</td>
          <td class="py-3 text-right px-8 font-semibold">$1,975</td>
        </tr>
      </tbody>
    </table>
  </div>
  <figcaption>Example Vacancy & Credit Loss</figcaption>
</figure>

If there are unexpected vacancies or credit losses in actuals when
compared to projections, a good practice is to highlight those issues in
a footnote similar to how issues are highlighted in other financial
reports.

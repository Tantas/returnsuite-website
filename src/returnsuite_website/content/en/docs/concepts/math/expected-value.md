---
title: Overview - Key Math Concepts used in Finance - ReturnSuite Docs
description: TODO - Add a description
nav-title: Expected value
nav-group: Key Math Concepts in Finance
---

# Expected Value

## How to value uncertainty in real estate

Expected Value is a statistical measure used to determine the likely
average outcome of an investment over a range of possible scenarios. It
is calculated by multiplying each possible outcome by its probability of
occurrence and summing these products. This method provides a single
metric that summarizes the weighted average of all possible outcomes,
offering a powerful tool for decision-making under uncertainty.

This is a valuable tool in real estate, which can often have added
complexity–tenants can renew or not, rental rates can go up or not and
expenses can happen or not. Expected Value provides us with a way to
incorporate these complexities.

Expected Values for Future Values, Present Values and Net Present Values
are often shown with the abbreviation <b>E[XX]</b>:

<ul class="list-disc pl-8 font-medium text-gray-800 text-lg pb-4 leading-8">
  <li>E[PV] is the Expected Present Value</li>
  <li>E[FV] is the Expected Future Value</li>
  <li>E[NPV] is the Expected Net Present Value</li>
</ul>

<hr class="mt-2 mb-6 border-gray-300">

### Example

Let’s say we have a tenant occupying a space at a rate of $120,000 per
year under a two-year lease. At the end of the two years, we expect
that the tenant has a 50% chance of renewing their lease for an
additional three years.

If they renew their lease, we believe that they will renew at a rate
of $150,000 per year. However, if they do not renew their lease, we
believe it will take six months to find a new tenant who will likely
pay $140,000 per year. In both cases we believe we will be able to sell
the property in Year 5 for $2,400,000.

If we are using a Discount Rate of 6.0%, what is the E[PV] of the
property?

Open up the attached spreadsheet and work through the example to
understand the mechanics.

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - Expected Value - Worksheet.xlsx">Expected Value - Worksheet.xlsx</a>
  <a download href="/sheets/ReturnSuite - Expected Value - Worksheet.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

#### Scenario 1

<ul class="list-disc pl-8 text-gray-800 text-base pb-4 leading-8">
  <li>
    The rental income in Row 3 increases from $120,000 per year to
    $150,000 per year in Year 3 with no break in revenue
  </li>
  <li>
    In Year 5, we receive the $150,000 in rent plus the $2,400,000 from the
    sale of the property (<i>Cell F4</i>)
  </li>
  <li>
    We can then determine our Future Value cash flows in Row 5
  </li>
  <li>
    The Future Value cash flows multiplied by the probability of the scenario
    (50%) to give us our E[FV] Net Cash Flows (Row 7)
  </li>
</ul>

#### Scenario 2

<ul class="list-disc pl-8 text-gray-800 text-base pb-4 leading-8">
  <li>
    The rental income in Row 10 increases from $120,000 per year to
    $140,000 per year in Year 3, but there is a six-month break in revenue
    in Year 3, reducing income to $70,000 (<i>Cell D10</i>)
  </li>
  <li>
    The same process is used to determine the E[FV] Net Cash Flows (Row 14)
  </li>
</ul>

#### Combining the Scenarios

<ul class="list-disc pl-8 text-gray-800 text-base pb-4 leading-8">
  <li>
    We can determine the Total E[FV] Net Cash Flows (<i>Row 17</i>) by summing the
    E[FV] Cash Flows of each of the scenarios together
  </li>
  <li>
    The E[PV] Net Cash Flows (<i>Row 19</i>) can then be calculated by dividing
    the E[FV] Cash Flows by the Discount Factor (<i>Row 18</i>)
  </li>
  <li>
    The E[PV] of the Property of $2,468,730 (<i>Cell B20</i>) is equal to the sum
    of all of the E[PV] Net Cash Flows.
  </li>
</ul>

<hr class="mt-2 mb-6 border-gray-300">

### Exercise

Using the same spreadsheet, try making the following changes.

#### Task 1

What happens to the **E[PV]** of the property if the expected amount of time to
find a replacement tenant is extended to nine months?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Changing the Months Vacant variable (<i>Cell C26</i>) from 6 to 9 months
      results in expected rental income in Year 3 in the vacate scenario
      to drop to <b>$35,000</b> (<i>Cell D10</i>). This ripples down through
      the financial model, eventually decreasing the <b>E[PV] to $2,453,155</b>
      (<i>Cell B20</i>).
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Task 2

What happens to the **E[PV]** of the property if the sale price in Year 5 under
the renewal scenario is increased to **$2,550,000**?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Increasing the expected Sale Price for the renewal scenario from
      <b>$2,400,000 to $2,550,000</b> (<i>Cell C29</i>) also causes a ripple
      of changes that eventually results in the <b>E[PV]</b> of the property
      increasing to <b>$2,512,562</b> (<i>Cell B20</i>).
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Task 3

What happens to the Property **E[PV]** if the current tenant informed us that
they definitely wanted to renew their lease at the expected rate?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Changing the Probability of Scenario variable for the renewal scenario
      from <b>50% to 100%</b> (<i>Cell B23</i>) also requires changing the
      Probability of Scenario variable for the vacate scenario from
      <b>50% to 0%</b> (<i>Cell C23</i>). The <b>E[PV]</b> of the property
      will increase to <b>$2,631,303</b> (<i>Cell B20</i>) since the
      weighted average of the two scenarios is now weighted entirely on the
      renewal scenario.
    </p>
  </div>
</div>

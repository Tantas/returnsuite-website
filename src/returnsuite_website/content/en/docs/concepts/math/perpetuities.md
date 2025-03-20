---
title: Perpetuities
description: How to calculate the value of a Perpetuity
nav-title: Perpetuities
nav-group: Key Math Concepts in Finance
---

# Perpetuities

## How to calculate the value of a Perpetuity

Perpetuities are a type of annuity that pays an infinite series of cash
flows (in perpetuity). They are used for financial modeling and valuation
when it’s assumed that a property or business will generate a constant
cash flow indefinitely.

Perpetuities are commonly used in two types of scenarios when building
financial models in real estate:

<ol class="list-decimal pl-8 text-gray-800 text-base pb-2 leading-8">
  <li>
    Often in commercial real estate investments, a substantial portion of
    the returns are expected when the property is sold–and since the
    property will continue to earn profits after the sale, the perpetuity
    is used to calculate the sale price.
  </li>
  <li>
    Or a real estate investor expects to hold a property indefinitely, a
    perpetuity is used to calculate the future benefits beyond the analysis
    period since the property still has value at the end of the analysis
    period.
  </li>
</ol>

However, because of the Time Value of Money, we know that with a constant
cash flow stretching into infinity, money received sooner is always worth
more than money received later. This means that each year's cash flow is
worth a little less than the last–the further away the money is, the less
it's worth right now.

The formula for the present value of a perpetuity is fairly simple:

<figure>
  <math>
    <mi>Present Value</mi>
    <mo>=</mo>
    <mfrac>
      <mpadded height="1.2em" voffset="0.2em">
        <mi>Cash Flow</mi>
      </mpadded>
      <mpadded height="1.1em">
        <mi>Discount Rate</mi>
      </mpadded>
    </mfrac>
  </math>
</figure>

 <hr class="mt-2 mb-6 border-gray-300">

### Exercises

To take a closer look at the mechanics of a Perpetuity, download and open
this sample spreadsheet which uses cash flows over 50 periods.

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - Perpetuities - Worksheet.xlsx">Perpetuities - Worksheet.xlsx</a>
  <a download href="/sheets/ReturnSuite - Perpetuities - Worksheet.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

#### Task 1

Try using the fill handle to copy the cash flows down another 100 rows
(highlight <i>Cells A50:D51</i>, click & drag the bottom right corner down as far
as <i>Cells A101:D51</i>). What do you notice about the Present Value?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Notice that <i>Cells G8 and G9</i> are now within <b>$1</b> of each other
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Task 2

Now try changing the Discount Rate (<i>Cell G4</i>) to <b>5%</b> and then
<b>15%</b>. What do you notice about the Present Value of the Perpetuity?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Notice that the Discount Rate and the Value of the Perpetuity are
      inversely correlated with each other–the higher Discount Rate, the
      less the Perpetuity is worth.
    </p>
  </div>
</div>

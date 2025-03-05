---
title: Overview - Key Math Concepts used in Finance - ReturnSuite Docs
description: TODO - Add a description
nav-title: Gordon growth model
nav-group: Key Math Concepts in Finance
---

# Gordon Growth Model

## How to calculate the value of a growing Perpetuity

The Gordon Growth Model, also known as the Dividend Discount Model, is a
method used in finance to value a cash flow that is growing at a constant
rate–a growing Perpetuity. Rather than valuing an infinite stream of cash
flows, where each cash flow is the same amount, the cash flows are
changing at a constant rate.

The formula for determining the Present Value of a g is a slight twist on
the Perpetuity formula by factoring in the Growth Rate:

<figure>
  <div class="w-1/2 flex flex-col place-items-start gap-4">
    <math>
      <mi>Present Value</mi>
      <mo>=</mo>
      <mfrac>
        <mpadded height="1.2em" voffset="0.2em">
          <mi>Cash Flow</mi>
        </mpadded>
        <mpadded height="1.1em">
          <mrow>
            <mo>(</mo>
            <mi>Discount Rate</mi>
            <mo>-</mo>
            <mi>Growth Rate</mi>
            <mo>)</mo>
          </mrow>
        </mpadded>
      </mfrac>
    </math>
  </div>
</figure>

For example, the present value of a Perpetuity of $100 per period at a
Discount Rate of 10% is $1,000.

<figure>
  <div class="w-1/2 flex flex-col place-items-start gap-4">
    <math>
      <mi>PV</mi>
      <mo>=</mo>
      <mi>Cash Flow</mi>
      <mo>/</mo>
      <mi>Discount Rate</mi>
    </math>
    <math>
      <mphantom>
        <mi>PV</mi>
      </mphantom>
      <mo>=</mo>
      <mn>$100</mn>
      <mo>/</mo>
      <mn>10%</mn>
    </math>
    <math>
      <mphantom>
        <mi>PV</mi>
      </mphantom>
      <mo>=</mo>
      <mn>$1,000</mn>
    </math>
  </div>
</figure>

If we then said that the cash flows were growing at a rate of 2% per
period, we’d use the Gordon Growth Model Formula:

<figure>
  <div class="w-1/2 flex flex-col place-items-start gap-4">
    <math>
      <mi>PV</mi>
      <mo>=</mo>
      <mi>Cash Flow</mi>
      <mo>/</mo>
      <mo>(</mo>
      <mi>Discount Rate</mi>
      <mo>-</mo>
      <mi>Growth Rate</mi>
      <mo>)</mo>
    </math>
    <math>
      <mphantom>
        <mi>PV</mi>
      </mphantom>
      <mo>=</mo>
      <mn>$100</mn>
      <mo>/</mo>
      <mo>(</mo>
      <mn>10%</mn>
      <mo>-</mo>
      <mn>2%</mn>
      <mo>)</mo>
    </math>
    <math>
      <mpadded width="135%">
        <mphantom>
          <mi>PV</mi>
        </mphantom>
      </mpadded>
      <mo>=</mo>
      <mn>$100</mn>
      <mo>/</mo>
      <mn>8%</mn>
    </math>
    <math>
      <mpadded width="135%">
        <mphantom>
          <mi>PV</mi>
        </mphantom>
      </mpadded>
      <mo>=</mo>
      <mn>$1,250</mn>
    </math>
  </div>
</figure>

The Gordon Growth Model can be used for non-growing cash flows (since the
Growth Rate will be zero), leaving us with the formula for valuing a
Perpetuity.

While much less common in real estate, the Gordon Growth Model can also
be used to constantly declining cash flows–with a negative growth rate in
the formula, the denominator becomes larger, lowering the Present Value
of the Perpetuity.

<hr class="mt-2 mb-6 border-gray-300">

## Exercise

To take a closer look at the mechanics of the Gordon Growth Model,
download and open this worksheet which begins where the Perpetuity
worksheet left off.

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - Gordon Growth Model - Worksheet.xlsx">Gordon Growth Model - Worksheet.xlsx</a>
  <a download href="/sheets/ReturnSuite - Gordon Growth Model - Worksheet.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

Notice that the starting Present Value of the Perpetuity (<i>Cell G8</i>)
is **$10,000**.

### Task 1

Try changing the Discount Rate (<i>Cell G4</i>) to **12%**. What do
you notice happens to the Present Value of the Perpetuity?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Notice that the Present Value of the Perpetuity (<i>Cell G8</i>) has
      decreased to <b>$8,333</b>.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

### Task 2

Now try changing the Growth Rate (<i>Cell G5</i>) from **0%** to **2%**. What do
you notice happens to the Present Value of the Perpetuity?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Notice that the Present Value of the Perpetuity (<i>Cell G8</i>) has
      increased back up to <b>$10,000</b>.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

### Task 3

Try changing the Discount Rate (<i>Cell G4</i>) back to **10%** and the growth
rate (<i>Cell G5</i>) from **2%** to **5%**. What do you notice happens to the
present value of the perpetuity?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Notice that the Present Value of the Perpetuity (<i>Cell G8</i>) has
      doubled to <b>$20,000</b>.
    </p>
    <p>
      So even though the investor has a Discount Rate of 10%, they will be
      willing to pay $20,000 for an investment in which they will only
      receive $1,000 in Period 1 (implying a 5%, not only expects to
      receive $1,000 on their $20,000 in Period 1 (5% return) and they
      have a Discount Rate of 10%, the high level of growth.
    </p>
    <p>
      This is the underlying mechanics of high growth investments and why
      many investors are willing to pay high multiples on earnings in
      investments that might have smaller cash flows now but are expected
      to grow rapidly in the future.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

<div class="flex">
  <aside class="rounded-md border border-gray-300 shadow-lg px-6 py-4 w-3/4">
    <span style="padding-top: 0; padding-bottom: 0" class="text-gray-900 font-medium text-base">Further Reading:</span>
    <h2 class="py-2"><a target="_blank" href="#">Investors will pay for two things: Safety and Growth</a></h2>
    <img src="/img/blog/2024-03-28/balance-between-a-secure-investment-and-high-growth-opportunity.webp" alt="Like plane flights, rental space is a perishable good–potential revenue is lost forever once it takes off." class="rounded-md shadow-sm">
    <p class="text-gray-900 text-sm">
      Very few industries offer investors 20x multiples on earnings.
      Software is able to achieve high multiples through high levels of
      earnings growth, while real estate has offered investors bond-like
      safety. Office investors are currently facing a double headwind–not
      only has the Risk Free Rate increased, but market sentiment has also
      moved against offices. In order to stay in the 20x club, we need to
      re-look at what levers are available to us.
    </p>
    <a target="_blank" href="#" class="flex place-items-center hover:underline">
      <span class="text-base">Read article</span>
      <svg class="inline-block h-6" viewBox="0 0 24 24" fill="currentColor">
        <path d="M10.02 6L8.61 7.41 13.19 12l-4.58 4.59L10.02 18l6-6-6-6z"></path>
      </svg>
    </a>
  </aside>
</div>

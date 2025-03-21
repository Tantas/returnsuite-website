---
title: Internal Rate of Return
description: How the Internal Rate of Return relates to NPV
nav-title: Internal rate of return
nav-group: Key Math Concepts in Finance
---

# Internal Rate of Return

## How the Internal Rate of Return relates to NPV

The Internal Rate of Return (IRR) is a measure of return that is often
used in finance and real estate. IRR is the Discount Rate in which the
NPV is equal to zero. So if an investment’s IRR is greater than the
Discount Rate, the NPV is positive and if the IRR is less than the
Discount Rate, the NPV is negative.

### Calculating IRR

Calculating an IRR is technically possible, but is very time consuming
with the difficulty increasing with each additional cash flow added to
the analysis. Because the IRR is the Discount Rate which provides us with
a NPV of zero, the formula we start with is the NPV (or the cash flow in
period 0) is equal to the sum of the Present Values of the cash flows
from the investment, when the IRR is equal to the Discount Rate.

This formula can then be rearranged so we can solve for IRR.

<figure>
  <div class="flex flex-col place-items-start gap-6">
    <math>
      <mpadded width="110%">
        <mphantom>
          <mi>Equivalent to:</mi>
        </mphantom>
      </mpadded>
      <mi>NPV</mi>
      <mo>=</mo>
      <msub>
        <mi>CF</mi>
        <mn>0</mn>
      </msub>
      <mo>+</mo>
      <mi>PV</mi>
      <mo>(</mo>
      <msub>
        <mi>CF</mi>
        <mn>1</mn>
      </msub>
      <mo>)</mo>
      <mo>+</mo>
      <mi>PV</mi>
      <mo>(</mo>
      <msub>
        <mi>CF</mi>
        <mn>2</mn>
      </msub>
      <mo>)</mo>
      <mo>+</mo>
      <mo>...</mo>
      <mo>+</mo>
      <mi>PV</mi>
      <mo>(</mo>
      <msub>
        <mi>CF</mi>
        <mo>n</mo>
      </msub>
      <mo>)</mo>
    </math>
    <math>
      <mpadded width="110%">
        <mi>Equivalent to:</mi>
      </mpadded>
      <mi>NPV</mi>
      <mo>=</mo>
      <msub>
        <mi>CF</mi>
        <mn>0</mn>
      </msub>
      <mo>+</mo>
      <mfrac>
        <msub>
          <mi>CF</mi>
          <mn>1</mn>
        </msub>
        <msup>
          <mrow>
            <mo>(</mo>
            <mn>1</mn>
            <mo>+</mo>
            <mi>IRR</mi>
            <mo>)</mo>
          </mrow>
          <mn>1</mn>
        </msup>
      </mfrac>
      <mo>+</mo>
      <mfrac>
        <msub>
          <mi>CF</mi>
          <mn>2</mn>
        </msub>
        <msup>
          <mrow>
            <mo>(</mo>
            <mn>1</mn>
            <mo>+</mo>
            <mi>IRR</mi>
            <mo>)</mo>
          </mrow>
          <mn>2</mn>
        </msup>
      </mfrac>
      <mo>+</mo>
      <mi>...</mi>
      <mo>+</mo>
      <mfrac>
        <msub>
          <mi>CF</mi>
          <mn>n</mn>
        </msub>
        <msup>
          <mrow>
            <mo>(</mo>
            <mn>1</mn>
            <mo>+</mo>
            <mi>IRR</mi>
            <mo>)</mo>
          </mrow>
          <mn>n</mn>
        </msup>
      </mfrac>
    </math>
  </div>
</figure>

<hr class="mt-2 mb-6 border-gray-300">

### Example

For a single cash inflow and outflow, calculating the IRR is relatively
straightforward. For example, say we made an investment of $1,000 three
years ago that just matured, providing us with a $1,405 payout.

What was the IRR of our investment?

#### Solution

Calculating the IRR requires solving the equation below

<figure>
  <math>
    <mi>NPV</mi>
    <mo>=</mo>
    <msub>
      <mi>CF</mi>
      <mn>0</mn>
    </msub>
    <mo>+</mo>
    <mfrac>
      <msub>
        <mi>CF</mi>
        <mn>3</mn>
      </msub>
      <msup>
        <mrow>
          <mo>(</mo>
          <mn>1</mn>
          <mo>+</mo>
          <mi>IRR</mi>
          <mo>)</mo>
        </mrow>
        <mn>3</mn>
      </msup>
    </mfrac>
  </math>
</figure>

Given that:

<ul class="list-disc text-base font-medium pl-6 text-gray-800">
  <li><var>NPV</var> must equal <b>$0</b></li>
  <li><var>CF<sub>0</sub></var> is <b>-$1,000</b></li>
  <li><var>CF<sub>3</sub></var> is <b>$1,405</b></li>
</ul>

However, a much simpler approach is to rely on a spreadsheet to calculate
the IRR. The easiest spreadsheet tool to use is the
[XIRR function](https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d){:target="_blank"}
which requires dates, but allows for uneven payment timing.

For our example, we can pick a random initial investment date–here we
picked January 1st, 2020 and a payout date three years later
(December 31, 2022).

<figure>
  <div class="w-3/5 flex flex-col">
    <img src="/img/concepts/2-foundation-concepts/xirr-usage-screenshot.svg" alt="XIRR usage screenshot">
  </div>
  <figcaption>XIRR spreadsheet function usage</figcaption>
</figure>

The XIRR function gives us an IRR of 12.00%.

### Issues with IRR

Like NPV, IRR can be used to rank different investment options, but it’s
important to note a couple of limitations:

1. IRR is a percentage return and does not factor in scale. Deciding on one
   investment over another could overlook the relative scale of the two
   options – with a higher IRR investment earning only a fraction of the NPV of
   a much larger, but lower IRR investment. An extreme example would be a huge
   company investing in a lemonade stand–the IRR might be great, but the
   NPV versus investing in the next generation of their product would be
   miniscule.

2. IRR also assumes that the cash flows from an investment can be reinvested at
   the same return–an assumption that is often unrealistic which can lead to the
   overestimation of returns.

<hr class="mt-2 mb-6 border-gray-300">

### Exercise

Let’s say that as an investor you typically expect 6.0% returns per year,
however two extraordinary investment opportunities presented themselves
and unfortunately you can only choose one of them.

The choices are:

<ul class="list-disc pl-8 text-gray-800 text-base pb-4 leading-8">
  <li><b>Investment #1</b> is a one-year investment with an IRR of 50%.</li>
  <li><b>Investment #2</b> is a five-year investment with an IRR of 18%.</li>
</ul>

Feel free to use the attached worksheet to complete the following tasks.

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - IRR - Worksheet.xlsx">IRR - Worksheet.xlsx</a>
  <a download href="/sheets/ReturnSuite - IRR - Worksheet.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

#### Task 1

Which investment should you choose if your only goal is to maximize the
total value of your portfolio by the end of year 5?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      While Investment #1 has a higher IRR, the initial returns can only be
      reinvested at the typical IRR of 6.0% after the one-year investment
      is complete. So over a five-year time horizon you shouldn’t expect to
      continue to achieve the 50% IRR, instead earning an expected 6.0%
      between years two to five–therefore <b>Investment #2</b>, even at a
      lower IRR of is the preferable investment.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Task 2

What is the expected IRR over the five years for each of the investment options?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      There are two ways to approach this question. The first is to use the
      NPV formula to solve for IRR and the second is to use the XIRR
      function within the spreadsheet.
    </p>
    <p>
      Note: Investment #1 is two investments–at the end of Year #1, the
      first investment has a cash inflow of $1,500 for the investor, but
      that is immediately reinvested for the next four years at the 6.0%
      return. Therefore, at the end of Year 1 there is both a cash inflow
      and a cash outflow resulting in a net cash flow of <b>$0</b>.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Task 3

What is the NPV of each investment option?

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      There are two ways to approach this question.
    </p>
    <h4>Method 1</h4>
    <ol class="list-decimal pl-8 text-gray-800 text-base pb-4 leading-8">
      <li>Use the forecasted Future Values from Task #1 to build an expected cash flow forecast.</li>
      <li>Using the Cost of Capital, build a Discount Factor for each of the years.</li>
      <li>Divide each of the Future Values by the Discount Factor to determine the Present Values of each cash flow.</li>
      <li>The NPV of each investment option is the sum of their PV cash flows.</li>
    </ol>
    <h4>Method 2</h4>
    <ol class="list-decimal pl-8 text-gray-800 text-base pb-4 leading-8">
      <li>Use the forecasted Future Values from Task #1 to build an expected cash flow forecast and include a column of dates.</li>
      <li>
        Use the
        <a target="_blank" href="https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7">XNPV spreadsheet function</a>
        to calculate the NPVs of each of the investment options.
      </li>
    </ol>
    <p>
      Note: The <b>XNPV function</b> can’t have empty cells in the date or
      cash flow ranges–make sure to fill in dates or $0 for any cells that
      are being referred to.
    </p>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

#### Solution

Compare your answer against the solutions in this spreadsheet.

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - IRR - Solutions.xlsx">IRR - Solutions.xlsx</a>
  <a download href="/sheets/ReturnSuite - IRR - Solutions.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

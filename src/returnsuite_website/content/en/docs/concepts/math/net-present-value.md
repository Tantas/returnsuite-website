---
title: Overview - Key Math Concepts used in Finance - ReturnSuite Docs
description: TODO - Add a description
nav-title: Net present value
nav-group: Key Math Concepts in Finance
---

# Net Present Value

## How net present value is calculated and used in real estate

A closely related concept to Present and Future Value is Net Present Value
(NPV). NPV is a measure of profitability that discounts all future cash
inflows to their present value and subtracts the present value of the
outflows that were required to earn them.

<figure>
  <math>
    <mi>NPV</mi>
    <mo>=</mo>
    <msub>
      <mi>PV</mi>
      <mi>cash inflows</mi>
    </msub>
    <mo>-</mo>
    <msub>
      <mi>PV</mi>
      <mi>cash outflows</mi>
    </msub>
  </math>
</figure>

Comparing the NPV of different investment options allows investors to
evaluate their relative attractiveness.

A positive NPV indicates the investment is worth pursuing as the future
returns outweigh the money we need to forgo today, even when factoring in
the time value of money.

A negative NPV indicates the investment doesn’t earn future returns that
cover the Cost of Capital, and an NPV of zero indicates that an investor
should be indifferent to investing.

In commercial real estate, the technique is used to evaluate investment
properties by determining the Present Value of all the future cash inflows
and outflows expected during the entire ownership cycle of the
property–boiling those cash flows down to a single number.

<hr class="mt-2 mb-6 border-gray-300">

## Example

Let’s say we had a real estate investment that offered us $115 next year
for an investment of $100 now. If our Discount Rate was 8%, what would be
the NPV of the investment?

Let’s say we had a real estate investment that offered us $115 next year
for an investment of $100 now. If our Discount Rate was 8%, what would be
the NPV of the investment?

To determine the NPV of the investment, we need to calculate the Present
Value of each cash flow. Those Present Values would then be summed up.

The Present Value of the cash inflow is $106.48 and the Present Value of
the cash outflow is $100. Therefore, the Net Present Value of the
opportunity to our investor is $6.48.

<figure>
  <div class="flex flex-col gap-4 place-items-start">
    <math>
      <mi>NPV</mi>
      <mo>=</mo>
      <msub>
        <mi>PV</mi>
        <mi>cash inflows</mi>
      </msub>
      <mo>-</mo>
      <msub>
        <mi>PV</mi>
        <mi>cash outflows</mi>
      </msub>
    </math>
    <math>
      <mi>NPV</mi>
      <mo>=</mo>
      <mn>$106.48</mn>
      <mo>-</mo>
      <mn>$100</mn>
    </math>
    <math>
      <mi>NPV</mi>
      <mo>=</mo>
      <mn>$6.48</mn>
    </math>
  </div>
</figure>

With a positive NPV, the investment covers our Cost of Capital and would
therefore be a good investment.

## Discount factor

An alternative way to calculate a large series of Present Values is to
determine the Discount Factor (not to be confused with the related
Discount Rate) in each period and divide the net Future Value cash flows
of that period by the Discount Factor.

The Discount Factor is the denominator of the Present Value formula and is
an index representing the hurdle to cover the Cost of Capital in any given
period.

<figure>
  <div class="flex flex-col place-items-start gap-6">
    <math>
      <mi>PV</mi>
      <mo>=</mo>
      <mfrac>
        <mpadded height="1.2em" voffset="0.2em">
          <mn>FV</mn>
        </mpadded>
        <mpadded height="1.1em">
          <msup>
            <mrow>
              <mo>(</mo>
              <mn>1</mn>
              <mo>+</mo>
              <mi>r</mi>
              <mo>)</mo>
            </mrow>
            <mi>n</mi>
          </msup>
        </mpadded>
      </mfrac>
      <mo>=</mo>
      <mfrac>
        <mpadded height="1.2em" voffset="0.2em">
          <mn>FV</mn>
        </mpadded>
        <mpadded height="1.1em">
          <mn>Discount Factor</mn>
        </mpadded>
      </mfrac>
    </math>
    <math>
      <mi>Discount Factor</mi>
      <mo>=</mo>
      <msup>
        <mrow>
          <mo>(</mo>
          <mn>1</mn>
          <mo>+</mo>
          <mi>r</mi>
          <mo>)</mo>
        </mrow>
        <mi>n</mi>
      </msup>
    </math>
  </div>
</figure>

For example, if you had a series of cash flows and a Discount Rate of 10%,
the Discount Factor could be used to determine the Present Value of all
the cash flows in each period. The Discount Factor can then divide each net cash
flow in Future Values to arrive at the net cash flow in Present Values, with the
Net Present Value being equal to the sum of all the Present Values.

<figure>
  <div class="rounded-md shadow-sm border border-gray-300 overflow-auto max-w-fit pt-3">
    <table class="table-auto border-collapse font-medium">
      <thead>
        <tr>
          <th></th>
          <th colspan="5">Period</th>
        </tr>
        <tr>
          <th class="border-b border-gray-300 pb-3 font-semibold text-left px-8 whitespace-nowrap">Future Values</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">0</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">1</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">2</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">3</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">4</th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700 border-r">Cash inflows</th>
          <td class="border-b py-3 text-right px-8">-</td>
          <td class="border-b py-3 text-right px-8">$500</td>
          <td class="border-b py-3 text-right px-8">$400</td>
          <td class="border-b py-3 text-right px-8">$650</td>
          <td class="border-b py-3 text-right px-8">$1,800</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Cash outflows</th>
          <td class="border-b py-3 text-right px-8 text-red-500">-$1,000</td>
          <td class="border-b py-3 text-right px-8 text-red-500">-$100</td>
          <td class="border-b py-3 text-right px-8">-</td>
          <td class="border-b py-3 text-right px-8 text-red-500">-$50</td>
          <td class="border-b py-3 text-right px-8 text-red-500">-$200</td>
        </tr>
        <tr class="bg-white">
          <th class="border-b py-3 font-semibold text-left px-8 whitespace-nowrap">Net cash flows (FV)</th>
          <td class="border-b py-3 text-right px-8 font-semibold text-red-500">-$1,000</td>
          <td class="border-b py-3 text-right px-8 font-semibold">$400</td>
          <td class="border-b py-3 text-right px-8 font-semibold">$400</td>
          <td class="border-b py-3 text-right px-8 font-semibold">$600</td>
          <td class="border-b py-3 text-right px-8 font-semibold">$1,600</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Discount Factor</th>
          <td class="border-b py-3 text-right px-8">1</td>
          <td class="border-b py-3 text-right px-8">1.1</td>
          <td class="border-b py-3 text-right px-8">1.21</td>
          <td class="border-b py-3 text-right px-8">1.331</td>
          <td class="border-b py-3 text-right px-8">1.4641</td>
        </tr>
        <tr class="bg-white">
          <th class="py-3 font-semibold text-left px-8 whitespace-nowrap">Net cash flows (PV)</th>
          <td class="py-3 text-right px-8 font-semibold text-red-500">-$1,000</td>
          <td class="py-3 text-right px-8 font-semibold">$364</td>
          <td class="py-3 text-right px-8 font-semibold">$331</td>
          <td class="py-3 text-right px-8 font-semibold">$451</td>
          <td class="py-3 text-right px-8 font-semibold">$1,093</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="py-3 font-semibold text-left px-8 whitespace-nowrap">Net Present Value</th>
          <td class="py-3 text-right px-8 font-semibold">$1,238</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
  </div>
  <figcaption>Sample application of discount rate to cash flows</figcaption>
</figure>

<hr class="mt-2 mb-6 border-gray-300">

## Exercise

A property owner has two choices to attract a potential tenant on a five-year
lease:

<ul class="list-disc pl-8 font-medium text-gray-800 text-base pb-4 leading-8">
  <li><b>Option #1</b> - Tenant pays an annual rent of $120,000 per year with no landlord contribution to tenant improvements, or</li>
  <li><b>Option #2</b> - Tenant pays an annual rent of $140,000 per year, but the landlord makes a $90,000 upfront tenant improvement contribution.</li>
</ul>

If the Landlord’s Cost of Capital is 8%, what is the NPV of each of the
options? Which option is preferable?

<div class="documentation-download">
  <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
  <a download href="/sheets/ReturnSuite - NPV - Worksheet.xlsx">NPV - Worksheet.xlsx</a>
  <a download href="/sheets/ReturnSuite - NPV - Worksheet.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
    <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
      <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
    </svg>
  </a>
</div>

<hr class="mt-2 mb-6 border-gray-300">

### Task 1

If the Landlord’s Cost of Capital is 8%, what is the NPV of each of the
options? Which option is preferable?

Use the spreadsheet to calculate the NPV of each option.

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show hint
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Hint</span>
    <p>
      Ignoring the Time Value of Money, <b>Option #2</b> earns more cash,
    even with the landlord's contribution towards tenant improvements.
    </p>
    <figure>
      <div class="rounded-md shadow-sm border border-gray-300 overflow-auto max-w-fit pt-3">
        <table class="table-auto border-collapse font-medium">
          <thead>
            <tr>
              <th class="border-b border-gray-300 pb-3 font-semibold text-left px-8 whitespace-nowrap"></th>
              <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Option #1</th>
              <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Option #2</th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-white">
              <th class="border-b py-3 font-semibold text-left px-8 whitespace-nowrap">Total Rent Received</th>
              <td class="border-b py-3 text-right px-8 font-semibold">$600,000</td>
              <td class="border-b py-3 text-right px-8 font-semibold">$700,000</td>
            </tr>
            <tr class="bg-gray-50">
              <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">Less: Tenant Improvement Contribution</th>
              <td class="border-b py-3 text-right px-8">$0</td>
              <td class="border-b py-3 text-right px-8 text-red-500">-$90,000</td>
            </tr>
            <tr class="bg-white">
              <th class="py-3 font-semibold text-left px-8 whitespace-nowrap">Net Cash Received</th>
              <td class="py-3 text-right px-8 font-semibold">$600,000</td>
              <td class="py-3 text-right px-8 font-semibold">$610,000</td>
            </tr>
          </tbody>
        </table>
      </div>
    </figure>
    <p>
      But in order to properly answer the question, one additional piece of
      information is needed–what is the landlord’s Opportunity Cost of
      Capital?.
    </p>
    <p>
      If the Landlord’s Cost of Capital is 8%, then the Net Present Value
      (NPV) of the cash flows generated from Option #1 is <b>$517,455</b>
      and the NPV of Option #2 is <b>$513,638</b>.
    </p>
  </div>
</div>

<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show solution
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Solution</span>
    <p>
      Compare your answer against the solution in this spreadsheet
    </p>
    <div class="documentation-download">
      <img src="/img/integration/excel.svg" alt="Microsoft Excel Logo" class="h-10">
      <a download href="/sheets/ReturnSuite - NPV - Solution.xlsx">NPV - Solution.xlsx</a>
      <a download href="/sheets/ReturnSuite - NPV - Solution.xlsx" title="Download" class="ml-auto hover:bg-gray-100 hover:text-gray-800 rounded-full p-2">
        <svg class="inline-block h-8" viewBox="0 -960 960 960" fill="currentColor">
          <path d="M480-320 280-520l56-58 104 104v-326h80v326l104-104 56 58-200 200ZM240-160q-33 0-56.5-23.5T160-240v-120h80v120h480v-120h80v120q0 33-23.5 56.5T720-160H240Z"></path>
        </svg>
      </a>
    </div>
    <p>
      Let’s take a closer look at Option #2 and see what is happening
      ‘underneath the hood’:
    </p>
    <ul class="list-disc pl-8 text-gray-800 text-base pb-4 leading-8">
      <li>
        The Rental Income line shows the projected cash flows from rent
        (<b>$140,000</b> per year). These cash flows are the actual dollars
        the landlord is expected to receive on the anniversary date of the
        lease.
      </li>
      <li>
        The Tenant Improvement Contribution line (more specifically in the
        first year) shows the landlord’s initial cash outflows up front
        (<b>-$90,000</b>).
      </li>
      <li>
        The Discount Factor is an intermediate step, the number by which the
        projected cash flows are divided to determine their Present Value.
        <ul class="list-[circle] pl-8 text-gray-800 text-base pb-4 leading-8">
          <li>
            The discount factor is 1 in Year 1 since we don't have to
            discount today’s dollars to get to their Present Value, but in
            each subsequent year, the Discount Factor increases by 8.0%. It
            compounds, so while the Discount Factor is 1.08 in Year 2, it is
            1.1664 in Year 3 (1.08x1.08), rather than simply 1.16.
          </li>
        </ul>
      </li>
    </ul>
  </div>
</div>

<hr class="mt-2 mb-6 border-gray-300">

### Task 2: A feel for the dynamics

Using your completed spreadsheet, watch how each of the following changes
flips the landlord’s preferred choice:

<ol class="list-decimal pl-8 font-medium text-gray-800 text-base pb-4 leading-8">
  <li>Decrease the Discount Rate to <b>5%</b></li>
  <li>Then, reduce the annual rent for Option #2 to <b>$135,000</b> per year</li>
  <li>Then, adjust the end value of the tenant improvements (<i>cell D26</i>) to <b>$30,000</b></li>
</ol>
<div x-data="{showHint: false}" class="pb-4">
  <button type="button" @click="showHint = true" x-show="!showHint" class="button font-medium">
    Show solution
  </button>
  <div x-show="showHint" class="border border-green-500 rounded-md p-6">
    <span class="text-lg font-medium text-green-500 tracking-wide">Solution</span>
    <p>
      Each change in the variables flips the landlord's correct decision
      back and forth between the two options based on their NPV.
    </p>
    <p>Results of each change:</p>
    <figure>
      <div class="rounded-md shadow-sm border border-gray-300 overflow-auto max-w-fit pt-3">
        <table class="table-auto border-collapse font-medium">
          <thead>
            <tr>
              <th></th>
              <th colspan="2" class="pb-4 font-semibold text-center px-8 whitespace-nowrap tracking-wide">Net Present Value</th>
            </tr>
            <tr>
              <th class="border-b border-gray-300 pb-3 font-semibold text-left px-8 whitespace-nowrap"></th>
              <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Option #1</th>
              <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">Option #2</th>
            </tr>
          </thead>
          <tbody>
            <tr class="bg-white">
              <th class="border-b py-3 font-semibold text-left px-8 whitespace-nowrap">Starting NPVs</th>
              <td class="border-b py-3 text-right px-8 font-bold text-green-500">$517,455</td>
              <td class="border-b py-3 text-right px-8">$513,638</td>
            </tr>
            <tr class="bg-gray-50">
              <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
                <span class="mr-3">+</span>
                <span>Decreasing Discount Rates to 5%</span>
              </th>
              <td class="border-b py-3 text-right px-8">$545,514</td>
              <td class="border-b py-3 text-right px-8 font-bold text-green-500">$546,433</td>
            </tr>
            <tr class="bg-white">
              <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
                <span class="mr-3">+</span>
                <span>Reducing rent on Option #2 to $135,000 per year</span>
              </th>
              <td class="border-b py-3 text-right px-8 font-bold text-green-500">$545,514</td>
              <td class="border-b py-3 text-right px-8">$523,703</td>
            </tr>
            <tr class="bg-gray-50">
              <th class="py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
                <span class="mr-3">+</span>
                <span>Adj. end value of improvements to $30,000</span>
              </th>
              <td class="py-3 text-right px-8">$545,514</td>
              <td class="py-3 text-right px-8 font-bold text-green-500">$548,384</td>
            </tr>
          </tbody>
        </table>
      </div>
      <figcaption>Solution to Task 2</figcaption>
    </figure>
  </div>
</div>

---
title: TODO
description: TODO - Add a description
nav-title: Time Value of Money
nav-group: Key Math Concepts in Finance
---

# Time Value of Money

## Present Value, Future Value and the Time Value of Money

The Time Value of Money is a fundamental concept in finance. It says that
money can be invested today to earn a return in the future, and so it
follows that a dollar today is worth more than a dollar tomorrow. This
economic theory is used to examine the trade-offs we face in our decision
to keep (or spend) our money today, or to forfeit it for more money in
the future.

Real estate is a capital-intensive business, usually requiring large
upfront investments to earn a long-term stream of smaller cash flows.
This makes the Time Value of Money an especially important tool in real
estate valuation.

Let’s say we had $100 and could use it to buy a government bond, getting
$108 returned to you a year from now. We refer to the $100 today as the
Present Value (Value at t=0) and the $108 as the Future Value (Value at
t=1).

<figure>
  <div class="w-3/5 flex flex-col">
    <img src="/img/concepts/2-foundation-concepts/time-value-of-money.jpg" alt="Time value of money">
    <ul class="list-disc pl-6 text-xl text-gray-800">
      <li><var class="font-semibold text-gray-900">t</var> is the time period</li>
    </ul>
  </div>
  <figcaption>Time value of money</figcaption>
</figure>

The difference between the Future Value and the Present Value is the
interest or price that is paid to borrow money, and in finance it is often
referred to as the Discount Rate. In our example, the government is paying
us $8 to borrow our $100 for the year, which is an 8% interest rate.

The concept of the Time Value of Money allows us to convert Present Values
to Future Values and vice versa.

The formula for calculating Present Value is:

<figure>
  <div class="flex flex-col gap-6">
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
    </math>
    <ul class="list-disc leading-7 text-gray-800 font-medium">
      <li><var class="font-semibold">PV</var> is the Present Value</li>
      <li><var class="font-semibold">FV</var> is the Future Value</li>
      <li><var class="font-semibold">r</var> is the Discount Rate (Opportunity Cost of Capital)</li>
      <li><var class="font-semibold">n</var> is the number of periods</li>
    </ul>
  </div>
</figure>

As long as we have any three of these pieces of information, we can
calculate the fourth.

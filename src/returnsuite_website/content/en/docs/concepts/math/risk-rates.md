---
title: The Risk-Free Rate and the Risk-Adjusted Discount Rate
description: How to determine the Risk-Free Rate and the Risk-Adjusted Discount Rate
nav-title: Risk rates
nav-group: Key Math Concepts in Finance
---

# The Risk-Free Rate and the Risk-Adjusted Discount Rate

## How to determine the Risk-Free Rate and the Risk-Adjusted Discount Rate

The Risk-Free Rate is the rate of return an investor can get on a
riskless investment while the Risk-Adjusted Discount Rate (RADR) is the
Discount Rate required by an investor to be compensated for all the
risks above and beyond the Risk-Free Rate.

Typically, government securities like US Treasury bills, UK Gilts, German
Bunds or Canadian Treasury bills are used as proxies for the Risk-Free
Rate since they are as close to riskless as possible. However, most
investments carry some degree of risk greater than government securities,
so when investors speak about Discount Rates, they are often referring to
the RADR or the All Risks Rate–the Rate that factors in all the risks
associated with the specific investment.

### RADR in Practise

A common method for determining an investment’s RADR is to begin with the
Risk-Free Rate and add on a premium for each different component of risk
that an investor is taking on with an investment. In real estate these
could include risks such as specific property risk, location risk,
tenant/credit risk, lease structure risk and an illiquidity premium.

Let’s say we were considering an investment in an office property. The
office is slightly older and considered a Class B property with a location
slightly off mass transit. The tenants are a mix of relatively strong
credit quality corporations, however a few of the leases are up for
renewal shortly. How should we go about determining their Discount Rate?

We would begin with the Risk-Free Rate–because of the long-term nature
of real estate investment, the yield on 10-year government bonds is
often used as a proxy for the Risk-Free Rate. We then may decide to
add on various risk premiums:

<ul class="list-disc pl-8 text-gray-800 text-base pb-2 leading-8">
  <li>1.0% risk premium to account for the property being older and risks being less attractive to potential tenants in the future</li>
  <li>0.5% risk premium to account for location risk</li>
  <li>1.25% risk premium to account for the tenants having lower creditworthiness than the government</li>
  <li>0.75% risk premium to adjust for the risk of tenant turnover with the upcoming lease expiries</li>
</ul>

<figure>
  <div class="rounded-md shadow-sm border border-gray-300 overflow-auto max-w-fit pt-3">
    <table class="table-auto border-collapse font-medium">
      <thead>
        <tr>
          <th class="border-b border-gray-300 pb-3 font-semibold text-left px-8 whitespace-nowrap">Risk Free Rate</th>
          <th class="border-b border-gray-300 pb-3 font-semibold text-right px-8 whitespace-nowrap tracking-wide">4.25%</th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
            <span class="mr-3">+</span>
            <span>Property Specific Risk</span>
          </th>
          <td class="border-b py-3 text-right px-8">1.0%</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
            <span class="mr-3">+</span>
            <span>Location Risk</span>
          </th>
          <td class="border-b py-3 text-right px-8">0.5%</td>
        </tr>
        <tr class="bg-white">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
            <span class="mr-3">+</span>
            <span>Credit Risk</span>
          </th>
          <td class="border-b py-3 text-right px-8">1.25%</td>
        </tr>
        <tr class="bg-gray-50">
          <th class="border-b py-3 font-medium text-left px-8 pl-12 whitespace-nowrap text-gray-700">
            <span class="mr-3">+</span>
            <span>Leasing Risk</span>
          </th>
          <td class="border-b py-3 text-right px-8">0.75%</td>
        </tr>
        <tr class="bg-white">
          <th class="py-3 font-semibold text-left px-8 whitespace-nowrap">Risk-Adjusted Discount Rate (RADR)</th>
          <td class="py-3 text-right px-8 font-semibold">7.75%</td>
        </tr>
      </tbody>
    </table>
  </div>
  <figcaption>Example RADR calculation</figcaption>
</figure>

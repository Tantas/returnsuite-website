---
title: Modeling real estate
description: How real estate model project cash flows
nav-title: Modeling real estate
nav-group: NOI and cash flow
---

# Inner workings of a real estate financial model

## How real estate model project cash flows

Big picture, what a financial model does is predict the amounts and
timings of all the cash inflows and outflows of the spaces that make up
a property within a set time frame.

In the physical world, a property can be divided up into spaces, which
at any point in time can either be leased or vacant. The cash inflow
predictions are a function of the current leases and the expected
replacement leases.

The lease status of a space directly affects cash inflows via rent, but
there are numerous indirect effects as well. The occupancy level of a
property affects other property revenue such as parking and signage. It
also affects any variable operating costs like cleaning, maintenance and
utilities. Tenant turnover can come with significant expenditures beyond
the missing rent, including broker commissions, free rent concessions
and tenant improvement allowances.

So what drives much of a financial model is the underlying leases and
their projected replacements–as one real estate operator put it,
Valuation tools are a function of “Stacking Leases”.
<sup><a href="#citation-1">1</a></sup>

Real estate financial models can be seen like a game of Tetris–the
existing leases at the bottom of the screen and a series of projected
leases dropping down from the top of the screen to fill in the gaps
caused by vacancies. The two layers of leases–existing and projected–are
then summed together to create the projected cash inflows of a property.

<figure>
  <div class="w-2/3 flex flex-col place-items-center">
    <img src="/img/concepts/4-noi-statement/leasing-rules.jpg" alt="Leasing rules" class="pr-32">
  </div>
  <figcaption>Leasing rules projecting future leases</figcaption>
</figure>

The projected leases are created using a set of Leasing Rules that are a
reasonable estimate for the future. For example, we may have a model
that handled vacancies from tenant turnover with the following leasing
rules:

<ul class="flex flex-col gap-1 list-disc pl-12">
  <li class="text-gray-800 text-lg">It takes six months to release the space</li>
  <li class="text-gray-800 text-lg">The new lease will be at the current market rent for that time period</li>
  <li class="text-gray-800 text-lg">The new tenant is expected to sign a five-year lease</li>
  <li class="text-gray-800 text-lg">
    To sign the tenant, the landlord will need to provide the tenant
    with three months Free Rent and a $5 per square foot tenant
    improvement contribution.</li>
  <li class="text-gray-800 text-lg">
    It’s expected that a 2% commission will be paid to a leasing agent
    upon signing the new lease.
  </li>
</ul>

Each time a space becomes vacant in our model, a projected lease is
created using these rules and is dropped into the vacancy.

So if we used the above leasing rules and a space was scheduled to
become vacant, our cash flow model would model a six-month vacancy
followed by a new five-year lease at the market rate (for that time
period). We’d also notice a cash outflow to cover the tenant improvement
allowance and commission to the leasing agent and a three-month delay in
receiving rental income because of the Free Rent period.

With that mental model, let’s go through building a NOI Statement
line-by-line.

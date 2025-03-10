---
title: TODO - ReturnSuite Docs
description: TODO - Add a description
nav-title: Property location
nav-group: Changing property details
---

# Property location

## Placing the property on the map

### Adding the property's location

It is recommended to add the property's location using the map's search widget
at the top left of the map. Input the properties location and select the correct
address. This will place the pin on the maps and fill out the form beneath.

Moving the pin on the map will update the latitude and longitude of the location
without altering the address information, allowing the exact location to be
adjusted.

The map integration may not determine all the address information or get a
perfect result. Manually override any additional information in the form below.

The neighborhood / sub-market field should reflect the sub-market as defined by
other properties in the real estate sector the property operates, rather than
the neighborhood a city-native may use.

All form fields are optional and may not apply to all countries.


##### Form fields

Latitude and longitude
:   The coordinates of the property. This is used to place the pin for the
    property when reporting.

Civic address
:   The practical address for the property. For Example, 100 Street Name Avenue.
    Multiple address lines can be used.

Legal address
:   The optional, precise legal definitional of the property. This should only
    be entered if the legal address is different from the civic address.

Neighborhood / Sub-market
:   The sub-market as defined by other properties in the real estate sector the
    in which the property operates.

City
:   The name of the city the property resides.

State / Province / Region
:   The second level administrative area. This is dependant on the country that
    the property resides.

Country
:   The country in which the property is located.

Zip code / Postal code
:   The mailing code for the property.


### Maps feature

The maps feature integrates with a third party service. The service provides
geocoding and places a pin on a map. Minimal information is sent to the third
party service.

The maps feature can be disabled for privacy reasons on a property in
`property → general settings`. When disabled, the geocoding function is not
available and all fields must be input manually.

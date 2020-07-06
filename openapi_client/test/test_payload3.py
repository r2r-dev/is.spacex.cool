# coding: utf-8

"""
    r/SpaceX API Docs

    ## Disclaimer *We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Space Exploration Technologies Inc (SpaceX), or any of its subsidiaries or its affiliates. The names SpaceX as well as related names, marks, emblems and images are registered trademarks of their respective owners.*  ## Base URL The most current version of the API is v3, with the following base URL `https://api.spacexdata.com/v3`  ## API Status See the [status](https://status.spacexdata.com) page for details  ## Authentication No authentication is required to use this public API  ## JSON Field Masking Smaller JSON payloads can be generated through the use of the `filter` querystring. When using this querystring, all fields not included in the query will be omitted from the response.  For example, on the launches endpoint, you could include `filter=flight_number` to only return the flight number of every launch. Nested JSON fields can be expressed using a forward slash for each nested level. Ex: `filter=rocket/second_stage/payloads` to only return the payload objects from each launch. Multiple filters can be listed using a comma separator Ex: `filter=rocket/second_stage/payloads,flight_number,mission_name`.  More information on the syntax can be found on the json-mask [github](https://github.com/nemtsov/json-mask) page.  ## Pagination All endpoints that return an array of objects can be paginated by using the `limit` and `offset` querystrings. This allows you to limit results and create pages of results to offset or skip.  On all endpoints that return an array, the header `spacex-api-count` is included with the total number of items in the array. This can be used to page through the results. By default, there is no limit set.  For example, the url `https://api.spacexdata.com/v3/launches?limit=1&offset=5` will only return launch #6, because we limited the results to a single launch, and skipped the first 5 launches using offset.  ## Pretty Printing JSON pretty printing is turned off by default to reduce payload size. It can be enabled by including the querystring `pretty=true` in the url. ```http GET https://api.spacexdata.com/v3/launches/latest?pretty=true ```  ## Privacy I do not log IP addresses or any personally identifiable information at the app or web server level. I collect timestamps, HTTP methods, urls, and response times to adjust caching strategies on popular endpoints. Below is a sample log line output: ```bash [27/Aug/2018:00:42:06 +0000] \"GET /v3/launches/latest HTTP/1.1\" 200 - 51.478 ms ```  I use [Cloudflare](https://www.cloudflare.com/) in front of the API. Please see their [privacy policy](https://www.cloudflare.com/privacypolicy/) for more details on data collection policies.  ## Rate Limiting The API has a rate limit of 50 req/sec per IP address, if exceeded, a response of 429 will be given until the rate drops back below 50 req/sec  ## Caching In general, the standard cache times are as follows:  * launches - 30 seconds * ships, payloads, roadster - 5 minutes * capsules, cores, launchpads, landpads - 1 hour * dragons, rockets, missions, history, company info - 24 hours  ## Date field FAQ's Dates and Date related field explanations:  `launch_year` - Year of the launch in string form (Will be deprecated soon)  `launch_date_unix` - UTC launch date/time as a UNIX timestamp in seconds  `launch_date_utc` - UTC launch date/time in ISO 8601 format  `launch_date_local` - Local launch time with time zone offset in ISO 8601 format  `is_tentative` - Set as true until a launch has an time attached to the date  `tentative_max_precision` - Gives the current known precision for the launch date. Valid values are `quarter`, `half`, `year`, `month`, `day`, `hour`. This allows us to give more context when representing partial dates like `November 2019` with a precision of `month`  `tbd` - Set as false when the date includes a day number or a day number with a time, otherwise the date is considered to be TBD and set as true  `upcoming` - Set as true until the moment of launch  `static_fire_date_utc` - UTC date/time for the rocket static fire test in ISO 8601 format  `static_fire_date_unix` - UTC date/time for the rocket static fire test as a UNIX timestamp in seconds  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.payload3 import Payload3  # noqa: E501
from openapi_client.rest import ApiException

class TestPayload3(unittest.TestCase):
    """Payload3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Payload3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payload3.Payload3()  # noqa: E501
        if include_optional :
            return Payload3(
                payload_id = '0', 
                norad_id = [
                    56
                    ], 
                reused = True, 
                customers = [
                    '0'
                    ], 
                nationality = '0', 
                manufacturer = '0', 
                payload_type = '0', 
                payload_mass_kg = 56, 
                payload_mass_lbs = 1.337, 
                orbit = '0', 
                orbit_params = {"reference_system":"geocentric","regime":"low-earth","longitude":null,"semi_major_axis_km":7155.799,"eccentricity":1.578E-4,"periapsis_km":776.534,"apoapsis_km":778.793,"inclination_deg":86.3952,"period_min":100.403,"lifespan_years":15,"epoch":"2019-02-04T11:45:18Z","mean_motion":14.34219278,"raan":37.5829,"arg_of_pericenter":49.2066,"mean_anomaly":310.9266}
            )
        else :
            return Payload3(
                payload_id = '0',
                norad_id = [
                    56
                    ],
                reused = True,
                customers = [
                    '0'
                    ],
                nationality = '0',
                manufacturer = '0',
                payload_type = '0',
                payload_mass_kg = 56,
                payload_mass_lbs = 1.337,
                orbit = '0',
                orbit_params = {"reference_system":"geocentric","regime":"low-earth","longitude":null,"semi_major_axis_km":7155.799,"eccentricity":1.578E-4,"periapsis_km":776.534,"apoapsis_km":778.793,"inclination_deg":86.3952,"period_min":100.403,"lifespan_years":15,"epoch":"2019-02-04T11:45:18Z","mean_motion":14.34219278,"raan":37.5829,"arg_of_pericenter":49.2066,"mean_anomaly":310.9266},
        )

    def testPayload3(self):
        """Test Payload3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

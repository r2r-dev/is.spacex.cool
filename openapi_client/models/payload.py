# coding: utf-8

"""
    r/SpaceX API Docs

    ## Disclaimer *We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Space Exploration Technologies Inc (SpaceX), or any of its subsidiaries or its affiliates. The names SpaceX as well as related names, marks, emblems and images are registered trademarks of their respective owners.*  ## Base URL The most current version of the API is v3, with the following base URL `https://api.spacexdata.com/v3`  ## API Status See the [status](https://status.spacexdata.com) page for details  ## Authentication No authentication is required to use this public API  ## JSON Field Masking Smaller JSON payloads can be generated through the use of the `filter` querystring. When using this querystring, all fields not included in the query will be omitted from the response.  For example, on the launches endpoint, you could include `filter=flight_number` to only return the flight number of every launch. Nested JSON fields can be expressed using a forward slash for each nested level. Ex: `filter=rocket/second_stage/payloads` to only return the payload objects from each launch. Multiple filters can be listed using a comma separator Ex: `filter=rocket/second_stage/payloads,flight_number,mission_name`.  More information on the syntax can be found on the json-mask [github](https://github.com/nemtsov/json-mask) page.  ## Pagination All endpoints that return an array of objects can be paginated by using the `limit` and `offset` querystrings. This allows you to limit results and create pages of results to offset or skip.  On all endpoints that return an array, the header `spacex-api-count` is included with the total number of items in the array. This can be used to page through the results. By default, there is no limit set.  For example, the url `https://api.spacexdata.com/v3/launches?limit=1&offset=5` will only return launch #6, because we limited the results to a single launch, and skipped the first 5 launches using offset.  ## Pretty Printing JSON pretty printing is turned off by default to reduce payload size. It can be enabled by including the querystring `pretty=true` in the url. ```http GET https://api.spacexdata.com/v3/launches/latest?pretty=true ```  ## Privacy I do not log IP addresses or any personally identifiable information at the app or web server level. I collect timestamps, HTTP methods, urls, and response times to adjust caching strategies on popular endpoints. Below is a sample log line output: ```bash [27/Aug/2018:00:42:06 +0000] \"GET /v3/launches/latest HTTP/1.1\" 200 - 51.478 ms ```  I use [Cloudflare](https://www.cloudflare.com/) in front of the API. Please see their [privacy policy](https://www.cloudflare.com/privacypolicy/) for more details on data collection policies.  ## Rate Limiting The API has a rate limit of 50 req/sec per IP address, if exceeded, a response of 429 will be given until the rate drops back below 50 req/sec  ## Caching In general, the standard cache times are as follows:  * launches - 30 seconds * ships, payloads, roadster - 5 minutes * capsules, cores, launchpads, landpads - 1 hour * dragons, rockets, missions, history, company info - 24 hours  ## Date field FAQ's Dates and Date related field explanations:  `launch_year` - Year of the launch in string form (Will be deprecated soon)  `launch_date_unix` - UTC launch date/time as a UNIX timestamp in seconds  `launch_date_utc` - UTC launch date/time in ISO 8601 format  `launch_date_local` - Local launch time with time zone offset in ISO 8601 format  `is_tentative` - Set as true until a launch has an time attached to the date  `tentative_max_precision` - Gives the current known precision for the launch date. Valid values are `quarter`, `half`, `year`, `month`, `day`, `hour`. This allows us to give more context when representing partial dates like `November 2019` with a precision of `month`  `tbd` - Set as false when the date includes a day number or a day number with a time, otherwise the date is considered to be TBD and set as true  `upcoming` - Set as true until the moment of launch  `static_fire_date_utc` - UTC date/time for the rocket static fire test in ISO 8601 format  `static_fire_date_unix` - UTC date/time for the rocket static fire test as a UNIX timestamp in seconds  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Payload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'payload_id': 'str',
        'norad_id': 'list[str]',
        'reused': 'bool',
        'customers': 'list[str]',
        'nationality': 'str',
        'manufacturer': 'str',
        'payload_type': 'str',
        'payload_mass_kg': 'int',
        'payload_mass_lbs': 'int',
        'orbit': 'str',
        'orbit_params': 'OrbitParams',
        'cap_serial': 'str',
        'mass_returned_kg': 'str',
        'mass_returned_lbs': 'str',
        'flight_time_sec': 'int',
        'cargo_manifest': 'str'
    }

    attribute_map = {
        'payload_id': 'payload_id',
        'norad_id': 'norad_id',
        'reused': 'reused',
        'customers': 'customers',
        'nationality': 'nationality',
        'manufacturer': 'manufacturer',
        'payload_type': 'payload_type',
        'payload_mass_kg': 'payload_mass_kg',
        'payload_mass_lbs': 'payload_mass_lbs',
        'orbit': 'orbit',
        'orbit_params': 'orbit_params',
        'cap_serial': 'cap_serial',
        'mass_returned_kg': 'mass_returned_kg',
        'mass_returned_lbs': 'mass_returned_lbs',
        'flight_time_sec': 'flight_time_sec',
        'cargo_manifest': 'cargo_manifest'
    }

    def __init__(self, payload_id=None, norad_id=None, reused=None, customers=None, nationality=None, manufacturer=None, payload_type=None, payload_mass_kg=None, payload_mass_lbs=None, orbit=None, orbit_params=None, cap_serial=None, mass_returned_kg=None, mass_returned_lbs=None, flight_time_sec=None, cargo_manifest=None, local_vars_configuration=None):  # noqa: E501
        """Payload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payload_id = None
        self._norad_id = None
        self._reused = None
        self._customers = None
        self._nationality = None
        self._manufacturer = None
        self._payload_type = None
        self._payload_mass_kg = None
        self._payload_mass_lbs = None
        self._orbit = None
        self._orbit_params = None
        self._cap_serial = None
        self._mass_returned_kg = None
        self._mass_returned_lbs = None
        self._flight_time_sec = None
        self._cargo_manifest = None
        self.discriminator = None

        self.payload_id = payload_id
        self.norad_id = norad_id
        self.reused = reused
        self.customers = customers
        self.nationality = nationality
        self.manufacturer = manufacturer
        self.payload_type = payload_type
        self.payload_mass_kg = payload_mass_kg
        self.payload_mass_lbs = payload_mass_lbs
        self.orbit = orbit
        self.orbit_params = orbit_params
        self.cap_serial = cap_serial
        self.mass_returned_kg = mass_returned_kg
        self.mass_returned_lbs = mass_returned_lbs
        self.flight_time_sec = flight_time_sec
        self.cargo_manifest = cargo_manifest

    @property
    def payload_id(self):
        """Gets the payload_id of this Payload.  # noqa: E501


        :return: The payload_id of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._payload_id

    @payload_id.setter
    def payload_id(self, payload_id):
        """Sets the payload_id of this Payload.


        :param payload_id: The payload_id of this Payload.  # noqa: E501
        :type: str
        """


        self._payload_id = payload_id

    @property
    def norad_id(self):
        """Gets the norad_id of this Payload.  # noqa: E501


        :return: The norad_id of this Payload.  # noqa: E501
        :rtype: list[str]
        """
        return self._norad_id

    @norad_id.setter
    def norad_id(self, norad_id):
        """Sets the norad_id of this Payload.


        :param norad_id: The norad_id of this Payload.  # noqa: E501
        :type: list[str]
        """


        self._norad_id = norad_id

    @property
    def reused(self):
        """Gets the reused of this Payload.  # noqa: E501


        :return: The reused of this Payload.  # noqa: E501
        :rtype: bool
        """
        return self._reused

    @reused.setter
    def reused(self, reused):
        """Sets the reused of this Payload.


        :param reused: The reused of this Payload.  # noqa: E501
        :type: bool
        """


        self._reused = reused

    @property
    def customers(self):
        """Gets the customers of this Payload.  # noqa: E501


        :return: The customers of this Payload.  # noqa: E501
        :rtype: list[str]
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this Payload.


        :param customers: The customers of this Payload.  # noqa: E501
        :type: list[str]
        """


        self._customers = customers

    @property
    def nationality(self):
        """Gets the nationality of this Payload.  # noqa: E501


        :return: The nationality of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this Payload.


        :param nationality: The nationality of this Payload.  # noqa: E501
        :type: str
        """

        self._nationality = nationality

    @property
    def manufacturer(self):
        """Gets the manufacturer of this Payload.  # noqa: E501


        :return: The manufacturer of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this Payload.


        :param manufacturer: The manufacturer of this Payload.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def payload_type(self):
        """Gets the payload_type of this Payload.  # noqa: E501


        :return: The payload_type of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this Payload.


        :param payload_type: The payload_type of this Payload.  # noqa: E501
        :type: str
        """


        self._payload_type = payload_type

    @property
    def payload_mass_kg(self):
        """Gets the payload_mass_kg of this Payload.  # noqa: E501


        :return: The payload_mass_kg of this Payload.  # noqa: E501
        :rtype: int
        """
        return self._payload_mass_kg

    @payload_mass_kg.setter
    def payload_mass_kg(self, payload_mass_kg):
        """Sets the payload_mass_kg of this Payload.


        :param payload_mass_kg: The payload_mass_kg of this Payload.  # noqa: E501
        :type: int
        """

        self._payload_mass_kg = payload_mass_kg

    @property
    def payload_mass_lbs(self):
        """Gets the payload_mass_lbs of this Payload.  # noqa: E501


        :return: The payload_mass_lbs of this Payload.  # noqa: E501
        :rtype: int
        """
        return self._payload_mass_lbs

    @payload_mass_lbs.setter
    def payload_mass_lbs(self, payload_mass_lbs):
        """Sets the payload_mass_lbs of this Payload.


        :param payload_mass_lbs: The payload_mass_lbs of this Payload.  # noqa: E501
        :type: int
        """

        self._payload_mass_lbs = payload_mass_lbs

    @property
    def orbit(self):
        """Gets the orbit of this Payload.  # noqa: E501


        :return: The orbit of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._orbit

    @orbit.setter
    def orbit(self, orbit):
        """Sets the orbit of this Payload.


        :param orbit: The orbit of this Payload.  # noqa: E501
        :type: str
        """


        self._orbit = orbit

    @property
    def orbit_params(self):
        """Gets the orbit_params of this Payload.  # noqa: E501


        :return: The orbit_params of this Payload.  # noqa: E501
        :rtype: OrbitParams
        """
        return self._orbit_params

    @orbit_params.setter
    def orbit_params(self, orbit_params):
        """Sets the orbit_params of this Payload.


        :param orbit_params: The orbit_params of this Payload.  # noqa: E501
        :type: OrbitParams
        """


        self._orbit_params = orbit_params

    @property
    def cap_serial(self):
        """Gets the cap_serial of this Payload.  # noqa: E501


        :return: The cap_serial of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._cap_serial

    @cap_serial.setter
    def cap_serial(self, cap_serial):
        """Sets the cap_serial of this Payload.


        :param cap_serial: The cap_serial of this Payload.  # noqa: E501
        :type: str
        """

        self._cap_serial = cap_serial

    @property
    def mass_returned_kg(self):
        """Gets the mass_returned_kg of this Payload.  # noqa: E501


        :return: The mass_returned_kg of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._mass_returned_kg

    @mass_returned_kg.setter
    def mass_returned_kg(self, mass_returned_kg):
        """Sets the mass_returned_kg of this Payload.


        :param mass_returned_kg: The mass_returned_kg of this Payload.  # noqa: E501
        :type: str
        """

        self._mass_returned_kg = mass_returned_kg

    @property
    def mass_returned_lbs(self):
        """Gets the mass_returned_lbs of this Payload.  # noqa: E501


        :return: The mass_returned_lbs of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._mass_returned_lbs

    @mass_returned_lbs.setter
    def mass_returned_lbs(self, mass_returned_lbs):
        """Sets the mass_returned_lbs of this Payload.


        :param mass_returned_lbs: The mass_returned_lbs of this Payload.  # noqa: E501
        :type: str
        """

        self._mass_returned_lbs = mass_returned_lbs

    @property
    def flight_time_sec(self):
        """Gets the flight_time_sec of this Payload.  # noqa: E501


        :return: The flight_time_sec of this Payload.  # noqa: E501
        :rtype: int
        """
        return self._flight_time_sec

    @flight_time_sec.setter
    def flight_time_sec(self, flight_time_sec):
        """Sets the flight_time_sec of this Payload.


        :param flight_time_sec: The flight_time_sec of this Payload.  # noqa: E501
        :type: int
        """

        self._flight_time_sec = flight_time_sec

    @property
    def cargo_manifest(self):
        """Gets the cargo_manifest of this Payload.  # noqa: E501


        :return: The cargo_manifest of this Payload.  # noqa: E501
        :rtype: str
        """
        return self._cargo_manifest

    @cargo_manifest.setter
    def cargo_manifest(self, cargo_manifest):
        """Sets the cargo_manifest of this Payload.


        :param cargo_manifest: The cargo_manifest of this Payload.  # noqa: E501
        :type: str
        """

        self._cargo_manifest = cargo_manifest

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Payload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payload):
            return True

        return self.to_dict() != other.to_dict()

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


class Roadster(object):
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
        'name': 'str',
        'launch_date_utc': 'str',
        'launch_date_unix': 'int',
        'launch_mass_kg': 'int',
        'launch_mass_lbs': 'int',
        'norad_id': 'int',
        'epoch_jd': 'float',
        'orbit_type': 'str',
        'apoapsis_au': 'float',
        'periapsis_au': 'float',
        'semi_major_axis_au': 'float',
        'eccentricity': 'float',
        'inclination': 'float',
        'longitude': 'float',
        'periapsis_arg': 'float',
        'period_days': 'float',
        'speed_kph': 'float',
        'speed_mph': 'float',
        'earth_distance_km': 'float',
        'earth_distance_mi': 'float',
        'mars_distance_km': 'float',
        'mars_distance_mi': 'float',
        'wikipedia': 'str',
        'details': 'str'
    }

    attribute_map = {
        'name': 'name',
        'launch_date_utc': 'launch_date_utc',
        'launch_date_unix': 'launch_date_unix',
        'launch_mass_kg': 'launch_mass_kg',
        'launch_mass_lbs': 'launch_mass_lbs',
        'norad_id': 'norad_id',
        'epoch_jd': 'epoch_jd',
        'orbit_type': 'orbit_type',
        'apoapsis_au': 'apoapsis_au',
        'periapsis_au': 'periapsis_au',
        'semi_major_axis_au': 'semi_major_axis_au',
        'eccentricity': 'eccentricity',
        'inclination': 'inclination',
        'longitude': 'longitude',
        'periapsis_arg': 'periapsis_arg',
        'period_days': 'period_days',
        'speed_kph': 'speed_kph',
        'speed_mph': 'speed_mph',
        'earth_distance_km': 'earth_distance_km',
        'earth_distance_mi': 'earth_distance_mi',
        'mars_distance_km': 'mars_distance_km',
        'mars_distance_mi': 'mars_distance_mi',
        'wikipedia': 'wikipedia',
        'details': 'details'
    }

    def __init__(self, name=None, launch_date_utc=None, launch_date_unix=None, launch_mass_kg=None, launch_mass_lbs=None, norad_id=None, epoch_jd=None, orbit_type=None, apoapsis_au=None, periapsis_au=None, semi_major_axis_au=None, eccentricity=None, inclination=None, longitude=None, periapsis_arg=None, period_days=None, speed_kph=None, speed_mph=None, earth_distance_km=None, earth_distance_mi=None, mars_distance_km=None, mars_distance_mi=None, wikipedia=None, details=None, local_vars_configuration=None):  # noqa: E501
        """Roadster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._launch_date_utc = None
        self._launch_date_unix = None
        self._launch_mass_kg = None
        self._launch_mass_lbs = None
        self._norad_id = None
        self._epoch_jd = None
        self._orbit_type = None
        self._apoapsis_au = None
        self._periapsis_au = None
        self._semi_major_axis_au = None
        self._eccentricity = None
        self._inclination = None
        self._longitude = None
        self._periapsis_arg = None
        self._period_days = None
        self._speed_kph = None
        self._speed_mph = None
        self._earth_distance_km = None
        self._earth_distance_mi = None
        self._mars_distance_km = None
        self._mars_distance_mi = None
        self._wikipedia = None
        self._details = None
        self.discriminator = None

        self.name = name
        self.launch_date_utc = launch_date_utc
        self.launch_date_unix = launch_date_unix
        self.launch_mass_kg = launch_mass_kg
        self.launch_mass_lbs = launch_mass_lbs
        self.norad_id = norad_id
        self.epoch_jd = epoch_jd
        self.orbit_type = orbit_type
        self.apoapsis_au = apoapsis_au
        self.periapsis_au = periapsis_au
        self.semi_major_axis_au = semi_major_axis_au
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.longitude = longitude
        self.periapsis_arg = periapsis_arg
        self.period_days = period_days
        self.speed_kph = speed_kph
        self.speed_mph = speed_mph
        self.earth_distance_km = earth_distance_km
        self.earth_distance_mi = earth_distance_mi
        self.mars_distance_km = mars_distance_km
        self.mars_distance_mi = mars_distance_mi
        self.wikipedia = wikipedia
        self.details = details

    @property
    def name(self):
        """Gets the name of this Roadster.  # noqa: E501


        :return: The name of this Roadster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Roadster.


        :param name: The name of this Roadster.  # noqa: E501
        :type: str
        """


        self._name = name

    @property
    def launch_date_utc(self):
        """Gets the launch_date_utc of this Roadster.  # noqa: E501


        :return: The launch_date_utc of this Roadster.  # noqa: E501
        :rtype: str
        """
        return self._launch_date_utc

    @launch_date_utc.setter
    def launch_date_utc(self, launch_date_utc):
        """Sets the launch_date_utc of this Roadster.


        :param launch_date_utc: The launch_date_utc of this Roadster.  # noqa: E501
        :type: str
        """


        self._launch_date_utc = launch_date_utc

    @property
    def launch_date_unix(self):
        """Gets the launch_date_unix of this Roadster.  # noqa: E501


        :return: The launch_date_unix of this Roadster.  # noqa: E501
        :rtype: int
        """
        return self._launch_date_unix

    @launch_date_unix.setter
    def launch_date_unix(self, launch_date_unix):
        """Sets the launch_date_unix of this Roadster.


        :param launch_date_unix: The launch_date_unix of this Roadster.  # noqa: E501
        :type: int
        """


        self._launch_date_unix = launch_date_unix

    @property
    def launch_mass_kg(self):
        """Gets the launch_mass_kg of this Roadster.  # noqa: E501


        :return: The launch_mass_kg of this Roadster.  # noqa: E501
        :rtype: int
        """
        return self._launch_mass_kg

    @launch_mass_kg.setter
    def launch_mass_kg(self, launch_mass_kg):
        """Sets the launch_mass_kg of this Roadster.


        :param launch_mass_kg: The launch_mass_kg of this Roadster.  # noqa: E501
        :type: int
        """


        self._launch_mass_kg = launch_mass_kg

    @property
    def launch_mass_lbs(self):
        """Gets the launch_mass_lbs of this Roadster.  # noqa: E501


        :return: The launch_mass_lbs of this Roadster.  # noqa: E501
        :rtype: int
        """
        return self._launch_mass_lbs

    @launch_mass_lbs.setter
    def launch_mass_lbs(self, launch_mass_lbs):
        """Sets the launch_mass_lbs of this Roadster.


        :param launch_mass_lbs: The launch_mass_lbs of this Roadster.  # noqa: E501
        :type: int
        """


        self._launch_mass_lbs = launch_mass_lbs

    @property
    def norad_id(self):
        """Gets the norad_id of this Roadster.  # noqa: E501


        :return: The norad_id of this Roadster.  # noqa: E501
        :rtype: int
        """
        return self._norad_id

    @norad_id.setter
    def norad_id(self, norad_id):
        """Sets the norad_id of this Roadster.


        :param norad_id: The norad_id of this Roadster.  # noqa: E501
        :type: int
        """


        self._norad_id = norad_id

    @property
    def epoch_jd(self):
        """Gets the epoch_jd of this Roadster.  # noqa: E501


        :return: The epoch_jd of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._epoch_jd

    @epoch_jd.setter
    def epoch_jd(self, epoch_jd):
        """Sets the epoch_jd of this Roadster.


        :param epoch_jd: The epoch_jd of this Roadster.  # noqa: E501
        :type: float
        """


        self._epoch_jd = epoch_jd

    @property
    def orbit_type(self):
        """Gets the orbit_type of this Roadster.  # noqa: E501


        :return: The orbit_type of this Roadster.  # noqa: E501
        :rtype: str
        """
        return self._orbit_type

    @orbit_type.setter
    def orbit_type(self, orbit_type):
        """Sets the orbit_type of this Roadster.


        :param orbit_type: The orbit_type of this Roadster.  # noqa: E501
        :type: str
        """


        self._orbit_type = orbit_type

    @property
    def apoapsis_au(self):
        """Gets the apoapsis_au of this Roadster.  # noqa: E501


        :return: The apoapsis_au of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._apoapsis_au

    @apoapsis_au.setter
    def apoapsis_au(self, apoapsis_au):
        """Sets the apoapsis_au of this Roadster.


        :param apoapsis_au: The apoapsis_au of this Roadster.  # noqa: E501
        :type: float
        """


        self._apoapsis_au = apoapsis_au

    @property
    def periapsis_au(self):
        """Gets the periapsis_au of this Roadster.  # noqa: E501


        :return: The periapsis_au of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._periapsis_au

    @periapsis_au.setter
    def periapsis_au(self, periapsis_au):
        """Sets the periapsis_au of this Roadster.


        :param periapsis_au: The periapsis_au of this Roadster.  # noqa: E501
        :type: float
        """


        self._periapsis_au = periapsis_au

    @property
    def semi_major_axis_au(self):
        """Gets the semi_major_axis_au of this Roadster.  # noqa: E501


        :return: The semi_major_axis_au of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._semi_major_axis_au

    @semi_major_axis_au.setter
    def semi_major_axis_au(self, semi_major_axis_au):
        """Sets the semi_major_axis_au of this Roadster.


        :param semi_major_axis_au: The semi_major_axis_au of this Roadster.  # noqa: E501
        :type: float
        """


        self._semi_major_axis_au = semi_major_axis_au

    @property
    def eccentricity(self):
        """Gets the eccentricity of this Roadster.  # noqa: E501


        :return: The eccentricity of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._eccentricity

    @eccentricity.setter
    def eccentricity(self, eccentricity):
        """Sets the eccentricity of this Roadster.


        :param eccentricity: The eccentricity of this Roadster.  # noqa: E501
        :type: float
        """


        self._eccentricity = eccentricity

    @property
    def inclination(self):
        """Gets the inclination of this Roadster.  # noqa: E501


        :return: The inclination of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._inclination

    @inclination.setter
    def inclination(self, inclination):
        """Sets the inclination of this Roadster.


        :param inclination: The inclination of this Roadster.  # noqa: E501
        :type: float
        """


        self._inclination = inclination

    @property
    def longitude(self):
        """Gets the longitude of this Roadster.  # noqa: E501


        :return: The longitude of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Roadster.


        :param longitude: The longitude of this Roadster.  # noqa: E501
        :type: float
        """


        self._longitude = longitude

    @property
    def periapsis_arg(self):
        """Gets the periapsis_arg of this Roadster.  # noqa: E501


        :return: The periapsis_arg of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._periapsis_arg

    @periapsis_arg.setter
    def periapsis_arg(self, periapsis_arg):
        """Sets the periapsis_arg of this Roadster.


        :param periapsis_arg: The periapsis_arg of this Roadster.  # noqa: E501
        :type: float
        """


        self._periapsis_arg = periapsis_arg

    @property
    def period_days(self):
        """Gets the period_days of this Roadster.  # noqa: E501


        :return: The period_days of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._period_days

    @period_days.setter
    def period_days(self, period_days):
        """Sets the period_days of this Roadster.


        :param period_days: The period_days of this Roadster.  # noqa: E501
        :type: float
        """


        self._period_days = period_days

    @property
    def speed_kph(self):
        """Gets the speed_kph of this Roadster.  # noqa: E501


        :return: The speed_kph of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._speed_kph

    @speed_kph.setter
    def speed_kph(self, speed_kph):
        """Sets the speed_kph of this Roadster.


        :param speed_kph: The speed_kph of this Roadster.  # noqa: E501
        :type: float
        """


        self._speed_kph = speed_kph

    @property
    def speed_mph(self):
        """Gets the speed_mph of this Roadster.  # noqa: E501


        :return: The speed_mph of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._speed_mph

    @speed_mph.setter
    def speed_mph(self, speed_mph):
        """Sets the speed_mph of this Roadster.


        :param speed_mph: The speed_mph of this Roadster.  # noqa: E501
        :type: float
        """


        self._speed_mph = speed_mph

    @property
    def earth_distance_km(self):
        """Gets the earth_distance_km of this Roadster.  # noqa: E501


        :return: The earth_distance_km of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._earth_distance_km

    @earth_distance_km.setter
    def earth_distance_km(self, earth_distance_km):
        """Sets the earth_distance_km of this Roadster.


        :param earth_distance_km: The earth_distance_km of this Roadster.  # noqa: E501
        :type: float
        """


        self._earth_distance_km = earth_distance_km

    @property
    def earth_distance_mi(self):
        """Gets the earth_distance_mi of this Roadster.  # noqa: E501


        :return: The earth_distance_mi of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._earth_distance_mi

    @earth_distance_mi.setter
    def earth_distance_mi(self, earth_distance_mi):
        """Sets the earth_distance_mi of this Roadster.


        :param earth_distance_mi: The earth_distance_mi of this Roadster.  # noqa: E501
        :type: float
        """


        self._earth_distance_mi = earth_distance_mi

    @property
    def mars_distance_km(self):
        """Gets the mars_distance_km of this Roadster.  # noqa: E501


        :return: The mars_distance_km of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._mars_distance_km

    @mars_distance_km.setter
    def mars_distance_km(self, mars_distance_km):
        """Sets the mars_distance_km of this Roadster.


        :param mars_distance_km: The mars_distance_km of this Roadster.  # noqa: E501
        :type: float
        """


        self._mars_distance_km = mars_distance_km

    @property
    def mars_distance_mi(self):
        """Gets the mars_distance_mi of this Roadster.  # noqa: E501


        :return: The mars_distance_mi of this Roadster.  # noqa: E501
        :rtype: float
        """
        return self._mars_distance_mi

    @mars_distance_mi.setter
    def mars_distance_mi(self, mars_distance_mi):
        """Sets the mars_distance_mi of this Roadster.


        :param mars_distance_mi: The mars_distance_mi of this Roadster.  # noqa: E501
        :type: float
        """


        self._mars_distance_mi = mars_distance_mi

    @property
    def wikipedia(self):
        """Gets the wikipedia of this Roadster.  # noqa: E501


        :return: The wikipedia of this Roadster.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia

    @wikipedia.setter
    def wikipedia(self, wikipedia):
        """Sets the wikipedia of this Roadster.


        :param wikipedia: The wikipedia of this Roadster.  # noqa: E501
        :type: str
        """


        self._wikipedia = wikipedia

    @property
    def details(self):
        """Gets the details of this Roadster.  # noqa: E501


        :return: The details of this Roadster.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Roadster.


        :param details: The details of this Roadster.  # noqa: E501
        :type: str
        """


        self._details = details

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
        if not isinstance(other, Roadster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Roadster):
            return True

        return self.to_dict() != other.to_dict()
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


class OrbitParams1(object):
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
        'reference_system': 'str',
        'regime': 'str',
        'longitude': 'int',
        'semi_major_axis_km': 'float',
        'eccentricity': 'float',
        'periapsis_km': 'float',
        'apoapsis_km': 'float',
        'inclination_deg': 'float',
        'period_min': 'float',
        'lifespan_years': 'int',
        'epoch': 'str',
        'mean_motion': 'float',
        'raan': 'float',
        'arg_of_pericenter': 'float',
        'mean_anomaly': 'float'
    }

    attribute_map = {
        'reference_system': 'reference_system',
        'regime': 'regime',
        'longitude': 'longitude',
        'semi_major_axis_km': 'semi_major_axis_km',
        'eccentricity': 'eccentricity',
        'periapsis_km': 'periapsis_km',
        'apoapsis_km': 'apoapsis_km',
        'inclination_deg': 'inclination_deg',
        'period_min': 'period_min',
        'lifespan_years': 'lifespan_years',
        'epoch': 'epoch',
        'mean_motion': 'mean_motion',
        'raan': 'raan',
        'arg_of_pericenter': 'arg_of_pericenter',
        'mean_anomaly': 'mean_anomaly'
    }

    def __init__(self, reference_system=None, regime=None, longitude=None, semi_major_axis_km=None, eccentricity=None, periapsis_km=None, apoapsis_km=None, inclination_deg=None, period_min=None, lifespan_years=None, epoch=None, mean_motion=None, raan=None, arg_of_pericenter=None, mean_anomaly=None, local_vars_configuration=None):  # noqa: E501
        """OrbitParams1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reference_system = None
        self._regime = None
        self._longitude = None
        self._semi_major_axis_km = None
        self._eccentricity = None
        self._periapsis_km = None
        self._apoapsis_km = None
        self._inclination_deg = None
        self._period_min = None
        self._lifespan_years = None
        self._epoch = None
        self._mean_motion = None
        self._raan = None
        self._arg_of_pericenter = None
        self._mean_anomaly = None
        self.discriminator = None

        self.reference_system = reference_system
        self.regime = regime
        self.longitude = longitude
        self.semi_major_axis_km = semi_major_axis_km
        self.eccentricity = eccentricity
        self.periapsis_km = periapsis_km
        self.apoapsis_km = apoapsis_km
        self.inclination_deg = inclination_deg
        self.period_min = period_min
        self.lifespan_years = lifespan_years
        self.epoch = epoch
        self.mean_motion = mean_motion
        self.raan = raan
        self.arg_of_pericenter = arg_of_pericenter
        self.mean_anomaly = mean_anomaly

    @property
    def reference_system(self):
        """Gets the reference_system of this OrbitParams1.  # noqa: E501


        :return: The reference_system of this OrbitParams1.  # noqa: E501
        :rtype: str
        """
        return self._reference_system

    @reference_system.setter
    def reference_system(self, reference_system):
        """Sets the reference_system of this OrbitParams1.


        :param reference_system: The reference_system of this OrbitParams1.  # noqa: E501
        :type: str
        """


        self._reference_system = reference_system

    @property
    def regime(self):
        """Gets the regime of this OrbitParams1.  # noqa: E501


        :return: The regime of this OrbitParams1.  # noqa: E501
        :rtype: str
        """
        return self._regime

    @regime.setter
    def regime(self, regime):
        """Sets the regime of this OrbitParams1.


        :param regime: The regime of this OrbitParams1.  # noqa: E501
        :type: str
        """


        self._regime = regime

    @property
    def longitude(self):
        """Gets the longitude of this OrbitParams1.  # noqa: E501


        :return: The longitude of this OrbitParams1.  # noqa: E501
        :rtype: int
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this OrbitParams1.


        :param longitude: The longitude of this OrbitParams1.  # noqa: E501
        :type: int
        """


        self._longitude = longitude

    @property
    def semi_major_axis_km(self):
        """Gets the semi_major_axis_km of this OrbitParams1.  # noqa: E501


        :return: The semi_major_axis_km of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._semi_major_axis_km

    @semi_major_axis_km.setter
    def semi_major_axis_km(self, semi_major_axis_km):
        """Sets the semi_major_axis_km of this OrbitParams1.


        :param semi_major_axis_km: The semi_major_axis_km of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._semi_major_axis_km = semi_major_axis_km

    @property
    def eccentricity(self):
        """Gets the eccentricity of this OrbitParams1.  # noqa: E501


        :return: The eccentricity of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._eccentricity

    @eccentricity.setter
    def eccentricity(self, eccentricity):
        """Sets the eccentricity of this OrbitParams1.


        :param eccentricity: The eccentricity of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._eccentricity = eccentricity

    @property
    def periapsis_km(self):
        """Gets the periapsis_km of this OrbitParams1.  # noqa: E501


        :return: The periapsis_km of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._periapsis_km

    @periapsis_km.setter
    def periapsis_km(self, periapsis_km):
        """Sets the periapsis_km of this OrbitParams1.


        :param periapsis_km: The periapsis_km of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._periapsis_km = periapsis_km

    @property
    def apoapsis_km(self):
        """Gets the apoapsis_km of this OrbitParams1.  # noqa: E501


        :return: The apoapsis_km of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._apoapsis_km

    @apoapsis_km.setter
    def apoapsis_km(self, apoapsis_km):
        """Sets the apoapsis_km of this OrbitParams1.


        :param apoapsis_km: The apoapsis_km of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._apoapsis_km = apoapsis_km

    @property
    def inclination_deg(self):
        """Gets the inclination_deg of this OrbitParams1.  # noqa: E501


        :return: The inclination_deg of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._inclination_deg

    @inclination_deg.setter
    def inclination_deg(self, inclination_deg):
        """Sets the inclination_deg of this OrbitParams1.


        :param inclination_deg: The inclination_deg of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._inclination_deg = inclination_deg

    @property
    def period_min(self):
        """Gets the period_min of this OrbitParams1.  # noqa: E501


        :return: The period_min of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._period_min

    @period_min.setter
    def period_min(self, period_min):
        """Sets the period_min of this OrbitParams1.


        :param period_min: The period_min of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._period_min = period_min

    @property
    def lifespan_years(self):
        """Gets the lifespan_years of this OrbitParams1.  # noqa: E501


        :return: The lifespan_years of this OrbitParams1.  # noqa: E501
        :rtype: int
        """
        return self._lifespan_years

    @lifespan_years.setter
    def lifespan_years(self, lifespan_years):
        """Sets the lifespan_years of this OrbitParams1.


        :param lifespan_years: The lifespan_years of this OrbitParams1.  # noqa: E501
        :type: int
        """


        self._lifespan_years = lifespan_years

    @property
    def epoch(self):
        """Gets the epoch of this OrbitParams1.  # noqa: E501


        :return: The epoch of this OrbitParams1.  # noqa: E501
        :rtype: str
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this OrbitParams1.


        :param epoch: The epoch of this OrbitParams1.  # noqa: E501
        :type: str
        """


        self._epoch = epoch

    @property
    def mean_motion(self):
        """Gets the mean_motion of this OrbitParams1.  # noqa: E501


        :return: The mean_motion of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._mean_motion

    @mean_motion.setter
    def mean_motion(self, mean_motion):
        """Sets the mean_motion of this OrbitParams1.


        :param mean_motion: The mean_motion of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._mean_motion = mean_motion

    @property
    def raan(self):
        """Gets the raan of this OrbitParams1.  # noqa: E501


        :return: The raan of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._raan

    @raan.setter
    def raan(self, raan):
        """Sets the raan of this OrbitParams1.


        :param raan: The raan of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._raan = raan

    @property
    def arg_of_pericenter(self):
        """Gets the arg_of_pericenter of this OrbitParams1.  # noqa: E501


        :return: The arg_of_pericenter of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._arg_of_pericenter

    @arg_of_pericenter.setter
    def arg_of_pericenter(self, arg_of_pericenter):
        """Sets the arg_of_pericenter of this OrbitParams1.


        :param arg_of_pericenter: The arg_of_pericenter of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._arg_of_pericenter = arg_of_pericenter

    @property
    def mean_anomaly(self):
        """Gets the mean_anomaly of this OrbitParams1.  # noqa: E501


        :return: The mean_anomaly of this OrbitParams1.  # noqa: E501
        :rtype: float
        """
        return self._mean_anomaly

    @mean_anomaly.setter
    def mean_anomaly(self, mean_anomaly):
        """Sets the mean_anomaly of this OrbitParams1.


        :param mean_anomaly: The mean_anomaly of this OrbitParams1.  # noqa: E501
        :type: float
        """


        self._mean_anomaly = mean_anomaly

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
        if not isinstance(other, OrbitParams1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrbitParams1):
            return True

        return self.to_dict() != other.to_dict()

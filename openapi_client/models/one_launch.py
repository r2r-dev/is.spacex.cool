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


class OneLaunch(object):
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
        'flight_number': 'int',
        'mission_name': 'str',
        'mission_id': 'list[str]',
        'launch_year': 'str',
        'launch_date_unix': 'int',
        'launch_date_utc': 'str',
        'launch_date_local': 'str',
        'is_tentative': 'bool',
        'tentative_max_precision': 'str',
        'tbd': 'bool',
        'launch_window': 'int',
        'rocket': 'Rocket1',
        'ships': 'list[str]',
        'telemetry': 'Telemetry1',
        'launch_site': 'LaunchSite',
        'launch_success': 'bool',
        'links': 'Links3',
        'details': 'str',
        'upcoming': 'bool',
        'static_fire_date_utc': 'str',
        'static_fire_date_unix': 'int',
        'timeline': 'Timeline1'
    }

    attribute_map = {
        'flight_number': 'flight_number',
        'mission_name': 'mission_name',
        'mission_id': 'mission_id',
        'launch_year': 'launch_year',
        'launch_date_unix': 'launch_date_unix',
        'launch_date_utc': 'launch_date_utc',
        'launch_date_local': 'launch_date_local',
        'is_tentative': 'is_tentative',
        'tentative_max_precision': 'tentative_max_precision',
        'tbd': 'tbd',
        'launch_window': 'launch_window',
        'rocket': 'rocket',
        'ships': 'ships',
        'telemetry': 'telemetry',
        'launch_site': 'launch_site',
        'launch_success': 'launch_success',
        'links': 'links',
        'details': 'details',
        'upcoming': 'upcoming',
        'static_fire_date_utc': 'static_fire_date_utc',
        'static_fire_date_unix': 'static_fire_date_unix',
        'timeline': 'timeline'
    }

    def __init__(self, flight_number=None, mission_name=None, mission_id=None, launch_year=None, launch_date_unix=None, launch_date_utc=None, launch_date_local=None, is_tentative=None, tentative_max_precision=None, tbd=None, launch_window=None, rocket=None, ships=None, telemetry=None, launch_site=None, launch_success=None, links=None, details=None, upcoming=None, static_fire_date_utc=None, static_fire_date_unix=None, timeline=None, local_vars_configuration=None):  # noqa: E501
        """OneLaunch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._flight_number = None
        self._mission_name = None
        self._mission_id = None
        self._launch_year = None
        self._launch_date_unix = None
        self._launch_date_utc = None
        self._launch_date_local = None
        self._is_tentative = None
        self._tentative_max_precision = None
        self._tbd = None
        self._launch_window = None
        self._rocket = None
        self._ships = None
        self._telemetry = None
        self._launch_site = None
        self._launch_success = None
        self._links = None
        self._details = None
        self._upcoming = None
        self._static_fire_date_utc = None
        self._static_fire_date_unix = None
        self._timeline = None
        self.discriminator = None

        self.flight_number = flight_number
        self.mission_name = mission_name
        self.mission_id = mission_id
        self.launch_year = launch_year
        self.launch_date_unix = launch_date_unix
        self.launch_date_utc = launch_date_utc
        self.launch_date_local = launch_date_local
        self.is_tentative = is_tentative
        self.tentative_max_precision = tentative_max_precision
        self.tbd = tbd
        self.launch_window = launch_window
        self.rocket = rocket
        self.ships = ships
        self.telemetry = telemetry
        self.launch_site = launch_site
        self.launch_success = launch_success
        self.links = links
        self.details = details
        self.upcoming = upcoming
        self.static_fire_date_utc = static_fire_date_utc
        self.static_fire_date_unix = static_fire_date_unix
        self.timeline = timeline

    @property
    def flight_number(self):
        """Gets the flight_number of this OneLaunch.  # noqa: E501


        :return: The flight_number of this OneLaunch.  # noqa: E501
        :rtype: int
        """
        return self._flight_number

    @flight_number.setter
    def flight_number(self, flight_number):
        """Sets the flight_number of this OneLaunch.


        :param flight_number: The flight_number of this OneLaunch.  # noqa: E501
        :type: int
        """


        self._flight_number = flight_number

    @property
    def mission_name(self):
        """Gets the mission_name of this OneLaunch.  # noqa: E501


        :return: The mission_name of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._mission_name

    @mission_name.setter
    def mission_name(self, mission_name):
        """Sets the mission_name of this OneLaunch.


        :param mission_name: The mission_name of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._mission_name = mission_name

    @property
    def mission_id(self):
        """Gets the mission_id of this OneLaunch.  # noqa: E501


        :return: The mission_id of this OneLaunch.  # noqa: E501
        :rtype: list[str]
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this OneLaunch.


        :param mission_id: The mission_id of this OneLaunch.  # noqa: E501
        :type: list[str]
        """


        self._mission_id = mission_id

    @property
    def launch_year(self):
        """Gets the launch_year of this OneLaunch.  # noqa: E501


        :return: The launch_year of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._launch_year

    @launch_year.setter
    def launch_year(self, launch_year):
        """Sets the launch_year of this OneLaunch.


        :param launch_year: The launch_year of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._launch_year = launch_year

    @property
    def launch_date_unix(self):
        """Gets the launch_date_unix of this OneLaunch.  # noqa: E501


        :return: The launch_date_unix of this OneLaunch.  # noqa: E501
        :rtype: int
        """
        return self._launch_date_unix

    @launch_date_unix.setter
    def launch_date_unix(self, launch_date_unix):
        """Sets the launch_date_unix of this OneLaunch.


        :param launch_date_unix: The launch_date_unix of this OneLaunch.  # noqa: E501
        :type: int
        """


        self._launch_date_unix = launch_date_unix

    @property
    def launch_date_utc(self):
        """Gets the launch_date_utc of this OneLaunch.  # noqa: E501


        :return: The launch_date_utc of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._launch_date_utc

    @launch_date_utc.setter
    def launch_date_utc(self, launch_date_utc):
        """Sets the launch_date_utc of this OneLaunch.


        :param launch_date_utc: The launch_date_utc of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._launch_date_utc = launch_date_utc

    @property
    def launch_date_local(self):
        """Gets the launch_date_local of this OneLaunch.  # noqa: E501


        :return: The launch_date_local of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._launch_date_local

    @launch_date_local.setter
    def launch_date_local(self, launch_date_local):
        """Sets the launch_date_local of this OneLaunch.


        :param launch_date_local: The launch_date_local of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._launch_date_local = launch_date_local

    @property
    def is_tentative(self):
        """Gets the is_tentative of this OneLaunch.  # noqa: E501


        :return: The is_tentative of this OneLaunch.  # noqa: E501
        :rtype: bool
        """
        return self._is_tentative

    @is_tentative.setter
    def is_tentative(self, is_tentative):
        """Sets the is_tentative of this OneLaunch.


        :param is_tentative: The is_tentative of this OneLaunch.  # noqa: E501
        :type: bool
        """


        self._is_tentative = is_tentative

    @property
    def tentative_max_precision(self):
        """Gets the tentative_max_precision of this OneLaunch.  # noqa: E501


        :return: The tentative_max_precision of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._tentative_max_precision

    @tentative_max_precision.setter
    def tentative_max_precision(self, tentative_max_precision):
        """Sets the tentative_max_precision of this OneLaunch.


        :param tentative_max_precision: The tentative_max_precision of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._tentative_max_precision = tentative_max_precision

    @property
    def tbd(self):
        """Gets the tbd of this OneLaunch.  # noqa: E501


        :return: The tbd of this OneLaunch.  # noqa: E501
        :rtype: bool
        """
        return self._tbd

    @tbd.setter
    def tbd(self, tbd):
        """Sets the tbd of this OneLaunch.


        :param tbd: The tbd of this OneLaunch.  # noqa: E501
        :type: bool
        """


        self._tbd = tbd

    @property
    def launch_window(self):
        """Gets the launch_window of this OneLaunch.  # noqa: E501


        :return: The launch_window of this OneLaunch.  # noqa: E501
        :rtype: int
        """
        return self._launch_window

    @launch_window.setter
    def launch_window(self, launch_window):
        """Sets the launch_window of this OneLaunch.


        :param launch_window: The launch_window of this OneLaunch.  # noqa: E501
        :type: int
        """


        self._launch_window = launch_window

    @property
    def rocket(self):
        """Gets the rocket of this OneLaunch.  # noqa: E501


        :return: The rocket of this OneLaunch.  # noqa: E501
        :rtype: Rocket1
        """
        return self._rocket

    @rocket.setter
    def rocket(self, rocket):
        """Sets the rocket of this OneLaunch.


        :param rocket: The rocket of this OneLaunch.  # noqa: E501
        :type: Rocket1
        """


        self._rocket = rocket

    @property
    def ships(self):
        """Gets the ships of this OneLaunch.  # noqa: E501


        :return: The ships of this OneLaunch.  # noqa: E501
        :rtype: list[str]
        """
        return self._ships

    @ships.setter
    def ships(self, ships):
        """Sets the ships of this OneLaunch.


        :param ships: The ships of this OneLaunch.  # noqa: E501
        :type: list[str]
        """


        self._ships = ships

    @property
    def telemetry(self):
        """Gets the telemetry of this OneLaunch.  # noqa: E501


        :return: The telemetry of this OneLaunch.  # noqa: E501
        :rtype: Telemetry1
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this OneLaunch.


        :param telemetry: The telemetry of this OneLaunch.  # noqa: E501
        :type: Telemetry1
        """


        self._telemetry = telemetry

    @property
    def launch_site(self):
        """Gets the launch_site of this OneLaunch.  # noqa: E501


        :return: The launch_site of this OneLaunch.  # noqa: E501
        :rtype: LaunchSite
        """
        return self._launch_site

    @launch_site.setter
    def launch_site(self, launch_site):
        """Sets the launch_site of this OneLaunch.


        :param launch_site: The launch_site of this OneLaunch.  # noqa: E501
        :type: LaunchSite
        """


        self._launch_site = launch_site

    @property
    def launch_success(self):
        """Gets the launch_success of this OneLaunch.  # noqa: E501


        :return: The launch_success of this OneLaunch.  # noqa: E501
        :rtype: bool
        """
        return self._launch_success

    @launch_success.setter
    def launch_success(self, launch_success):
        """Sets the launch_success of this OneLaunch.


        :param launch_success: The launch_success of this OneLaunch.  # noqa: E501
        :type: bool
        """


        self._launch_success = launch_success

    @property
    def links(self):
        """Gets the links of this OneLaunch.  # noqa: E501


        :return: The links of this OneLaunch.  # noqa: E501
        :rtype: Links3
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OneLaunch.


        :param links: The links of this OneLaunch.  # noqa: E501
        :type: Links3
        """


        self._links = links

    @property
    def details(self):
        """Gets the details of this OneLaunch.  # noqa: E501


        :return: The details of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this OneLaunch.


        :param details: The details of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._details = details

    @property
    def upcoming(self):
        """Gets the upcoming of this OneLaunch.  # noqa: E501


        :return: The upcoming of this OneLaunch.  # noqa: E501
        :rtype: bool
        """
        return self._upcoming

    @upcoming.setter
    def upcoming(self, upcoming):
        """Sets the upcoming of this OneLaunch.


        :param upcoming: The upcoming of this OneLaunch.  # noqa: E501
        :type: bool
        """


        self._upcoming = upcoming

    @property
    def static_fire_date_utc(self):
        """Gets the static_fire_date_utc of this OneLaunch.  # noqa: E501


        :return: The static_fire_date_utc of this OneLaunch.  # noqa: E501
        :rtype: str
        """
        return self._static_fire_date_utc

    @static_fire_date_utc.setter
    def static_fire_date_utc(self, static_fire_date_utc):
        """Sets the static_fire_date_utc of this OneLaunch.


        :param static_fire_date_utc: The static_fire_date_utc of this OneLaunch.  # noqa: E501
        :type: str
        """


        self._static_fire_date_utc = static_fire_date_utc

    @property
    def static_fire_date_unix(self):
        """Gets the static_fire_date_unix of this OneLaunch.  # noqa: E501


        :return: The static_fire_date_unix of this OneLaunch.  # noqa: E501
        :rtype: int
        """
        return self._static_fire_date_unix

    @static_fire_date_unix.setter
    def static_fire_date_unix(self, static_fire_date_unix):
        """Sets the static_fire_date_unix of this OneLaunch.


        :param static_fire_date_unix: The static_fire_date_unix of this OneLaunch.  # noqa: E501
        :type: int
        """


        self._static_fire_date_unix = static_fire_date_unix

    @property
    def timeline(self):
        """Gets the timeline of this OneLaunch.  # noqa: E501


        :return: The timeline of this OneLaunch.  # noqa: E501
        :rtype: Timeline1
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this OneLaunch.


        :param timeline: The timeline of this OneLaunch.  # noqa: E501
        :type: Timeline1
        """

        self._timeline = timeline

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
        if not isinstance(other, OneLaunch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneLaunch):
            return True

        return self.to_dict() != other.to_dict()

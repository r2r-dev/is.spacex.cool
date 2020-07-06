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


class AllLandingPad(object):
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
        'id': 'str',
        'full_name': 'str',
        'status': 'str',
        'location': 'Location',
        'landing_type': 'str',
        'attempted_landings': 'int',
        'successful_landings': 'int',
        'wikipedia': 'str',
        'details': 'str'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'full_name',
        'status': 'status',
        'location': 'location',
        'landing_type': 'landing_type',
        'attempted_landings': 'attempted_landings',
        'successful_landings': 'successful_landings',
        'wikipedia': 'wikipedia',
        'details': 'details'
    }

    def __init__(self, id=None, full_name=None, status=None, location=None, landing_type=None, attempted_landings=None, successful_landings=None, wikipedia=None, details=None, local_vars_configuration=None):  # noqa: E501
        """AllLandingPad - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._full_name = None
        self._status = None
        self._location = None
        self._landing_type = None
        self._attempted_landings = None
        self._successful_landings = None
        self._wikipedia = None
        self._details = None
        self.discriminator = None

        self.id = id
        self.full_name = full_name
        self.status = status
        self.location = location
        self.landing_type = landing_type
        self.attempted_landings = attempted_landings
        self.successful_landings = successful_landings
        self.wikipedia = wikipedia
        self.details = details

    @property
    def id(self):
        """Gets the id of this AllLandingPad.  # noqa: E501


        :return: The id of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllLandingPad.


        :param id: The id of this AllLandingPad.  # noqa: E501
        :type: str
        """


        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this AllLandingPad.  # noqa: E501


        :return: The full_name of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this AllLandingPad.


        :param full_name: The full_name of this AllLandingPad.  # noqa: E501
        :type: str
        """


        self._full_name = full_name

    @property
    def status(self):
        """Gets the status of this AllLandingPad.  # noqa: E501


        :return: The status of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AllLandingPad.


        :param status: The status of this AllLandingPad.  # noqa: E501
        :type: str
        """


        self._status = status

    @property
    def location(self):
        """Gets the location of this AllLandingPad.  # noqa: E501


        :return: The location of this AllLandingPad.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AllLandingPad.


        :param location: The location of this AllLandingPad.  # noqa: E501
        :type: Location
        """


        self._location = location

    @property
    def landing_type(self):
        """Gets the landing_type of this AllLandingPad.  # noqa: E501


        :return: The landing_type of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._landing_type

    @landing_type.setter
    def landing_type(self, landing_type):
        """Sets the landing_type of this AllLandingPad.


        :param landing_type: The landing_type of this AllLandingPad.  # noqa: E501
        :type: str
        """


        self._landing_type = landing_type

    @property
    def attempted_landings(self):
        """Gets the attempted_landings of this AllLandingPad.  # noqa: E501


        :return: The attempted_landings of this AllLandingPad.  # noqa: E501
        :rtype: int
        """
        return self._attempted_landings

    @attempted_landings.setter
    def attempted_landings(self, attempted_landings):
        """Sets the attempted_landings of this AllLandingPad.


        :param attempted_landings: The attempted_landings of this AllLandingPad.  # noqa: E501
        :type: int
        """


        self._attempted_landings = attempted_landings

    @property
    def successful_landings(self):
        """Gets the successful_landings of this AllLandingPad.  # noqa: E501


        :return: The successful_landings of this AllLandingPad.  # noqa: E501
        :rtype: int
        """
        return self._successful_landings

    @successful_landings.setter
    def successful_landings(self, successful_landings):
        """Sets the successful_landings of this AllLandingPad.


        :param successful_landings: The successful_landings of this AllLandingPad.  # noqa: E501
        :type: int
        """


        self._successful_landings = successful_landings

    @property
    def wikipedia(self):
        """Gets the wikipedia of this AllLandingPad.  # noqa: E501


        :return: The wikipedia of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia

    @wikipedia.setter
    def wikipedia(self, wikipedia):
        """Sets the wikipedia of this AllLandingPad.


        :param wikipedia: The wikipedia of this AllLandingPad.  # noqa: E501
        :type: str
        """


        self._wikipedia = wikipedia

    @property
    def details(self):
        """Gets the details of this AllLandingPad.  # noqa: E501


        :return: The details of this AllLandingPad.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AllLandingPad.


        :param details: The details of this AllLandingPad.  # noqa: E501
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
        if not isinstance(other, AllLandingPad):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllLandingPad):
            return True

        return self.to_dict() != other.to_dict()

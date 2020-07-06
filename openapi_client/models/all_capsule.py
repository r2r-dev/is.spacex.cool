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


class AllCapsule(object):
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
        'capsule_serial': 'str',
        'capsule_id': 'str',
        'status': 'str',
        'original_launch': 'str',
        'original_launch_unix': 'int',
        'missions': 'list[Mission]',
        'landings': 'int',
        'type': 'str',
        'details': 'str',
        'reuse_count': 'int'
    }

    attribute_map = {
        'capsule_serial': 'capsule_serial',
        'capsule_id': 'capsule_id',
        'status': 'status',
        'original_launch': 'original_launch',
        'original_launch_unix': 'original_launch_unix',
        'missions': 'missions',
        'landings': 'landings',
        'type': 'type',
        'details': 'details',
        'reuse_count': 'reuse_count'
    }

    def __init__(self, capsule_serial=None, capsule_id=None, status=None, original_launch=None, original_launch_unix=None, missions=None, landings=None, type=None, details=None, reuse_count=None, local_vars_configuration=None):  # noqa: E501
        """AllCapsule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capsule_serial = None
        self._capsule_id = None
        self._status = None
        self._original_launch = None
        self._original_launch_unix = None
        self._missions = None
        self._landings = None
        self._type = None
        self._details = None
        self._reuse_count = None
        self.discriminator = None

        self.capsule_serial = capsule_serial
        self.capsule_id = capsule_id
        self.status = status
        self.original_launch = original_launch
        self.original_launch_unix = original_launch_unix
        self.missions = missions
        self.landings = landings
        self.type = type
        self.details = details
        self.reuse_count = reuse_count

    @property
    def capsule_serial(self):
        """Gets the capsule_serial of this AllCapsule.  # noqa: E501


        :return: The capsule_serial of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._capsule_serial

    @capsule_serial.setter
    def capsule_serial(self, capsule_serial):
        """Sets the capsule_serial of this AllCapsule.


        :param capsule_serial: The capsule_serial of this AllCapsule.  # noqa: E501
        :type: str
        """


        self._capsule_serial = capsule_serial

    @property
    def capsule_id(self):
        """Gets the capsule_id of this AllCapsule.  # noqa: E501


        :return: The capsule_id of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._capsule_id

    @capsule_id.setter
    def capsule_id(self, capsule_id):
        """Sets the capsule_id of this AllCapsule.


        :param capsule_id: The capsule_id of this AllCapsule.  # noqa: E501
        :type: str
        """


        self._capsule_id = capsule_id

    @property
    def status(self):
        """Gets the status of this AllCapsule.  # noqa: E501


        :return: The status of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AllCapsule.


        :param status: The status of this AllCapsule.  # noqa: E501
        :type: str
        """


        self._status = status

    @property
    def original_launch(self):
        """Gets the original_launch of this AllCapsule.  # noqa: E501


        :return: The original_launch of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._original_launch

    @original_launch.setter
    def original_launch(self, original_launch):
        """Sets the original_launch of this AllCapsule.


        :param original_launch: The original_launch of this AllCapsule.  # noqa: E501
        :type: str
        """

        self._original_launch = original_launch

    @property
    def original_launch_unix(self):
        """Gets the original_launch_unix of this AllCapsule.  # noqa: E501


        :return: The original_launch_unix of this AllCapsule.  # noqa: E501
        :rtype: int
        """
        return self._original_launch_unix

    @original_launch_unix.setter
    def original_launch_unix(self, original_launch_unix):
        """Sets the original_launch_unix of this AllCapsule.


        :param original_launch_unix: The original_launch_unix of this AllCapsule.  # noqa: E501
        :type: int
        """

        self._original_launch_unix = original_launch_unix

    @property
    def missions(self):
        """Gets the missions of this AllCapsule.  # noqa: E501


        :return: The missions of this AllCapsule.  # noqa: E501
        :rtype: list[Mission]
        """
        return self._missions

    @missions.setter
    def missions(self, missions):
        """Sets the missions of this AllCapsule.


        :param missions: The missions of this AllCapsule.  # noqa: E501
        :type: list[Mission]
        """


        self._missions = missions

    @property
    def landings(self):
        """Gets the landings of this AllCapsule.  # noqa: E501


        :return: The landings of this AllCapsule.  # noqa: E501
        :rtype: int
        """
        return self._landings

    @landings.setter
    def landings(self, landings):
        """Sets the landings of this AllCapsule.


        :param landings: The landings of this AllCapsule.  # noqa: E501
        :type: int
        """


        self._landings = landings

    @property
    def type(self):
        """Gets the type of this AllCapsule.  # noqa: E501


        :return: The type of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllCapsule.


        :param type: The type of this AllCapsule.  # noqa: E501
        :type: str
        """


        self._type = type

    @property
    def details(self):
        """Gets the details of this AllCapsule.  # noqa: E501


        :return: The details of this AllCapsule.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AllCapsule.


        :param details: The details of this AllCapsule.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def reuse_count(self):
        """Gets the reuse_count of this AllCapsule.  # noqa: E501


        :return: The reuse_count of this AllCapsule.  # noqa: E501
        :rtype: int
        """
        return self._reuse_count

    @reuse_count.setter
    def reuse_count(self, reuse_count):
        """Sets the reuse_count of this AllCapsule.


        :param reuse_count: The reuse_count of this AllCapsule.  # noqa: E501
        :type: int
        """


        self._reuse_count = reuse_count

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
        if not isinstance(other, AllCapsule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllCapsule):
            return True

        return self.to_dict() != other.to_dict()

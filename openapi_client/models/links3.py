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


class Links3(object):
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
        'mission_patch': 'str',
        'mission_patch_small': 'str',
        'reddit_campaign': 'str',
        'reddit_launch': 'str',
        'reddit_recovery': 'str',
        'reddit_media': 'str',
        'presskit': 'str',
        'article_link': 'str',
        'wikipedia': 'str',
        'video_link': 'str',
        'youtube_id': 'str',
        'flickr_images': 'list[str]'
    }

    attribute_map = {
        'mission_patch': 'mission_patch',
        'mission_patch_small': 'mission_patch_small',
        'reddit_campaign': 'reddit_campaign',
        'reddit_launch': 'reddit_launch',
        'reddit_recovery': 'reddit_recovery',
        'reddit_media': 'reddit_media',
        'presskit': 'presskit',
        'article_link': 'article_link',
        'wikipedia': 'wikipedia',
        'video_link': 'video_link',
        'youtube_id': 'youtube_id',
        'flickr_images': 'flickr_images'
    }

    def __init__(self, mission_patch=None, mission_patch_small=None, reddit_campaign=None, reddit_launch=None, reddit_recovery=None, reddit_media=None, presskit=None, article_link=None, wikipedia=None, video_link=None, youtube_id=None, flickr_images=None, local_vars_configuration=None):  # noqa: E501
        """Links3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mission_patch = None
        self._mission_patch_small = None
        self._reddit_campaign = None
        self._reddit_launch = None
        self._reddit_recovery = None
        self._reddit_media = None
        self._presskit = None
        self._article_link = None
        self._wikipedia = None
        self._video_link = None
        self._youtube_id = None
        self._flickr_images = None
        self.discriminator = None

        self.mission_patch = mission_patch
        self.mission_patch_small = mission_patch_small
        self.reddit_campaign = reddit_campaign
        self.reddit_launch = reddit_launch
        self.reddit_recovery = reddit_recovery
        self.reddit_media = reddit_media
        self.presskit = presskit
        self.article_link = article_link
        self.wikipedia = wikipedia
        self.video_link = video_link
        self.youtube_id = youtube_id
        self.flickr_images = flickr_images

    @property
    def mission_patch(self):
        """Gets the mission_patch of this Links3.  # noqa: E501


        :return: The mission_patch of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._mission_patch

    @mission_patch.setter
    def mission_patch(self, mission_patch):
        """Sets the mission_patch of this Links3.


        :param mission_patch: The mission_patch of this Links3.  # noqa: E501
        :type: str
        """


        self._mission_patch = mission_patch

    @property
    def mission_patch_small(self):
        """Gets the mission_patch_small of this Links3.  # noqa: E501


        :return: The mission_patch_small of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._mission_patch_small

    @mission_patch_small.setter
    def mission_patch_small(self, mission_patch_small):
        """Sets the mission_patch_small of this Links3.


        :param mission_patch_small: The mission_patch_small of this Links3.  # noqa: E501
        :type: str
        """


        self._mission_patch_small = mission_patch_small

    @property
    def reddit_campaign(self):
        """Gets the reddit_campaign of this Links3.  # noqa: E501


        :return: The reddit_campaign of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._reddit_campaign

    @reddit_campaign.setter
    def reddit_campaign(self, reddit_campaign):
        """Sets the reddit_campaign of this Links3.


        :param reddit_campaign: The reddit_campaign of this Links3.  # noqa: E501
        :type: str
        """


        self._reddit_campaign = reddit_campaign

    @property
    def reddit_launch(self):
        """Gets the reddit_launch of this Links3.  # noqa: E501


        :return: The reddit_launch of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._reddit_launch

    @reddit_launch.setter
    def reddit_launch(self, reddit_launch):
        """Sets the reddit_launch of this Links3.


        :param reddit_launch: The reddit_launch of this Links3.  # noqa: E501
        :type: str
        """


        self._reddit_launch = reddit_launch

    @property
    def reddit_recovery(self):
        """Gets the reddit_recovery of this Links3.  # noqa: E501


        :return: The reddit_recovery of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._reddit_recovery

    @reddit_recovery.setter
    def reddit_recovery(self, reddit_recovery):
        """Sets the reddit_recovery of this Links3.


        :param reddit_recovery: The reddit_recovery of this Links3.  # noqa: E501
        :type: str
        """

        self._reddit_recovery = reddit_recovery

    @property
    def reddit_media(self):
        """Gets the reddit_media of this Links3.  # noqa: E501


        :return: The reddit_media of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._reddit_media

    @reddit_media.setter
    def reddit_media(self, reddit_media):
        """Sets the reddit_media of this Links3.


        :param reddit_media: The reddit_media of this Links3.  # noqa: E501
        :type: str
        """


        self._reddit_media = reddit_media

    @property
    def presskit(self):
        """Gets the presskit of this Links3.  # noqa: E501


        :return: The presskit of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._presskit

    @presskit.setter
    def presskit(self, presskit):
        """Sets the presskit of this Links3.


        :param presskit: The presskit of this Links3.  # noqa: E501
        :type: str
        """


        self._presskit = presskit

    @property
    def article_link(self):
        """Gets the article_link of this Links3.  # noqa: E501


        :return: The article_link of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._article_link

    @article_link.setter
    def article_link(self, article_link):
        """Sets the article_link of this Links3.


        :param article_link: The article_link of this Links3.  # noqa: E501
        :type: str
        """


        self._article_link = article_link

    @property
    def wikipedia(self):
        """Gets the wikipedia of this Links3.  # noqa: E501


        :return: The wikipedia of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia

    @wikipedia.setter
    def wikipedia(self, wikipedia):
        """Sets the wikipedia of this Links3.


        :param wikipedia: The wikipedia of this Links3.  # noqa: E501
        :type: str
        """


        self._wikipedia = wikipedia

    @property
    def video_link(self):
        """Gets the video_link of this Links3.  # noqa: E501


        :return: The video_link of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._video_link

    @video_link.setter
    def video_link(self, video_link):
        """Sets the video_link of this Links3.


        :param video_link: The video_link of this Links3.  # noqa: E501
        :type: str
        """


        self._video_link = video_link

    @property
    def youtube_id(self):
        """Gets the youtube_id of this Links3.  # noqa: E501


        :return: The youtube_id of this Links3.  # noqa: E501
        :rtype: str
        """
        return self._youtube_id

    @youtube_id.setter
    def youtube_id(self, youtube_id):
        """Sets the youtube_id of this Links3.


        :param youtube_id: The youtube_id of this Links3.  # noqa: E501
        :type: str
        """


        self._youtube_id = youtube_id

    @property
    def flickr_images(self):
        """Gets the flickr_images of this Links3.  # noqa: E501


        :return: The flickr_images of this Links3.  # noqa: E501
        :rtype: list[str]
        """
        return self._flickr_images

    @flickr_images.setter
    def flickr_images(self, flickr_images):
        """Sets the flickr_images of this Links3.


        :param flickr_images: The flickr_images of this Links3.  # noqa: E501
        :type: list[str]
        """


        self._flickr_images = flickr_images

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
        if not isinstance(other, Links3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Links3):
            return True

        return self.to_dict() != other.to_dict()

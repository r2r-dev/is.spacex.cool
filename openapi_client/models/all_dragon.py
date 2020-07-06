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


class AllDragon(object):
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
        'name': 'str',
        'type': 'str',
        'active': 'bool',
        'crew_capacity': 'int',
        'sidewall_angle_deg': 'int',
        'orbit_duration_yr': 'int',
        'dry_mass_kg': 'int',
        'dry_mass_lb': 'int',
        'first_flight': 'str',
        'heat_shield': 'HeatShield',
        'thrusters': 'list[Thruster]',
        'launch_payload_mass': 'LaunchPayloadMass',
        'launch_payload_vol': 'LaunchPayloadVol',
        'return_payload_mass': 'ReturnPayloadMass',
        'return_payload_vol': 'ReturnPayloadVol',
        'pressurized_capsule': 'PressurizedCapsule',
        'trunk': 'Trunk',
        'height_w_trunk': 'HeightWTrunk',
        'diameter': 'Diameter',
        'wikipedia': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'active': 'active',
        'crew_capacity': 'crew_capacity',
        'sidewall_angle_deg': 'sidewall_angle_deg',
        'orbit_duration_yr': 'orbit_duration_yr',
        'dry_mass_kg': 'dry_mass_kg',
        'dry_mass_lb': 'dry_mass_lb',
        'first_flight': 'first_flight',
        'heat_shield': 'heat_shield',
        'thrusters': 'thrusters',
        'launch_payload_mass': 'launch_payload_mass',
        'launch_payload_vol': 'launch_payload_vol',
        'return_payload_mass': 'return_payload_mass',
        'return_payload_vol': 'return_payload_vol',
        'pressurized_capsule': 'pressurized_capsule',
        'trunk': 'trunk',
        'height_w_trunk': 'height_w_trunk',
        'diameter': 'diameter',
        'wikipedia': 'wikipedia',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, type=None, active=None, crew_capacity=None, sidewall_angle_deg=None, orbit_duration_yr=None, dry_mass_kg=None, dry_mass_lb=None, first_flight=None, heat_shield=None, thrusters=None, launch_payload_mass=None, launch_payload_vol=None, return_payload_mass=None, return_payload_vol=None, pressurized_capsule=None, trunk=None, height_w_trunk=None, diameter=None, wikipedia=None, description=None, local_vars_configuration=None):  # noqa: E501
        """AllDragon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._active = None
        self._crew_capacity = None
        self._sidewall_angle_deg = None
        self._orbit_duration_yr = None
        self._dry_mass_kg = None
        self._dry_mass_lb = None
        self._first_flight = None
        self._heat_shield = None
        self._thrusters = None
        self._launch_payload_mass = None
        self._launch_payload_vol = None
        self._return_payload_mass = None
        self._return_payload_vol = None
        self._pressurized_capsule = None
        self._trunk = None
        self._height_w_trunk = None
        self._diameter = None
        self._wikipedia = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.active = active
        self.crew_capacity = crew_capacity
        self.sidewall_angle_deg = sidewall_angle_deg
        self.orbit_duration_yr = orbit_duration_yr
        self.dry_mass_kg = dry_mass_kg
        self.dry_mass_lb = dry_mass_lb
        self.first_flight = first_flight
        self.heat_shield = heat_shield
        self.thrusters = thrusters
        self.launch_payload_mass = launch_payload_mass
        self.launch_payload_vol = launch_payload_vol
        self.return_payload_mass = return_payload_mass
        self.return_payload_vol = return_payload_vol
        self.pressurized_capsule = pressurized_capsule
        self.trunk = trunk
        self.height_w_trunk = height_w_trunk
        self.diameter = diameter
        self.wikipedia = wikipedia
        self.description = description

    @property
    def id(self):
        """Gets the id of this AllDragon.  # noqa: E501


        :return: The id of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllDragon.


        :param id: The id of this AllDragon.  # noqa: E501
        :type: str
        """


        self._id = id

    @property
    def name(self):
        """Gets the name of this AllDragon.  # noqa: E501


        :return: The name of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AllDragon.


        :param name: The name of this AllDragon.  # noqa: E501
        :type: str
        """


        self._name = name

    @property
    def type(self):
        """Gets the type of this AllDragon.  # noqa: E501


        :return: The type of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllDragon.


        :param type: The type of this AllDragon.  # noqa: E501
        :type: str
        """


        self._type = type

    @property
    def active(self):
        """Gets the active of this AllDragon.  # noqa: E501


        :return: The active of this AllDragon.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AllDragon.


        :param active: The active of this AllDragon.  # noqa: E501
        :type: bool
        """


        self._active = active

    @property
    def crew_capacity(self):
        """Gets the crew_capacity of this AllDragon.  # noqa: E501


        :return: The crew_capacity of this AllDragon.  # noqa: E501
        :rtype: int
        """
        return self._crew_capacity

    @crew_capacity.setter
    def crew_capacity(self, crew_capacity):
        """Sets the crew_capacity of this AllDragon.


        :param crew_capacity: The crew_capacity of this AllDragon.  # noqa: E501
        :type: int
        """


        self._crew_capacity = crew_capacity

    @property
    def sidewall_angle_deg(self):
        """Gets the sidewall_angle_deg of this AllDragon.  # noqa: E501


        :return: The sidewall_angle_deg of this AllDragon.  # noqa: E501
        :rtype: int
        """
        return self._sidewall_angle_deg

    @sidewall_angle_deg.setter
    def sidewall_angle_deg(self, sidewall_angle_deg):
        """Sets the sidewall_angle_deg of this AllDragon.


        :param sidewall_angle_deg: The sidewall_angle_deg of this AllDragon.  # noqa: E501
        :type: int
        """


        self._sidewall_angle_deg = sidewall_angle_deg

    @property
    def orbit_duration_yr(self):
        """Gets the orbit_duration_yr of this AllDragon.  # noqa: E501


        :return: The orbit_duration_yr of this AllDragon.  # noqa: E501
        :rtype: int
        """
        return self._orbit_duration_yr

    @orbit_duration_yr.setter
    def orbit_duration_yr(self, orbit_duration_yr):
        """Sets the orbit_duration_yr of this AllDragon.


        :param orbit_duration_yr: The orbit_duration_yr of this AllDragon.  # noqa: E501
        :type: int
        """


        self._orbit_duration_yr = orbit_duration_yr

    @property
    def dry_mass_kg(self):
        """Gets the dry_mass_kg of this AllDragon.  # noqa: E501


        :return: The dry_mass_kg of this AllDragon.  # noqa: E501
        :rtype: int
        """
        return self._dry_mass_kg

    @dry_mass_kg.setter
    def dry_mass_kg(self, dry_mass_kg):
        """Sets the dry_mass_kg of this AllDragon.


        :param dry_mass_kg: The dry_mass_kg of this AllDragon.  # noqa: E501
        :type: int
        """


        self._dry_mass_kg = dry_mass_kg

    @property
    def dry_mass_lb(self):
        """Gets the dry_mass_lb of this AllDragon.  # noqa: E501


        :return: The dry_mass_lb of this AllDragon.  # noqa: E501
        :rtype: int
        """
        return self._dry_mass_lb

    @dry_mass_lb.setter
    def dry_mass_lb(self, dry_mass_lb):
        """Sets the dry_mass_lb of this AllDragon.


        :param dry_mass_lb: The dry_mass_lb of this AllDragon.  # noqa: E501
        :type: int
        """


        self._dry_mass_lb = dry_mass_lb

    @property
    def first_flight(self):
        """Gets the first_flight of this AllDragon.  # noqa: E501


        :return: The first_flight of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._first_flight

    @first_flight.setter
    def first_flight(self, first_flight):
        """Sets the first_flight of this AllDragon.


        :param first_flight: The first_flight of this AllDragon.  # noqa: E501
        :type: str
        """

        self._first_flight = first_flight

    @property
    def heat_shield(self):
        """Gets the heat_shield of this AllDragon.  # noqa: E501


        :return: The heat_shield of this AllDragon.  # noqa: E501
        :rtype: HeatShield
        """
        return self._heat_shield

    @heat_shield.setter
    def heat_shield(self, heat_shield):
        """Sets the heat_shield of this AllDragon.


        :param heat_shield: The heat_shield of this AllDragon.  # noqa: E501
        :type: HeatShield
        """


        self._heat_shield = heat_shield

    @property
    def thrusters(self):
        """Gets the thrusters of this AllDragon.  # noqa: E501


        :return: The thrusters of this AllDragon.  # noqa: E501
        :rtype: list[Thruster]
        """
        return self._thrusters

    @thrusters.setter
    def thrusters(self, thrusters):
        """Sets the thrusters of this AllDragon.


        :param thrusters: The thrusters of this AllDragon.  # noqa: E501
        :type: list[Thruster]
        """


        self._thrusters = thrusters

    @property
    def launch_payload_mass(self):
        """Gets the launch_payload_mass of this AllDragon.  # noqa: E501


        :return: The launch_payload_mass of this AllDragon.  # noqa: E501
        :rtype: LaunchPayloadMass
        """
        return self._launch_payload_mass

    @launch_payload_mass.setter
    def launch_payload_mass(self, launch_payload_mass):
        """Sets the launch_payload_mass of this AllDragon.


        :param launch_payload_mass: The launch_payload_mass of this AllDragon.  # noqa: E501
        :type: LaunchPayloadMass
        """


        self._launch_payload_mass = launch_payload_mass

    @property
    def launch_payload_vol(self):
        """Gets the launch_payload_vol of this AllDragon.  # noqa: E501


        :return: The launch_payload_vol of this AllDragon.  # noqa: E501
        :rtype: LaunchPayloadVol
        """
        return self._launch_payload_vol

    @launch_payload_vol.setter
    def launch_payload_vol(self, launch_payload_vol):
        """Sets the launch_payload_vol of this AllDragon.


        :param launch_payload_vol: The launch_payload_vol of this AllDragon.  # noqa: E501
        :type: LaunchPayloadVol
        """


        self._launch_payload_vol = launch_payload_vol

    @property
    def return_payload_mass(self):
        """Gets the return_payload_mass of this AllDragon.  # noqa: E501


        :return: The return_payload_mass of this AllDragon.  # noqa: E501
        :rtype: ReturnPayloadMass
        """
        return self._return_payload_mass

    @return_payload_mass.setter
    def return_payload_mass(self, return_payload_mass):
        """Sets the return_payload_mass of this AllDragon.


        :param return_payload_mass: The return_payload_mass of this AllDragon.  # noqa: E501
        :type: ReturnPayloadMass
        """


        self._return_payload_mass = return_payload_mass

    @property
    def return_payload_vol(self):
        """Gets the return_payload_vol of this AllDragon.  # noqa: E501


        :return: The return_payload_vol of this AllDragon.  # noqa: E501
        :rtype: ReturnPayloadVol
        """
        return self._return_payload_vol

    @return_payload_vol.setter
    def return_payload_vol(self, return_payload_vol):
        """Sets the return_payload_vol of this AllDragon.


        :param return_payload_vol: The return_payload_vol of this AllDragon.  # noqa: E501
        :type: ReturnPayloadVol
        """


        self._return_payload_vol = return_payload_vol

    @property
    def pressurized_capsule(self):
        """Gets the pressurized_capsule of this AllDragon.  # noqa: E501


        :return: The pressurized_capsule of this AllDragon.  # noqa: E501
        :rtype: PressurizedCapsule
        """
        return self._pressurized_capsule

    @pressurized_capsule.setter
    def pressurized_capsule(self, pressurized_capsule):
        """Sets the pressurized_capsule of this AllDragon.


        :param pressurized_capsule: The pressurized_capsule of this AllDragon.  # noqa: E501
        :type: PressurizedCapsule
        """


        self._pressurized_capsule = pressurized_capsule

    @property
    def trunk(self):
        """Gets the trunk of this AllDragon.  # noqa: E501


        :return: The trunk of this AllDragon.  # noqa: E501
        :rtype: Trunk
        """
        return self._trunk

    @trunk.setter
    def trunk(self, trunk):
        """Sets the trunk of this AllDragon.


        :param trunk: The trunk of this AllDragon.  # noqa: E501
        :type: Trunk
        """


        self._trunk = trunk

    @property
    def height_w_trunk(self):
        """Gets the height_w_trunk of this AllDragon.  # noqa: E501


        :return: The height_w_trunk of this AllDragon.  # noqa: E501
        :rtype: HeightWTrunk
        """
        return self._height_w_trunk

    @height_w_trunk.setter
    def height_w_trunk(self, height_w_trunk):
        """Sets the height_w_trunk of this AllDragon.


        :param height_w_trunk: The height_w_trunk of this AllDragon.  # noqa: E501
        :type: HeightWTrunk
        """


        self._height_w_trunk = height_w_trunk

    @property
    def diameter(self):
        """Gets the diameter of this AllDragon.  # noqa: E501


        :return: The diameter of this AllDragon.  # noqa: E501
        :rtype: Diameter
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this AllDragon.


        :param diameter: The diameter of this AllDragon.  # noqa: E501
        :type: Diameter
        """


        self._diameter = diameter

    @property
    def wikipedia(self):
        """Gets the wikipedia of this AllDragon.  # noqa: E501


        :return: The wikipedia of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia

    @wikipedia.setter
    def wikipedia(self, wikipedia):
        """Sets the wikipedia of this AllDragon.


        :param wikipedia: The wikipedia of this AllDragon.  # noqa: E501
        :type: str
        """


        self._wikipedia = wikipedia

    @property
    def description(self):
        """Gets the description of this AllDragon.  # noqa: E501


        :return: The description of this AllDragon.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllDragon.


        :param description: The description of this AllDragon.  # noqa: E501
        :type: str
        """


        self._description = description

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
        if not isinstance(other, AllDragon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllDragon):
            return True

        return self.to_dict() != other.to_dict()

# openapi_client.LaunchesApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_launches**](LaunchesApi.md#all_launches) | **GET** /v3/launches | All Launches
[**latest_launch**](LaunchesApi.md#latest_launch) | **GET** /v3/launches/latest | Latest Launch
[**next_launch**](LaunchesApi.md#next_launch) | **GET** /v3/launches/next | Next Launch
[**one_launch**](LaunchesApi.md#one_launch) | **GET** /v3/launches/{flight_number} | One Launch
[**past_launches**](LaunchesApi.md#past_launches) | **GET** /v3/launches/past | Past Launches
[**upcoming_launches**](LaunchesApi.md#upcoming_launches) | **GET** /v3/launches/upcoming | Upcoming Launches


# **all_launches**
> list[AllLaunch] all_launches()

All Launches

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | flight_id | `5a9fc479ab70786ba5a1eaaa` | string | Filter launches by mongo document id | | start/end | `start=2017-06-22&end=2017-06-25` | valid JavaScript date format | Include both to sort by date range | | flight_number | `60` | integer | Filter by flight number | | launch_year | `2018` | integer | Filter by launch year | | launch_date_utc | `2017-06-23T19:10:000Z` | UTC ISO timestamp | Filter by utc launch date | | launch_date_local | `2017-06-23T19:10:000Z` | Local ISO timestamp | Filter by local launch date | | tbd | `true` | boolean | Filter by TBD launches | | rocket_id | `falconheavy` | string | Filter by rocket ID | | rocket_name | `Falcon+Heavy` | string | Filter by rocket name | | rocket_type | `FT` | string | Filter by rocket type | | core_serial | `B1045` | string | Filter by core serial number | | land_success | `true` | boolean | Filter by successful core landings | | landing_intent | `true` | boolean | Filter by landing intention | | landing_type | `ASDS` | string | Filter by landing method | | landing_vehicle | `OCISLY` | string | Filter by landing vehicle | | cap_serial | `C111` | string | Filter by capsule serial number | | core_flight | `2` | integer | Filter by number of previous core flights | | block | `5` | integer | Filter by core block number | | gridfins | `true` | boolean | Filter launches by cores that used gridfins | | legs | `true` | boolean | Filter launches by cores that used landing legs | | core_reuse | `true` | boolean | Filter launches by reused cores | | capsule_reuse | `true` | boolean | Filter launches by reused capsules | | fairings_reused | `true` | boolean | Filter by reused fairings | | fairings_recovery_attempt | `false` | boolean | Filter by fairing recovery attempts | | fairings_recovered | `false` | boolean | Filter by recovered fairings | | fairings_ship | `MRSTEVEN` | string | Filter by fairings ship used | | site_id | `ksc_lc_39a` | string | Filter by launch site ID | | site_name | `KSC LC 39A` | string | Filter by launch site ID | | payload_id | `BulgariaSat-1` | string | Filter by payload ID | | norad_id | `43571` | integer | Filter by NORAD ID | | customer | `Iridium` | string | Filter by launch payload customer | | nationality | `Bulgaria` | string | Filter by payload nationality | | manufacturer | `SSL` | string | Filter by payload manufacturer | | payload_type | `Satellite` | string | Filter by payload type | | orbit | `GTO` | string | Filter by payload orbit | | reference_system | `geocentric` | string | Filter by payload orbit reference system | | regime | `geostationary` | string | Filter by payload orbit regime | | longitude | `-108` | float | Filter by payload orbit longitude | | semi_major_axis_km | `21226.178` | float | Filter by payload orbit semi major axis | | eccentricity | `0.6904141` | float | Filter by payload orbit eccentricity | | periapsis_km | `193.19` | float | Filter by payload orbit periapsis | | apoapsis_km | `29502.896` | float | Filter by payload orbit apoapsis | | inclination_deg | `27.0648` | float | Filter by payload orbit inclination | | period_min | `512.941` | float | Filter by payload orbit period | | lifespan_years | `512.941` | integer | Filter by payload lifespan in years | | epoch | `2018-08-07T06:57:16.000Z` | string | Filter by payload orbit epoch | | mean_motion | `2.80734018` | float | Filter by payload orbit mean motion | | raan | `227.0228` | float | Filter by payload orbit right ascension of the ascending node | | launch_success | `true` | boolean | Filter by launch success |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `flight_number` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    
    try:
        # All Launches
        api_response = api_instance.all_launches()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->all_launches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllLaunch]**](AllLaunch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_launch**
> LatestLaunch latest_launch()

Latest Launch

Returns the most recent launch

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    
    try:
        # Latest Launch
        api_response = api_instance.latest_launch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->latest_launch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LatestLaunch**](LatestLaunch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **next_launch**
> NextLaunch next_launch()

Next Launch

Returns the closest upcoming launch

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    
    try:
        # Next Launch
        api_response = api_instance.next_launch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->next_launch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NextLaunch**](NextLaunch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **one_launch**
> OneLaunch one_launch(flight_number)

One Launch

 #### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | flight_number | `64` | integer | get one launch by flight number |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    flight_number = 'flight_number_example' # str | 

    try:
        # One Launch
        api_response = api_instance.one_launch(flight_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->one_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flight_number** | **str**|  | 

### Return type

[**OneLaunch**](OneLaunch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Koa-Redis-Cache -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_launches**
> list[str] past_launches()

Past Launches

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | flight_id | `5a9fc479ab70786ba5a1eaaa` | string | Filter launches by mongo document id | | start/end | `start=2017-06-22&end=2017-06-25` | valid JavaScript date format | Include both to sort by date range | | flight_number | `60` | integer | Filter by flight number | | launch_year | `2018` | integer | Filter by launch year | | launch_date_utc | `2017-06-23T19:10:000Z` | UTC ISO timestamp | Filter by utc launch date | | launch_date_local | `2017-06-23T19:10:000Z` | Local ISO timestamp | Filter by local launch date | | tbd | `true` | boolean | Filter by TBD launches | | rocket_id | `falconheavy` | string | Filter by rocket ID | | rocket_name | `Falcon+Heavy` | string | Filter by rocket name | | rocket_type | `FT` | string | Filter by rocket type | | core_serial | `B1045` | string | Filter by core serial number | | land_success | `true` | boolean | Filter by successful core landings | | landing_intent | `true` | boolean | Filter by landing intention | | landing_type | `ASDS` | string | Filter by landing method | | landing_vehicle | `OCISLY` | string | Filter by landing vehicle | | cap_serial | `C111` | string | Filter by capsule serial number | | core_flight | `2` | integer | Filter by number of previous core flights | | block | `5` | integer | Filter by core block number | | gridfins | `true` | boolean | Filter launches by cores that used gridfins | | legs | `true` | boolean | Filter launches by cores that used landing legs | | core_reuse | `true` | boolean | Filter launches by reused cores | | capsule_reuse | `true` | boolean | Filter launches by reused capsules | | fairings_reused | `true` | boolean | Filter by reused fairings | | fairings_recovery_attempt | `false` | boolean | Filter by fairing recovery attempts | | fairings_recovered | `false` | boolean | Filter by recovered fairings | | fairings_ship | `MRSTEVEN` | string | Filter by fairings ship used | | site_id | `ksc_lc_39a` | string | Filter by launch site ID | | site_name | `KSC LC 39A` | string | Filter by launch site ID | | payload_id | `BulgariaSat-1` | string | Filter by payload ID | | norad_id | `43571` | integer | Filter by NORAD ID | | customer | `Iridium` | string | Filter by launch payload customer | | nationality | `Bulgaria` | string | Filter by payload nationality | | manufacturer | `SSL` | string | Filter by payload manufacturer | | payload_type | `Satellite` | string | Filter by payload type | | orbit | `GTO` | string | Filter by payload orbit | | reference_system | `geocentric` | string | Filter by payload orbit reference system | | regime | `geostationary` | string | Filter by payload orbit regime | | longitude | `-108` | float | Filter by payload orbit longitude | | semi_major_axis_km | `21226.178` | float | Filter by payload orbit semi major axis | | eccentricity | `0.6904141` | float | Filter by payload orbit eccentricity | | periapsis_km | `193.19` | float | Filter by payload orbit periapsis | | apoapsis_km | `29502.896` | float | Filter by payload orbit apoapsis | | inclination_deg | `27.0648` | float | Filter by payload orbit inclination | | period_min | `512.941` | float | Filter by payload orbit period | | lifespan_years | `512.941` | integer | Filter by payload lifespan in years | | epoch | `2018-08-07T06:57:16.000Z` | string | Filter by payload orbit epoch | | mean_motion | `2.80734018` | float | Filter by payload orbit mean motion | | raan | `227.0228` | float | Filter by payload orbit right ascension of the ascending node | | launch_success | `true` | boolean | Filter by launch success |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `flight_number` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    
    try:
        # Past Launches
        api_response = api_instance.past_launches()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->past_launches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upcoming_launches**
> list[UpcomingLaunch] upcoming_launches()

Upcoming Launches

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | flight_id | `5a9fc479ab70786ba5a1eaaa` | string | Filter launches by mongo document id | | start/end | `start=2017-06-22&end=2017-06-25` | valid JavaScript date format | Include both to sort by date range | | flight_number | `60` | integer | Filter by flight number | | launch_year | `2018` | integer | Filter by launch year | | launch_date_utc | `2017-06-23T19:10:000Z` | UTC ISO timestamp | Filter by utc launch date | | launch_date_local | `2017-06-23T19:10:000Z` | Local ISO timestamp | Filter by local launch date | | tbd | `true` | boolean | Filter by TBD launches | | rocket_id | `falconheavy` | string | Filter by rocket ID | | rocket_name | `Falcon+Heavy` | string | Filter by rocket name | | rocket_type | `FT` | string | Filter by rocket type | | core_serial | `B1045` | string | Filter by core serial number | | land_success | `true` | boolean | Filter by successful core landings | | landing_intent | `true` | boolean | Filter by landing intention | | landing_type | `ASDS` | string | Filter by landing method | | landing_vehicle | `OCISLY` | string | Filter by landing vehicle | | cap_serial | `C111` | string | Filter by capsule serial number | | core_flight | `2` | integer | Filter by number of previous core flights | | block | `5` | integer | Filter by core block number | | gridfins | `true` | boolean | Filter launches by cores that used gridfins | | legs | `true` | boolean | Filter launches by cores that used landing legs | | core_reuse | `true` | boolean | Filter launches by reused cores | | capsule_reuse | `true` | boolean | Filter launches by reused capsules | | fairings_reused | `true` | boolean | Filter by reused fairings | | fairings_recovery_attempt | `false` | boolean | Filter by fairing recovery attempts | | fairings_recovered | `false` | boolean | Filter by recovered fairings | | fairings_ship | `MRSTEVEN` | string | Filter by fairings ship used | | site_id | `ksc_lc_39a` | string | Filter by launch site ID | | site_name | `KSC LC 39A` | string | Filter by launch site ID | | payload_id | `BulgariaSat-1` | string | Filter by payload ID | | norad_id | `43571` | integer | Filter by NORAD ID | | customer | `Iridium` | string | Filter by launch payload customer | | nationality | `Bulgaria` | string | Filter by payload nationality | | manufacturer | `SSL` | string | Filter by payload manufacturer | | payload_type | `Satellite` | string | Filter by payload type | | orbit | `GTO` | string | Filter by payload orbit | | reference_system | `geocentric` | string | Filter by payload orbit reference system | | regime | `geostationary` | string | Filter by payload orbit regime | | longitude | `-108` | float | Filter by payload orbit longitude | | semi_major_axis_km | `21226.178` | float | Filter by payload orbit semi major axis | | eccentricity | `0.6904141` | float | Filter by payload orbit eccentricity | | periapsis_km | `193.19` | float | Filter by payload orbit periapsis | | apoapsis_km | `29502.896` | float | Filter by payload orbit apoapsis | | inclination_deg | `27.0648` | float | Filter by payload orbit inclination | | period_min | `512.941` | float | Filter by payload orbit period | | lifespan_years | `512.941` | integer | Filter by payload lifespan in years | | epoch | `2018-08-07T06:57:16.000Z` | string | Filter by payload orbit epoch | | mean_motion | `2.80734018` | float | Filter by payload orbit mean motion | | raan | `227.0228` | float | Filter by payload orbit right ascension of the ascending node | | launch_success | `true` | boolean | Filter by launch success |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `flight_number` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.spacexdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.spacexdata.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LaunchesApi(api_client)
    
    try:
        # Upcoming Launches
        api_response = api_instance.upcoming_launches()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LaunchesApi->upcoming_launches: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UpcomingLaunch]**](UpcomingLaunch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


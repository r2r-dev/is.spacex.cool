# openapi_client.CoresApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_cores**](CoresApi.md#all_cores) | **GET** /v3/cores | All Cores
[**one_core**](CoresApi.md#one_core) | **GET** /v3/cores/{core_serial} | One Core
[**past_cores**](CoresApi.md#past_cores) | **GET** /v3/cores/past | Past Cores
[**upcoming_cores**](CoresApi.md#upcoming_cores) | **GET** /v3/cores/upcoming | Upcoming Cores


# **all_cores**
> list[str] all_cores()

All Cores

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | core_serial | `B1037` | string | Filter by core serial | | block | `5` | integer | Filter by core block number | | status | `active` | string | Filter by core status | | original_launch | `2017-07-05T23:35:00.000Z` | UTC ISO timestamp | Filter by core original launch date | | mission | `Intelsat 35e` | string | Filter by core mission | | reuse_count | `1` | integer | Filter by number of times the core was reused | | rtls_attempts | `1` | integer | Filter by RTLS attempted landings | | rtls_landings | `1` | integer | Filter by RTLS successful landings | | asds_attempts | `1` | integer | Filter by ASDS attempted landings | | asds_landings | `1` | integer | Filter by ASDS successful landings | | water_landing | `1` | boolean | Filter by water landings |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `core_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CoresApi(api_client)
    
    try:
        # All Cores
        api_response = api_instance.all_cores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoresApi->all_cores: %s\n" % e)
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

# **one_core**
> OneCore one_core(core_serial)

One Core

#### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | core_serial | `B1032` | string | get one core by serial |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.CoresApi(api_client)
    core_serial = 'core_serial_example' # str | 

    try:
        # One Core
        api_response = api_instance.one_core(core_serial)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoresApi->one_core: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_serial** | **str**|  | 

### Return type

[**OneCore**](OneCore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Access-Control-Allow-Origin -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Response-Time -  <br>  * X-XSS-Protection -  <br>  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **past_cores**
> list[PastCore] past_cores()

Past Cores

Lists cores that have launched  #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | core_serial | `B1037` | string | Filter by core serial | | block | `5` | integer | Filter by core block number | | status | `active` | string | Filter by core status | | original_launch | `2017-07-05T23:35:00.000Z` | UTC ISO timestamp | Filter by core original launch date | | mission | `Intelsat 35e` | string | Filter by core mission | | reuse_count | `1` | integer | Filter by number of times the core was reused | | rtls_attempts | `1` | integer | Filter by RTLS attempted landings | | rtls_landings | `1` | integer | Filter by RTLS successful landings | | asds_attempts | `1` | integer | Filter by ASDS attempted landings | | asds_landings | `1` | integer | Filter by ASDS successful landings | | water_landing | `1` | boolean | Filter by water landings |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `core_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CoresApi(api_client)
    
    try:
        # Past Cores
        api_response = api_instance.past_cores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoresApi->past_cores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PastCore]**](PastCore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Date -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Vary -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Access-Control-Allow-Origin -  <br>  * X-Response-Time -  <br>  * Content-Encoding -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upcoming_cores**
> list[UpcomingCore] upcoming_cores()

Upcoming Cores

Lists cores that haven't launched yet  #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | core_serial | `B1037` | string | Filter by core serial | | block | `5` | integer | Filter by core block number | | status | `active` | string | Filter by core status | | original_launch | `2017-07-05T23:35:00.000Z` | UTC ISO timestamp | Filter by core original launch date | | mission | `Intelsat 35e` | string | Filter by core mission | | reuse_count | `1` | integer | Filter by number of times the core was reused | | rtls_attempts | `1` | integer | Filter by RTLS attempted landings | | rtls_landings | `1` | integer | Filter by RTLS successful landings | | asds_attempts | `1` | integer | Filter by ASDS attempted landings | | asds_landings | `1` | integer | Filter by ASDS successful landings | | water_landing | `1` | boolean | Filter by water landings |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `core_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CoresApi(api_client)
    
    try:
        # Upcoming Cores
        api_response = api_instance.upcoming_cores()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoresApi->upcoming_cores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UpcomingCore]**](UpcomingCore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Date -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Vary -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Access-Control-Allow-Origin -  <br>  * X-Response-Time -  <br>  * Content-Encoding -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


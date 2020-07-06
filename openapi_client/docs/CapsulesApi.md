# openapi_client.CapsulesApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_capsules**](CapsulesApi.md#all_capsules) | **GET** /v3/capsules | All Capsules
[**one_capsule**](CapsulesApi.md#one_capsule) | **GET** /v3/capsules/{capsule_serial} | One Capsule
[**past_capsules**](CapsulesApi.md#past_capsules) | **GET** /v3/capsules/past | Past Capsules
[**upcoming_capsules**](CapsulesApi.md#upcoming_capsules) | **GET** /v3/capsules/upcoming | Upcoming Capsules


# **all_capsules**
> list[AllCapsule] all_capsules()

All Capsules

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | capsule_serial | `C112` | string | Filter by capsule serial | | capsule_id | `dragon1` | string | Filter by capsule id | | status | `active` | string | Filter by capsule status | | original_launch | `2017-02-19T14:39:00.000Z` | UTC ISO timestamp | Filter by capsule original launch date | | mission | `SpaceX CRS-5` | string | Filter by capsule mission | | landings | `2` | integer | Filter by capsule landings | | type | `Dragon 1.1` | string | Filter by capsule type | | reuse_count | `1` | integer | Filter by number of times the capsule was reused |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `capsule_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CapsulesApi(api_client)
    
    try:
        # All Capsules
        api_response = api_instance.all_capsules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapsulesApi->all_capsules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllCapsule]**](AllCapsule.md)

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

# **one_capsule**
> OneCapsule one_capsule(capsule_serial)

One Capsule

#### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | capsule_serial | `C113` | string | get one capsule by serial |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.CapsulesApi(api_client)
    capsule_serial = 'capsule_serial_example' # str | 

    try:
        # One Capsule
        api_response = api_instance.one_capsule(capsule_serial)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapsulesApi->one_capsule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capsule_serial** | **str**|  | 

### Return type

[**OneCapsule**](OneCapsule.md)

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

# **past_capsules**
> list[str] past_capsules()

Past Capsules

Lists capsules that have launched  #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | capsule_serial | `C112` | string | Filter by capsule serial | | capsule_id | `dragon1` | string | Filter by capsule id | | status | `active` | string | Filter by capsule status | | original_launch | `2017-02-19T14:39:00.000Z` | UTC ISO timestamp | Filter by capsule original launch date | | mission | `SpaceX CRS-5` | string | Filter by capsule mission | | landings | `2` | integer | Filter by capsule landings | | type | `Dragon 1.1` | string | Filter by capsule type | | reuse_count | `1` | integer | Filter by number of times the capsule was reused |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `capsule_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CapsulesApi(api_client)
    
    try:
        # Past Capsules
        api_response = api_instance.past_capsules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapsulesApi->past_capsules: %s\n" % e)
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
**200** |  |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Vary -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Access-Control-Allow-Origin -  <br>  * X-Response-Time -  <br>  * Accept-Ranges -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upcoming_capsules**
> list[str] upcoming_capsules()

Upcoming Capsules

Lists capsules that haven't launched yet  #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | capsule_serial | `C112` | string | Filter by capsule serial | | capsule_id | `dragon1` | string | Filter by capsule id | | status | `active` | string | Filter by capsule status | | original_launch | `2017-02-19T14:39:00.000Z` | UTC ISO timestamp | Filter by capsule original launch date | | mission | `SpaceX CRS-5` | string | Filter by capsule mission | | landings | `2` | integer | Filter by capsule landings | | type | `Dragon 1.1` | string | Filter by capsule type | | reuse_count | `1` | integer | Filter by number of times the capsule was reused |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `capsule_serial` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.CapsulesApi(api_client)
    
    try:
        # Upcoming Capsules
        api_response = api_instance.upcoming_capsules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapsulesApi->upcoming_capsules: %s\n" % e)
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
**200** |  |  * Date -  <br>  * Content-Length -  <br>  * Connection -  <br>  * Vary -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Access-Control-Allow-Origin -  <br>  * X-Response-Time -  <br>  * Accept-Ranges -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


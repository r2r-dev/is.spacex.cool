# openapi_client.LandingPadsApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_landing_pads**](LandingPadsApi.md#all_landing_pads) | **GET** /v3/landpads | All Landing Pads
[**one_landing_pad**](LandingPadsApi.md#one_landing_pad) | **GET** /v3/landpads/{id} | One Landing Pad


# **all_landing_pads**
> list[AllLandingPad] all_landing_pads()

All Landing Pads

Returns all landing pads  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query |

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
    api_instance = openapi_client.LandingPadsApi(api_client)
    
    try:
        # All Landing Pads
        api_response = api_instance.all_landing_pads()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LandingPadsApi->all_landing_pads: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllLandingPad]**](AllLandingPad.md)

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

# **one_landing_pad**
> OneLandingPad one_landing_pad(id)

One Landing Pad

Returns a specific landing pad  #### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `LZ-4` | string | get one launchpad by id |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.LandingPadsApi(api_client)
    id = 'id_example' # str | 

    try:
        # One Landing Pad
        api_response = api_instance.one_landing_pad(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LandingPadsApi->one_landing_pad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OneLandingPad**](OneLandingPad.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Date -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Vary -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Access-Control-Allow-Origin -  <br>  * X-Response-Time -  <br>  * Content-Encoding -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


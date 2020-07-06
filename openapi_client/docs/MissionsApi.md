# openapi_client.MissionsApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_missions**](MissionsApi.md#all_missions) | **GET** /v3/missions | All Missions
[**one_mission**](MissionsApi.md#one_mission) | **GET** /v3/missions/{mission_id} | One Mission


# **all_missions**
> list[AllMission] all_missions()

All Missions

Returns all missions  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query |

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
    api_instance = openapi_client.MissionsApi(api_client)
    
    try:
        # All Missions
        api_response = api_instance.all_missions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionsApi->all_missions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllMission]**](AllMission.md)

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

# **one_mission**
> OneMission one_mission(mission_id)

One Mission

 #### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | mission_id | `SES` | string | get one mission by id |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.MissionsApi(api_client)
    mission_id = 'mission_id_example' # str | 

    try:
        # One Mission
        api_response = api_instance.one_mission(mission_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MissionsApi->one_mission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_id** | **str**|  | 

### Return type

[**OneMission**](OneMission.md)

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


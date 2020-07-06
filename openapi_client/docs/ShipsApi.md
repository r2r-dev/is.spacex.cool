# openapi_client.ShipsApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_ships**](ShipsApi.md#all_ships) | **GET** /v3/ships | All Ships
[**one_ship**](ShipsApi.md#one_ship) | **GET** /v3/ships/{ship_id} | One Ship


# **all_ships**
> list[str] all_ships()

All Ships

#### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | ship_id | `MRSTEVEN` | string | filter results by ship id | | ship_name | `MR STEVEN` | string | filter results by ship name | | ship_model | `Marmac 300` | string | filter results by ship model | | ship_type | `Tug` | string | filter results by ship type | | role | `Support Ship` | string | filter results by ship role | | active | `true` | boolean | filter results by active ships | | imo | `7434016` | integer | filter results by imo id number | | mmsi | `367020820` | integer | filter results by mmsi id number | | abs | `571252` | integer | filter results by abs id number | | class | `7604342` | integer | filter results by class id number | | weight_lbs | `588000` | integer | filter results by gross weight in lbs | | weight_kg | `266712` | integer | filter results by gross weight in kg | | year_built | `2015` | integer | filter results by year built | | home_port | `Port of Los Angeles` | string | filter results by home port | | status | `Stopped` | string | filter results by ship status | | speed_kn | `9` | integer | filter results by current ship speed | | course_deg | `57` | integer | filter results by current ship course in degrees | | latitude | `25.98623` | float | filter results by current ship latitude | | longitude | `-97.3115` | float | filter results by current ship longitude | | successful_landings | `2` | integer | filter results by successful landings | | attempted_landings | `8` | integer | filter results by current attempted landings | | mission | `CRS-7` | string | filter results by mission involved in |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `ship_id` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.ShipsApi(api_client)
    
    try:
        # All Ships
        api_response = api_instance.all_ships()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipsApi->all_ships: %s\n" % e)
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

# **one_ship**
> OneShip one_ship(ship_id)

One Ship

 #### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | ship_id | `MRSTEVEN` | string | get one ship by id |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.ShipsApi(api_client)
    ship_id = 'ship_id_example' # str | 

    try:
        # One Ship
        api_response = api_instance.one_ship(ship_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipsApi->one_ship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ship_id** | **str**|  | 

### Return type

[**OneShip**](OneShip.md)

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


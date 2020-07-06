# openapi_client.PayloadsApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_payloads**](PayloadsApi.md#all_payloads) | **GET** /v3/payloads | All Payloads
[**one_payload**](PayloadsApi.md#one_payload) | **GET** /v3/payloads/{payload_id} | One Payload


# **all_payloads**
> list[AllPayload] all_payloads()

All Payloads

 #### Optional Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | flight_id | `5a9fc479ab70786ba5a1eaaa` | string | Filter launches by mongo document id | | start/end | `start=2017-06-22&end=2017-06-25` | valid JavaScript date format | Include both to sort by date range | | flight_number | `60` | integer | Filter by flight number | | launch_year | `2018` | integer | Filter by launch year | | launch_date_utc | `2017-06-23T19:10:000Z` | UTC ISO timestamp | Filter by utc launch date | | launch_date_local | `2017-06-23T19:10:000Z` | Local ISO timestamp | Filter by local launch date | | rocket_id | `falconheavy` | string | Filter by rocket ID | | rocket_name | `Falcon+Heavy` | string | Filter by rocket name | | rocket_type | `FT` | string | Filter by rocket type | | core_serial | `B1045` | string | Filter by core serial number | | land_success | `true` | boolean | Filter by successful core landings | | landing_intent | `true` | boolean | Filter by landing intention | | landing_type | `ASDS` | string | Filter by landing method | | landing_vehicle | `OCISLY` | string | Filter by landing vehicle | | cap_serial | `C111` | string | Filter by capsule serial number | | core_flight | `2` | integer | Filter by number of previous core flights | | block | `5` | integer | Filter by core block number | | core_reuse | `true` | boolean | Filter launches by reused cores | | capsule_reuse | `true` | boolean | Filter launches by reused capsules | | fairings_reused | `true` | boolean | Filter by reused fairings | | fairings_recovery_attempt | `false` | boolean | Filter by fairing recovery attempts | | fairings_recovered | `false` | boolean | Filter by recovered fairings | | fairings_ship | `MRSTEVEN` | string | Filter by fairings ship used | | site_id | `ksc_lc_39a` | string | Filter by launch site ID | | site_name | `KSC LC 39A` | string | Filter by launch site ID | | payload_id | `BulgariaSat-1` | string | Filter by payload ID | | norad_id | `43571` | integer | Filter by NORAD ID | | customer | `Iridium` | string | Filter by launch payload customer | | nationality | `Bulgaria` | string | Filter by payload nationality | | manufacturer | `SSL` | string | Filter by payload manufacturer | | payload_type | `Satellite` | string | Filter by payload type | | orbit | `GTO` | string | Filter by payload orbit | | reference_system | `geocentric` | string | Filter by payload orbit reference system | | regime | `geostationary` | string | Filter by payload orbit regime | | longitude | `-108` | float | Filter by payload orbit longitude | | semi_major_axis_km | `21226.178` | float | Filter by payload orbit semi major axis | | eccentricity | `0.6904141` | float | Filter by payload orbit eccentricity | | periapsis_km | `193.19` | float | Filter by payload orbit periapsis | | apoapsis_km | `29502.896` | float | Filter by payload orbit apoapsis | | inclination_deg | `27.0648` | float | Filter by payload orbit inclination | | period_min | `512.941` | float | Filter by payload orbit period | | lifespan_years | `512.941` | integer | Filter by payload lifespan in years | | epoch | `2018-08-07T06:57:16.000Z` | string | Filter by payload orbit epoch | | mean_motion | `2.80734018` | float | Filter by payload orbit mean motion | | raan | `227.0228` | float | Filter by payload orbit right ascension of the ascending node | | launch_success | `true` | boolean | Filter by launch success |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's | | limit | `3` | integer | Limit results returned, defaults to all documents returned | | offset | `3` | integer | Offset or skip results from the beginning of the query | | sort | `flight_number` | string | Change result sorting by setting value to any parameter in this list | | order | `desc` | string | Change result ordering by setting values of `asc` or `desc` |

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
    api_instance = openapi_client.PayloadsApi(api_client)
    
    try:
        # All Payloads
        api_response = api_instance.all_payloads()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadsApi->all_payloads: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AllPayload]**](AllPayload.md)

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

# **one_payload**
> OnePayload one_payload(payload_id)

One Payload

 #### Params  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | payload_id | `TESS` | string | get one payload by id |  #### Optional Ouput Control Querystrings  | Param  | Sample | Type | Description | | --- | --- | --- | --- | | id | `true` | boolean | Set as `true` to show mongo document id's |

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
    api_instance = openapi_client.PayloadsApi(api_client)
    payload_id = 'payload_id_example' # str | 

    try:
        # One Payload
        api_response = api_instance.one_payload(payload_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayloadsApi->one_payload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id** | **str**|  | 

### Return type

[**OnePayload**](OnePayload.md)

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


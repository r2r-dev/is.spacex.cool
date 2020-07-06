# openapi_client.RoadsterApi

All URIs are relative to *https://api.spacexdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roadster**](RoadsterApi.md#roadster) | **GET** /v3/roadster | Roadster


# **roadster**
> Roadster roadster()

Roadster

Get current roadster orbit data

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
    api_instance = openapi_client.RoadsterApi(api_client)
    
    try:
        # Roadster
        api_response = api_instance.roadster()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoadsterApi->roadster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Roadster**](Roadster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


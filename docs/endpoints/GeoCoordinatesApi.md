# modelcatalog.GeoCoordinatesApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geocoordinatess_get**](GeoCoordinatesApi.md#geocoordinatess_get) | **GET** /geocoordinatess | List all GeoCoordinates entities
[**geocoordinatess_id_delete**](GeoCoordinatesApi.md#geocoordinatess_id_delete) | **DELETE** /geocoordinatess/{id} | Delete a GeoCoordinates
[**geocoordinatess_id_get**](GeoCoordinatesApi.md#geocoordinatess_id_get) | **GET** /geocoordinatess/{id} | Get a GeoCoordinates
[**geocoordinatess_id_put**](GeoCoordinatesApi.md#geocoordinatess_id_put) | **PUT** /geocoordinatess/{id} | Update a GeoCoordinates
[**geocoordinatess_post**](GeoCoordinatesApi.md#geocoordinatess_post) | **POST** /geocoordinatess | Create a GeoCoordinates


# **geocoordinatess_get**
> list[GeoCoordinates] geocoordinatess_get(username=username, label=label)

List all GeoCoordinates entities

Gets a list of all GeoCoordinates entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all GeoCoordinates entities
    api_response = api_instance.geocoordinatess_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[GeoCoordinates]**](GeoCoordinates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of GeoCoordinates entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_id_delete**
> geocoordinatess_id_delete(id, user)

Delete a GeoCoordinates

Delete an existing GeoCoordinates

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a GeoCoordinates
    api_instance.geocoordinatess_id_delete(id, user)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deleted |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_id_get**
> GeoCoordinates geocoordinatess_id_get(id, username=username)

Get a GeoCoordinates

Gets the details of a single instance of a GeoCoordinates

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a GeoCoordinates
    api_response = api_instance.geocoordinatess_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**GeoCoordinates**](GeoCoordinates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of  GeoCoordinates |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_id_put**
> GeoCoordinates geocoordinatess_id_put(id, user, geo_coordinates=geo_coordinates)

Update a GeoCoordinates

Updates an existing GeoCoordinates

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
geo_coordinates = modelcatalog.GeoCoordinates() # GeoCoordinates | An old GeoCoordinatesto be updated (optional)

try:
    # Update a GeoCoordinates
    api_response = api_instance.geocoordinatess_id_put(id, user, geo_coordinates=geo_coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md)| An old GeoCoordinatesto be updated | [optional] 

### Return type

[**GeoCoordinates**](GeoCoordinates.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_post**
> GeoCoordinates geocoordinatess_post(user, geo_coordinates=geo_coordinates)

Create a GeoCoordinates

Create a new instance of a GeoCoordinates

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint
configuration = modelcatalog.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
geo_coordinates = modelcatalog.GeoCoordinates() # GeoCoordinates | A new GeoCoordinatesto be created (optional)

try:
    # Create a GeoCoordinates
    api_response = api_instance.geocoordinatess_post(user, geo_coordinates=geo_coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md)| A new GeoCoordinatesto be created | [optional] 

### Return type

[**GeoCoordinates**](GeoCoordinates.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


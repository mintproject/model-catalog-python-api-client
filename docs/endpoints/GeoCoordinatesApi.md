# modelcatalog.GeoCoordinatesApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geocoordinatess_get**](GeoCoordinatesApi.md#geocoordinatess_get) | **GET** /geocoordinatess | List all instances of GeoCoordinates
[**geocoordinatess_id_delete**](GeoCoordinatesApi.md#geocoordinatess_id_delete) | **DELETE** /geocoordinatess/{id} | Delete an existing GeoCoordinates
[**geocoordinatess_id_get**](GeoCoordinatesApi.md#geocoordinatess_id_get) | **GET** /geocoordinatess/{id} | Get a single GeoCoordinates by its id
[**geocoordinatess_id_put**](GeoCoordinatesApi.md#geocoordinatess_id_put) | **PUT** /geocoordinatess/{id} | Update an existing GeoCoordinates
[**geocoordinatess_post**](GeoCoordinatesApi.md#geocoordinatess_post) | **POST** /geocoordinatess | Create one GeoCoordinates


# **geocoordinatess_get**
> list[GeoCoordinates] geocoordinatess_get(username=username, label=label, page=page, per_page=per_page)

List all instances of GeoCoordinates

Gets a list of all instances of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of GeoCoordinates
    api_response = api_instance.geocoordinatess_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

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
**200** | Successful response - returns an array with the instances of GeoCoordinates. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_id_delete**
> geocoordinatess_id_delete(id, user)

Delete an existing GeoCoordinates

Delete an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the GeoCoordinates to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing GeoCoordinates
    api_instance.geocoordinatess_id_delete(id, user)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoCoordinates to be retrieved | 
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

Get a single GeoCoordinates by its id

Gets the details of a given GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi()
id = 'id_example' # str | The ID of the GeoCoordinates to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single GeoCoordinates by its id
    api_response = api_instance.geocoordinatess_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoCoordinates to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

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
**200** | Gets the details of a given GeoCoordinates |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geocoordinatess_id_put**
> GeoCoordinates geocoordinatess_id_put(id, user, geo_coordinates=geo_coordinates)

Update an existing GeoCoordinates

Updates an existing GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the GeoCoordinates to be retrieved
user = 'user_example' # str | Username
geo_coordinates = modelcatalog.GeoCoordinates() # GeoCoordinates | An old GeoCoordinatesto be updated (optional)

try:
    # Update an existing GeoCoordinates
    api_response = api_instance.geocoordinatess_id_put(id, user, geo_coordinates=geo_coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoCoordinates to be retrieved | 
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

Create one GeoCoordinates

Create a new instance of GeoCoordinates (more information in https://w3id.org/okn/o/sdm#GeoCoordinates)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoCoordinatesApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
geo_coordinates = modelcatalog.GeoCoordinates() # GeoCoordinates | Information about the GeoCoordinatesto be created (optional)

try:
    # Create one GeoCoordinates
    api_response = api_instance.geocoordinatess_post(user, geo_coordinates=geo_coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoCoordinatesApi->geocoordinatess_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md)| Information about the GeoCoordinatesto be created | [optional] 

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


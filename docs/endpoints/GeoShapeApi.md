# modelcatalog.GeoShapeApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geoshapes_get**](GeoShapeApi.md#geoshapes_get) | **GET** /geoshapes | List all instances of GeoShape
[**geoshapes_id_delete**](GeoShapeApi.md#geoshapes_id_delete) | **DELETE** /geoshapes/{id} | Delete an existing GeoShape
[**geoshapes_id_get**](GeoShapeApi.md#geoshapes_id_get) | **GET** /geoshapes/{id} | Get a single GeoShape by its id
[**geoshapes_id_put**](GeoShapeApi.md#geoshapes_id_put) | **PUT** /geoshapes/{id} | Update an existing GeoShape
[**geoshapes_post**](GeoShapeApi.md#geoshapes_post) | **POST** /geoshapes | Create one GeoShape


# **geoshapes_get**
> list[GeoShape] geoshapes_get(username=username, label=label, page=page, per_page=per_page)

List all instances of GeoShape

Gets a list of all instances of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoShapeApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of GeoShape
    api_response = api_instance.geoshapes_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[GeoShape]**](GeoShape.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of GeoShape. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geoshapes_id_delete**
> geoshapes_id_delete(id, user)

Delete an existing GeoShape

Delete an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the GeoShape to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing GeoShape
    api_instance.geoshapes_id_delete(id, user)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoShape to be retrieved | 
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

# **geoshapes_id_get**
> GeoShape geoshapes_id_get(id, username=username)

Get a single GeoShape by its id

Gets the details of a given GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GeoShapeApi()
id = 'id_example' # str | The ID of the GeoShape to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single GeoShape by its id
    api_response = api_instance.geoshapes_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoShape to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given GeoShape |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **geoshapes_id_put**
> GeoShape geoshapes_id_put(id, user, geo_shape=geo_shape)

Update an existing GeoShape

Updates an existing GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the GeoShape to be retrieved
user = 'user_example' # str | Username
geo_shape = modelcatalog.GeoShape() # GeoShape | An old GeoShapeto be updated (optional)

try:
    # Update an existing GeoShape
    api_response = api_instance.geoshapes_id_put(id, user, geo_shape=geo_shape)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GeoShape to be retrieved | 
 **user** | **str**| Username | 
 **geo_shape** | [**GeoShape**](GeoShape.md)| An old GeoShapeto be updated | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

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

# **geoshapes_post**
> GeoShape geoshapes_post(user, geo_shape=geo_shape)

Create one GeoShape

Create a new instance of GeoShape (more information in https://w3id.org/okn/o/sdm#GeoShape)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
geo_shape = modelcatalog.GeoShape() # GeoShape | Information about the GeoShapeto be created (optional)

try:
    # Create one GeoShape
    api_response = api_instance.geoshapes_post(user, geo_shape=geo_shape)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **geo_shape** | [**GeoShape**](GeoShape.md)| Information about the GeoShapeto be created | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

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


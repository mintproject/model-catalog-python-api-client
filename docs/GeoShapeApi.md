# modelcatalog.GeoShapeApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geoshapes_get**](GeoShapeApi.md#geoshapes_get) | **GET** /geoshapes | List all GeoShape entities
[**geoshapes_id_delete**](GeoShapeApi.md#geoshapes_id_delete) | **DELETE** /geoshapes/{id} | Delete a GeoShape
[**geoshapes_id_get**](GeoShapeApi.md#geoshapes_id_get) | **GET** /geoshapes/{id} | Get a GeoShape
[**geoshapes_id_put**](GeoShapeApi.md#geoshapes_id_put) | **PUT** /geoshapes/{id} | Update a GeoShape
[**geoshapes_post**](GeoShapeApi.md#geoshapes_post) | **POST** /geoshapes | Create a GeoShape


# **geoshapes_get**
> list[GeoShape] geoshapes_get(username=username, label=label)

List all GeoShape entities

Gets a list of all GeoShape entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.GeoShapeApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all GeoShape entities
    api_response = api_instance.geoshapes_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[GeoShape]**](GeoShape.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geoshapes_id_delete**
> geoshapes_id_delete(id, user)

Delete a GeoShape

Delete an existing GeoShape

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

# create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a GeoShape
    api_instance.geoshapes_id_delete(id, user)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geoshapes_id_get**
> GeoShape geoshapes_id_get(id, username=username)

Get a GeoShape

Gets the details of a single instance of a GeoShape

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.GeoShapeApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a GeoShape
    api_response = api_instance.geoshapes_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geoshapes_id_put**
> GeoShape geoshapes_id_put(id, user, geo_shape=geo_shape)

Update a GeoShape

Updates an existing GeoShape

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

# create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
geo_shape = modelcatalog.GeoShape() # GeoShape | An old GeoShapeto be updated (optional)

try:
    # Update a GeoShape
    api_response = api_instance.geoshapes_id_put(id, user, geo_shape=geo_shape)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **geo_shape** | [**GeoShape**](GeoShape.md)| An old GeoShapeto be updated | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geoshapes_post**
> GeoShape geoshapes_post(user, geo_shape=geo_shape)

Create a GeoShape

Create a new instance of a GeoShape

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

# create an instance of the API class
api_instance = modelcatalog.GeoShapeApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
geo_shape = modelcatalog.GeoShape() # GeoShape | A new GeoShapeto be created (optional)

try:
    # Create a GeoShape
    api_response = api_instance.geoshapes_post(user, geo_shape=geo_shape)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoShapeApi->geoshapes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **geo_shape** | [**GeoShape**](GeoShape.md)| A new GeoShapeto be created | [optional] 

### Return type

[**GeoShape**](GeoShape.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


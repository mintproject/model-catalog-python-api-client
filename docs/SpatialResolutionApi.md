# modelcatalog.SpatialResolutionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialresolutions_get**](SpatialResolutionApi.md#spatialresolutions_get) | **GET** /spatialresolutions | List all SpatialResolution entities
[**spatialresolutions_id_delete**](SpatialResolutionApi.md#spatialresolutions_id_delete) | **DELETE** /spatialresolutions/{id} | Delete a SpatialResolution
[**spatialresolutions_id_get**](SpatialResolutionApi.md#spatialresolutions_id_get) | **GET** /spatialresolutions/{id} | Get a SpatialResolution
[**spatialresolutions_id_put**](SpatialResolutionApi.md#spatialresolutions_id_put) | **PUT** /spatialresolutions/{id} | Update a SpatialResolution
[**spatialresolutions_post**](SpatialResolutionApi.md#spatialresolutions_post) | **POST** /spatialresolutions | Create a SpatialResolution


# **spatialresolutions_get**
> list[SpatialResolution] spatialresolutions_get(username=username, label=label)

List all SpatialResolution entities

Gets a list of all SpatialResolution entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SpatialResolution entities
    api_response = api_instance.spatialresolutions_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SpatialResolution]**](SpatialResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatialresolutions_id_delete**
> spatialresolutions_id_delete(id, user)

Delete a SpatialResolution

Delete an existing SpatialResolution

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
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SpatialResolution
    api_instance.spatialresolutions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_delete: %s\n" % e)
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

# **spatialresolutions_id_get**
> SpatialResolution spatialresolutions_id_get(id, username=username)

Get a SpatialResolution

Gets the details of a single instance of a SpatialResolution

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SpatialResolution
    api_response = api_instance.spatialresolutions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatialresolutions_id_put**
> SpatialResolution spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)

Update a SpatialResolution

Updates an existing SpatialResolution

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
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
spatial_resolution = modelcatalog.SpatialResolution() # SpatialResolution | An old SpatialResolutionto be updated (optional)

try:
    # Update a SpatialResolution
    api_response = api_instance.spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **spatial_resolution** | [**SpatialResolution**](SpatialResolution.md)| An old SpatialResolutionto be updated | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatialresolutions_post**
> SpatialResolution spatialresolutions_post(user, spatial_resolution=spatial_resolution)

Create a SpatialResolution

Create a new instance of a SpatialResolution

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
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
spatial_resolution = modelcatalog.SpatialResolution() # SpatialResolution | A new SpatialResolutionto be created (optional)

try:
    # Create a SpatialResolution
    api_response = api_instance.spatialresolutions_post(user, spatial_resolution=spatial_resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatial_resolution** | [**SpatialResolution**](SpatialResolution.md)| A new SpatialResolutionto be created | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


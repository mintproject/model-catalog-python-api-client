# mint_client.SpatialResolutionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialresolutions_get**](SpatialResolutionApi.md#spatialresolutions_get) | **GET** /spatialresolutions | List all SpatialResolution entities
[**spatialresolutions_id_delete**](SpatialResolutionApi.md#spatialresolutions_id_delete) | **DELETE** /spatialresolutions/{id} | Delete a SpatialResolution
[**spatialresolutions_id_get**](SpatialResolutionApi.md#spatialresolutions_id_get) | **GET** /spatialresolutions/{id} | Get a SpatialResolution
[**spatialresolutions_id_put**](SpatialResolutionApi.md#spatialresolutions_id_put) | **PUT** /spatialresolutions/{id} | Update a SpatialResolution
[**spatialresolutions_post**](SpatialResolutionApi.md#spatialresolutions_post) | **POST** /spatialresolutions | Create a SpatialResolution


# **spatialresolutions_get**
> list[SpatialResolution] spatialresolutions_get(username=username)

List all SpatialResolution entities

Gets a list of all SpatialResolution entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SpatialResolutionApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all SpatialResolution entities
    api_response = api_instance.spatialresolutions_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

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
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.SpatialResolutionApi(mint_client.ApiClient(configuration))
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
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SpatialResolutionApi()
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
> spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)

Update a SpatialResolution

Updates an existing SpatialResolution

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.SpatialResolutionApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
spatial_resolution = mint_client.SpatialResolution() # SpatialResolution | An old SpatialResolutionto be updated (optional)

try:
    # Update a SpatialResolution
    api_instance.spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)
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

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatialresolutions_post**
> spatialresolutions_post(user, spatial_resolution=spatial_resolution)

Create a SpatialResolution

Create a new instance of a SpatialResolution

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.SpatialResolutionApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
spatial_resolution = mint_client.SpatialResolution() # SpatialResolution | A new SpatialResolutionto be created (optional)

try:
    # Create a SpatialResolution
    api_instance.spatialresolutions_post(user, spatial_resolution=spatial_resolution)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatial_resolution** | [**SpatialResolution**](SpatialResolution.md)| A new SpatialResolutionto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


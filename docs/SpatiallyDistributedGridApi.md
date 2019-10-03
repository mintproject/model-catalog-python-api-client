# mint_client.SpatiallyDistributedGridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatiallydistributedgrids_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_get) | **GET** /spatiallydistributedgrids | List all SpatiallyDistributedGrid entities
[**spatiallydistributedgrids_id_delete**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_delete) | **DELETE** /spatiallydistributedgrids/{id} | Delete a SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_get) | **GET** /spatiallydistributedgrids/{id} | Get a SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_put**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_put) | **PUT** /spatiallydistributedgrids/{id} | Update a SpatiallyDistributedGrid
[**spatiallydistributedgrids_post**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_post) | **POST** /spatiallydistributedgrids | Create a SpatiallyDistributedGrid


# **spatiallydistributedgrids_get**
> list[SpatiallyDistributedGrid] spatiallydistributedgrids_get(username=username)

List all SpatiallyDistributedGrid entities

Gets a list of all SpatiallyDistributedGrid entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SpatiallyDistributedGridApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all SpatiallyDistributedGrid entities
    api_response = api_instance.spatiallydistributedgrids_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[SpatiallyDistributedGrid]**](SpatiallyDistributedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatiallydistributedgrids_id_delete**
> spatiallydistributedgrids_id_delete(id, user)

Delete a SpatiallyDistributedGrid

Delete an existing SpatiallyDistributedGrid

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
api_instance = mint_client.SpatiallyDistributedGridApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SpatiallyDistributedGrid
    api_instance.spatiallydistributedgrids_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_delete: %s\n" % e)
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

# **spatiallydistributedgrids_id_get**
> SpatiallyDistributedGrid spatiallydistributedgrids_id_get(id, username=username)

Get a SpatiallyDistributedGrid

Gets the details of a single instance of a SpatiallyDistributedGrid

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SpatiallyDistributedGridApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatiallydistributedgrids_id_put**
> spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)

Update a SpatiallyDistributedGrid

Updates an existing SpatiallyDistributedGrid

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
api_instance = mint_client.SpatiallyDistributedGridApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
spatially_distributed_grid = mint_client.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | An old SpatiallyDistributedGridto be updated (optional)

try:
    # Update a SpatiallyDistributedGrid
    api_instance.spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **spatially_distributed_grid** | [**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)| An old SpatiallyDistributedGridto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spatiallydistributedgrids_post**
> spatiallydistributedgrids_post(user, spatially_distributed_grid=spatially_distributed_grid)

Create a SpatiallyDistributedGrid

Create a new instance of a SpatiallyDistributedGrid

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
api_instance = mint_client.SpatiallyDistributedGridApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
spatially_distributed_grid = mint_client.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | A new SpatiallyDistributedGridto be created (optional)

try:
    # Create a SpatiallyDistributedGrid
    api_instance.spatiallydistributedgrids_post(user, spatially_distributed_grid=spatially_distributed_grid)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatially_distributed_grid** | [**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)| A new SpatiallyDistributedGridto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

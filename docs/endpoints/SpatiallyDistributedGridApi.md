# modelcatalog.SpatiallyDistributedGridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatiallydistributedgrids_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_get) | **GET** /spatiallydistributedgrids | List all SpatiallyDistributedGrid entities
[**spatiallydistributedgrids_id_delete**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_delete) | **DELETE** /spatiallydistributedgrids/{id} | Delete a SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_get) | **GET** /spatiallydistributedgrids/{id} | Get a SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_put**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_put) | **PUT** /spatiallydistributedgrids/{id} | Update a SpatiallyDistributedGrid
[**spatiallydistributedgrids_post**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_post) | **POST** /spatiallydistributedgrids | Create a SpatiallyDistributedGrid


# **spatiallydistributedgrids_get**
> list[SpatiallyDistributedGrid] spatiallydistributedgrids_get(username=username, label=label)

List all SpatiallyDistributedGrid entities

Gets a list of all SpatiallyDistributedGrid entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatiallyDistributedGridApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SpatiallyDistributedGrid entities
    api_response = api_instance.spatiallydistributedgrids_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SpatiallyDistributedGrid]**](SpatiallyDistributedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of SpatiallyDistributedGrid entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatiallydistributedgrids_id_delete**
> spatiallydistributedgrids_id_delete(id, user)

Delete a SpatiallyDistributedGrid

Delete an existing SpatiallyDistributedGrid

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
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

# **spatiallydistributedgrids_id_get**
> SpatiallyDistributedGrid spatiallydistributedgrids_id_get(id, username=username)

Get a SpatiallyDistributedGrid

Gets the details of a single instance of a SpatiallyDistributedGrid

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatiallyDistributedGridApi()
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of  SpatiallyDistributedGrid |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatiallydistributedgrids_id_put**
> SpatiallyDistributedGrid spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)

Update a SpatiallyDistributedGrid

Updates an existing SpatiallyDistributedGrid

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
spatially_distributed_grid = modelcatalog.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | An old SpatiallyDistributedGridto be updated (optional)

try:
    # Update a SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)
    pprint(api_response)
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

[**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)

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

# **spatiallydistributedgrids_post**
> SpatiallyDistributedGrid spatiallydistributedgrids_post(user, spatially_distributed_grid=spatially_distributed_grid)

Create a SpatiallyDistributedGrid

Create a new instance of a SpatiallyDistributedGrid

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
spatially_distributed_grid = modelcatalog.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | A new SpatiallyDistributedGridto be created (optional)

try:
    # Create a SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_post(user, spatially_distributed_grid=spatially_distributed_grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatially_distributed_grid** | [**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)| A new SpatiallyDistributedGridto be created | [optional] 

### Return type

[**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)

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


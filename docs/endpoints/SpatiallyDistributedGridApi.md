# modelcatalog.SpatiallyDistributedGridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatiallydistributedgrids_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_get) | **GET** /spatiallydistributedgrids | List all instances of SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_delete**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_delete) | **DELETE** /spatiallydistributedgrids/{id} | Delete an existing SpatiallyDistributedGrid
[**spatiallydistributedgrids_id_get**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_get) | **GET** /spatiallydistributedgrids/{id} | Get a single SpatiallyDistributedGrid by its id
[**spatiallydistributedgrids_id_put**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_put) | **PUT** /spatiallydistributedgrids/{id} | Update an existing SpatiallyDistributedGrid
[**spatiallydistributedgrids_post**](SpatiallyDistributedGridApi.md#spatiallydistributedgrids_post) | **POST** /spatiallydistributedgrids | Create one SpatiallyDistributedGrid


# **spatiallydistributedgrids_get**
> list[SpatiallyDistributedGrid] spatiallydistributedgrids_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SpatiallyDistributedGrid

Gets a list of all instances of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatiallyDistributedGridApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

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
**200** | Successful response - returns an array with the instances of SpatiallyDistributedGrid. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatiallydistributedgrids_id_delete**
> spatiallydistributedgrids_id_delete(id, user)

Delete an existing SpatiallyDistributedGrid

Delete an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SpatiallyDistributedGrid to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SpatiallyDistributedGrid
    api_instance.spatiallydistributedgrids_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatiallyDistributedGrid to be retrieved | 
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

Get a single SpatiallyDistributedGrid by its id

Gets the details of a given SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatiallyDistributedGridApi()
id = 'id_example' # str | The ID of the SpatiallyDistributedGrid to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SpatiallyDistributedGrid by its id
    api_response = api_instance.spatiallydistributedgrids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatiallyDistributedGrid to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

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
**200** | Gets the details of a given SpatiallyDistributedGrid |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatiallydistributedgrids_id_put**
> SpatiallyDistributedGrid spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)

Update an existing SpatiallyDistributedGrid

Updates an existing SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SpatiallyDistributedGrid to be retrieved
user = 'user_example' # str | Username
spatially_distributed_grid = modelcatalog.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | An old SpatiallyDistributedGridto be updated (optional)

try:
    # Update an existing SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_id_put(id, user, spatially_distributed_grid=spatially_distributed_grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatiallyDistributedGrid to be retrieved | 
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

Create one SpatiallyDistributedGrid

Create a new instance of SpatiallyDistributedGrid (more information in https://w3id.org/okn/o/sdm#SpatiallyDistributedGrid)

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
api_instance = modelcatalog.SpatiallyDistributedGridApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
spatially_distributed_grid = modelcatalog.SpatiallyDistributedGrid() # SpatiallyDistributedGrid | Information about the SpatiallyDistributedGridto be created (optional)

try:
    # Create one SpatiallyDistributedGrid
    api_response = api_instance.spatiallydistributedgrids_post(user, spatially_distributed_grid=spatially_distributed_grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatiallyDistributedGridApi->spatiallydistributedgrids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatially_distributed_grid** | [**SpatiallyDistributedGrid**](SpatiallyDistributedGrid.md)| Information about the SpatiallyDistributedGridto be created | [optional] 

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


# modelcatalog.PointBasedGridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pointbasedgrids_get**](PointBasedGridApi.md#pointbasedgrids_get) | **GET** /pointbasedgrids | List all instances of PointBasedGrid
[**pointbasedgrids_id_delete**](PointBasedGridApi.md#pointbasedgrids_id_delete) | **DELETE** /pointbasedgrids/{id} | Delete an existing PointBasedGrid
[**pointbasedgrids_id_get**](PointBasedGridApi.md#pointbasedgrids_id_get) | **GET** /pointbasedgrids/{id} | Get a single PointBasedGrid by its id
[**pointbasedgrids_id_put**](PointBasedGridApi.md#pointbasedgrids_id_put) | **PUT** /pointbasedgrids/{id} | Update an existing PointBasedGrid
[**pointbasedgrids_post**](PointBasedGridApi.md#pointbasedgrids_post) | **POST** /pointbasedgrids | Create one PointBasedGrid


# **pointbasedgrids_get**
> list[PointBasedGrid] pointbasedgrids_get(username=username, label=label, page=page, per_page=per_page)

List all instances of PointBasedGrid

Gets a list of all instances of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of PointBasedGrid
    api_response = api_instance.pointbasedgrids_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[PointBasedGrid]**](PointBasedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of PointBasedGrid. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **pointbasedgrids_id_delete**
> pointbasedgrids_id_delete(id, user=user)

Delete an existing PointBasedGrid

Delete an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the PointBasedGrid to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing PointBasedGrid
    api_instance.pointbasedgrids_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the PointBasedGrid to be retrieved | 
 **user** | **str**| Username | [optional] 

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

# **pointbasedgrids_id_get**
> PointBasedGrid pointbasedgrids_id_get(id, username=username)

Get a single PointBasedGrid by its id

Gets the details of a given PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi()
id = 'id_example' # str | The ID of the PointBasedGrid to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single PointBasedGrid by its id
    api_response = api_instance.pointbasedgrids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the PointBasedGrid to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**PointBasedGrid**](PointBasedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given PointBasedGrid |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **pointbasedgrids_id_put**
> PointBasedGrid pointbasedgrids_id_put(id, user=user, point_based_grid=point_based_grid)

Update an existing PointBasedGrid

Updates an existing PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the PointBasedGrid to be retrieved
user = 'user_example' # str | Username (optional)
point_based_grid = modelcatalog.PointBasedGrid() # PointBasedGrid | An old PointBasedGridto be updated (optional)

try:
    # Update an existing PointBasedGrid
    api_response = api_instance.pointbasedgrids_id_put(id, user=user, point_based_grid=point_based_grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the PointBasedGrid to be retrieved | 
 **user** | **str**| Username | [optional] 
 **point_based_grid** | [**PointBasedGrid**](PointBasedGrid.md)| An old PointBasedGridto be updated | [optional] 

### Return type

[**PointBasedGrid**](PointBasedGrid.md)

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

# **pointbasedgrids_post**
> PointBasedGrid pointbasedgrids_post(user=user, point_based_grid=point_based_grid)

Create one PointBasedGrid

Create a new instance of PointBasedGrid (more information in https://w3id.org/okn/o/sdm#PointBasedGrid)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
point_based_grid = modelcatalog.PointBasedGrid() # PointBasedGrid | Information about the PointBasedGridto be created (optional)

try:
    # Create one PointBasedGrid
    api_response = api_instance.pointbasedgrids_post(user=user, point_based_grid=point_based_grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **point_based_grid** | [**PointBasedGrid**](PointBasedGrid.md)| Information about the PointBasedGridto be created | [optional] 

### Return type

[**PointBasedGrid**](PointBasedGrid.md)

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


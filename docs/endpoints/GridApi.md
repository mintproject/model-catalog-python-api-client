# modelcatalog.GridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grids_get**](GridApi.md#grids_get) | **GET** /grids | List all instances of Grid
[**grids_id_delete**](GridApi.md#grids_id_delete) | **DELETE** /grids/{id} | Delete an existing Grid
[**grids_id_get**](GridApi.md#grids_id_get) | **GET** /grids/{id} | Get a single Grid by its id
[**grids_id_put**](GridApi.md#grids_id_put) | **PUT** /grids/{id} | Update an existing Grid
[**grids_post**](GridApi.md#grids_post) | **POST** /grids | Create one Grid


# **grids_get**
> list[Grid] grids_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Grid

Gets a list of all instances of Grid (more information in https://w3id.org/okn/o/sdm#Grid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GridApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Grid
    api_response = api_instance.grids_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Grid]**](Grid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Grid. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **grids_id_delete**
> grids_id_delete(id, user=user)

Delete an existing Grid

Delete an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid)

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
api_instance = modelcatalog.GridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Grid to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Grid
    api_instance.grids_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Grid to be retrieved | 
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

# **grids_id_get**
> Grid grids_id_get(id, username=username)

Get a single Grid by its id

Gets the details of a given Grid (more information in https://w3id.org/okn/o/sdm#Grid)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.GridApi()
id = 'id_example' # str | The ID of the Grid to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Grid by its id
    api_response = api_instance.grids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Grid to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Grid**](Grid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Grid |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **grids_id_put**
> Grid grids_id_put(id, user=user, grid=grid)

Update an existing Grid

Updates an existing Grid (more information in https://w3id.org/okn/o/sdm#Grid)

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
api_instance = modelcatalog.GridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Grid to be retrieved
user = 'user_example' # str | Username (optional)
grid = modelcatalog.Grid() # Grid | An old Gridto be updated (optional)

try:
    # Update an existing Grid
    api_response = api_instance.grids_id_put(id, user=user, grid=grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Grid to be retrieved | 
 **user** | **str**| Username | [optional] 
 **grid** | [**Grid**](Grid.md)| An old Gridto be updated | [optional] 

### Return type

[**Grid**](Grid.md)

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

# **grids_post**
> Grid grids_post(user=user, grid=grid)

Create one Grid

Create a new instance of Grid (more information in https://w3id.org/okn/o/sdm#Grid)

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
api_instance = modelcatalog.GridApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
grid = modelcatalog.Grid() # Grid | Information about the Gridto be created (optional)

try:
    # Create one Grid
    api_response = api_instance.grids_post(user=user, grid=grid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **grid** | [**Grid**](Grid.md)| Information about the Gridto be created | [optional] 

### Return type

[**Grid**](Grid.md)

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


# modelcatalog.PointBasedGridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pointbasedgrids_get**](PointBasedGridApi.md#pointbasedgrids_get) | **GET** /pointbasedgrids | List all PointBasedGrid entities
[**pointbasedgrids_id_delete**](PointBasedGridApi.md#pointbasedgrids_id_delete) | **DELETE** /pointbasedgrids/{id} | Delete a PointBasedGrid
[**pointbasedgrids_id_get**](PointBasedGridApi.md#pointbasedgrids_id_get) | **GET** /pointbasedgrids/{id} | Get a PointBasedGrid
[**pointbasedgrids_id_put**](PointBasedGridApi.md#pointbasedgrids_id_put) | **PUT** /pointbasedgrids/{id} | Update a PointBasedGrid
[**pointbasedgrids_post**](PointBasedGridApi.md#pointbasedgrids_post) | **POST** /pointbasedgrids | Create a PointBasedGrid


# **pointbasedgrids_get**
> list[PointBasedGrid] pointbasedgrids_get(username=username, label=label)

List all PointBasedGrid entities

Gets a list of all PointBasedGrid entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all PointBasedGrid entities
    api_response = api_instance.pointbasedgrids_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[PointBasedGrid]**](PointBasedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pointbasedgrids_id_delete**
> pointbasedgrids_id_delete(id, user)

Delete a PointBasedGrid

Delete an existing PointBasedGrid

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
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a PointBasedGrid
    api_instance.pointbasedgrids_id_delete(id, user)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_delete: %s\n" % e)
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

# **pointbasedgrids_id_get**
> PointBasedGrid pointbasedgrids_id_get(id, username=username)

Get a PointBasedGrid

Gets the details of a single instance of a PointBasedGrid

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.PointBasedGridApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a PointBasedGrid
    api_response = api_instance.pointbasedgrids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**PointBasedGrid**](PointBasedGrid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pointbasedgrids_id_put**
> pointbasedgrids_id_put(id, user, point_based_grid=point_based_grid)

Update a PointBasedGrid

Updates an existing PointBasedGrid

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
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
point_based_grid = modelcatalog.PointBasedGrid() # PointBasedGrid | An old PointBasedGridto be updated (optional)

try:
    # Update a PointBasedGrid
    api_instance.pointbasedgrids_id_put(id, user, point_based_grid=point_based_grid)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **point_based_grid** | [**PointBasedGrid**](PointBasedGrid.md)| An old PointBasedGridto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pointbasedgrids_post**
> pointbasedgrids_post(user, point_based_grid=point_based_grid)

Create a PointBasedGrid

Create a new instance of a PointBasedGrid

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
api_instance = modelcatalog.PointBasedGridApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
point_based_grid = modelcatalog.PointBasedGrid() # PointBasedGrid | A new PointBasedGridto be created (optional)

try:
    # Create a PointBasedGrid
    api_instance.pointbasedgrids_post(user, point_based_grid=point_based_grid)
except ApiException as e:
    print("Exception when calling PointBasedGridApi->pointbasedgrids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **point_based_grid** | [**PointBasedGrid**](PointBasedGrid.md)| A new PointBasedGridto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


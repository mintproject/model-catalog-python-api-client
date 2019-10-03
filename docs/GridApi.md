# mint_client.GridApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grids_get**](GridApi.md#grids_get) | **GET** /grids | List all Grid entities
[**grids_id_delete**](GridApi.md#grids_id_delete) | **DELETE** /grids/{id} | Delete a Grid
[**grids_id_get**](GridApi.md#grids_id_get) | **GET** /grids/{id} | Get a Grid
[**grids_id_put**](GridApi.md#grids_id_put) | **PUT** /grids/{id} | Update a Grid
[**grids_post**](GridApi.md#grids_post) | **POST** /grids | Create a Grid


# **grids_get**
> list[Grid] grids_get(username=username)

List all Grid entities

Gets a list of all Grid entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.GridApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Grid entities
    api_response = api_instance.grids_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Grid]**](Grid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grids_id_delete**
> grids_id_delete(id, user)

Delete a Grid

Delete an existing Grid

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
api_instance = mint_client.GridApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Grid
    api_instance.grids_id_delete(id, user)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_delete: %s\n" % e)
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

# **grids_id_get**
> Grid grids_id_get(id, username=username)

Get a Grid

Gets the details of a single instance of a Grid

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.GridApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Grid
    api_response = api_instance.grids_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Grid**](Grid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grids_id_put**
> grids_id_put(id, user, grid=grid)

Update a Grid

Updates an existing Grid

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
api_instance = mint_client.GridApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
grid = mint_client.Grid() # Grid | An old Gridto be updated (optional)

try:
    # Update a Grid
    api_instance.grids_id_put(id, user, grid=grid)
except ApiException as e:
    print("Exception when calling GridApi->grids_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **grid** | [**Grid**](Grid.md)| An old Gridto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grids_post**
> grids_post(user, grid=grid)

Create a Grid

Create a new instance of a Grid

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
api_instance = mint_client.GridApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
grid = mint_client.Grid() # Grid | A new Gridto be created (optional)

try:
    # Create a Grid
    api_instance.grids_post(user, grid=grid)
except ApiException as e:
    print("Exception when calling GridApi->grids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **grid** | [**Grid**](Grid.md)| A new Gridto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


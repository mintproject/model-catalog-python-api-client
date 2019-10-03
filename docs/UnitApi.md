# mint_client.UnitApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_get**](UnitApi.md#units_get) | **GET** /units | List all Unit entities
[**units_id_delete**](UnitApi.md#units_id_delete) | **DELETE** /units/{id} | Delete a Unit
[**units_id_get**](UnitApi.md#units_id_get) | **GET** /units/{id} | Get a Unit
[**units_id_put**](UnitApi.md#units_id_put) | **PUT** /units/{id} | Update a Unit
[**units_post**](UnitApi.md#units_post) | **POST** /units | Create a Unit


# **units_get**
> list[Unit] units_get(username=username)

List all Unit entities

Gets a list of all Unit entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.UnitApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Unit entities
    api_response = api_instance.units_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Unit]**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_id_delete**
> units_id_delete(id, user)

Delete a Unit

Delete an existing Unit

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
api_instance = mint_client.UnitApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Unit
    api_instance.units_id_delete(id, user)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_delete: %s\n" % e)
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

# **units_id_get**
> Unit units_id_get(id, username=username)

Get a Unit

Gets the details of a single instance of a Unit

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.UnitApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Unit
    api_response = api_instance.units_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_id_put**
> units_id_put(id, user, unit=unit)

Update a Unit

Updates an existing Unit

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
api_instance = mint_client.UnitApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
unit = mint_client.Unit() # Unit | An old Unitto be updated (optional)

try:
    # Update a Unit
    api_instance.units_id_put(id, user, unit=unit)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **unit** | [**Unit**](Unit.md)| An old Unitto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_post**
> units_post(user, unit=unit)

Create a Unit

Create a new instance of a Unit

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
api_instance = mint_client.UnitApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
unit = mint_client.Unit() # Unit | A new Unitto be created (optional)

try:
    # Create a Unit
    api_instance.units_post(user, unit=unit)
except ApiException as e:
    print("Exception when calling UnitApi->units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **unit** | [**Unit**](Unit.md)| A new Unitto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# mint_client.VariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variables_get**](VariableApi.md#variables_get) | **GET** /variables | List all Variable entities
[**variables_id_delete**](VariableApi.md#variables_id_delete) | **DELETE** /variables/{id} | Delete a Variable
[**variables_id_get**](VariableApi.md#variables_id_get) | **GET** /variables/{id} | Get a Variable
[**variables_id_put**](VariableApi.md#variables_id_put) | **PUT** /variables/{id} | Update a Variable
[**variables_post**](VariableApi.md#variables_post) | **POST** /variables | Create a Variable


# **variables_get**
> list[Variable] variables_get(username=username)

List all Variable entities

Gets a list of all Variable entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.VariableApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Variable entities
    api_response = api_instance.variables_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Variable]**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_id_delete**
> variables_id_delete(id, user)

Delete a Variable

Delete an existing Variable

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
api_instance = mint_client.VariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Variable
    api_instance.variables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_delete: %s\n" % e)
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

# **variables_id_get**
> Variable variables_id_get(id, username=username)

Get a Variable

Gets the details of a single instance of a Variable

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.VariableApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Variable
    api_response = api_instance.variables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_id_put**
> variables_id_put(id, user, variable=variable)

Update a Variable

Updates an existing Variable

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
api_instance = mint_client.VariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
variable = mint_client.Variable() # Variable | An old Variableto be updated (optional)

try:
    # Update a Variable
    api_instance.variables_id_put(id, user, variable=variable)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **variable** | [**Variable**](Variable.md)| An old Variableto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variables_post**
> variables_post(user, variable=variable)

Create a Variable

Create a new instance of a Variable

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
api_instance = mint_client.VariableApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
variable = mint_client.Variable() # Variable | A new Variableto be created (optional)

try:
    # Create a Variable
    api_instance.variables_post(user, variable=variable)
except ApiException as e:
    print("Exception when calling VariableApi->variables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **variable** | [**Variable**](Variable.md)| A new Variableto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

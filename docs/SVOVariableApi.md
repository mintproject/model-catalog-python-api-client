# mint_client.SVOVariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**svovariables_get**](SVOVariableApi.md#svovariables_get) | **GET** /svovariables | List all SVOVariable entities
[**svovariables_id_delete**](SVOVariableApi.md#svovariables_id_delete) | **DELETE** /svovariables/{id} | Delete a SVOVariable
[**svovariables_id_get**](SVOVariableApi.md#svovariables_id_get) | **GET** /svovariables/{id} | Get a SVOVariable
[**svovariables_id_put**](SVOVariableApi.md#svovariables_id_put) | **PUT** /svovariables/{id} | Update a SVOVariable
[**svovariables_post**](SVOVariableApi.md#svovariables_post) | **POST** /svovariables | Create a SVOVariable


# **svovariables_get**
> list[SVOVariable] svovariables_get(username=username)

List all SVOVariable entities

Gets a list of all SVOVariable entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SVOVariableApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all SVOVariable entities
    api_response = api_instance.svovariables_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[SVOVariable]**](SVOVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svovariables_id_delete**
> svovariables_id_delete(id, user)

Delete a SVOVariable

Delete an existing SVOVariable

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
api_instance = mint_client.SVOVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SVOVariable
    api_instance.svovariables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_delete: %s\n" % e)
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

# **svovariables_id_get**
> SVOVariable svovariables_id_get(id, username=username)

Get a SVOVariable

Gets the details of a single instance of a SVOVariable

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.SVOVariableApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SVOVariable
    api_response = api_instance.svovariables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SVOVariable**](SVOVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svovariables_id_put**
> svovariables_id_put(id, user, svo_variable=svo_variable)

Update a SVOVariable

Updates an existing SVOVariable

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
api_instance = mint_client.SVOVariableApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
svo_variable = mint_client.SVOVariable() # SVOVariable | An old SVOVariableto be updated (optional)

try:
    # Update a SVOVariable
    api_instance.svovariables_id_put(id, user, svo_variable=svo_variable)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **svo_variable** | [**SVOVariable**](SVOVariable.md)| An old SVOVariableto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svovariables_post**
> svovariables_post(user, svo_variable=svo_variable)

Create a SVOVariable

Create a new instance of a SVOVariable

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
api_instance = mint_client.SVOVariableApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
svo_variable = mint_client.SVOVariable() # SVOVariable | A new SVOVariableto be created (optional)

try:
    # Create a SVOVariable
    api_instance.svovariables_post(user, svo_variable=svo_variable)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **svo_variable** | [**SVOVariable**](SVOVariable.md)| A new SVOVariableto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


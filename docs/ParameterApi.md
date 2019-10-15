# modelcatalog.ParameterApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parameters_get**](ParameterApi.md#parameters_get) | **GET** /parameters | List all Parameter entities
[**parameters_id_delete**](ParameterApi.md#parameters_id_delete) | **DELETE** /parameters/{id} | Delete a Parameter
[**parameters_id_get**](ParameterApi.md#parameters_id_get) | **GET** /parameters/{id} | Get a Parameter
[**parameters_id_put**](ParameterApi.md#parameters_id_put) | **PUT** /parameters/{id} | Update a Parameter
[**parameters_post**](ParameterApi.md#parameters_post) | **POST** /parameters | Create a Parameter


# **parameters_get**
> list[Parameter] parameters_get(username=username, label=label)

List all Parameter entities

Gets a list of all Parameter entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ParameterApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Parameter entities
    api_response = api_instance.parameters_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Parameter]**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_id_delete**
> parameters_id_delete(id, user)

Delete a Parameter

Delete an existing Parameter

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
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Parameter
    api_instance.parameters_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_delete: %s\n" % e)
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

# **parameters_id_get**
> Parameter parameters_id_get(id, username=username)

Get a Parameter

Gets the details of a single instance of a Parameter

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ParameterApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Parameter
    api_response = api_instance.parameters_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Parameter**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_id_put**
> Parameter parameters_id_put(id, user, parameter=parameter)

Update a Parameter

Updates an existing Parameter

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
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
parameter = modelcatalog.Parameter() # Parameter | An old Parameterto be updated (optional)

try:
    # Update a Parameter
    api_response = api_instance.parameters_id_put(id, user, parameter=parameter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **parameter** | [**Parameter**](Parameter.md)| An old Parameterto be updated | [optional] 

### Return type

[**Parameter**](Parameter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_post**
> Parameter parameters_post(user, parameter=parameter)

Create a Parameter

Create a new instance of a Parameter

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
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
parameter = modelcatalog.Parameter() # Parameter | A new Parameterto be created (optional)

try:
    # Create a Parameter
    api_response = api_instance.parameters_post(user, parameter=parameter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **parameter** | [**Parameter**](Parameter.md)| A new Parameterto be created | [optional] 

### Return type

[**Parameter**](Parameter.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


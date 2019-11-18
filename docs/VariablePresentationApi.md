# modelcatalog.VariablePresentationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variablepresentations_get**](VariablePresentationApi.md#variablepresentations_get) | **GET** /variablepresentations | List all VariablePresentation entities
[**variablepresentations_id_delete**](VariablePresentationApi.md#variablepresentations_id_delete) | **DELETE** /variablepresentations/{id} | Delete a VariablePresentation
[**variablepresentations_id_get**](VariablePresentationApi.md#variablepresentations_id_get) | **GET** /variablepresentations/{id} | Get a VariablePresentation
[**variablepresentations_id_put**](VariablePresentationApi.md#variablepresentations_id_put) | **PUT** /variablepresentations/{id} | Update a VariablePresentation
[**variablepresentations_post**](VariablePresentationApi.md#variablepresentations_post) | **POST** /variablepresentations | Create a VariablePresentation


# **variablepresentations_get**
> list[VariablePresentation] variablepresentations_get(username=username, label=label)

List all VariablePresentation entities

Gets a list of all VariablePresentation entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.VariablePresentationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all VariablePresentation entities
    api_response = api_instance.variablepresentations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[VariablePresentation]**](VariablePresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variablepresentations_id_delete**
> variablepresentations_id_delete(id, user)

Delete a VariablePresentation

Delete an existing VariablePresentation

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a VariablePresentation
    api_instance.variablepresentations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_delete: %s\n" % e)
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

# **variablepresentations_id_get**
> VariablePresentation variablepresentations_id_get(id, username=username)

Get a VariablePresentation

Gets the details of a single instance of a VariablePresentation

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.VariablePresentationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a VariablePresentation
    api_response = api_instance.variablepresentations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variablepresentations_id_put**
> VariablePresentation variablepresentations_id_put(id, user, variable_presentation=variable_presentation)

Update a VariablePresentation

Updates an existing VariablePresentation

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
variable_presentation = modelcatalog.VariablePresentation() # VariablePresentation | An old VariablePresentationto be updated (optional)

try:
    # Update a VariablePresentation
    api_response = api_instance.variablepresentations_id_put(id, user, variable_presentation=variable_presentation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **variable_presentation** | [**VariablePresentation**](VariablePresentation.md)| An old VariablePresentationto be updated | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variablepresentations_post**
> VariablePresentation variablepresentations_post(user, variable_presentation=variable_presentation)

Create a VariablePresentation

Create a new instance of a VariablePresentation

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
variable_presentation = modelcatalog.VariablePresentation() # VariablePresentation | A new VariablePresentationto be created (optional)

try:
    # Create a VariablePresentation
    api_response = api_instance.variablepresentations_post(user, variable_presentation=variable_presentation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **variable_presentation** | [**VariablePresentation**](VariablePresentation.md)| A new VariablePresentationto be created | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


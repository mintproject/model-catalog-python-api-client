# modelcatalog.VariablePresentationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variablepresentations_get**](VariablePresentationApi.md#variablepresentations_get) | **GET** /variablepresentations | List all instances of VariablePresentation
[**variablepresentations_id_delete**](VariablePresentationApi.md#variablepresentations_id_delete) | **DELETE** /variablepresentations/{id} | Delete an existing VariablePresentation
[**variablepresentations_id_get**](VariablePresentationApi.md#variablepresentations_id_get) | **GET** /variablepresentations/{id} | Get a single VariablePresentation by its id
[**variablepresentations_id_put**](VariablePresentationApi.md#variablepresentations_id_put) | **PUT** /variablepresentations/{id} | Update an existing VariablePresentation
[**variablepresentations_post**](VariablePresentationApi.md#variablepresentations_post) | **POST** /variablepresentations | Create one VariablePresentation


# **variablepresentations_get**
> list[VariablePresentation] variablepresentations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of VariablePresentation

Gets a list of all instances of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VariablePresentationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of VariablePresentation
    api_response = api_instance.variablepresentations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[VariablePresentation]**](VariablePresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of VariablePresentation. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **variablepresentations_id_delete**
> variablepresentations_id_delete(id, user=user)

Delete an existing VariablePresentation

Delete an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the VariablePresentation to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing VariablePresentation
    api_instance.variablepresentations_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the VariablePresentation to be retrieved | 
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

# **variablepresentations_id_get**
> VariablePresentation variablepresentations_id_get(id, username=username)

Get a single VariablePresentation by its id

Gets the details of a given VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VariablePresentationApi()
id = 'id_example' # str | The ID of the VariablePresentation to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single VariablePresentation by its id
    api_response = api_instance.variablepresentations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the VariablePresentation to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given VariablePresentation |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **variablepresentations_id_put**
> VariablePresentation variablepresentations_id_put(id, user=user, variable_presentation=variable_presentation)

Update an existing VariablePresentation

Updates an existing VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the VariablePresentation to be retrieved
user = 'user_example' # str | Username (optional)
variable_presentation = modelcatalog.VariablePresentation() # VariablePresentation | An old VariablePresentationto be updated (optional)

try:
    # Update an existing VariablePresentation
    api_response = api_instance.variablepresentations_id_put(id, user=user, variable_presentation=variable_presentation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the VariablePresentation to be retrieved | 
 **user** | **str**| Username | [optional] 
 **variable_presentation** | [**VariablePresentation**](VariablePresentation.md)| An old VariablePresentationto be updated | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

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

# **variablepresentations_post**
> VariablePresentation variablepresentations_post(user=user, variable_presentation=variable_presentation)

Create one VariablePresentation

Create a new instance of VariablePresentation (more information in https://w3id.org/okn/o/sd#VariablePresentation)

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
api_instance = modelcatalog.VariablePresentationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
variable_presentation = modelcatalog.VariablePresentation() # VariablePresentation | Information about the VariablePresentationto be created (optional)

try:
    # Create one VariablePresentation
    api_response = api_instance.variablepresentations_post(user=user, variable_presentation=variable_presentation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablePresentationApi->variablepresentations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **variable_presentation** | [**VariablePresentation**](VariablePresentation.md)| Information about the VariablePresentationto be created | [optional] 

### Return type

[**VariablePresentation**](VariablePresentation.md)

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


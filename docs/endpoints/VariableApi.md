# modelcatalog.VariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variables_get**](VariableApi.md#variables_get) | **GET** /variables | List all instances of Variable
[**variables_id_delete**](VariableApi.md#variables_id_delete) | **DELETE** /variables/{id} | Delete an existing Variable
[**variables_id_get**](VariableApi.md#variables_id_get) | **GET** /variables/{id} | Get a single Variable by its id
[**variables_id_put**](VariableApi.md#variables_id_put) | **PUT** /variables/{id} | Update an existing Variable
[**variables_post**](VariableApi.md#variables_post) | **POST** /variables | Create one Variable


# **variables_get**
> list[Variable] variables_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Variable

Gets a list of all instances of Variable (more information in https://w3id.org/okn/o/sd#Variable)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VariableApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Variable
    api_response = api_instance.variables_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Variable]**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Variable. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **variables_id_delete**
> variables_id_delete(id, user)

Delete an existing Variable

Delete an existing Variable (more information in https://w3id.org/okn/o/sd#Variable)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.VariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Variable to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Variable
    api_instance.variables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Variable to be retrieved | 
 **user** | **str**| Username | 

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

# **variables_id_get**
> Variable variables_id_get(id, username=username)

Get a single Variable by its id

Gets the details of a given Variable (more information in https://w3id.org/okn/o/sd#Variable)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VariableApi()
id = 'id_example' # str | The ID of the Variable to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Variable by its id
    api_response = api_instance.variables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Variable to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Variable |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **variables_id_put**
> Variable variables_id_put(id, user, variable=variable)

Update an existing Variable

Updates an existing Variable (more information in https://w3id.org/okn/o/sd#Variable)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.VariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Variable to be retrieved
user = 'user_example' # str | Username
variable = modelcatalog.Variable() # Variable | An old Variableto be updated (optional)

try:
    # Update an existing Variable
    api_response = api_instance.variables_id_put(id, user, variable=variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Variable to be retrieved | 
 **user** | **str**| Username | 
 **variable** | [**Variable**](Variable.md)| An old Variableto be updated | [optional] 

### Return type

[**Variable**](Variable.md)

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

# **variables_post**
> Variable variables_post(user, variable=variable)

Create one Variable

Create a new instance of Variable (more information in https://w3id.org/okn/o/sd#Variable)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.VariableApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
variable = modelcatalog.Variable() # Variable | Information about the Variableto be created (optional)

try:
    # Create one Variable
    api_response = api_instance.variables_post(user, variable=variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableApi->variables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **variable** | [**Variable**](Variable.md)| Information about the Variableto be created | [optional] 

### Return type

[**Variable**](Variable.md)

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


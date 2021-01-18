# modelcatalog.ParameterApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parameters_get**](ParameterApi.md#parameters_get) | **GET** /parameters | List all instances of Parameter
[**parameters_id_delete**](ParameterApi.md#parameters_id_delete) | **DELETE** /parameters/{id} | Delete an existing Parameter
[**parameters_id_get**](ParameterApi.md#parameters_id_get) | **GET** /parameters/{id} | Get a single Parameter by its id
[**parameters_id_put**](ParameterApi.md#parameters_id_put) | **PUT** /parameters/{id} | Update an existing Parameter
[**parameters_post**](ParameterApi.md#parameters_post) | **POST** /parameters | Create one Parameter


# **parameters_get**
> list[Parameter] parameters_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Parameter

Gets a list of all instances of Parameter (more information in https://w3id.org/okn/o/sd#Parameter)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ParameterApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Parameter
    api_response = api_instance.parameters_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Parameter]**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **parameters_id_delete**
> parameters_id_delete(id, user=user)

Delete an existing Parameter

Delete an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Parameter to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Parameter
    api_instance.parameters_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Parameter to be retrieved | 
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

# **parameters_id_get**
> Parameter parameters_id_get(id, username=username)

Get a single Parameter by its id

Gets the details of a given Parameter (more information in https://w3id.org/okn/o/sd#Parameter)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ParameterApi()
id = 'id_example' # str | The ID of the Parameter to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Parameter by its id
    api_response = api_instance.parameters_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Parameter to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Parameter**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Parameter |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **parameters_id_put**
> Parameter parameters_id_put(id, user=user, parameter=parameter)

Update an existing Parameter

Updates an existing Parameter (more information in https://w3id.org/okn/o/sd#Parameter)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Parameter to be retrieved
user = 'user_example' # str | Username (optional)
parameter = modelcatalog.Parameter() # Parameter | An old Parameterto be updated (optional)

try:
    # Update an existing Parameter
    api_response = api_instance.parameters_id_put(id, user=user, parameter=parameter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Parameter to be retrieved | 
 **user** | **str**| Username | [optional] 
 **parameter** | [**Parameter**](Parameter.md)| An old Parameterto be updated | [optional] 

### Return type

[**Parameter**](Parameter.md)

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

# **parameters_post**
> Parameter parameters_post(user=user, parameter=parameter)

Create one Parameter

Create a new instance of Parameter (more information in https://w3id.org/okn/o/sd#Parameter)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.ParameterApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
parameter = modelcatalog.Parameter() # Parameter | Information about the Parameterto be created (optional)

try:
    # Create one Parameter
    api_response = api_instance.parameters_post(user=user, parameter=parameter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->parameters_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **parameter** | [**Parameter**](Parameter.md)| Information about the Parameterto be created | [optional] 

### Return type

[**Parameter**](Parameter.md)

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


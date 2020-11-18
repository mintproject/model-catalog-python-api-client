# modelcatalog.StandardVariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standardvariables_get**](StandardVariableApi.md#standardvariables_get) | **GET** /standardvariables | List all instances of StandardVariable
[**standardvariables_id_delete**](StandardVariableApi.md#standardvariables_id_delete) | **DELETE** /standardvariables/{id} | Delete an existing StandardVariable
[**standardvariables_id_get**](StandardVariableApi.md#standardvariables_id_get) | **GET** /standardvariables/{id} | Get a single StandardVariable by its id
[**standardvariables_id_put**](StandardVariableApi.md#standardvariables_id_put) | **PUT** /standardvariables/{id} | Update an existing StandardVariable
[**standardvariables_post**](StandardVariableApi.md#standardvariables_post) | **POST** /standardvariables | Create one StandardVariable


# **standardvariables_get**
> list[StandardVariable] standardvariables_get(username=username, label=label, page=page, per_page=per_page)

List all instances of StandardVariable

Gets a list of all instances of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.StandardVariableApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of StandardVariable
    api_response = api_instance.standardvariables_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[StandardVariable]**](StandardVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of StandardVariable. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **standardvariables_id_delete**
> standardvariables_id_delete(id, user)

Delete an existing StandardVariable

Delete an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)

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
api_instance = modelcatalog.StandardVariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the StandardVariable to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing StandardVariable
    api_instance.standardvariables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the StandardVariable to be retrieved | 
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

# **standardvariables_id_get**
> StandardVariable standardvariables_id_get(id, username=username)

Get a single StandardVariable by its id

Gets the details of a given StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.StandardVariableApi()
id = 'id_example' # str | The ID of the StandardVariable to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single StandardVariable by its id
    api_response = api_instance.standardvariables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the StandardVariable to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**StandardVariable**](StandardVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given StandardVariable |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **standardvariables_id_put**
> StandardVariable standardvariables_id_put(id, user, standard_variable=standard_variable)

Update an existing StandardVariable

Updates an existing StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)

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
api_instance = modelcatalog.StandardVariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the StandardVariable to be retrieved
user = 'user_example' # str | Username
standard_variable = modelcatalog.StandardVariable() # StandardVariable | An old StandardVariableto be updated (optional)

try:
    # Update an existing StandardVariable
    api_response = api_instance.standardvariables_id_put(id, user, standard_variable=standard_variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the StandardVariable to be retrieved | 
 **user** | **str**| Username | 
 **standard_variable** | [**StandardVariable**](StandardVariable.md)| An old StandardVariableto be updated | [optional] 

### Return type

[**StandardVariable**](StandardVariable.md)

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

# **standardvariables_post**
> StandardVariable standardvariables_post(user, standard_variable=standard_variable)

Create one StandardVariable

Create a new instance of StandardVariable (more information in https://w3id.org/okn/o/sd#StandardVariable)

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
api_instance = modelcatalog.StandardVariableApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
standard_variable = modelcatalog.StandardVariable() # StandardVariable | Information about the StandardVariableto be created (optional)

try:
    # Create one StandardVariable
    api_response = api_instance.standardvariables_post(user, standard_variable=standard_variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariableApi->standardvariables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **standard_variable** | [**StandardVariable**](StandardVariable.md)| Information about the StandardVariableto be created | [optional] 

### Return type

[**StandardVariable**](StandardVariable.md)

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


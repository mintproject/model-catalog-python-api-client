# modelcatalog.ModelConfigurationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_modelconfigurationsetups_id_get**](ModelConfigurationSetupApi.md#custom_modelconfigurationsetups_id_get) | **GET** /custom/modelconfigurationsetups/{id} | Get a ModelConfigurationSetup
[**custom_modelconfigurationsetups_variable_get**](ModelConfigurationSetupApi.md#custom_modelconfigurationsetups_variable_get) | **GET** /custom/modelconfigurationsetups/variable | Get a list  Model
[**modelconfigurationsetups_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_get) | **GET** /modelconfigurationsetups | List all instances of ModelConfigurationSetup
[**modelconfigurationsetups_id_delete**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_delete) | **DELETE** /modelconfigurationsetups/{id} | Delete an existing ModelConfigurationSetup
[**modelconfigurationsetups_id_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_get) | **GET** /modelconfigurationsetups/{id} | Get a single ModelConfigurationSetup by its id
[**modelconfigurationsetups_id_put**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_put) | **PUT** /modelconfigurationsetups/{id} | Update an existing ModelConfigurationSetup
[**modelconfigurationsetups_post**](ModelConfigurationSetupApi.md#modelconfigurationsetups_post) | **POST** /modelconfigurationsetups | Create one ModelConfigurationSetup


# **custom_modelconfigurationsetups_id_get**
> ModelConfigurationSetup custom_modelconfigurationsetups_id_get(id, username=username, custom_query_name=custom_query_name)

Get a ModelConfigurationSetup

Gets the details of a single instance of a ModelConfigurationSetup

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)
custom_query_name = 'custom_modelconfigurationsetups' # str | Name of the custom query (optional) (default to 'custom_modelconfigurationsetups')

try:
    # Get a ModelConfigurationSetup
    api_response = api_instance.custom_modelconfigurationsetups_id_get(id, username=username, custom_query_name=custom_query_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->custom_modelconfigurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_modelconfigurationsetups&#39;]

### Return type

[**ModelConfigurationSetup**](ModelConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of  ModelConfigurationSetup |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_modelconfigurationsetups_variable_get**
> list[ModelConfigurationSetup] custom_modelconfigurationsetups_variable_get(label, custom_query_name=custom_query_name, username=username)

Get a list  Model

Get model configurations by variable name

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi()
label = 'label_example' # str | variable to search
custom_query_name = 'custom_modelconfigurationsetups_variable' # str | Name of the custom query (optional) (default to 'custom_modelconfigurationsetups_variable')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a list  Model
    api_response = api_instance.custom_modelconfigurationsetups_variable_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->custom_modelconfigurationsetups_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| variable to search | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_modelconfigurationsetups_variable&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[ModelConfigurationSetup]**](ModelConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of instance of ModelConfigurationSetup |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurationsetups_get**
> list[ModelConfigurationSetup] modelconfigurationsetups_get(username=username, label=label, page=page, per_page=per_page)

List all instances of ModelConfigurationSetup

Gets a list of all instances of ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[ModelConfigurationSetup]**](ModelConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of ModelConfigurationSetup. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurationsetups_id_delete**
> modelconfigurationsetups_id_delete(id, user=user)

Delete an existing ModelConfigurationSetup

Delete an existing ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)

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
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelConfigurationSetup to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing ModelConfigurationSetup
    api_instance.modelconfigurationsetups_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfigurationSetup to be retrieved | 
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

# **modelconfigurationsetups_id_get**
> ModelConfigurationSetup modelconfigurationsetups_id_get(id, username=username)

Get a single ModelConfigurationSetup by its id

Gets the details of a given ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi()
id = 'id_example' # str | The ID of the ModelConfigurationSetup to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single ModelConfigurationSetup by its id
    api_response = api_instance.modelconfigurationsetups_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfigurationSetup to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**ModelConfigurationSetup**](ModelConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given ModelConfigurationSetup |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurationsetups_id_put**
> ModelConfigurationSetup modelconfigurationsetups_id_put(id, user=user, model_configuration_setup=model_configuration_setup)

Update an existing ModelConfigurationSetup

Updates an existing ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)

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
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelConfigurationSetup to be retrieved
user = 'user_example' # str | Username (optional)
model_configuration_setup = modelcatalog.ModelConfigurationSetup() # ModelConfigurationSetup | An old ModelConfigurationSetupto be updated (optional)

try:
    # Update an existing ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_id_put(id, user=user, model_configuration_setup=model_configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfigurationSetup to be retrieved | 
 **user** | **str**| Username | [optional] 
 **model_configuration_setup** | [**ModelConfigurationSetup**](ModelConfigurationSetup.md)| An old ModelConfigurationSetupto be updated | [optional] 

### Return type

[**ModelConfigurationSetup**](ModelConfigurationSetup.md)

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

# **modelconfigurationsetups_post**
> ModelConfigurationSetup modelconfigurationsetups_post(user=user, model_configuration_setup=model_configuration_setup)

Create one ModelConfigurationSetup

Create a new instance of ModelConfigurationSetup (more information in https://w3id.org/okn/o/sdm#ModelConfigurationSetup)

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
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
model_configuration_setup = modelcatalog.ModelConfigurationSetup() # ModelConfigurationSetup | Information about the ModelConfigurationSetupto be created (optional)

try:
    # Create one ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_post(user=user, model_configuration_setup=model_configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **model_configuration_setup** | [**ModelConfigurationSetup**](ModelConfigurationSetup.md)| Information about the ModelConfigurationSetupto be created | [optional] 

### Return type

[**ModelConfigurationSetup**](ModelConfigurationSetup.md)

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


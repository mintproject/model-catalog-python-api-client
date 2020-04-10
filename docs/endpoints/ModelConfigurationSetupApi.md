# modelcatalog.ModelConfigurationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_modelconfigurationsetups_id_get**](ModelConfigurationSetupApi.md#custom_modelconfigurationsetups_id_get) | **GET** /custom/modelconfigurationsetups/{id} | Get a ModelConfigurationSetup
[**custom_modelconfigurationsetups_variable_get**](ModelConfigurationSetupApi.md#custom_modelconfigurationsetups_variable_get) | **GET** /custom/modelconfigurationsetups/variable | Get a list  Model
[**modelconfigurationsetups_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_get) | **GET** /modelconfigurationsetups | List all ModelConfigurationSetup entities
[**modelconfigurationsetups_id_delete**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_delete) | **DELETE** /modelconfigurationsetups/{id} | Delete a ModelConfigurationSetup
[**modelconfigurationsetups_id_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_get) | **GET** /modelconfigurationsetups/{id} | Get a ModelConfigurationSetup
[**modelconfigurationsetups_id_put**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_put) | **PUT** /modelconfigurationsetups/{id} | Update a ModelConfigurationSetup
[**modelconfigurationsetups_post**](ModelConfigurationSetupApi.md#modelconfigurationsetups_post) | **POST** /modelconfigurationsetups | Create a ModelConfigurationSetup


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
> list[ModelConfigurationSetup] modelconfigurationsetups_get(username=username, label=label)

List all ModelConfigurationSetup entities

Gets a list of all ModelConfigurationSetup entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all ModelConfigurationSetup entities
    api_response = api_instance.modelconfigurationsetups_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

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
**200** | Successful response - returns an array of ModelConfigurationSetup entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurationsetups_id_delete**
> modelconfigurationsetups_id_delete(id, user)

Delete a ModelConfigurationSetup

Delete an existing ModelConfigurationSetup

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a ModelConfigurationSetup
    api_instance.modelconfigurationsetups_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
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

# **modelconfigurationsetups_id_get**
> ModelConfigurationSetup modelconfigurationsetups_id_get(id, username=username)

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

try:
    # Get a ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

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

# **modelconfigurationsetups_id_put**
> ModelConfigurationSetup modelconfigurationsetups_id_put(id, user, model_configuration_setup=model_configuration_setup)

Update a ModelConfigurationSetup

Updates an existing ModelConfigurationSetup

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
model_configuration_setup = modelcatalog.ModelConfigurationSetup() # ModelConfigurationSetup | An old ModelConfigurationSetupto be updated (optional)

try:
    # Update a ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_id_put(id, user, model_configuration_setup=model_configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
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
> ModelConfigurationSetup modelconfigurationsetups_post(user, model_configuration_setup=model_configuration_setup)

Create a ModelConfigurationSetup

Create a new instance of a ModelConfigurationSetup

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationSetupApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model_configuration_setup = modelcatalog.ModelConfigurationSetup() # ModelConfigurationSetup | A new ModelConfigurationSetupto be created (optional)

try:
    # Create a ModelConfigurationSetup
    api_response = api_instance.modelconfigurationsetups_post(user, model_configuration_setup=model_configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationSetupApi->modelconfigurationsetups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model_configuration_setup** | [**ModelConfigurationSetup**](ModelConfigurationSetup.md)| A new ModelConfigurationSetupto be created | [optional] 

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


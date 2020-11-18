# modelcatalog.ModelConfigurationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_modelconfigurations_id_get**](ModelConfigurationApi.md#custom_modelconfigurations_id_get) | **GET** /custom/modelconfigurations/{id} | Get a ModelConfiguration
[**modelconfigurations_get**](ModelConfigurationApi.md#modelconfigurations_get) | **GET** /modelconfigurations | List all instances of ModelConfiguration
[**modelconfigurations_id_delete**](ModelConfigurationApi.md#modelconfigurations_id_delete) | **DELETE** /modelconfigurations/{id} | Delete an existing ModelConfiguration
[**modelconfigurations_id_get**](ModelConfigurationApi.md#modelconfigurations_id_get) | **GET** /modelconfigurations/{id} | Get a single ModelConfiguration by its id
[**modelconfigurations_id_put**](ModelConfigurationApi.md#modelconfigurations_id_put) | **PUT** /modelconfigurations/{id} | Update an existing ModelConfiguration
[**modelconfigurations_post**](ModelConfigurationApi.md#modelconfigurations_post) | **POST** /modelconfigurations | Create one ModelConfiguration


# **custom_modelconfigurations_id_get**
> ModelConfiguration custom_modelconfigurations_id_get(id, username=username, custom_query_name=custom_query_name)

Get a ModelConfiguration

Gets the details of a single instance of a ModelConfiguration

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)
custom_query_name = 'custom_modelconfigurations' # str | Name of the custom query (optional) (default to 'custom_modelconfigurations')

try:
    # Get a ModelConfiguration
    api_response = api_instance.custom_modelconfigurations_id_get(id, username=username, custom_query_name=custom_query_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->custom_modelconfigurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_modelconfigurations&#39;]

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of ModelConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurations_get**
> list[ModelConfiguration] modelconfigurations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of ModelConfiguration

Gets a list of all instances of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of ModelConfiguration
    api_response = api_instance.modelconfigurations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[ModelConfiguration]**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of ModelConfiguration. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurations_id_delete**
> modelconfigurations_id_delete(id, user)

Delete an existing ModelConfiguration

Delete an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelConfiguration to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing ModelConfiguration
    api_instance.modelconfigurations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfiguration to be retrieved | 
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

# **modelconfigurations_id_get**
> ModelConfiguration modelconfigurations_id_get(id, username=username)

Get a single ModelConfiguration by its id

Gets the details of a given ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
id = 'id_example' # str | The ID of the ModelConfiguration to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single ModelConfiguration by its id
    api_response = api_instance.modelconfigurations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfiguration to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given ModelConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelconfigurations_id_put**
> ModelConfiguration modelconfigurations_id_put(id, user, model_configuration=model_configuration)

Update an existing ModelConfiguration

Updates an existing ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelConfiguration to be retrieved
user = 'user_example' # str | Username
model_configuration = modelcatalog.ModelConfiguration() # ModelConfiguration | An old ModelConfigurationto be updated (optional)

try:
    # Update an existing ModelConfiguration
    api_response = api_instance.modelconfigurations_id_put(id, user, model_configuration=model_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelConfiguration to be retrieved | 
 **user** | **str**| Username | 
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)| An old ModelConfigurationto be updated | [optional] 

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

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

# **modelconfigurations_post**
> ModelConfiguration modelconfigurations_post(user, model_configuration=model_configuration)

Create one ModelConfiguration

Create a new instance of ModelConfiguration (more information in https://w3id.org/okn/o/sdm#ModelConfiguration)

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model_configuration = modelcatalog.ModelConfiguration() # ModelConfiguration | Information about the ModelConfigurationto be created (optional)

try:
    # Create one ModelConfiguration
    api_response = api_instance.modelconfigurations_post(user, model_configuration=model_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)| Information about the ModelConfigurationto be created | [optional] 

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

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


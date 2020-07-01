# modelcatalog.ConfigurationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationsetups_get**](ConfigurationSetupApi.md#configurationsetups_get) | **GET** /configurationsetups | List all instances of ConfigurationSetup
[**configurationsetups_id_delete**](ConfigurationSetupApi.md#configurationsetups_id_delete) | **DELETE** /configurationsetups/{id} | Delete an existing ConfigurationSetup
[**configurationsetups_id_get**](ConfigurationSetupApi.md#configurationsetups_id_get) | **GET** /configurationsetups/{id} | Get a single ConfigurationSetup by its id
[**configurationsetups_id_put**](ConfigurationSetupApi.md#configurationsetups_id_put) | **PUT** /configurationsetups/{id} | Update an existing ConfigurationSetup
[**configurationsetups_post**](ConfigurationSetupApi.md#configurationsetups_post) | **POST** /configurationsetups | Create one ConfigurationSetup
[**custom_configurationsetups_id_get**](ConfigurationSetupApi.md#custom_configurationsetups_id_get) | **GET** /custom/configurationsetups/{id} | Get a ModelConfigurationSetup


# **configurationsetups_get**
> list[ConfigurationSetup] configurationsetups_get(username=username, label=label, page=page, per_page=per_page)

List all instances of ConfigurationSetup

Gets a list of all instances of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of ConfigurationSetup
    api_response = api_instance.configurationsetups_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[ConfigurationSetup]**](ConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of ConfigurationSetup. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **configurationsetups_id_delete**
> configurationsetups_id_delete(id, user)

Delete an existing ConfigurationSetup

Delete an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ConfigurationSetup to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing ConfigurationSetup
    api_instance.configurationsetups_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ConfigurationSetup to be retrieved | 
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

# **configurationsetups_id_get**
> ConfigurationSetup configurationsetups_id_get(id, username=username)

Get a single ConfigurationSetup by its id

Gets the details of a given ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi()
id = 'id_example' # str | The ID of the ConfigurationSetup to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single ConfigurationSetup by its id
    api_response = api_instance.configurationsetups_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ConfigurationSetup to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given ConfigurationSetup |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **configurationsetups_id_put**
> ConfigurationSetup configurationsetups_id_put(id, user, configuration_setup=configuration_setup)

Update an existing ConfigurationSetup

Updates an existing ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ConfigurationSetup to be retrieved
user = 'user_example' # str | Username
configuration_setup = modelcatalog.ConfigurationSetup() # ConfigurationSetup | An old ConfigurationSetupto be updated (optional)

try:
    # Update an existing ConfigurationSetup
    api_response = api_instance.configurationsetups_id_put(id, user, configuration_setup=configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ConfigurationSetup to be retrieved | 
 **user** | **str**| Username | 
 **configuration_setup** | [**ConfigurationSetup**](ConfigurationSetup.md)| An old ConfigurationSetupto be updated | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

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

# **configurationsetups_post**
> ConfigurationSetup configurationsetups_post(user, configuration_setup=configuration_setup)

Create one ConfigurationSetup

Create a new instance of ConfigurationSetup (more information in https://w3id.org/okn/o/sd#ConfigurationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
configuration_setup = modelcatalog.ConfigurationSetup() # ConfigurationSetup | Information about the ConfigurationSetupto be created (optional)

try:
    # Create one ConfigurationSetup
    api_response = api_instance.configurationsetups_post(user, configuration_setup=configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **configuration_setup** | [**ConfigurationSetup**](ConfigurationSetup.md)| Information about the ConfigurationSetupto be created | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

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

# **custom_configurationsetups_id_get**
> ModelConfigurationSetup custom_configurationsetups_id_get(id, username=username, custom_query_name=custom_query_name)

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
api_instance = modelcatalog.ConfigurationSetupApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)
custom_query_name = 'custom_configurationsetups' # str | Name of the custom query (optional) (default to 'custom_configurationsetups')

try:
    # Get a ModelConfigurationSetup
    api_response = api_instance.custom_configurationsetups_id_get(id, username=username, custom_query_name=custom_query_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->custom_configurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_configurationsetups&#39;]

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


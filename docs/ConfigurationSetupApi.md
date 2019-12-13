# modelcatalog.ConfigurationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationsetups_get**](ConfigurationSetupApi.md#configurationsetups_get) | **GET** /configurationsetups | List all ConfigurationSetup entities
[**configurationsetups_id_delete**](ConfigurationSetupApi.md#configurationsetups_id_delete) | **DELETE** /configurationsetups/{id} | Delete a ConfigurationSetup
[**configurationsetups_id_get**](ConfigurationSetupApi.md#configurationsetups_id_get) | **GET** /configurationsetups/{id} | Get a ConfigurationSetup
[**configurationsetups_id_put**](ConfigurationSetupApi.md#configurationsetups_id_put) | **PUT** /configurationsetups/{id} | Update a ConfigurationSetup
[**configurationsetups_post**](ConfigurationSetupApi.md#configurationsetups_post) | **POST** /configurationsetups | Create a ConfigurationSetup
[**custom_configurationsetups_id_get**](ConfigurationSetupApi.md#custom_configurationsetups_id_get) | **GET** /custom/configurationsetups/{id} | Get a ModelConfigurationSetup


# **configurationsetups_get**
> list[ConfigurationSetup] configurationsetups_get(username=username, label=label)

List all ConfigurationSetup entities

Gets a list of all ConfigurationSetup entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all ConfigurationSetup entities
    api_response = api_instance.configurationsetups_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[ConfigurationSetup]**](ConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurationsetups_id_delete**
> configurationsetups_id_delete(id, user)

Delete a ConfigurationSetup

Delete an existing ConfigurationSetup

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
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a ConfigurationSetup
    api_instance.configurationsetups_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_delete: %s\n" % e)
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

# **configurationsetups_id_get**
> ConfigurationSetup configurationsetups_id_get(id, username=username)

Get a ConfigurationSetup

Gets the details of a single instance of a ConfigurationSetup

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ConfigurationSetupApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a ConfigurationSetup
    api_response = api_instance.configurationsetups_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurationsetups_id_put**
> ConfigurationSetup configurationsetups_id_put(id, user, configuration_setup=configuration_setup)

Update a ConfigurationSetup

Updates an existing ConfigurationSetup

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
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
configuration_setup = modelcatalog.ConfigurationSetup() # ConfigurationSetup | An old ConfigurationSetupto be updated (optional)

try:
    # Update a ConfigurationSetup
    api_response = api_instance.configurationsetups_id_put(id, user, configuration_setup=configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **configuration_setup** | [**ConfigurationSetup**](ConfigurationSetup.md)| An old ConfigurationSetupto be updated | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurationsetups_post**
> ConfigurationSetup configurationsetups_post(user, configuration_setup=configuration_setup)

Create a ConfigurationSetup

Create a new instance of a ConfigurationSetup

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
api_instance = modelcatalog.ConfigurationSetupApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
configuration_setup = modelcatalog.ConfigurationSetup() # ConfigurationSetup | A new ConfigurationSetupto be created (optional)

try:
    # Create a ConfigurationSetup
    api_response = api_instance.configurationsetups_post(user, configuration_setup=configuration_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationSetupApi->configurationsetups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **configuration_setup** | [**ConfigurationSetup**](ConfigurationSetup.md)| A new ConfigurationSetupto be created | [optional] 

### Return type

[**ConfigurationSetup**](ConfigurationSetup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


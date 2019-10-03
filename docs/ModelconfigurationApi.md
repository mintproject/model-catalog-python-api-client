# modelcatalog.ModelConfigurationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelconfigurations_get**](ModelConfigurationApi.md#modelconfigurations_get) | **GET** /modelconfigurations | List all ModelConfiguration entities
[**modelconfigurations_id_delete**](ModelConfigurationApi.md#modelconfigurations_id_delete) | **DELETE** /modelconfigurations/{id} | Delete a ModelConfiguration
[**modelconfigurations_id_get**](ModelConfigurationApi.md#modelconfigurations_id_get) | **GET** /modelconfigurations/{id} | Get a ModelConfiguration
[**modelconfigurations_id_put**](ModelConfigurationApi.md#modelconfigurations_id_put) | **PUT** /modelconfigurations/{id} | Update a ModelConfiguration
[**modelconfigurations_post**](ModelConfigurationApi.md#modelconfigurations_post) | **POST** /modelconfigurations | Create a ModelConfiguration


# **modelconfigurations_get**
> list[ModelConfiguration] modelconfigurations_get(username=username)

List all ModelConfiguration entities

Gets a list of all ModelConfiguration entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all ModelConfiguration entities
    api_response = api_instance.modelconfigurations_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[ModelConfiguration]**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelconfigurations_id_delete**
> modelconfigurations_id_delete(id, user)

Delete a ModelConfiguration

Delete an existing ModelConfiguration

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a ModelConfiguration
    api_instance.modelconfigurations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_delete: %s\n" % e)
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

# **modelconfigurations_id_get**
> ModelConfiguration modelconfigurations_id_get(id, username=username)

Get a ModelConfiguration

Gets the details of a single instance of a ModelConfiguration

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a ModelConfiguration
    api_response = api_instance.modelconfigurations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelconfigurations_id_put**
> modelconfigurations_id_put(id, user, model_configuration=model_configuration)

Update a ModelConfiguration

Updates an existing ModelConfiguration

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
model_configuration = modelcatalog.ModelConfiguration() # ModelConfiguration | An old ModelConfigurationto be updated (optional)

try:
    # Update a ModelConfiguration
    api_instance.modelconfigurations_id_put(id, user, model_configuration=model_configuration)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)| An old ModelConfigurationto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelconfigurations_post**
> modelconfigurations_post(user, model_configuration=model_configuration)

Create a ModelConfiguration

Create a new instance of a ModelConfiguration

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
api_instance = modelcatalog.ModelConfigurationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model_configuration = modelcatalog.ModelConfiguration() # ModelConfiguration | A new ModelConfigurationto be created (optional)

try:
    # Create a ModelConfiguration
    api_instance.modelconfigurations_post(user, model_configuration=model_configuration)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->modelconfigurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)| A new ModelConfigurationto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


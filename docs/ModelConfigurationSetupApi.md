# modelcatalog.ModelConfigurationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelconfigurationsetups_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_get) | **GET** /modelconfigurationsetups | List all ModelConfigurationSetup entities
[**modelconfigurationsetups_id_delete**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_delete) | **DELETE** /modelconfigurationsetups/{id} | Delete a ModelConfigurationSetup
[**modelconfigurationsetups_id_get**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_get) | **GET** /modelconfigurationsetups/{id} | Get a ModelConfigurationSetup
[**modelconfigurationsetups_id_put**](ModelConfigurationSetupApi.md#modelconfigurationsetups_id_put) | **PUT** /modelconfigurationsetups/{id} | Update a ModelConfigurationSetup
[**modelconfigurationsetups_post**](ModelConfigurationSetupApi.md#modelconfigurationsetups_post) | **POST** /modelconfigurationsetups | Create a ModelConfigurationSetup


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

# create an instance of the API class
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# create an instance of the API class
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


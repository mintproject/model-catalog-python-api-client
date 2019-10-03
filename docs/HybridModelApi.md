# modelcatalog.HybridModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hybridmodels_get**](HybridModelApi.md#hybridmodels_get) | **GET** /hybridmodels | List all HybridModel entities
[**hybridmodels_id_delete**](HybridModelApi.md#hybridmodels_id_delete) | **DELETE** /hybridmodels/{id} | Delete a HybridModel
[**hybridmodels_id_get**](HybridModelApi.md#hybridmodels_id_get) | **GET** /hybridmodels/{id} | Get a HybridModel
[**hybridmodels_id_put**](HybridModelApi.md#hybridmodels_id_put) | **PUT** /hybridmodels/{id} | Update a HybridModel
[**hybridmodels_post**](HybridModelApi.md#hybridmodels_post) | **POST** /hybridmodels | Create a HybridModel


# **hybridmodels_get**
> list[HybridModel] hybridmodels_get(username=username)

List all HybridModel entities

Gets a list of all HybridModel entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.HybridModelApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all HybridModel entities
    api_response = api_instance.hybridmodels_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[HybridModel]**](HybridModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hybridmodels_id_delete**
> hybridmodels_id_delete(id, user)

Delete a HybridModel

Delete an existing HybridModel

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a HybridModel
    api_instance.hybridmodels_id_delete(id, user)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_delete: %s\n" % e)
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

# **hybridmodels_id_get**
> HybridModel hybridmodels_id_get(id, username=username)

Get a HybridModel

Gets the details of a single instance of a HybridModel

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.HybridModelApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a HybridModel
    api_response = api_instance.hybridmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**HybridModel**](HybridModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hybridmodels_id_put**
> hybridmodels_id_put(id, user, hybrid_model=hybrid_model)

Update a HybridModel

Updates an existing HybridModel

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
hybrid_model = modelcatalog.HybridModel() # HybridModel | An old HybridModelto be updated (optional)

try:
    # Update a HybridModel
    api_instance.hybridmodels_id_put(id, user, hybrid_model=hybrid_model)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **hybrid_model** | [**HybridModel**](HybridModel.md)| An old HybridModelto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hybridmodels_post**
> hybridmodels_post(user, hybrid_model=hybrid_model)

Create a HybridModel

Create a new instance of a HybridModel

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
hybrid_model = modelcatalog.HybridModel() # HybridModel | A new HybridModelto be created (optional)

try:
    # Create a HybridModel
    api_instance.hybridmodels_post(user, hybrid_model=hybrid_model)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **hybrid_model** | [**HybridModel**](HybridModel.md)| A new HybridModelto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


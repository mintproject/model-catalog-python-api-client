# modelcatalog.EmpiricalModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**empiricalmodels_get**](EmpiricalModelApi.md#empiricalmodels_get) | **GET** /empiricalmodels | List all EmpiricalModel entities
[**empiricalmodels_id_delete**](EmpiricalModelApi.md#empiricalmodels_id_delete) | **DELETE** /empiricalmodels/{id} | Delete a EmpiricalModel
[**empiricalmodels_id_get**](EmpiricalModelApi.md#empiricalmodels_id_get) | **GET** /empiricalmodels/{id} | Get a EmpiricalModel
[**empiricalmodels_id_put**](EmpiricalModelApi.md#empiricalmodels_id_put) | **PUT** /empiricalmodels/{id} | Update a EmpiricalModel
[**empiricalmodels_post**](EmpiricalModelApi.md#empiricalmodels_post) | **POST** /empiricalmodels | Create a EmpiricalModel


# **empiricalmodels_get**
> list[EmpiricalModel] empiricalmodels_get(username=username, label=label)

List all EmpiricalModel entities

Gets a list of all EmpiricalModel entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.EmpiricalModelApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all EmpiricalModel entities
    api_response = api_instance.empiricalmodels_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[EmpiricalModel]**](EmpiricalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empiricalmodels_id_delete**
> empiricalmodels_id_delete(id, user)

Delete a EmpiricalModel

Delete an existing EmpiricalModel

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a EmpiricalModel
    api_instance.empiricalmodels_id_delete(id, user)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_delete: %s\n" % e)
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

# **empiricalmodels_id_get**
> EmpiricalModel empiricalmodels_id_get(id, username=username)

Get a EmpiricalModel

Gets the details of a single instance of a EmpiricalModel

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.EmpiricalModelApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a EmpiricalModel
    api_response = api_instance.empiricalmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empiricalmodels_id_put**
> EmpiricalModel empiricalmodels_id_put(id, user, empirical_model=empirical_model)

Update a EmpiricalModel

Updates an existing EmpiricalModel

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
empirical_model = modelcatalog.EmpiricalModel() # EmpiricalModel | An old EmpiricalModelto be updated (optional)

try:
    # Update a EmpiricalModel
    api_response = api_instance.empiricalmodels_id_put(id, user, empirical_model=empirical_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **empirical_model** | [**EmpiricalModel**](EmpiricalModel.md)| An old EmpiricalModelto be updated | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empiricalmodels_post**
> EmpiricalModel empiricalmodels_post(user, empirical_model=empirical_model)

Create a EmpiricalModel

Create a new instance of a EmpiricalModel

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
empirical_model = modelcatalog.EmpiricalModel() # EmpiricalModel | A new EmpiricalModelto be created (optional)

try:
    # Create a EmpiricalModel
    api_response = api_instance.empiricalmodels_post(user, empirical_model=empirical_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **empirical_model** | [**EmpiricalModel**](EmpiricalModel.md)| A new EmpiricalModelto be created | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


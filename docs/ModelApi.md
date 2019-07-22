# mint_client.ModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelApi.md#create_model) | **POST** /models | Create a model
[**delete_model**](ModelApi.md#delete_model) | **DELETE** /model/{id} | Delete a Model
[**get_model**](ModelApi.md#get_model) | **GET** /model/{id} | Get a Model
[**get_models**](ModelApi.md#get_models) | **GET** /models | List All models
[**update_model**](ModelApi.md#update_model) | **PUT** /model/{id} | Update a Model


# **create_model**
> create_model(model)

Create a model

Creates a new instance of a `model`.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.ModelApi(mint_client.ApiClient(configuration))
model = mint_client.Model() # Model | A new `model` to be created.

try:
    # Create a model
    api_instance.create_model(model)
except ApiException as e:
    print("Exception when calling ModelApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**Model**](Model.md)| A new &#x60;model&#x60; to be created. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(id, username=username)

Delete a Model

Deletes an existing `Model`.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.ModelApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for a `Model`.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Delete a Model
    api_instance.delete_model(id, username=username)
except ApiException as e:
    print("Exception when calling ModelApi->delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;Model&#x60;. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id, username=username)

Get a Model

Gets the details of a single instance of a `Model`.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelApi()
id = 'id_example' # str | A unique identifier for a `Model`.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get a Model
    api_response = api_instance.get_model(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;Model&#x60;. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> list[Model] get_models(username=username)

List All models

Gets a list of all `model` entities.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelApi()
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List All models
    api_response = api_instance.get_models(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> update_model(id, model, username=username)

Update a Model

Updates an existing `Model`.

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.ModelApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for a `Model`.
model = mint_client.Model() # Model | Updated `Model` information.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Update a Model
    api_instance.update_model(id, model, username=username)
except ApiException as e:
    print("Exception when calling ModelApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;Model&#x60;. | 
 **model** | [**Model**](Model.md)| Updated &#x60;Model&#x60; information. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


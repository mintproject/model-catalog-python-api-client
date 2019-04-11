# mint_client.ModelversionApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model_version**](ModelversionApi.md#create_model_version) | **POST** /modelversions | Create a ModelVersion
[**delete_model_version**](ModelversionApi.md#delete_model_version) | **DELETE** /modelversion/{id} | Delete a ModelVersion
[**get_model_version**](ModelversionApi.md#get_model_version) | **GET** /modelversion/{id} | Get a ModelVersion
[**get_model_versions**](ModelversionApi.md#get_model_versions) | **GET** /modelversions | List All ModelVersions
[**update_model_version**](ModelversionApi.md#update_model_version) | **PUT** /modelversion/{id} | Update a ModelVersion


# **create_model_version**
> create_model_version(model_version)

Create a ModelVersion

Creates a new instance of a `ModelVersion`.

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
api_instance = mint_client.ModelversionApi(mint_client.ApiClient(configuration))
model_version = mint_client.ModelVersion() # ModelVersion | A new `ModelVersion` to be created.

try:
    # Create a ModelVersion
    api_instance.create_model_version(model_version)
except ApiException as e:
    print("Exception when calling ModelversionApi->create_model_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_version** | [**ModelVersion**](ModelVersion.md)| A new &#x60;ModelVersion&#x60; to be created. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_version**
> delete_model_version(id)

Delete a ModelVersion

Deletes an existing `ModelVersion`.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelversionApi()
id = 'id_example' # str | A unique identifier for a `ModelVersion`.

try:
    # Delete a ModelVersion
    api_instance.delete_model_version(id)
except ApiException as e:
    print("Exception when calling ModelversionApi->delete_model_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelVersion&#x60;. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_version**
> ModelVersion get_model_version(id, username=username)

Get a ModelVersion

Gets the details of a single instance of a `ModelVersion`.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelversionApi()
id = 'id_example' # str | A unique identifier for a `ModelVersion`.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get a ModelVersion
    api_response = api_instance.get_model_version(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelversionApi->get_model_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelVersion&#x60;. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**ModelVersion**](ModelVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_versions**
> list[ModelVersion] get_model_versions(username=username)

List All ModelVersions

Gets a list of all `ModelVersion` entities.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelversionApi()
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List All ModelVersions
    api_response = api_instance.get_model_versions(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelversionApi->get_model_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[ModelVersion]**](ModelVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_version**
> update_model_version(id, model_version)

Update a ModelVersion

Updates an existing `ModelVersion`.

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
api_instance = mint_client.ModelversionApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for a `ModelVersion`.
model_version = mint_client.ModelVersion() # ModelVersion | Updated `ModelVersion` information.

try:
    # Update a ModelVersion
    api_instance.update_model_version(id, model_version)
except ApiException as e:
    print("Exception when calling ModelversionApi->update_model_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelVersion&#x60;. | 
 **model_version** | [**ModelVersion**](ModelVersion.md)| Updated &#x60;ModelVersion&#x60; information. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


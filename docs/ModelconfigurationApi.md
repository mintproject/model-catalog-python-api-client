# mint_client.ModelconfigurationApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inputs_by_modelconfiguration**](ModelconfigurationApi.md#create_inputs_by_modelconfiguration) | **POST** /modelconfiguration/{id}/inputs | Creates a new instance of a &#x60;DatasetSpecification&#x60; related as Input.
[**create_model_configuration**](ModelconfigurationApi.md#create_model_configuration) | **POST** /modelconfigurations | Create a model configuration
[**create_outputs_by_modelconfiguration**](ModelconfigurationApi.md#create_outputs_by_modelconfiguration) | **POST** /modelconfiguration/{id}/outputs | Create the output of a model configuration
[**create_parameters_by_modelconfiguration**](ModelconfigurationApi.md#create_parameters_by_modelconfiguration) | **POST** /modelconfiguration/{id}/parameters | Create the inputs of a model configuration
[**delete_model_configuration**](ModelconfigurationApi.md#delete_model_configuration) | **DELETE** /modelconfiguration/{id} | Delete a ModelConfiguration
[**get_inputs_by_modelconfiguration**](ModelconfigurationApi.md#get_inputs_by_modelconfiguration) | **GET** /modelconfiguration/{id}/inputs | Get the inputs of a model configuration
[**get_model_configuration**](ModelconfigurationApi.md#get_model_configuration) | **GET** /modelconfiguration/{id} | Get modelconfiguration
[**get_model_configurations**](ModelconfigurationApi.md#get_model_configurations) | **GET** /modelconfigurations | List modelconfiguration
[**get_outputs_by_modelconfiguration**](ModelconfigurationApi.md#get_outputs_by_modelconfiguration) | **GET** /modelconfiguration/{id}/outputs | Get the outputs of a model configuration
[**get_parameters_by_modelconfiguration**](ModelconfigurationApi.md#get_parameters_by_modelconfiguration) | **GET** /modelconfiguration/{id}/parameters | Get the parameters of a model configuration
[**update_model_configuration**](ModelconfigurationApi.md#update_model_configuration) | **PUT** /modelconfiguration/{id} | Update model configuration


# **create_inputs_by_modelconfiguration**
> create_inputs_by_modelconfiguration(id, dataset_specification)

Creates a new instance of a `DatasetSpecification` related as Input.

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | 
dataset_specification = [mint_client.DatasetSpecification()] # list[DatasetSpecification] | 

try:
    # Creates a new instance of a `DatasetSpecification` related as Input.
    api_instance.create_inputs_by_modelconfiguration(id, dataset_specification)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->create_inputs_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dataset_specification** | [**list[DatasetSpecification]**](DatasetSpecification.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_configuration**
> create_model_configuration(model_configuration)

Create a model configuration

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
model_configuration = mint_client.ModelConfiguration() # ModelConfiguration | 

try:
    # Create a model configuration
    api_instance.create_model_configuration(model_configuration)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->create_model_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_outputs_by_modelconfiguration**
> create_outputs_by_modelconfiguration(id, dataset_specification)

Create the output of a model configuration

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | 
dataset_specification = [mint_client.DatasetSpecification()] # list[DatasetSpecification] | 

try:
    # Create the output of a model configuration
    api_instance.create_outputs_by_modelconfiguration(id, dataset_specification)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->create_outputs_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dataset_specification** | [**list[DatasetSpecification]**](DatasetSpecification.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_parameters_by_modelconfiguration**
> create_parameters_by_modelconfiguration(id, parameter)

Create the inputs of a model configuration

Creates a new instance of a `DatasetSpecification` and it related with the `ModelConfiguration`.

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | 
parameter = [mint_client.Parameter()] # list[Parameter] | 

try:
    # Create the inputs of a model configuration
    api_instance.create_parameters_by_modelconfiguration(id, parameter)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->create_parameters_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **parameter** | [**list[Parameter]**](Parameter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_configuration**
> delete_model_configuration(id)

Delete a ModelConfiguration

Deletes an existing `ModelConfiguration`.

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for a `ModelConfiguration`.

try:
    # Delete a ModelConfiguration
    api_instance.delete_model_configuration(id)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->delete_model_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelConfiguration&#x60;. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inputs_by_modelconfiguration**
> list[DatasetSpecification] get_inputs_by_modelconfiguration(id, username=username)

Get the inputs of a model configuration

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelconfigurationApi()
id = 'id_example' # str | The name of the resource 
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get the inputs of a model configuration
    api_response = api_instance.get_inputs_by_modelconfiguration(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_inputs_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the resource  | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_configuration**
> ModelConfiguration get_model_configuration(id, username=username)

Get modelconfiguration

Gets the details of a single instance of a `ModelConfiguration`.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelconfigurationApi()
id = 'id_example' # str | A unique identifier for a `ModelConfiguration`.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get modelconfiguration
    api_response = api_instance.get_model_configuration(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_model_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelConfiguration&#x60;. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**ModelConfiguration**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_configurations**
> list[ModelConfiguration] get_model_configurations(username=username)

List modelconfiguration

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelconfigurationApi()
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List modelconfiguration
    api_response = api_instance.get_model_configurations(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_model_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[ModelConfiguration]**](ModelConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outputs_by_modelconfiguration**
> list[DatasetSpecification] get_outputs_by_modelconfiguration(id, username=username)

Get the outputs of a model configuration

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelconfigurationApi()
id = 'id_example' # str | The name of the resource 
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get the outputs of a model configuration
    api_response = api_instance.get_outputs_by_modelconfiguration(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_outputs_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the resource  | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters_by_modelconfiguration**
> list[Parameter] get_parameters_by_modelconfiguration(id, username=username)

Get the parameters of a model configuration

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ModelconfigurationApi()
id = 'id_example' # str | The name of the resource 
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # Get the parameters of a model configuration
    api_response = api_instance.get_parameters_by_modelconfiguration(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->get_parameters_by_modelconfiguration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the resource  | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[Parameter]**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_configuration**
> update_model_configuration(id, model_configuration)

Update model configuration

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
api_instance = mint_client.ModelconfigurationApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for a `ModelConfiguration`.
model_configuration = mint_client.ModelConfiguration() # ModelConfiguration | 

try:
    # Update model configuration
    api_instance.update_model_configuration(id, model_configuration)
except ApiException as e:
    print("Exception when calling ModelconfigurationApi->update_model_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;ModelConfiguration&#x60;. | 
 **model_configuration** | [**ModelConfiguration**](ModelConfiguration.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


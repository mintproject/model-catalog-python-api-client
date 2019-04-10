# openapi_client.ParameterApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_parameter**](ParameterApi.md#create_parameter) | **POST** /parameters | Create a Parameter
[**get_parameters**](ParameterApi.md#get_parameters) | **GET** /parameters | List All Parameters


# **create_parameter**
> create_parameter(parameter)

Create a Parameter

Creates a new instance of a `Parameter`.

### Example

* Basic Authentication (BearerAuth): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BearerAuth
configuration = openapi_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = openapi_client.ParameterApi(openapi_client.ApiClient(configuration))
parameter = openapi_client.Parameter() # Parameter | A new `Parameter` to be created.

try:
    # Create a Parameter
    api_instance.create_parameter(parameter)
except ApiException as e:
    print("Exception when calling ParameterApi->create_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter** | [**Parameter**](Parameter.md)| A new &#x60;Parameter&#x60; to be created. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters**
> list[Parameter] get_parameters(username=username)

List All Parameters

Gets a list of all `Parameter` entities.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.ParameterApi()
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List All Parameters
    api_response = api_instance.get_parameters(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterApi->get_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[Parameter]**](Parameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.DatasetspecificationApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_set**](DatasetspecificationApi.md#create_data_set) | **POST** /datasetspecifications | Create a datasetspecification
[**get_data_sets**](DatasetspecificationApi.md#get_data_sets) | **GET** /datasetspecifications | List All datasetspecifications


# **create_data_set**
> create_data_set(dataset_specification)

Create a datasetspecification

Creates a new instance of a `datasetspecification`.

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
api_instance = openapi_client.DatasetspecificationApi(openapi_client.ApiClient(configuration))
dataset_specification = openapi_client.DatasetSpecification() # DatasetSpecification | A new `datasetspecification` to be created.

try:
    # Create a datasetspecification
    api_instance.create_data_set(dataset_specification)
except ApiException as e:
    print("Exception when calling DatasetspecificationApi->create_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_specification** | [**DatasetSpecification**](DatasetSpecification.md)| A new &#x60;datasetspecification&#x60; to be created. | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_sets**
> list[DatasetSpecification] get_data_sets(username=username)

List All datasetspecifications

Gets a list of all `datasetspecification` entities.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DatasetspecificationApi()
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List All datasetspecifications
    api_response = api_instance.get_data_sets(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetspecificationApi->get_data_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


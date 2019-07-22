# mint_client.VariablespresentationsApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasetspecification_id_variablepresentations_get**](VariablespresentationsApi.md#datasetspecification_id_variablepresentations_get) | **GET** /datasetspecification/{id}/variablepresentations | List variable presentations related with a datasetspecification


# **datasetspecification_id_variablepresentations_get**
> list[VariablePresentation] datasetspecification_id_variablepresentations_get(id, username=username)

List variable presentations related with a datasetspecification

Gets a list of all `VariablePresentation` entities.

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.VariablespresentationsApi()
id = 'id_example' # str | A unique identifier for a `DatasetSpecification`.
username = 'username_example' # str | To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username (optional)

try:
    # List variable presentations related with a datasetspecification
    api_response = api_instance.datasetspecification_id_variablepresentations_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablespresentationsApi->datasetspecification_id_variablepresentations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for a &#x60;DatasetSpecification&#x60;. | 
 **username** | **str**| To obtain the results maintained by the MINT project, you must not set up the variable. If you want the results of a user, you must set up the variable with the username | [optional] 

### Return type

[**list[VariablePresentation]**](VariablePresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


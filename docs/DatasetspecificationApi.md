# modelcatalog.DatasetSpecificationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasetspecifications_get**](DatasetSpecificationApi.md#datasetspecifications_get) | **GET** /datasetspecifications | List all DatasetSpecification entities
[**datasetspecifications_id_delete**](DatasetSpecificationApi.md#datasetspecifications_id_delete) | **DELETE** /datasetspecifications/{id} | Delete a DatasetSpecification
[**datasetspecifications_id_get**](DatasetSpecificationApi.md#datasetspecifications_id_get) | **GET** /datasetspecifications/{id} | Get a DatasetSpecification
[**datasetspecifications_id_put**](DatasetSpecificationApi.md#datasetspecifications_id_put) | **PUT** /datasetspecifications/{id} | Update a DatasetSpecification
[**datasetspecifications_post**](DatasetSpecificationApi.md#datasetspecifications_post) | **POST** /datasetspecifications | Create a DatasetSpecification


# **datasetspecifications_get**
> list[DatasetSpecification] datasetspecifications_get(username=username)

List all DatasetSpecification entities

Gets a list of all DatasetSpecification entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all DatasetSpecification entities
    api_response = api_instance.datasetspecifications_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasetspecifications_id_delete**
> datasetspecifications_id_delete(id, user)

Delete a DatasetSpecification

Delete an existing DatasetSpecification

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
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a DatasetSpecification
    api_instance.datasetspecifications_id_delete(id, user)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_delete: %s\n" % e)
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

# **datasetspecifications_id_get**
> DatasetSpecification datasetspecifications_id_get(id, username=username)

Get a DatasetSpecification

Gets the details of a single instance of a DatasetSpecification

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a DatasetSpecification
    api_response = api_instance.datasetspecifications_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**DatasetSpecification**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasetspecifications_id_put**
> datasetspecifications_id_put(id, user, dataset_specification=dataset_specification)

Update a DatasetSpecification

Updates an existing DatasetSpecification

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
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
dataset_specification = modelcatalog.DatasetSpecification() # DatasetSpecification | An old DatasetSpecificationto be updated (optional)

try:
    # Update a DatasetSpecification
    api_instance.datasetspecifications_id_put(id, user, dataset_specification=dataset_specification)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **dataset_specification** | [**DatasetSpecification**](DatasetSpecification.md)| An old DatasetSpecificationto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasetspecifications_post**
> datasetspecifications_post(user, dataset_specification=dataset_specification)

Create a DatasetSpecification

Create a new instance of a DatasetSpecification

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
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
dataset_specification = modelcatalog.DatasetSpecification() # DatasetSpecification | A new DatasetSpecificationto be created (optional)

try:
    # Create a DatasetSpecification
    api_instance.datasetspecifications_post(user, dataset_specification=dataset_specification)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **dataset_specification** | [**DatasetSpecification**](DatasetSpecification.md)| A new DatasetSpecificationto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


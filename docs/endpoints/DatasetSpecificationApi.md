# modelcatalog.DatasetSpecificationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_configuration_id_inputs_get**](DatasetSpecificationApi.md#custom_configuration_id_inputs_get) | **GET** /custom/configuration/{id}/inputs | Gets all inputs of a configuration
[**custom_datasetspecifications_get**](DatasetSpecificationApi.md#custom_datasetspecifications_get) | **GET** /custom/datasetspecifications | Gets all inputs of a configuration
[**datasetspecifications_get**](DatasetSpecificationApi.md#datasetspecifications_get) | **GET** /datasetspecifications | List all instances of DatasetSpecification
[**datasetspecifications_id_delete**](DatasetSpecificationApi.md#datasetspecifications_id_delete) | **DELETE** /datasetspecifications/{id} | Delete an existing DatasetSpecification
[**datasetspecifications_id_get**](DatasetSpecificationApi.md#datasetspecifications_id_get) | **GET** /datasetspecifications/{id} | Get a single DatasetSpecification by its id
[**datasetspecifications_id_put**](DatasetSpecificationApi.md#datasetspecifications_id_put) | **PUT** /datasetspecifications/{id} | Update an existing DatasetSpecification
[**datasetspecifications_post**](DatasetSpecificationApi.md#datasetspecifications_post) | **POST** /datasetspecifications | Create one DatasetSpecification


# **custom_configuration_id_inputs_get**
> list[DatasetSpecification] custom_configuration_id_inputs_get(id, username=username, custom_query_name=custom_query_name)

Gets all inputs of a configuration

Gets all inputs of a configuration

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)
custom_query_name = 'search_datasetspecification_by_configurationid' # str | Name of the custom query (optional) (default to 'search_datasetspecification_by_configurationid')

try:
    # Gets all inputs of a configuration
    api_response = api_instance.custom_configuration_id_inputs_get(id, username=username, custom_query_name=custom_query_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->custom_configuration_id_inputs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;search_datasetspecification_by_configurationid&#39;]

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets all inputs of a configuration |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_datasetspecifications_get**
> list[DatasetSpecification] custom_datasetspecifications_get(configurationid, username=username, custom_query_name=custom_query_name)

Gets all inputs of a configuration

Gets all inputs of a configuration

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
configurationid = 'configurationid_example' # str | The ID of the configuration
username = 'username_example' # str | Username to query (optional)
custom_query_name = 'custom_allinputs' # str | Name of the custom query (optional) (default to 'custom_allinputs')

try:
    # Gets all inputs of a configuration
    api_response = api_instance.custom_datasetspecifications_get(configurationid, username=username, custom_query_name=custom_query_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->custom_datasetspecifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationid** | **str**| The ID of the configuration | 
 **username** | **str**| Username to query | [optional] 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_allinputs&#39;]

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets all inputs of a configuration |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datasetspecifications_get**
> list[DatasetSpecification] datasetspecifications_get(username=username, label=label, page=page, per_page=per_page)

List all instances of DatasetSpecification

Gets a list of all instances of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of DatasetSpecification
    api_response = api_instance.datasetspecifications_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[DatasetSpecification]**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of DatasetSpecification. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datasetspecifications_id_delete**
> datasetspecifications_id_delete(id, user=user)

Delete an existing DatasetSpecification

Delete an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DatasetSpecification to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing DatasetSpecification
    api_instance.datasetspecifications_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DatasetSpecification to be retrieved | 
 **user** | **str**| Username | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deleted |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datasetspecifications_id_get**
> DatasetSpecification datasetspecifications_id_get(id, username=username)

Get a single DatasetSpecification by its id

Gets the details of a given DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi()
id = 'id_example' # str | The ID of the DatasetSpecification to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single DatasetSpecification by its id
    api_response = api_instance.datasetspecifications_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DatasetSpecification to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**DatasetSpecification**](DatasetSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given DatasetSpecification |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datasetspecifications_id_put**
> DatasetSpecification datasetspecifications_id_put(id, user=user, dataset_specification=dataset_specification)

Update an existing DatasetSpecification

Updates an existing DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DatasetSpecification to be retrieved
user = 'user_example' # str | Username (optional)
dataset_specification = modelcatalog.DatasetSpecification() # DatasetSpecification | An old DatasetSpecificationto be updated (optional)

try:
    # Update an existing DatasetSpecification
    api_response = api_instance.datasetspecifications_id_put(id, user=user, dataset_specification=dataset_specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DatasetSpecification to be retrieved | 
 **user** | **str**| Username | [optional] 
 **dataset_specification** | [**DatasetSpecification**](DatasetSpecification.md)| An old DatasetSpecificationto be updated | [optional] 

### Return type

[**DatasetSpecification**](DatasetSpecification.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datasetspecifications_post**
> DatasetSpecification datasetspecifications_post(user=user, dataset_specification=dataset_specification)

Create one DatasetSpecification

Create a new instance of DatasetSpecification (more information in https://w3id.org/okn/o/sd#DatasetSpecification)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DatasetSpecificationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
dataset_specification = modelcatalog.DatasetSpecification() # DatasetSpecification | Information about the DatasetSpecificationto be created (optional)

try:
    # Create one DatasetSpecification
    api_response = api_instance.datasetspecifications_post(user=user, dataset_specification=dataset_specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetSpecificationApi->datasetspecifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **dataset_specification** | [**DatasetSpecification**](DatasetSpecification.md)| Information about the DatasetSpecificationto be created | [optional] 

### Return type

[**DatasetSpecification**](DatasetSpecification.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


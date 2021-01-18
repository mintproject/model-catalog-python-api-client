# modelcatalog.DataTransformationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_datasetspecifications_id_datatransformations_get**](DataTransformationApi.md#custom_datasetspecifications_id_datatransformations_get) | **GET** /custom/datasetspecifications/{id}/datatransformations | Gets a list of data transformations related a dataset
[**datatransformations_get**](DataTransformationApi.md#datatransformations_get) | **GET** /datatransformations | List all instances of DataTransformation
[**datatransformations_id_delete**](DataTransformationApi.md#datatransformations_id_delete) | **DELETE** /datatransformations/{id} | Delete an existing DataTransformation
[**datatransformations_id_get**](DataTransformationApi.md#datatransformations_id_get) | **GET** /datatransformations/{id} | Get a single DataTransformation by its id
[**datatransformations_id_put**](DataTransformationApi.md#datatransformations_id_put) | **PUT** /datatransformations/{id} | Update an existing DataTransformation
[**datatransformations_post**](DataTransformationApi.md#datatransformations_post) | **POST** /datatransformations | Create one DataTransformation


# **custom_datasetspecifications_id_datatransformations_get**
> list[DataTransformation] custom_datasetspecifications_id_datatransformations_get(id, custom_query_name=custom_query_name, username=username)

Gets a list of data transformations related a dataset

Gets a list of data transformations related a dataset

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi()
id = 'id_example' # str | The ID of the dataspecification
custom_query_name = 'custom_datatransformations' # str | Name of the custom query (optional) (default to 'custom_datatransformations')
username = 'username_example' # str | Username to query (optional)

try:
    # Gets a list of data transformations related a dataset
    api_response = api_instance.custom_datasetspecifications_id_datatransformations_get(id, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationApi->custom_datasetspecifications_id_datatransformations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the dataspecification | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_datatransformations&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[DataTransformation]**](DataTransformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of data transformations filter related a dataset. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datatransformations_get**
> list[DataTransformation] datatransformations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of DataTransformation

Gets a list of all instances of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of DataTransformation
    api_response = api_instance.datatransformations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationApi->datatransformations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[DataTransformation]**](DataTransformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of DataTransformation. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datatransformations_id_delete**
> datatransformations_id_delete(id, user=user)

Delete an existing DataTransformation

Delete an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DataTransformation to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing DataTransformation
    api_instance.datatransformations_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling DataTransformationApi->datatransformations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformation to be retrieved | 
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

# **datatransformations_id_get**
> DataTransformation datatransformations_id_get(id, username=username)

Get a single DataTransformation by its id

Gets the details of a given DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi()
id = 'id_example' # str | The ID of the DataTransformation to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single DataTransformation by its id
    api_response = api_instance.datatransformations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationApi->datatransformations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformation to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**DataTransformation**](DataTransformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given DataTransformation |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datatransformations_id_put**
> DataTransformation datatransformations_id_put(id, user=user, data_transformation=data_transformation)

Update an existing DataTransformation

Updates an existing DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DataTransformation to be retrieved
user = 'user_example' # str | Username (optional)
data_transformation = modelcatalog.DataTransformation() # DataTransformation | An old DataTransformationto be updated (optional)

try:
    # Update an existing DataTransformation
    api_response = api_instance.datatransformations_id_put(id, user=user, data_transformation=data_transformation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationApi->datatransformations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformation to be retrieved | 
 **user** | **str**| Username | [optional] 
 **data_transformation** | [**DataTransformation**](DataTransformation.md)| An old DataTransformationto be updated | [optional] 

### Return type

[**DataTransformation**](DataTransformation.md)

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

# **datatransformations_post**
> DataTransformation datatransformations_post(user=user, data_transformation=data_transformation)

Create one DataTransformation

Create a new instance of DataTransformation (more information in https://w3id.org/okn/o/sd#DataTransformation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
data_transformation = modelcatalog.DataTransformation() # DataTransformation | Information about the DataTransformationto be created (optional)

try:
    # Create one DataTransformation
    api_response = api_instance.datatransformations_post(user=user, data_transformation=data_transformation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationApi->datatransformations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **data_transformation** | [**DataTransformation**](DataTransformation.md)| Information about the DataTransformationto be created | [optional] 

### Return type

[**DataTransformation**](DataTransformation.md)

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


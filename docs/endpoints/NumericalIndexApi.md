# modelcatalog.NumericalIndexApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numericalindexs_get**](NumericalIndexApi.md#numericalindexs_get) | **GET** /numericalindexs | List all instances of NumericalIndex
[**numericalindexs_id_delete**](NumericalIndexApi.md#numericalindexs_id_delete) | **DELETE** /numericalindexs/{id} | Delete an existing NumericalIndex
[**numericalindexs_id_get**](NumericalIndexApi.md#numericalindexs_id_get) | **GET** /numericalindexs/{id} | Get a single NumericalIndex by its id
[**numericalindexs_id_put**](NumericalIndexApi.md#numericalindexs_id_put) | **PUT** /numericalindexs/{id} | Update an existing NumericalIndex
[**numericalindexs_post**](NumericalIndexApi.md#numericalindexs_post) | **POST** /numericalindexs | Create one NumericalIndex


# **numericalindexs_get**
> list[NumericalIndex] numericalindexs_get(username=username, label=label, page=page, per_page=per_page)

List all instances of NumericalIndex

Gets a list of all instances of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.NumericalIndexApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of NumericalIndex
    api_response = api_instance.numericalindexs_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[NumericalIndex]**](NumericalIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of NumericalIndex. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **numericalindexs_id_delete**
> numericalindexs_id_delete(id, user=user)

Delete an existing NumericalIndex

Delete an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the NumericalIndex to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing NumericalIndex
    api_instance.numericalindexs_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the NumericalIndex to be retrieved | 
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

# **numericalindexs_id_get**
> NumericalIndex numericalindexs_id_get(id, username=username)

Get a single NumericalIndex by its id

Gets the details of a given NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.NumericalIndexApi()
id = 'id_example' # str | The ID of the NumericalIndex to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single NumericalIndex by its id
    api_response = api_instance.numericalindexs_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the NumericalIndex to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given NumericalIndex |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **numericalindexs_id_put**
> NumericalIndex numericalindexs_id_put(id, user=user, numerical_index=numerical_index)

Update an existing NumericalIndex

Updates an existing NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the NumericalIndex to be retrieved
user = 'user_example' # str | Username (optional)
numerical_index = modelcatalog.NumericalIndex() # NumericalIndex | An old NumericalIndexto be updated (optional)

try:
    # Update an existing NumericalIndex
    api_response = api_instance.numericalindexs_id_put(id, user=user, numerical_index=numerical_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the NumericalIndex to be retrieved | 
 **user** | **str**| Username | [optional] 
 **numerical_index** | [**NumericalIndex**](NumericalIndex.md)| An old NumericalIndexto be updated | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

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

# **numericalindexs_post**
> NumericalIndex numericalindexs_post(user=user, numerical_index=numerical_index)

Create one NumericalIndex

Create a new instance of NumericalIndex (more information in https://w3id.org/okn/o/sd#NumericalIndex)

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
numerical_index = modelcatalog.NumericalIndex() # NumericalIndex | Information about the NumericalIndexto be created (optional)

try:
    # Create one NumericalIndex
    api_response = api_instance.numericalindexs_post(user=user, numerical_index=numerical_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **numerical_index** | [**NumericalIndex**](NumericalIndex.md)| Information about the NumericalIndexto be created | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

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


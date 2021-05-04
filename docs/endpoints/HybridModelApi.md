# modelcatalog.HybridModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hybridmodels_get**](HybridModelApi.md#hybridmodels_get) | **GET** /hybridmodels | List all instances of HybridModel
[**hybridmodels_id_delete**](HybridModelApi.md#hybridmodels_id_delete) | **DELETE** /hybridmodels/{id} | Delete an existing HybridModel
[**hybridmodels_id_get**](HybridModelApi.md#hybridmodels_id_get) | **GET** /hybridmodels/{id} | Get a single HybridModel by its id
[**hybridmodels_id_put**](HybridModelApi.md#hybridmodels_id_put) | **PUT** /hybridmodels/{id} | Update an existing HybridModel
[**hybridmodels_post**](HybridModelApi.md#hybridmodels_post) | **POST** /hybridmodels | Create one HybridModel


# **hybridmodels_get**
> list[HybridModel] hybridmodels_get(username=username, label=label, page=page, per_page=per_page)

List all instances of HybridModel

Gets a list of all instances of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.HybridModelApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of HybridModel
    api_response = api_instance.hybridmodels_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[HybridModel]**](HybridModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of HybridModel. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **hybridmodels_id_delete**
> hybridmodels_id_delete(id, user=user)

Delete an existing HybridModel

Delete an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the HybridModel to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing HybridModel
    api_instance.hybridmodels_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the HybridModel to be retrieved | 
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

# **hybridmodels_id_get**
> HybridModel hybridmodels_id_get(id, username=username)

Get a single HybridModel by its id

Gets the details of a given HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.HybridModelApi()
id = 'id_example' # str | The ID of the HybridModel to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single HybridModel by its id
    api_response = api_instance.hybridmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the HybridModel to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**HybridModel**](HybridModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given HybridModel |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **hybridmodels_id_put**
> HybridModel hybridmodels_id_put(id, user=user, hybrid_model=hybrid_model)

Update an existing HybridModel

Updates an existing HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the HybridModel to be retrieved
user = 'user_example' # str | Username (optional)
hybrid_model = modelcatalog.HybridModel() # HybridModel | An old HybridModelto be updated (optional)

try:
    # Update an existing HybridModel
    api_response = api_instance.hybridmodels_id_put(id, user=user, hybrid_model=hybrid_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the HybridModel to be retrieved | 
 **user** | **str**| Username | [optional] 
 **hybrid_model** | [**HybridModel**](HybridModel.md)| An old HybridModelto be updated | [optional] 

### Return type

[**HybridModel**](HybridModel.md)

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

# **hybridmodels_post**
> HybridModel hybridmodels_post(user=user, hybrid_model=hybrid_model)

Create one HybridModel

Create a new instance of HybridModel (more information in https://w3id.org/okn/o/sdm#HybridModel)

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
api_instance = modelcatalog.HybridModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
hybrid_model = modelcatalog.HybridModel() # HybridModel | Information about the HybridModelto be created (optional)

try:
    # Create one HybridModel
    api_response = api_instance.hybridmodels_post(user=user, hybrid_model=hybrid_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HybridModelApi->hybridmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **hybrid_model** | [**HybridModel**](HybridModel.md)| Information about the HybridModelto be created | [optional] 

### Return type

[**HybridModel**](HybridModel.md)

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


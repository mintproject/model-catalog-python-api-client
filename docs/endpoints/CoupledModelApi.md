# modelcatalog.CoupledModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coupledmodels_get**](CoupledModelApi.md#coupledmodels_get) | **GET** /coupledmodels | List all instances of CoupledModel
[**coupledmodels_id_delete**](CoupledModelApi.md#coupledmodels_id_delete) | **DELETE** /coupledmodels/{id} | Delete an existing CoupledModel
[**coupledmodels_id_get**](CoupledModelApi.md#coupledmodels_id_get) | **GET** /coupledmodels/{id} | Get a single CoupledModel by its id
[**coupledmodels_id_put**](CoupledModelApi.md#coupledmodels_id_put) | **PUT** /coupledmodels/{id} | Update an existing CoupledModel
[**coupledmodels_post**](CoupledModelApi.md#coupledmodels_post) | **POST** /coupledmodels | Create one CoupledModel


# **coupledmodels_get**
> list[CoupledModel] coupledmodels_get(username=username, label=label, page=page, per_page=per_page)

List all instances of CoupledModel

Gets a list of all instances of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CoupledModelApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of CoupledModel
    api_response = api_instance.coupledmodels_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoupledModelApi->coupledmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[CoupledModel]**](CoupledModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of CoupledModel. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **coupledmodels_id_delete**
> coupledmodels_id_delete(id, user=user)

Delete an existing CoupledModel

Delete an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)

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
api_instance = modelcatalog.CoupledModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CoupledModel to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing CoupledModel
    api_instance.coupledmodels_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling CoupledModelApi->coupledmodels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CoupledModel to be retrieved | 
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

# **coupledmodels_id_get**
> CoupledModel coupledmodels_id_get(id, username=username)

Get a single CoupledModel by its id

Gets the details of a given CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CoupledModelApi()
id = 'id_example' # str | The ID of the CoupledModel to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single CoupledModel by its id
    api_response = api_instance.coupledmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoupledModelApi->coupledmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CoupledModel to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**CoupledModel**](CoupledModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given CoupledModel |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **coupledmodels_id_put**
> CoupledModel coupledmodels_id_put(id, user=user, coupled_model=coupled_model)

Update an existing CoupledModel

Updates an existing CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)

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
api_instance = modelcatalog.CoupledModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CoupledModel to be retrieved
user = 'user_example' # str | Username (optional)
coupled_model = modelcatalog.CoupledModel() # CoupledModel | An old CoupledModelto be updated (optional)

try:
    # Update an existing CoupledModel
    api_response = api_instance.coupledmodels_id_put(id, user=user, coupled_model=coupled_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoupledModelApi->coupledmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CoupledModel to be retrieved | 
 **user** | **str**| Username | [optional] 
 **coupled_model** | [**CoupledModel**](CoupledModel.md)| An old CoupledModelto be updated | [optional] 

### Return type

[**CoupledModel**](CoupledModel.md)

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

# **coupledmodels_post**
> CoupledModel coupledmodels_post(user=user, coupled_model=coupled_model)

Create one CoupledModel

Create a new instance of CoupledModel (more information in https://w3id.org/okn/o/sdm#CoupledModel)

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
api_instance = modelcatalog.CoupledModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
coupled_model = modelcatalog.CoupledModel() # CoupledModel | Information about the CoupledModelto be created (optional)

try:
    # Create one CoupledModel
    api_response = api_instance.coupledmodels_post(user=user, coupled_model=coupled_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoupledModelApi->coupledmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **coupled_model** | [**CoupledModel**](CoupledModel.md)| Information about the CoupledModelto be created | [optional] 

### Return type

[**CoupledModel**](CoupledModel.md)

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


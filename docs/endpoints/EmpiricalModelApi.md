# modelcatalog.EmpiricalModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**empiricalmodels_get**](EmpiricalModelApi.md#empiricalmodels_get) | **GET** /empiricalmodels | List all instances of EmpiricalModel
[**empiricalmodels_id_delete**](EmpiricalModelApi.md#empiricalmodels_id_delete) | **DELETE** /empiricalmodels/{id} | Delete an existing EmpiricalModel
[**empiricalmodels_id_get**](EmpiricalModelApi.md#empiricalmodels_id_get) | **GET** /empiricalmodels/{id} | Get a single EmpiricalModel by its id
[**empiricalmodels_id_put**](EmpiricalModelApi.md#empiricalmodels_id_put) | **PUT** /empiricalmodels/{id} | Update an existing EmpiricalModel
[**empiricalmodels_post**](EmpiricalModelApi.md#empiricalmodels_post) | **POST** /empiricalmodels | Create one EmpiricalModel


# **empiricalmodels_get**
> list[EmpiricalModel] empiricalmodels_get(username=username, label=label, page=page, per_page=per_page)

List all instances of EmpiricalModel

Gets a list of all instances of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EmpiricalModelApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of EmpiricalModel
    api_response = api_instance.empiricalmodels_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[EmpiricalModel]**](EmpiricalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of EmpiricalModel. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **empiricalmodels_id_delete**
> empiricalmodels_id_delete(id, user=user)

Delete an existing EmpiricalModel

Delete an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the EmpiricalModel to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing EmpiricalModel
    api_instance.empiricalmodels_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the EmpiricalModel to be retrieved | 
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

# **empiricalmodels_id_get**
> EmpiricalModel empiricalmodels_id_get(id, username=username)

Get a single EmpiricalModel by its id

Gets the details of a given EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EmpiricalModelApi()
id = 'id_example' # str | The ID of the EmpiricalModel to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single EmpiricalModel by its id
    api_response = api_instance.empiricalmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the EmpiricalModel to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given EmpiricalModel |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **empiricalmodels_id_put**
> EmpiricalModel empiricalmodels_id_put(id, user=user, empirical_model=empirical_model)

Update an existing EmpiricalModel

Updates an existing EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the EmpiricalModel to be retrieved
user = 'user_example' # str | Username (optional)
empirical_model = modelcatalog.EmpiricalModel() # EmpiricalModel | An old EmpiricalModelto be updated (optional)

try:
    # Update an existing EmpiricalModel
    api_response = api_instance.empiricalmodels_id_put(id, user=user, empirical_model=empirical_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the EmpiricalModel to be retrieved | 
 **user** | **str**| Username | [optional] 
 **empirical_model** | [**EmpiricalModel**](EmpiricalModel.md)| An old EmpiricalModelto be updated | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

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

# **empiricalmodels_post**
> EmpiricalModel empiricalmodels_post(user=user, empirical_model=empirical_model)

Create one EmpiricalModel

Create a new instance of EmpiricalModel (more information in https://w3id.org/okn/o/sdm#EmpiricalModel)

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
api_instance = modelcatalog.EmpiricalModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
empirical_model = modelcatalog.EmpiricalModel() # EmpiricalModel | Information about the EmpiricalModelto be created (optional)

try:
    # Create one EmpiricalModel
    api_response = api_instance.empiricalmodels_post(user=user, empirical_model=empirical_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpiricalModelApi->empiricalmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **empirical_model** | [**EmpiricalModel**](EmpiricalModel.md)| Information about the EmpiricalModelto be created | [optional] 

### Return type

[**EmpiricalModel**](EmpiricalModel.md)

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


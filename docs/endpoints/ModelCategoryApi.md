# modelcatalog.ModelCategoryApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelcategorys_get**](ModelCategoryApi.md#modelcategorys_get) | **GET** /modelcategorys | List all instances of ModelCategory
[**modelcategorys_id_delete**](ModelCategoryApi.md#modelcategorys_id_delete) | **DELETE** /modelcategorys/{id} | Delete an existing ModelCategory
[**modelcategorys_id_get**](ModelCategoryApi.md#modelcategorys_id_get) | **GET** /modelcategorys/{id} | Get a single ModelCategory by its id
[**modelcategorys_id_put**](ModelCategoryApi.md#modelcategorys_id_put) | **PUT** /modelcategorys/{id} | Update an existing ModelCategory
[**modelcategorys_post**](ModelCategoryApi.md#modelcategorys_post) | **POST** /modelcategorys | Create one ModelCategory


# **modelcategorys_get**
> list[ModelCategory] modelcategorys_get(username=username, label=label, page=page, per_page=per_page)

List all instances of ModelCategory

Gets a list of all instances of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelCategoryApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of ModelCategory
    api_response = api_instance.modelcategorys_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelCategoryApi->modelcategorys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[ModelCategory]**](ModelCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of ModelCategory. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelcategorys_id_delete**
> modelcategorys_id_delete(id, user)

Delete an existing ModelCategory

Delete an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelCategoryApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelCategory to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing ModelCategory
    api_instance.modelcategorys_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelCategoryApi->modelcategorys_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelCategory to be retrieved | 
 **user** | **str**| Username | 

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

# **modelcategorys_id_get**
> ModelCategory modelcategorys_id_get(id, username=username)

Get a single ModelCategory by its id

Gets the details of a given ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelCategoryApi()
id = 'id_example' # str | The ID of the ModelCategory to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single ModelCategory by its id
    api_response = api_instance.modelcategorys_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelCategoryApi->modelcategorys_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelCategory to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**ModelCategory**](ModelCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given ModelCategory |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **modelcategorys_id_put**
> ModelCategory modelcategorys_id_put(id, user, model_category=model_category)

Update an existing ModelCategory

Updates an existing ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelCategoryApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the ModelCategory to be retrieved
user = 'user_example' # str | Username
model_category = modelcatalog.ModelCategory() # ModelCategory | An old ModelCategoryto be updated (optional)

try:
    # Update an existing ModelCategory
    api_response = api_instance.modelcategorys_id_put(id, user, model_category=model_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelCategoryApi->modelcategorys_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ModelCategory to be retrieved | 
 **user** | **str**| Username | 
 **model_category** | [**ModelCategory**](ModelCategory.md)| An old ModelCategoryto be updated | [optional] 

### Return type

[**ModelCategory**](ModelCategory.md)

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

# **modelcategorys_post**
> ModelCategory modelcategorys_post(user, model_category=model_category)

Create one ModelCategory

Create a new instance of ModelCategory (more information in https://w3id.org/okn/o/sdm#ModelCategory)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.ModelCategoryApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model_category = modelcatalog.ModelCategory() # ModelCategory | Information about the ModelCategoryto be created (optional)

try:
    # Create one ModelCategory
    api_response = api_instance.modelcategorys_post(user, model_category=model_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelCategoryApi->modelcategorys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model_category** | [**ModelCategory**](ModelCategory.md)| Information about the ModelCategoryto be created | [optional] 

### Return type

[**ModelCategory**](ModelCategory.md)

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


# modelcatalog.ModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_model_index_get**](ModelApi.md#custom_model_index_get) | **GET** /custom/model/index | Get a Model
[**custom_model_intervention_get**](ModelApi.md#custom_model_intervention_get) | **GET** /custom/model/intervention | Get a Model
[**custom_model_region_get**](ModelApi.md#custom_model_region_get) | **GET** /custom/model/region | Get a Model
[**custom_models_standard_variable_get**](ModelApi.md#custom_models_standard_variable_get) | **GET** /custom/models/standard_variable | Get a list of models
[**custom_models_variable_get**](ModelApi.md#custom_models_variable_get) | **GET** /custom/models/variable | Get a list of Model
[**models_get**](ModelApi.md#models_get) | **GET** /models | List all instances of Model
[**models_id_delete**](ModelApi.md#models_id_delete) | **DELETE** /models/{id} | Delete an existing Model
[**models_id_get**](ModelApi.md#models_id_get) | **GET** /models/{id} | Get a single Model by its id
[**models_id_put**](ModelApi.md#models_id_put) | **PUT** /models/{id} | Update an existing Model
[**models_post**](ModelApi.md#models_post) | **POST** /models | Create one Model


# **custom_model_index_get**
> list[Model] custom_model_index_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | Label of NumericalIndex
custom_query_name = 'custom_model_index' # str | Name of the custom query (optional) (default to 'custom_model_index')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_index_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Label of NumericalIndex | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_index&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of Model |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_model_intervention_get**
> list[Model] custom_model_intervention_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | Label of intervation
custom_query_name = 'custom_model_intervetion' # str | Name of the custom query (optional) (default to 'custom_model_intervetion')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_intervention_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_intervention_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Label of intervation | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_intervetion&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of Model |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_model_region_get**
> list[Model] custom_model_region_get(label, custom_query_name=custom_query_name, username=username)

Get a Model

Gets the details of a single instance of a Model

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | region to search
custom_query_name = 'custom_model_region' # str | Name of the custom query (optional) (default to 'custom_model_region')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Model
    api_response = api_instance.custom_model_region_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_model_region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| region to search | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_region&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of Model |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_models_standard_variable_get**
> list[Model] custom_models_standard_variable_get(label, custom_query_name=custom_query_name, username=username)

Get a list of models

Gets a list of model filter by the label of a standard variable

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | standard variable name
custom_query_name = 'custom_model_standard_variable' # str | Name of the custom query (optional) (default to 'custom_model_standard_variable')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a list of models
    api_response = api_instance.custom_models_standard_variable_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_models_standard_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| standard variable name | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_model_standard_variable&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of models |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **custom_models_variable_get**
> list[Model] custom_models_variable_get(label, custom_query_name=custom_query_name, username=username)

Get a list of Model

Get models by variable name

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
label = 'label_example' # str | variable to search
custom_query_name = 'custom_models_variable' # str | Name of the custom query (optional) (default to 'custom_models_variable')
username = 'username_example' # str | Username to query (optional)

try:
    # Get a list of Model
    api_response = api_instance.custom_models_variable_get(label, custom_query_name=custom_query_name, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->custom_models_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| variable to search | 
 **custom_query_name** | **str**| Name of the custom query | [optional] [default to &#39;custom_models_variable&#39;]
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets a list of instance of Model |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_get**
> list[Model] models_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Model

Gets a list of all instances of Model (more information in https://w3id.org/okn/o/sdm#Model)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Model
    api_response = api_instance.models_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Model. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_id_delete**
> models_id_delete(id, user)

Delete an existing Model

Delete an existing Model (more information in https://w3id.org/okn/o/sdm#Model)

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Model to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Model
    api_instance.models_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Model to be retrieved | 
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

# **models_id_get**
> Model models_id_get(id, username=username)

Get a single Model by its id

Gets the details of a given Model (more information in https://w3id.org/okn/o/sdm#Model)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ModelApi()
id = 'id_example' # str | The ID of the Model to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Model by its id
    api_response = api_instance.models_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Model to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Model |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **models_id_put**
> Model models_id_put(id, user, model=model)

Update an existing Model

Updates an existing Model (more information in https://w3id.org/okn/o/sdm#Model)

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Model to be retrieved
user = 'user_example' # str | Username
model = modelcatalog.Model() # Model | An old Modelto be updated (optional)

try:
    # Update an existing Model
    api_response = api_instance.models_id_put(id, user, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Model to be retrieved | 
 **user** | **str**| Username | 
 **model** | [**Model**](Model.md)| An old Modelto be updated | [optional] 

### Return type

[**Model**](Model.md)

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

# **models_post**
> Model models_post(user, model=model)

Create one Model

Create a new instance of Model (more information in https://w3id.org/okn/o/sdm#Model)

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
api_instance = modelcatalog.ModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
model = modelcatalog.Model() # Model | Information about the Modelto be created (optional)

try:
    # Create one Model
    api_response = api_instance.models_post(user, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->models_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **model** | [**Model**](Model.md)| Information about the Modelto be created | [optional] 

### Return type

[**Model**](Model.md)

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


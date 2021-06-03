# modelcatalog.SampleExecutionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sampleexecutions_get**](SampleExecutionApi.md#sampleexecutions_get) | **GET** /sampleexecutions | List all instances of SampleExecution
[**sampleexecutions_id_delete**](SampleExecutionApi.md#sampleexecutions_id_delete) | **DELETE** /sampleexecutions/{id} | Delete an existing SampleExecution
[**sampleexecutions_id_get**](SampleExecutionApi.md#sampleexecutions_id_get) | **GET** /sampleexecutions/{id} | Get a single SampleExecution by its id
[**sampleexecutions_id_put**](SampleExecutionApi.md#sampleexecutions_id_put) | **PUT** /sampleexecutions/{id} | Update an existing SampleExecution
[**sampleexecutions_post**](SampleExecutionApi.md#sampleexecutions_post) | **POST** /sampleexecutions | Create one SampleExecution


# **sampleexecutions_get**
> list[SampleExecution] sampleexecutions_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SampleExecution

Gets a list of all instances of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleExecutionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SampleExecution
    api_response = api_instance.sampleexecutions_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SampleExecution]**](SampleExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SampleExecution. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_id_delete**
> sampleexecutions_id_delete(id, user=user)

Delete an existing SampleExecution

Delete an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleExecution to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing SampleExecution
    api_instance.sampleexecutions_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleExecution to be retrieved | 
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

# **sampleexecutions_id_get**
> SampleExecution sampleexecutions_id_get(id, username=username)

Get a single SampleExecution by its id

Gets the details of a given SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleExecutionApi()
id = 'id_example' # str | The ID of the SampleExecution to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SampleExecution by its id
    api_response = api_instance.sampleexecutions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleExecution to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SampleExecution |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_id_put**
> SampleExecution sampleexecutions_id_put(id, user=user, sample_execution=sample_execution)

Update an existing SampleExecution

Updates an existing SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleExecution to be retrieved
user = 'user_example' # str | Username (optional)
sample_execution = modelcatalog.SampleExecution() # SampleExecution | An old SampleExecutionto be updated (optional)

try:
    # Update an existing SampleExecution
    api_response = api_instance.sampleexecutions_id_put(id, user=user, sample_execution=sample_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleExecution to be retrieved | 
 **user** | **str**| Username | [optional] 
 **sample_execution** | [**SampleExecution**](SampleExecution.md)| An old SampleExecutionto be updated | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

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

# **sampleexecutions_post**
> SampleExecution sampleexecutions_post(user=user, sample_execution=sample_execution)

Create one SampleExecution

Create a new instance of SampleExecution (more information in https://w3id.org/okn/o/sd#SampleExecution)

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
sample_execution = modelcatalog.SampleExecution() # SampleExecution | Information about the SampleExecutionto be created (optional)

try:
    # Create one SampleExecution
    api_response = api_instance.sampleexecutions_post(user=user, sample_execution=sample_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **sample_execution** | [**SampleExecution**](SampleExecution.md)| Information about the SampleExecutionto be created | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

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


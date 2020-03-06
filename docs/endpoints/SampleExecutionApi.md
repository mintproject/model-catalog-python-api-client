# modelcatalog.SampleExecutionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sampleexecutions_get**](SampleExecutionApi.md#sampleexecutions_get) | **GET** /sampleexecutions | List all SampleExecution entities
[**sampleexecutions_id_delete**](SampleExecutionApi.md#sampleexecutions_id_delete) | **DELETE** /sampleexecutions/{id} | Delete a SampleExecution
[**sampleexecutions_id_get**](SampleExecutionApi.md#sampleexecutions_id_get) | **GET** /sampleexecutions/{id} | Get a SampleExecution
[**sampleexecutions_id_put**](SampleExecutionApi.md#sampleexecutions_id_put) | **PUT** /sampleexecutions/{id} | Update a SampleExecution
[**sampleexecutions_post**](SampleExecutionApi.md#sampleexecutions_post) | **POST** /sampleexecutions | Create a SampleExecution


# **sampleexecutions_get**
> list[SampleExecution] sampleexecutions_get(username=username, label=label)

List all SampleExecution entities

Gets a list of all SampleExecution entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleExecutionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SampleExecution entities
    api_response = api_instance.sampleexecutions_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SampleExecution]**](SampleExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_id_delete**
> sampleexecutions_id_delete(id, user)

Delete a SampleExecution

Delete an existing SampleExecution

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SampleExecution
    api_instance.sampleexecutions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_id_get**
> SampleExecution sampleexecutions_id_get(id, username=username)

Get a SampleExecution

Gets the details of a single instance of a SampleExecution

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleExecutionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SampleExecution
    api_response = api_instance.sampleexecutions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_id_put**
> SampleExecution sampleexecutions_id_put(id, user, sample_execution=sample_execution)

Update a SampleExecution

Updates an existing SampleExecution

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
sample_execution = modelcatalog.SampleExecution() # SampleExecution | An old SampleExecutionto be updated (optional)

try:
    # Update a SampleExecution
    api_response = api_instance.sampleexecutions_id_put(id, user, sample_execution=sample_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **sample_execution** | [**SampleExecution**](SampleExecution.md)| An old SampleExecutionto be updated | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleexecutions_post**
> SampleExecution sampleexecutions_post(user, sample_execution=sample_execution)

Create a SampleExecution

Create a new instance of a SampleExecution

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
api_instance = modelcatalog.SampleExecutionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
sample_execution = modelcatalog.SampleExecution() # SampleExecution | A new SampleExecutionto be created (optional)

try:
    # Create a SampleExecution
    api_response = api_instance.sampleexecutions_post(user, sample_execution=sample_execution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleExecutionApi->sampleexecutions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **sample_execution** | [**SampleExecution**](SampleExecution.md)| A new SampleExecutionto be created | [optional] 

### Return type

[**SampleExecution**](SampleExecution.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


# modelcatalog.ProcessApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processs_get**](ProcessApi.md#processs_get) | **GET** /processs | List all instances of Process
[**processs_id_delete**](ProcessApi.md#processs_id_delete) | **DELETE** /processs/{id} | Delete an existing Process
[**processs_id_get**](ProcessApi.md#processs_id_get) | **GET** /processs/{id} | Get a single Process by its id
[**processs_id_put**](ProcessApi.md#processs_id_put) | **PUT** /processs/{id} | Update an existing Process
[**processs_post**](ProcessApi.md#processs_post) | **POST** /processs | Create one Process


# **processs_get**
> list[Process] processs_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Process

Gets a list of all instances of Process (more information in https://w3id.org/okn/o/sdm#Process)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ProcessApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Process
    api_response = api_instance.processs_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Process. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **processs_id_delete**
> processs_id_delete(id, user)

Delete an existing Process

Delete an existing Process (more information in https://w3id.org/okn/o/sdm#Process)

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
api_instance = modelcatalog.ProcessApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Process to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Process
    api_instance.processs_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Process to be retrieved | 
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

# **processs_id_get**
> Process processs_id_get(id, username=username)

Get a single Process by its id

Gets the details of a given Process (more information in https://w3id.org/okn/o/sdm#Process)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ProcessApi()
id = 'id_example' # str | The ID of the Process to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Process by its id
    api_response = api_instance.processs_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Process to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Process**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Process |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **processs_id_put**
> Process processs_id_put(id, user, process=process)

Update an existing Process

Updates an existing Process (more information in https://w3id.org/okn/o/sdm#Process)

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
api_instance = modelcatalog.ProcessApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Process to be retrieved
user = 'user_example' # str | Username
process = modelcatalog.Process() # Process | An old Processto be updated (optional)

try:
    # Update an existing Process
    api_response = api_instance.processs_id_put(id, user, process=process)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Process to be retrieved | 
 **user** | **str**| Username | 
 **process** | [**Process**](Process.md)| An old Processto be updated | [optional] 

### Return type

[**Process**](Process.md)

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

# **processs_post**
> Process processs_post(user, process=process)

Create one Process

Create a new instance of Process (more information in https://w3id.org/okn/o/sdm#Process)

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
api_instance = modelcatalog.ProcessApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
process = modelcatalog.Process() # Process | Information about the Processto be created (optional)

try:
    # Create one Process
    api_response = api_instance.processs_post(user, process=process)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **process** | [**Process**](Process.md)| Information about the Processto be created | [optional] 

### Return type

[**Process**](Process.md)

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


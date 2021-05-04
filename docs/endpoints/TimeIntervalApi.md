# modelcatalog.TimeIntervalApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeintervals_get**](TimeIntervalApi.md#timeintervals_get) | **GET** /timeintervals | List all instances of TimeInterval
[**timeintervals_id_delete**](TimeIntervalApi.md#timeintervals_id_delete) | **DELETE** /timeintervals/{id} | Delete an existing TimeInterval
[**timeintervals_id_get**](TimeIntervalApi.md#timeintervals_id_get) | **GET** /timeintervals/{id} | Get a single TimeInterval by its id
[**timeintervals_id_put**](TimeIntervalApi.md#timeintervals_id_put) | **PUT** /timeintervals/{id} | Update an existing TimeInterval
[**timeintervals_post**](TimeIntervalApi.md#timeintervals_post) | **POST** /timeintervals | Create one TimeInterval


# **timeintervals_get**
> list[TimeInterval] timeintervals_get(username=username, label=label, page=page, per_page=per_page)

List all instances of TimeInterval

Gets a list of all instances of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of TimeInterval
    api_response = api_instance.timeintervals_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[TimeInterval]**](TimeInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of TimeInterval. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **timeintervals_id_delete**
> timeintervals_id_delete(id, user=user)

Delete an existing TimeInterval

Delete an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)

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
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the TimeInterval to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing TimeInterval
    api_instance.timeintervals_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the TimeInterval to be retrieved | 
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

# **timeintervals_id_get**
> TimeInterval timeintervals_id_get(id, username=username)

Get a single TimeInterval by its id

Gets the details of a given TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi()
id = 'id_example' # str | The ID of the TimeInterval to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single TimeInterval by its id
    api_response = api_instance.timeintervals_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the TimeInterval to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**TimeInterval**](TimeInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given TimeInterval |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **timeintervals_id_put**
> TimeInterval timeintervals_id_put(id, user=user, time_interval=time_interval)

Update an existing TimeInterval

Updates an existing TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)

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
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the TimeInterval to be retrieved
user = 'user_example' # str | Username (optional)
time_interval = modelcatalog.TimeInterval() # TimeInterval | An old TimeIntervalto be updated (optional)

try:
    # Update an existing TimeInterval
    api_response = api_instance.timeintervals_id_put(id, user=user, time_interval=time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the TimeInterval to be retrieved | 
 **user** | **str**| Username | [optional] 
 **time_interval** | [**TimeInterval**](TimeInterval.md)| An old TimeIntervalto be updated | [optional] 

### Return type

[**TimeInterval**](TimeInterval.md)

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

# **timeintervals_post**
> TimeInterval timeintervals_post(user=user, time_interval=time_interval)

Create one TimeInterval

Create a new instance of TimeInterval (more information in https://w3id.org/okn/o/sdm#TimeInterval)

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
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
time_interval = modelcatalog.TimeInterval() # TimeInterval | Information about the TimeIntervalto be created (optional)

try:
    # Create one TimeInterval
    api_response = api_instance.timeintervals_post(user=user, time_interval=time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **time_interval** | [**TimeInterval**](TimeInterval.md)| Information about the TimeIntervalto be created | [optional] 

### Return type

[**TimeInterval**](TimeInterval.md)

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


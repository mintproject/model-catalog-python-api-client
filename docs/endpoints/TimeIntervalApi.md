# modelcatalog.TimeIntervalApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeintervals_get**](TimeIntervalApi.md#timeintervals_get) | **GET** /timeintervals | List all TimeInterval entities
[**timeintervals_id_delete**](TimeIntervalApi.md#timeintervals_id_delete) | **DELETE** /timeintervals/{id} | Delete a TimeInterval
[**timeintervals_id_get**](TimeIntervalApi.md#timeintervals_id_get) | **GET** /timeintervals/{id} | Get a TimeInterval
[**timeintervals_id_put**](TimeIntervalApi.md#timeintervals_id_put) | **PUT** /timeintervals/{id} | Update a TimeInterval
[**timeintervals_post**](TimeIntervalApi.md#timeintervals_post) | **POST** /timeintervals | Create a TimeInterval


# **timeintervals_get**
> list[TimeInterval] timeintervals_get(username=username, label=label)

List all TimeInterval entities

Gets a list of all TimeInterval entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all TimeInterval entities
    api_response = api_instance.timeintervals_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

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
**200** | Successful response - returns an array of TimeInterval entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **timeintervals_id_delete**
> timeintervals_id_delete(id, user)

Delete a TimeInterval

Delete an existing TimeInterval

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a TimeInterval
    api_instance.timeintervals_id_delete(id, user)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_delete: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deleted |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **timeintervals_id_get**
> TimeInterval timeintervals_id_get(id, username=username)

Get a TimeInterval

Gets the details of a single instance of a TimeInterval

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a TimeInterval
    api_response = api_instance.timeintervals_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

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
**200** | Gets the details of a single instance of  TimeInterval |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **timeintervals_id_put**
> TimeInterval timeintervals_id_put(id, user, time_interval=time_interval)

Update a TimeInterval

Updates an existing TimeInterval

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
time_interval = modelcatalog.TimeInterval() # TimeInterval | An old TimeIntervalto be updated (optional)

try:
    # Update a TimeInterval
    api_response = api_instance.timeintervals_id_put(id, user, time_interval=time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
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
> TimeInterval timeintervals_post(user, time_interval=time_interval)

Create a TimeInterval

Create a new instance of a TimeInterval

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.TimeIntervalApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
time_interval = modelcatalog.TimeInterval() # TimeInterval | A new TimeIntervalto be created (optional)

try:
    # Create a TimeInterval
    api_response = api_instance.timeintervals_post(user, time_interval=time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **time_interval** | [**TimeInterval**](TimeInterval.md)| A new TimeIntervalto be created | [optional] 

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


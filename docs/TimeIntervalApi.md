# mint_client.TimeIntervalApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeintervals_get**](TimeIntervalApi.md#timeintervals_get) | **GET** /timeintervals | List all TimeInterval entities
[**timeintervals_id_delete**](TimeIntervalApi.md#timeintervals_id_delete) | **DELETE** /timeintervals/{id} | Delete a TimeInterval
[**timeintervals_id_get**](TimeIntervalApi.md#timeintervals_id_get) | **GET** /timeintervals/{id} | Get a TimeInterval
[**timeintervals_id_put**](TimeIntervalApi.md#timeintervals_id_put) | **PUT** /timeintervals/{id} | Update a TimeInterval
[**timeintervals_post**](TimeIntervalApi.md#timeintervals_post) | **POST** /timeintervals | Create a TimeInterval


# **timeintervals_get**
> list[TimeInterval] timeintervals_get(username=username)

List all TimeInterval entities

Gets a list of all TimeInterval entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.TimeIntervalApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all TimeInterval entities
    api_response = api_instance.timeintervals_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[TimeInterval]**](TimeInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeintervals_id_delete**
> timeintervals_id_delete(id, user)

Delete a TimeInterval

Delete an existing TimeInterval

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.TimeIntervalApi(mint_client.ApiClient(configuration))
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeintervals_id_get**
> TimeInterval timeintervals_id_get(id, username=username)

Get a TimeInterval

Gets the details of a single instance of a TimeInterval

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.TimeIntervalApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeintervals_id_put**
> timeintervals_id_put(id, user, time_interval=time_interval)

Update a TimeInterval

Updates an existing TimeInterval

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.TimeIntervalApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
time_interval = mint_client.TimeInterval() # TimeInterval | An old TimeIntervalto be updated (optional)

try:
    # Update a TimeInterval
    api_instance.timeintervals_id_put(id, user, time_interval=time_interval)
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

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeintervals_post**
> timeintervals_post(user, time_interval=time_interval)

Create a TimeInterval

Create a new instance of a TimeInterval

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint
configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.TimeIntervalApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
time_interval = mint_client.TimeInterval() # TimeInterval | A new TimeIntervalto be created (optional)

try:
    # Create a TimeInterval
    api_instance.timeintervals_post(user, time_interval=time_interval)
except ApiException as e:
    print("Exception when calling TimeIntervalApi->timeintervals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **time_interval** | [**TimeInterval**](TimeInterval.md)| A new TimeIntervalto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

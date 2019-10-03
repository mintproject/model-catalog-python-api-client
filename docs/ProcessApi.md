# mint_client.ProcessApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processs_get**](ProcessApi.md#processs_get) | **GET** /processs | List all Process entities
[**processs_id_delete**](ProcessApi.md#processs_id_delete) | **DELETE** /processs/{id} | Delete a Process
[**processs_id_get**](ProcessApi.md#processs_id_get) | **GET** /processs/{id} | Get a Process
[**processs_id_put**](ProcessApi.md#processs_id_put) | **PUT** /processs/{id} | Update a Process
[**processs_post**](ProcessApi.md#processs_post) | **POST** /processs | Create a Process


# **processs_get**
> list[Process] processs_get(username=username)

List all Process entities

Gets a list of all Process entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ProcessApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Process entities
    api_response = api_instance.processs_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Process]**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processs_id_delete**
> processs_id_delete(id, user)

Delete a Process

Delete an existing Process

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
api_instance = mint_client.ProcessApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Process
    api_instance.processs_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_delete: %s\n" % e)
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

# **processs_id_get**
> Process processs_id_get(id, username=username)

Get a Process

Gets the details of a single instance of a Process

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.ProcessApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Process
    api_response = api_instance.processs_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Process**](Process.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processs_id_put**
> processs_id_put(id, user, process=process)

Update a Process

Updates an existing Process

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
api_instance = mint_client.ProcessApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
process = mint_client.Process() # Process | An old Processto be updated (optional)

try:
    # Update a Process
    api_instance.processs_id_put(id, user, process=process)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **process** | [**Process**](Process.md)| An old Processto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processs_post**
> processs_post(user, process=process)

Create a Process

Create a new instance of a Process

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
api_instance = mint_client.ProcessApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
process = mint_client.Process() # Process | A new Processto be created (optional)

try:
    # Create a Process
    api_instance.processs_post(user, process=process)
except ApiException as e:
    print("Exception when calling ProcessApi->processs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **process** | [**Process**](Process.md)| A new Processto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


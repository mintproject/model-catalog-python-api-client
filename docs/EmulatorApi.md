# mint_client.EmulatorApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emulators_get**](EmulatorApi.md#emulators_get) | **GET** /emulators | List all Emulator entities
[**emulators_id_delete**](EmulatorApi.md#emulators_id_delete) | **DELETE** /emulators/{id} | Delete a Emulator
[**emulators_id_get**](EmulatorApi.md#emulators_id_get) | **GET** /emulators/{id} | Get a Emulator
[**emulators_id_put**](EmulatorApi.md#emulators_id_put) | **PUT** /emulators/{id} | Update a Emulator
[**emulators_post**](EmulatorApi.md#emulators_post) | **POST** /emulators | Create a Emulator


# **emulators_get**
> list[Emulator] emulators_get(username=username)

List all Emulator entities

Gets a list of all Emulator entities

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.EmulatorApi()
username = 'username_example' # str | Username to query (optional)

try:
    # List all Emulator entities
    api_response = api_instance.emulators_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 

### Return type

[**list[Emulator]**](Emulator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulators_id_delete**
> emulators_id_delete(id, user)

Delete a Emulator

Delete an existing Emulator

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
api_instance = mint_client.EmulatorApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Emulator
    api_instance.emulators_id_delete(id, user)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_delete: %s\n" % e)
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

# **emulators_id_get**
> Emulator emulators_id_get(id, username=username)

Get a Emulator

Gets the details of a single instance of a Emulator

### Example

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mint_client.EmulatorApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Emulator
    api_response = api_instance.emulators_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Emulator**](Emulator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulators_id_put**
> emulators_id_put(id, user, emulator=emulator)

Update a Emulator

Updates an existing Emulator

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
api_instance = mint_client.EmulatorApi(mint_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
emulator = mint_client.Emulator() # Emulator | An old Emulatorto be updated (optional)

try:
    # Update a Emulator
    api_instance.emulators_id_put(id, user, emulator=emulator)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **emulator** | [**Emulator**](Emulator.md)| An old Emulatorto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emulators_post**
> emulators_post(user, emulator=emulator)

Create a Emulator

Create a new instance of a Emulator

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
api_instance = mint_client.EmulatorApi(mint_client.ApiClient(configuration))
user = 'user_example' # str | Username
emulator = mint_client.Emulator() # Emulator | A new Emulatorto be created (optional)

try:
    # Create a Emulator
    api_instance.emulators_post(user, emulator=emulator)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **emulator** | [**Emulator**](Emulator.md)| A new Emulatorto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


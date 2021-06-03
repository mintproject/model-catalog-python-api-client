# modelcatalog.EmulatorApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emulators_get**](EmulatorApi.md#emulators_get) | **GET** /emulators | List all instances of Emulator
[**emulators_id_delete**](EmulatorApi.md#emulators_id_delete) | **DELETE** /emulators/{id} | Delete an existing Emulator
[**emulators_id_get**](EmulatorApi.md#emulators_id_get) | **GET** /emulators/{id} | Get a single Emulator by its id
[**emulators_id_put**](EmulatorApi.md#emulators_id_put) | **PUT** /emulators/{id} | Update an existing Emulator
[**emulators_post**](EmulatorApi.md#emulators_post) | **POST** /emulators | Create one Emulator


# **emulators_get**
> list[Emulator] emulators_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Emulator

Gets a list of all instances of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EmulatorApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Emulator
    api_response = api_instance.emulators_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Emulator]**](Emulator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Emulator. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **emulators_id_delete**
> emulators_id_delete(id, user=user)

Delete an existing Emulator

Delete an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)

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
api_instance = modelcatalog.EmulatorApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Emulator to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Emulator
    api_instance.emulators_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Emulator to be retrieved | 
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

# **emulators_id_get**
> Emulator emulators_id_get(id, username=username)

Get a single Emulator by its id

Gets the details of a given Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EmulatorApi()
id = 'id_example' # str | The ID of the Emulator to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Emulator by its id
    api_response = api_instance.emulators_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Emulator to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Emulator**](Emulator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Emulator |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **emulators_id_put**
> Emulator emulators_id_put(id, user=user, emulator=emulator)

Update an existing Emulator

Updates an existing Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)

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
api_instance = modelcatalog.EmulatorApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Emulator to be retrieved
user = 'user_example' # str | Username (optional)
emulator = modelcatalog.Emulator() # Emulator | An old Emulatorto be updated (optional)

try:
    # Update an existing Emulator
    api_response = api_instance.emulators_id_put(id, user=user, emulator=emulator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Emulator to be retrieved | 
 **user** | **str**| Username | [optional] 
 **emulator** | [**Emulator**](Emulator.md)| An old Emulatorto be updated | [optional] 

### Return type

[**Emulator**](Emulator.md)

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

# **emulators_post**
> Emulator emulators_post(user=user, emulator=emulator)

Create one Emulator

Create a new instance of Emulator (more information in https://w3id.org/okn/o/sdm#Emulator)

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
api_instance = modelcatalog.EmulatorApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
emulator = modelcatalog.Emulator() # Emulator | Information about the Emulatorto be created (optional)

try:
    # Create one Emulator
    api_response = api_instance.emulators_post(user=user, emulator=emulator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmulatorApi->emulators_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **emulator** | [**Emulator**](Emulator.md)| Information about the Emulatorto be created | [optional] 

### Return type

[**Emulator**](Emulator.md)

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


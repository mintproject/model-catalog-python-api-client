# modelcatalog.FarmingPracticesApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farmingpracticess_get**](FarmingPracticesApi.md#farmingpracticess_get) | **GET** /farmingpracticess | List all FarmingPractices entities
[**farmingpracticess_id_delete**](FarmingPracticesApi.md#farmingpracticess_id_delete) | **DELETE** /farmingpracticess/{id} | Delete a FarmingPractices
[**farmingpracticess_id_get**](FarmingPracticesApi.md#farmingpracticess_id_get) | **GET** /farmingpracticess/{id} | Get a FarmingPractices
[**farmingpracticess_id_put**](FarmingPracticesApi.md#farmingpracticess_id_put) | **PUT** /farmingpracticess/{id} | Update a FarmingPractices
[**farmingpracticess_post**](FarmingPracticesApi.md#farmingpracticess_post) | **POST** /farmingpracticess | Create a FarmingPractices


# **farmingpracticess_get**
> list[FarmingPractices] farmingpracticess_get(username=username, label=label)

List all FarmingPractices entities

Gets a list of all FarmingPractices entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.FarmingPracticesApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all FarmingPractices entities
    api_response = api_instance.farmingpracticess_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmingPracticesApi->farmingpracticess_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[FarmingPractices]**](FarmingPractices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of FarmingPractices entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **farmingpracticess_id_delete**
> farmingpracticess_id_delete(id, user)

Delete a FarmingPractices

Delete an existing FarmingPractices

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
api_instance = modelcatalog.FarmingPracticesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a FarmingPractices
    api_instance.farmingpracticess_id_delete(id, user)
except ApiException as e:
    print("Exception when calling FarmingPracticesApi->farmingpracticess_id_delete: %s\n" % e)
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

# **farmingpracticess_id_get**
> FarmingPractices farmingpracticess_id_get(id, username=username)

Get a FarmingPractices

Gets the details of a single instance of a FarmingPractices

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.FarmingPracticesApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a FarmingPractices
    api_response = api_instance.farmingpracticess_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmingPracticesApi->farmingpracticess_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**FarmingPractices**](FarmingPractices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a single instance of  FarmingPractices |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **farmingpracticess_id_put**
> FarmingPractices farmingpracticess_id_put(id, user, farming_practices=farming_practices)

Update a FarmingPractices

Updates an existing FarmingPractices

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
api_instance = modelcatalog.FarmingPracticesApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
farming_practices = modelcatalog.FarmingPractices() # FarmingPractices | An old FarmingPracticesto be updated (optional)

try:
    # Update a FarmingPractices
    api_response = api_instance.farmingpracticess_id_put(id, user, farming_practices=farming_practices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmingPracticesApi->farmingpracticess_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **farming_practices** | [**FarmingPractices**](FarmingPractices.md)| An old FarmingPracticesto be updated | [optional] 

### Return type

[**FarmingPractices**](FarmingPractices.md)

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

# **farmingpracticess_post**
> FarmingPractices farmingpracticess_post(user, farming_practices=farming_practices)

Create a FarmingPractices

Create a new instance of a FarmingPractices

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
api_instance = modelcatalog.FarmingPracticesApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
farming_practices = modelcatalog.FarmingPractices() # FarmingPractices | A new FarmingPracticesto be created (optional)

try:
    # Create a FarmingPractices
    api_response = api_instance.farmingpracticess_post(user, farming_practices=farming_practices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmingPracticesApi->farmingpracticess_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **farming_practices** | [**FarmingPractices**](FarmingPractices.md)| A new FarmingPracticesto be created | [optional] 

### Return type

[**FarmingPractices**](FarmingPractices.md)

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


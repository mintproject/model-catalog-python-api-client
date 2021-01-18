# modelcatalog.UnitApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_get**](UnitApi.md#units_get) | **GET** /units | List all instances of Unit
[**units_id_delete**](UnitApi.md#units_id_delete) | **DELETE** /units/{id} | Delete an existing Unit
[**units_id_get**](UnitApi.md#units_id_get) | **GET** /units/{id} | Get a single Unit by its id
[**units_id_put**](UnitApi.md#units_id_put) | **PUT** /units/{id} | Update an existing Unit
[**units_post**](UnitApi.md#units_post) | **POST** /units | Create one Unit


# **units_get**
> list[Unit] units_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Unit

Gets a list of all instances of Unit (more information in https://w3id.org/okn/o/sd#Unit)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.UnitApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Unit
    api_response = api_instance.units_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Unit]**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Unit. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **units_id_delete**
> units_id_delete(id, user=user)

Delete an existing Unit

Delete an existing Unit (more information in https://w3id.org/okn/o/sd#Unit)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.UnitApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Unit to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Unit
    api_instance.units_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Unit to be retrieved | 
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

# **units_id_get**
> Unit units_id_get(id, username=username)

Get a single Unit by its id

Gets the details of a given Unit (more information in https://w3id.org/okn/o/sd#Unit)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.UnitApi()
id = 'id_example' # str | The ID of the Unit to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Unit by its id
    api_response = api_instance.units_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Unit to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Unit |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **units_id_put**
> Unit units_id_put(id, user=user, unit=unit)

Update an existing Unit

Updates an existing Unit (more information in https://w3id.org/okn/o/sd#Unit)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.UnitApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Unit to be retrieved
user = 'user_example' # str | Username (optional)
unit = modelcatalog.Unit() # Unit | An old Unitto be updated (optional)

try:
    # Update an existing Unit
    api_response = api_instance.units_id_put(id, user=user, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Unit to be retrieved | 
 **user** | **str**| Username | [optional] 
 **unit** | [**Unit**](Unit.md)| An old Unitto be updated | [optional] 

### Return type

[**Unit**](Unit.md)

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

# **units_post**
> Unit units_post(user=user, unit=unit)

Create one Unit

Create a new instance of Unit (more information in https://w3id.org/okn/o/sd#Unit)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.UnitApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
unit = modelcatalog.Unit() # Unit | Information about the Unitto be created (optional)

try:
    # Create one Unit
    api_response = api_instance.units_post(user=user, unit=unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **unit** | [**Unit**](Unit.md)| Information about the Unitto be created | [optional] 

### Return type

[**Unit**](Unit.md)

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


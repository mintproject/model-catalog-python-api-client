# modelcatalog.SoftwareApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwares_get**](SoftwareApi.md#softwares_get) | **GET** /softwares | List all instances of Software
[**softwares_id_delete**](SoftwareApi.md#softwares_id_delete) | **DELETE** /softwares/{id} | Delete an existing Software
[**softwares_id_get**](SoftwareApi.md#softwares_id_get) | **GET** /softwares/{id} | Get a single Software by its id
[**softwares_id_put**](SoftwareApi.md#softwares_id_put) | **PUT** /softwares/{id} | Update an existing Software
[**softwares_post**](SoftwareApi.md#softwares_post) | **POST** /softwares | Create one Software


# **softwares_get**
> list[Software] softwares_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Software

Gets a list of all instances of Software (more information in https://w3id.org/okn/o/sd#Software)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Software
    api_response = api_instance.softwares_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Software]**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Software. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwares_id_delete**
> softwares_id_delete(id, user=user)

Delete an existing Software

Delete an existing Software (more information in https://w3id.org/okn/o/sd#Software)

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
api_instance = modelcatalog.SoftwareApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Software to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Software
    api_instance.softwares_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Software to be retrieved | 
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

# **softwares_id_get**
> Software softwares_id_get(id, username=username)

Get a single Software by its id

Gets the details of a given Software (more information in https://w3id.org/okn/o/sd#Software)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareApi()
id = 'id_example' # str | The ID of the Software to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Software by its id
    api_response = api_instance.softwares_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Software to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Software**](Software.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Software |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwares_id_put**
> Software softwares_id_put(id, user=user, software=software)

Update an existing Software

Updates an existing Software (more information in https://w3id.org/okn/o/sd#Software)

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
api_instance = modelcatalog.SoftwareApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Software to be retrieved
user = 'user_example' # str | Username (optional)
software = modelcatalog.Software() # Software | An old Softwareto be updated (optional)

try:
    # Update an existing Software
    api_response = api_instance.softwares_id_put(id, user=user, software=software)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Software to be retrieved | 
 **user** | **str**| Username | [optional] 
 **software** | [**Software**](Software.md)| An old Softwareto be updated | [optional] 

### Return type

[**Software**](Software.md)

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

# **softwares_post**
> Software softwares_post(user=user, software=software)

Create one Software

Create a new instance of Software (more information in https://w3id.org/okn/o/sd#Software)

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
api_instance = modelcatalog.SoftwareApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
software = modelcatalog.Software() # Software | Information about the Softwareto be created (optional)

try:
    # Create one Software
    api_response = api_instance.softwares_post(user=user, software=software)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareApi->softwares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **software** | [**Software**](Software.md)| Information about the Softwareto be created | [optional] 

### Return type

[**Software**](Software.md)

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


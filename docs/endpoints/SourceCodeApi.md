# modelcatalog.SourceCodeApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sourcecodes_get**](SourceCodeApi.md#sourcecodes_get) | **GET** /sourcecodes | List all instances of SourceCode
[**sourcecodes_id_delete**](SourceCodeApi.md#sourcecodes_id_delete) | **DELETE** /sourcecodes/{id} | Delete an existing SourceCode
[**sourcecodes_id_get**](SourceCodeApi.md#sourcecodes_id_get) | **GET** /sourcecodes/{id} | Get a single SourceCode by its id
[**sourcecodes_id_put**](SourceCodeApi.md#sourcecodes_id_put) | **PUT** /sourcecodes/{id} | Update an existing SourceCode
[**sourcecodes_post**](SourceCodeApi.md#sourcecodes_post) | **POST** /sourcecodes | Create one SourceCode


# **sourcecodes_get**
> list[SourceCode] sourcecodes_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SourceCode

Gets a list of all instances of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SourceCodeApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SourceCode
    api_response = api_instance.sourcecodes_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SourceCode]**](SourceCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SourceCode. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sourcecodes_id_delete**
> sourcecodes_id_delete(id, user)

Delete an existing SourceCode

Delete an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SourceCode to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SourceCode
    api_instance.sourcecodes_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SourceCode to be retrieved | 
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

# **sourcecodes_id_get**
> SourceCode sourcecodes_id_get(id, username=username)

Get a single SourceCode by its id

Gets the details of a given SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SourceCodeApi()
id = 'id_example' # str | The ID of the SourceCode to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SourceCode by its id
    api_response = api_instance.sourcecodes_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SourceCode to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SourceCode |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sourcecodes_id_put**
> SourceCode sourcecodes_id_put(id, user, source_code=source_code)

Update an existing SourceCode

Updates an existing SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SourceCode to be retrieved
user = 'user_example' # str | Username
source_code = modelcatalog.SourceCode() # SourceCode | An old SourceCodeto be updated (optional)

try:
    # Update an existing SourceCode
    api_response = api_instance.sourcecodes_id_put(id, user, source_code=source_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SourceCode to be retrieved | 
 **user** | **str**| Username | 
 **source_code** | [**SourceCode**](SourceCode.md)| An old SourceCodeto be updated | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

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

# **sourcecodes_post**
> SourceCode sourcecodes_post(user, source_code=source_code)

Create one SourceCode

Create a new instance of SourceCode (more information in https://w3id.org/okn/o/sd#SourceCode)

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
source_code = modelcatalog.SourceCode() # SourceCode | Information about the SourceCodeto be created (optional)

try:
    # Create one SourceCode
    api_response = api_instance.sourcecodes_post(user, source_code=source_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **source_code** | [**SourceCode**](SourceCode.md)| Information about the SourceCodeto be created | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

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


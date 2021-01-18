# modelcatalog.CausalDiagramApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**causaldiagrams_get**](CausalDiagramApi.md#causaldiagrams_get) | **GET** /causaldiagrams | List all instances of CausalDiagram
[**causaldiagrams_id_delete**](CausalDiagramApi.md#causaldiagrams_id_delete) | **DELETE** /causaldiagrams/{id} | Delete an existing CausalDiagram
[**causaldiagrams_id_get**](CausalDiagramApi.md#causaldiagrams_id_get) | **GET** /causaldiagrams/{id} | Get a single CausalDiagram by its id
[**causaldiagrams_id_put**](CausalDiagramApi.md#causaldiagrams_id_put) | **PUT** /causaldiagrams/{id} | Update an existing CausalDiagram
[**causaldiagrams_post**](CausalDiagramApi.md#causaldiagrams_post) | **POST** /causaldiagrams | Create one CausalDiagram


# **causaldiagrams_get**
> list[CausalDiagram] causaldiagrams_get(username=username, label=label, page=page, per_page=per_page)

List all instances of CausalDiagram

Gets a list of all instances of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CausalDiagramApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of CausalDiagram
    api_response = api_instance.causaldiagrams_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[CausalDiagram]**](CausalDiagram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of CausalDiagram. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **causaldiagrams_id_delete**
> causaldiagrams_id_delete(id, user=user)

Delete an existing CausalDiagram

Delete an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CausalDiagram to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing CausalDiagram
    api_instance.causaldiagrams_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CausalDiagram to be retrieved | 
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

# **causaldiagrams_id_get**
> CausalDiagram causaldiagrams_id_get(id, username=username)

Get a single CausalDiagram by its id

Gets the details of a given CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CausalDiagramApi()
id = 'id_example' # str | The ID of the CausalDiagram to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single CausalDiagram by its id
    api_response = api_instance.causaldiagrams_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CausalDiagram to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**CausalDiagram**](CausalDiagram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given CausalDiagram |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **causaldiagrams_id_put**
> CausalDiagram causaldiagrams_id_put(id, user=user, causal_diagram=causal_diagram)

Update an existing CausalDiagram

Updates an existing CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CausalDiagram to be retrieved
user = 'user_example' # str | Username (optional)
causal_diagram = modelcatalog.CausalDiagram() # CausalDiagram | An old CausalDiagramto be updated (optional)

try:
    # Update an existing CausalDiagram
    api_response = api_instance.causaldiagrams_id_put(id, user=user, causal_diagram=causal_diagram)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CausalDiagram to be retrieved | 
 **user** | **str**| Username | [optional] 
 **causal_diagram** | [**CausalDiagram**](CausalDiagram.md)| An old CausalDiagramto be updated | [optional] 

### Return type

[**CausalDiagram**](CausalDiagram.md)

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

# **causaldiagrams_post**
> CausalDiagram causaldiagrams_post(user=user, causal_diagram=causal_diagram)

Create one CausalDiagram

Create a new instance of CausalDiagram (more information in https://w3id.org/okn/o/sdm#CausalDiagram)

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
causal_diagram = modelcatalog.CausalDiagram() # CausalDiagram | Information about the CausalDiagramto be created (optional)

try:
    # Create one CausalDiagram
    api_response = api_instance.causaldiagrams_post(user=user, causal_diagram=causal_diagram)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **causal_diagram** | [**CausalDiagram**](CausalDiagram.md)| Information about the CausalDiagramto be created | [optional] 

### Return type

[**CausalDiagram**](CausalDiagram.md)

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


# modelcatalog.SampleResourceApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sampleresources_get**](SampleResourceApi.md#sampleresources_get) | **GET** /sampleresources | List all instances of SampleResource
[**sampleresources_id_delete**](SampleResourceApi.md#sampleresources_id_delete) | **DELETE** /sampleresources/{id} | Delete an existing SampleResource
[**sampleresources_id_get**](SampleResourceApi.md#sampleresources_id_get) | **GET** /sampleresources/{id} | Get a single SampleResource by its id
[**sampleresources_id_put**](SampleResourceApi.md#sampleresources_id_put) | **PUT** /sampleresources/{id} | Update an existing SampleResource
[**sampleresources_post**](SampleResourceApi.md#sampleresources_post) | **POST** /sampleresources | Create one SampleResource


# **sampleresources_get**
> list[SampleResource] sampleresources_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SampleResource

Gets a list of all instances of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleResourceApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SampleResource
    api_response = api_instance.sampleresources_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SampleResource]**](SampleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SampleResource. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_id_delete**
> sampleresources_id_delete(id, user=user)

Delete an existing SampleResource

Delete an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleResource to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing SampleResource
    api_instance.sampleresources_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleResource to be retrieved | 
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

# **sampleresources_id_get**
> SampleResource sampleresources_id_get(id, username=username)

Get a single SampleResource by its id

Gets the details of a given SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleResourceApi()
id = 'id_example' # str | The ID of the SampleResource to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SampleResource by its id
    api_response = api_instance.sampleresources_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleResource to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SampleResource |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_id_put**
> SampleResource sampleresources_id_put(id, user=user, sample_resource=sample_resource)

Update an existing SampleResource

Updates an existing SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleResource to be retrieved
user = 'user_example' # str | Username (optional)
sample_resource = modelcatalog.SampleResource() # SampleResource | An old SampleResourceto be updated (optional)

try:
    # Update an existing SampleResource
    api_response = api_instance.sampleresources_id_put(id, user=user, sample_resource=sample_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleResource to be retrieved | 
 **user** | **str**| Username | [optional] 
 **sample_resource** | [**SampleResource**](SampleResource.md)| An old SampleResourceto be updated | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

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

# **sampleresources_post**
> SampleResource sampleresources_post(user=user, sample_resource=sample_resource)

Create one SampleResource

Create a new instance of SampleResource (more information in https://w3id.org/okn/o/sd#SampleResource)

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
sample_resource = modelcatalog.SampleResource() # SampleResource | Information about the SampleResourceto be created (optional)

try:
    # Create one SampleResource
    api_response = api_instance.sampleresources_post(user=user, sample_resource=sample_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **sample_resource** | [**SampleResource**](SampleResource.md)| Information about the SampleResourceto be created | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

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


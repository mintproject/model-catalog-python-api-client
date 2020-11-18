# modelcatalog.SampleCollectionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samplecollections_get**](SampleCollectionApi.md#samplecollections_get) | **GET** /samplecollections | List all instances of SampleCollection
[**samplecollections_id_delete**](SampleCollectionApi.md#samplecollections_id_delete) | **DELETE** /samplecollections/{id} | Delete an existing SampleCollection
[**samplecollections_id_get**](SampleCollectionApi.md#samplecollections_id_get) | **GET** /samplecollections/{id} | Get a single SampleCollection by its id
[**samplecollections_id_put**](SampleCollectionApi.md#samplecollections_id_put) | **PUT** /samplecollections/{id} | Update an existing SampleCollection
[**samplecollections_post**](SampleCollectionApi.md#samplecollections_post) | **POST** /samplecollections | Create one SampleCollection


# **samplecollections_get**
> list[SampleCollection] samplecollections_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SampleCollection

Gets a list of all instances of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleCollectionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SampleCollection
    api_response = api_instance.samplecollections_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SampleCollection]**](SampleCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SampleCollection. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **samplecollections_id_delete**
> samplecollections_id_delete(id, user)

Delete an existing SampleCollection

Delete an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleCollection to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SampleCollection
    api_instance.samplecollections_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleCollection to be retrieved | 
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

# **samplecollections_id_get**
> SampleCollection samplecollections_id_get(id, username=username)

Get a single SampleCollection by its id

Gets the details of a given SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SampleCollectionApi()
id = 'id_example' # str | The ID of the SampleCollection to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SampleCollection by its id
    api_response = api_instance.samplecollections_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleCollection to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SampleCollection |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **samplecollections_id_put**
> SampleCollection samplecollections_id_put(id, user, sample_collection=sample_collection)

Update an existing SampleCollection

Updates an existing SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SampleCollection to be retrieved
user = 'user_example' # str | Username
sample_collection = modelcatalog.SampleCollection() # SampleCollection | An old SampleCollectionto be updated (optional)

try:
    # Update an existing SampleCollection
    api_response = api_instance.samplecollections_id_put(id, user, sample_collection=sample_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SampleCollection to be retrieved | 
 **user** | **str**| Username | 
 **sample_collection** | [**SampleCollection**](SampleCollection.md)| An old SampleCollectionto be updated | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

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

# **samplecollections_post**
> SampleCollection samplecollections_post(user, sample_collection=sample_collection)

Create one SampleCollection

Create a new instance of SampleCollection (more information in https://w3id.org/okn/o/sd#SampleCollection)

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
sample_collection = modelcatalog.SampleCollection() # SampleCollection | Information about the SampleCollectionto be created (optional)

try:
    # Create one SampleCollection
    api_response = api_instance.samplecollections_post(user, sample_collection=sample_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **sample_collection** | [**SampleCollection**](SampleCollection.md)| Information about the SampleCollectionto be created | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

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


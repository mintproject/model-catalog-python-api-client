# modelcatalog.SpatialResolutionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spatialresolutions_get**](SpatialResolutionApi.md#spatialresolutions_get) | **GET** /spatialresolutions | List all instances of SpatialResolution
[**spatialresolutions_id_delete**](SpatialResolutionApi.md#spatialresolutions_id_delete) | **DELETE** /spatialresolutions/{id} | Delete an existing SpatialResolution
[**spatialresolutions_id_get**](SpatialResolutionApi.md#spatialresolutions_id_get) | **GET** /spatialresolutions/{id} | Get a single SpatialResolution by its id
[**spatialresolutions_id_put**](SpatialResolutionApi.md#spatialresolutions_id_put) | **PUT** /spatialresolutions/{id} | Update an existing SpatialResolution
[**spatialresolutions_post**](SpatialResolutionApi.md#spatialresolutions_post) | **POST** /spatialresolutions | Create one SpatialResolution


# **spatialresolutions_get**
> list[SpatialResolution] spatialresolutions_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SpatialResolution

Gets a list of all instances of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SpatialResolution
    api_response = api_instance.spatialresolutions_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SpatialResolution]**](SpatialResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SpatialResolution. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatialresolutions_id_delete**
> spatialresolutions_id_delete(id, user)

Delete an existing SpatialResolution

Delete an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SpatialResolution to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SpatialResolution
    api_instance.spatialresolutions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatialResolution to be retrieved | 
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

# **spatialresolutions_id_get**
> SpatialResolution spatialresolutions_id_get(id, username=username)

Get a single SpatialResolution by its id

Gets the details of a given SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi()
id = 'id_example' # str | The ID of the SpatialResolution to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SpatialResolution by its id
    api_response = api_instance.spatialresolutions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatialResolution to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SpatialResolution |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **spatialresolutions_id_put**
> SpatialResolution spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)

Update an existing SpatialResolution

Updates an existing SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SpatialResolution to be retrieved
user = 'user_example' # str | Username
spatial_resolution = modelcatalog.SpatialResolution() # SpatialResolution | An old SpatialResolutionto be updated (optional)

try:
    # Update an existing SpatialResolution
    api_response = api_instance.spatialresolutions_id_put(id, user, spatial_resolution=spatial_resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SpatialResolution to be retrieved | 
 **user** | **str**| Username | 
 **spatial_resolution** | [**SpatialResolution**](SpatialResolution.md)| An old SpatialResolutionto be updated | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

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

# **spatialresolutions_post**
> SpatialResolution spatialresolutions_post(user, spatial_resolution=spatial_resolution)

Create one SpatialResolution

Create a new instance of SpatialResolution (more information in https://w3id.org/okn/o/sdm#SpatialResolution)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.SpatialResolutionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
spatial_resolution = modelcatalog.SpatialResolution() # SpatialResolution | Information about the SpatialResolutionto be created (optional)

try:
    # Create one SpatialResolution
    api_response = api_instance.spatialresolutions_post(user, spatial_resolution=spatial_resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialResolutionApi->spatialresolutions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **spatial_resolution** | [**SpatialResolution**](SpatialResolution.md)| Information about the SpatialResolutionto be created | [optional] 

### Return type

[**SpatialResolution**](SpatialResolution.md)

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


# modelcatalog.RegionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regions_get**](RegionApi.md#regions_get) | **GET** /regions | List all instances of Region
[**regions_id_delete**](RegionApi.md#regions_id_delete) | **DELETE** /regions/{id} | Delete an existing Region
[**regions_id_get**](RegionApi.md#regions_id_get) | **GET** /regions/{id} | Get a single Region by its id
[**regions_id_put**](RegionApi.md#regions_id_put) | **PUT** /regions/{id} | Update an existing Region
[**regions_post**](RegionApi.md#regions_post) | **POST** /regions | Create one Region


# **regions_get**
> list[Region] regions_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Region

Gets a list of all instances of Region (more information in https://w3id.org/okn/o/sdm#Region)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.RegionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Region
    api_response = api_instance.regions_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Region. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_id_delete**
> regions_id_delete(id, user)

Delete an existing Region

Delete an existing Region (more information in https://w3id.org/okn/o/sdm#Region)

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
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Region to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Region
    api_instance.regions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Region to be retrieved | 
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

# **regions_id_get**
> Region regions_id_get(id, username=username)

Get a single Region by its id

Gets the details of a given Region (more information in https://w3id.org/okn/o/sdm#Region)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.RegionApi()
id = 'id_example' # str | The ID of the Region to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Region by its id
    api_response = api_instance.regions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Region to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Region |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **regions_id_put**
> Region regions_id_put(id, user, region=region)

Update an existing Region

Updates an existing Region (more information in https://w3id.org/okn/o/sdm#Region)

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
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Region to be retrieved
user = 'user_example' # str | Username
region = modelcatalog.Region() # Region | An old Regionto be updated (optional)

try:
    # Update an existing Region
    api_response = api_instance.regions_id_put(id, user, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Region to be retrieved | 
 **user** | **str**| Username | 
 **region** | [**Region**](Region.md)| An old Regionto be updated | [optional] 

### Return type

[**Region**](Region.md)

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

# **regions_post**
> Region regions_post(user, region=region)

Create one Region

Create a new instance of Region (more information in https://w3id.org/okn/o/sdm#Region)

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
api_instance = modelcatalog.RegionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
region = modelcatalog.Region() # Region | Information about the Regionto be created (optional)

try:
    # Create one Region
    api_response = api_instance.regions_post(user, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->regions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **region** | [**Region**](Region.md)| Information about the Regionto be created | [optional] 

### Return type

[**Region**](Region.md)

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


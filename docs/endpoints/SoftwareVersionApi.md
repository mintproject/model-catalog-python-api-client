# modelcatalog.SoftwareVersionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareversions_get**](SoftwareVersionApi.md#softwareversions_get) | **GET** /softwareversions | List all instances of SoftwareVersion
[**softwareversions_id_delete**](SoftwareVersionApi.md#softwareversions_id_delete) | **DELETE** /softwareversions/{id} | Delete an existing SoftwareVersion
[**softwareversions_id_get**](SoftwareVersionApi.md#softwareversions_id_get) | **GET** /softwareversions/{id} | Get a single SoftwareVersion by its id
[**softwareversions_id_put**](SoftwareVersionApi.md#softwareversions_id_put) | **PUT** /softwareversions/{id} | Update an existing SoftwareVersion
[**softwareversions_post**](SoftwareVersionApi.md#softwareversions_post) | **POST** /softwareversions | Create one SoftwareVersion


# **softwareversions_get**
> list[SoftwareVersion] softwareversions_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SoftwareVersion

Gets a list of all instances of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareVersionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SoftwareVersion
    api_response = api_instance.softwareversions_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SoftwareVersion]**](SoftwareVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SoftwareVersion. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareversions_id_delete**
> softwareversions_id_delete(id, user=user)

Delete an existing SoftwareVersion

Delete an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareVersion to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing SoftwareVersion
    api_instance.softwareversions_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareVersion to be retrieved | 
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

# **softwareversions_id_get**
> SoftwareVersion softwareversions_id_get(id, username=username)

Get a single SoftwareVersion by its id

Gets the details of a given SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareVersionApi()
id = 'id_example' # str | The ID of the SoftwareVersion to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SoftwareVersion by its id
    api_response = api_instance.softwareversions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareVersion to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SoftwareVersion |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareversions_id_put**
> SoftwareVersion softwareversions_id_put(id, user=user, software_version=software_version)

Update an existing SoftwareVersion

Updates an existing SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareVersion to be retrieved
user = 'user_example' # str | Username (optional)
software_version = modelcatalog.SoftwareVersion() # SoftwareVersion | An old SoftwareVersionto be updated (optional)

try:
    # Update an existing SoftwareVersion
    api_response = api_instance.softwareversions_id_put(id, user=user, software_version=software_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareVersion to be retrieved | 
 **user** | **str**| Username | [optional] 
 **software_version** | [**SoftwareVersion**](SoftwareVersion.md)| An old SoftwareVersionto be updated | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

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

# **softwareversions_post**
> SoftwareVersion softwareversions_post(user=user, software_version=software_version)

Create one SoftwareVersion

Create a new instance of SoftwareVersion (more information in https://w3id.org/okn/o/sd#SoftwareVersion)

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
software_version = modelcatalog.SoftwareVersion() # SoftwareVersion | Information about the SoftwareVersionto be created (optional)

try:
    # Create one SoftwareVersion
    api_response = api_instance.softwareversions_post(user=user, software_version=software_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **software_version** | [**SoftwareVersion**](SoftwareVersion.md)| Information about the SoftwareVersionto be created | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

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


# modelcatalog.SoftwareImageApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareimages_get**](SoftwareImageApi.md#softwareimages_get) | **GET** /softwareimages | List all instances of SoftwareImage
[**softwareimages_id_delete**](SoftwareImageApi.md#softwareimages_id_delete) | **DELETE** /softwareimages/{id} | Delete an existing SoftwareImage
[**softwareimages_id_get**](SoftwareImageApi.md#softwareimages_id_get) | **GET** /softwareimages/{id} | Get a single SoftwareImage by its id
[**softwareimages_id_put**](SoftwareImageApi.md#softwareimages_id_put) | **PUT** /softwareimages/{id} | Update an existing SoftwareImage
[**softwareimages_post**](SoftwareImageApi.md#softwareimages_post) | **POST** /softwareimages | Create one SoftwareImage


# **softwareimages_get**
> list[SoftwareImage] softwareimages_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SoftwareImage

Gets a list of all instances of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SoftwareImage
    api_response = api_instance.softwareimages_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SoftwareImage]**](SoftwareImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SoftwareImage. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareimages_id_delete**
> softwareimages_id_delete(id, user)

Delete an existing SoftwareImage

Delete an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)

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
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareImage to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SoftwareImage
    api_instance.softwareimages_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareImage to be retrieved | 
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

# **softwareimages_id_get**
> SoftwareImage softwareimages_id_get(id, username=username)

Get a single SoftwareImage by its id

Gets the details of a given SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi()
id = 'id_example' # str | The ID of the SoftwareImage to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SoftwareImage by its id
    api_response = api_instance.softwareimages_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareImage to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SoftwareImage |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareimages_id_put**
> SoftwareImage softwareimages_id_put(id, user, software_image=software_image)

Update an existing SoftwareImage

Updates an existing SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)

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
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareImage to be retrieved
user = 'user_example' # str | Username
software_image = modelcatalog.SoftwareImage() # SoftwareImage | An old SoftwareImageto be updated (optional)

try:
    # Update an existing SoftwareImage
    api_response = api_instance.softwareimages_id_put(id, user, software_image=software_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareImage to be retrieved | 
 **user** | **str**| Username | 
 **software_image** | [**SoftwareImage**](SoftwareImage.md)| An old SoftwareImageto be updated | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

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

# **softwareimages_post**
> SoftwareImage softwareimages_post(user, software_image=software_image)

Create one SoftwareImage

Create a new instance of SoftwareImage (more information in https://w3id.org/okn/o/sd#SoftwareImage)

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
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
software_image = modelcatalog.SoftwareImage() # SoftwareImage | Information about the SoftwareImageto be created (optional)

try:
    # Create one SoftwareImage
    api_response = api_instance.softwareimages_post(user, software_image=software_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software_image** | [**SoftwareImage**](SoftwareImage.md)| Information about the SoftwareImageto be created | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

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


# modelcatalog.ImageApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_get**](ImageApi.md#images_get) | **GET** /images | List all instances of Image
[**images_id_delete**](ImageApi.md#images_id_delete) | **DELETE** /images/{id} | Delete an existing Image
[**images_id_get**](ImageApi.md#images_id_get) | **GET** /images/{id} | Get a single Image by its id
[**images_id_put**](ImageApi.md#images_id_put) | **PUT** /images/{id} | Update an existing Image
[**images_post**](ImageApi.md#images_post) | **POST** /images | Create one Image


# **images_get**
> list[Image] images_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Image

Gets a list of all instances of Image (more information in https://w3id.org/okn/o/sd#Image)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ImageApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Image
    api_response = api_instance.images_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Image. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **images_id_delete**
> images_id_delete(id, user=user)

Delete an existing Image

Delete an existing Image (more information in https://w3id.org/okn/o/sd#Image)

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
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Image to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Image
    api_instance.images_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Image to be retrieved | 
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

# **images_id_get**
> Image images_id_get(id, username=username)

Get a single Image by its id

Gets the details of a given Image (more information in https://w3id.org/okn/o/sd#Image)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ImageApi()
id = 'id_example' # str | The ID of the Image to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Image by its id
    api_response = api_instance.images_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Image to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Image |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **images_id_put**
> Image images_id_put(id, user=user, image=image)

Update an existing Image

Updates an existing Image (more information in https://w3id.org/okn/o/sd#Image)

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
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Image to be retrieved
user = 'user_example' # str | Username (optional)
image = modelcatalog.Image() # Image | An old Imageto be updated (optional)

try:
    # Update an existing Image
    api_response = api_instance.images_id_put(id, user=user, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Image to be retrieved | 
 **user** | **str**| Username | [optional] 
 **image** | [**Image**](Image.md)| An old Imageto be updated | [optional] 

### Return type

[**Image**](Image.md)

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

# **images_post**
> Image images_post(user=user, image=image)

Create one Image

Create a new instance of Image (more information in https://w3id.org/okn/o/sd#Image)

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
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
image = modelcatalog.Image() # Image | Information about the Imageto be created (optional)

try:
    # Create one Image
    api_response = api_instance.images_post(user=user, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **image** | [**Image**](Image.md)| Information about the Imageto be created | [optional] 

### Return type

[**Image**](Image.md)

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


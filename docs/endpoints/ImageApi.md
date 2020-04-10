# modelcatalog.ImageApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_get**](ImageApi.md#images_get) | **GET** /images | List all Image entities
[**images_id_delete**](ImageApi.md#images_id_delete) | **DELETE** /images/{id} | Delete a Image
[**images_id_get**](ImageApi.md#images_id_get) | **GET** /images/{id} | Get a Image
[**images_id_put**](ImageApi.md#images_id_put) | **PUT** /images/{id} | Update a Image
[**images_post**](ImageApi.md#images_post) | **POST** /images | Create a Image


# **images_get**
> list[Image] images_get(username=username, label=label)

List all Image entities

Gets a list of all Image entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ImageApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Image entities
    api_response = api_instance.images_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

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
**200** | Successful response - returns an array of Image entities. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **images_id_delete**
> images_id_delete(id, user)

Delete a Image

Delete an existing Image

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Image
    api_instance.images_id_delete(id, user)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
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

# **images_id_get**
> Image images_id_get(id, username=username)

Get a Image

Gets the details of a single instance of a Image

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ImageApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Image
    api_response = api_instance.images_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

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
**200** | Gets the details of a single instance of  Image |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **images_id_put**
> Image images_id_put(id, user, image=image)

Update a Image

Updates an existing Image

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
image = modelcatalog.Image() # Image | An old Imageto be updated (optional)

try:
    # Update a Image
    api_response = api_instance.images_id_put(id, user, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
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
> Image images_post(user, image=image)

Create a Image

Create a new instance of a Image

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.4.0
configuration.host = "https://api.models.mint.isi.edu/v1.4.0"
# Create an instance of the API class
api_instance = modelcatalog.ImageApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
image = modelcatalog.Image() # Image | A new Imageto be created (optional)

try:
    # Create a Image
    api_response = api_instance.images_post(user, image=image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **image** | [**Image**](Image.md)| A new Imageto be created | [optional] 

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


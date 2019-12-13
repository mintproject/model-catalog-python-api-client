# modelcatalog.SoftwareImageApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareimages_get**](SoftwareImageApi.md#softwareimages_get) | **GET** /softwareimages | List all SoftwareImage entities
[**softwareimages_id_delete**](SoftwareImageApi.md#softwareimages_id_delete) | **DELETE** /softwareimages/{id} | Delete a SoftwareImage
[**softwareimages_id_get**](SoftwareImageApi.md#softwareimages_id_get) | **GET** /softwareimages/{id} | Get a SoftwareImage
[**softwareimages_id_put**](SoftwareImageApi.md#softwareimages_id_put) | **PUT** /softwareimages/{id} | Update a SoftwareImage
[**softwareimages_post**](SoftwareImageApi.md#softwareimages_post) | **POST** /softwareimages | Create a SoftwareImage


# **softwareimages_get**
> list[SoftwareImage] softwareimages_get(username=username, label=label)

List all SoftwareImage entities

Gets a list of all SoftwareImage entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SoftwareImage entities
    api_response = api_instance.softwareimages_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SoftwareImage]**](SoftwareImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareimages_id_delete**
> softwareimages_id_delete(id, user)

Delete a SoftwareImage

Delete an existing SoftwareImage

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

# create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SoftwareImage
    api_instance.softwareimages_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareimages_id_get**
> SoftwareImage softwareimages_id_get(id, username=username)

Get a SoftwareImage

Gets the details of a single instance of a SoftwareImage

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SoftwareImage
    api_response = api_instance.softwareimages_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareimages_id_put**
> SoftwareImage softwareimages_id_put(id, user, software_image=software_image)

Update a SoftwareImage

Updates an existing SoftwareImage

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

# create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
software_image = modelcatalog.SoftwareImage() # SoftwareImage | An old SoftwareImageto be updated (optional)

try:
    # Update a SoftwareImage
    api_response = api_instance.softwareimages_id_put(id, user, software_image=software_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **software_image** | [**SoftwareImage**](SoftwareImage.md)| An old SoftwareImageto be updated | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareimages_post**
> SoftwareImage softwareimages_post(user, software_image=software_image)

Create a SoftwareImage

Create a new instance of a SoftwareImage

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

# create an instance of the API class
api_instance = modelcatalog.SoftwareImageApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
software_image = modelcatalog.SoftwareImage() # SoftwareImage | A new SoftwareImageto be created (optional)

try:
    # Create a SoftwareImage
    api_response = api_instance.softwareimages_post(user, software_image=software_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software_image** | [**SoftwareImage**](SoftwareImage.md)| A new SoftwareImageto be created | [optional] 

### Return type

[**SoftwareImage**](SoftwareImage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


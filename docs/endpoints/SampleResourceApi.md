# modelcatalog.SampleResourceApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sampleresources_get**](SampleResourceApi.md#sampleresources_get) | **GET** /sampleresources | List all SampleResource entities
[**sampleresources_id_delete**](SampleResourceApi.md#sampleresources_id_delete) | **DELETE** /sampleresources/{id} | Delete a SampleResource
[**sampleresources_id_get**](SampleResourceApi.md#sampleresources_id_get) | **GET** /sampleresources/{id} | Get a SampleResource
[**sampleresources_id_put**](SampleResourceApi.md#sampleresources_id_put) | **PUT** /sampleresources/{id} | Update a SampleResource
[**sampleresources_post**](SampleResourceApi.md#sampleresources_post) | **POST** /sampleresources | Create a SampleResource


# **sampleresources_get**
> list[SampleResource] sampleresources_get(username=username, label=label)

List all SampleResource entities

Gets a list of all SampleResource entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleResourceApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SampleResource entities
    api_response = api_instance.sampleresources_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SampleResource]**](SampleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_id_delete**
> sampleresources_id_delete(id, user)

Delete a SampleResource

Delete an existing SampleResource

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SampleResource
    api_instance.sampleresources_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_id_get**
> SampleResource sampleresources_id_get(id, username=username)

Get a SampleResource

Gets the details of a single instance of a SampleResource

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleResourceApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SampleResource
    api_response = api_instance.sampleresources_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_id_put**
> SampleResource sampleresources_id_put(id, user, sample_resource=sample_resource)

Update a SampleResource

Updates an existing SampleResource

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
sample_resource = modelcatalog.SampleResource() # SampleResource | An old SampleResourceto be updated (optional)

try:
    # Update a SampleResource
    api_response = api_instance.sampleresources_id_put(id, user, sample_resource=sample_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **sample_resource** | [**SampleResource**](SampleResource.md)| An old SampleResourceto be updated | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **sampleresources_post**
> SampleResource sampleresources_post(user, sample_resource=sample_resource)

Create a SampleResource

Create a new instance of a SampleResource

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
api_instance = modelcatalog.SampleResourceApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
sample_resource = modelcatalog.SampleResource() # SampleResource | A new SampleResourceto be created (optional)

try:
    # Create a SampleResource
    api_response = api_instance.sampleresources_post(user, sample_resource=sample_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleResourceApi->sampleresources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **sample_resource** | [**SampleResource**](SampleResource.md)| A new SampleResourceto be created | [optional] 

### Return type

[**SampleResource**](SampleResource.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


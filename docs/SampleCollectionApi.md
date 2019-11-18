# modelcatalog.SampleCollectionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**samplecollections_get**](SampleCollectionApi.md#samplecollections_get) | **GET** /samplecollections | List all SampleCollection entities
[**samplecollections_id_delete**](SampleCollectionApi.md#samplecollections_id_delete) | **DELETE** /samplecollections/{id} | Delete a SampleCollection
[**samplecollections_id_get**](SampleCollectionApi.md#samplecollections_id_get) | **GET** /samplecollections/{id} | Get a SampleCollection
[**samplecollections_id_put**](SampleCollectionApi.md#samplecollections_id_put) | **PUT** /samplecollections/{id} | Update a SampleCollection
[**samplecollections_post**](SampleCollectionApi.md#samplecollections_post) | **POST** /samplecollections | Create a SampleCollection


# **samplecollections_get**
> list[SampleCollection] samplecollections_get(username=username, label=label)

List all SampleCollection entities

Gets a list of all SampleCollection entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleCollectionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SampleCollection entities
    api_response = api_instance.samplecollections_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SampleCollection]**](SampleCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplecollections_id_delete**
> samplecollections_id_delete(id, user)

Delete a SampleCollection

Delete an existing SampleCollection

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SampleCollection
    api_instance.samplecollections_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_delete: %s\n" % e)
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

# **samplecollections_id_get**
> SampleCollection samplecollections_id_get(id, username=username)

Get a SampleCollection

Gets the details of a single instance of a SampleCollection

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SampleCollectionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SampleCollection
    api_response = api_instance.samplecollections_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplecollections_id_put**
> SampleCollection samplecollections_id_put(id, user, sample_collection=sample_collection)

Update a SampleCollection

Updates an existing SampleCollection

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
sample_collection = modelcatalog.SampleCollection() # SampleCollection | An old SampleCollectionto be updated (optional)

try:
    # Update a SampleCollection
    api_response = api_instance.samplecollections_id_put(id, user, sample_collection=sample_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **sample_collection** | [**SampleCollection**](SampleCollection.md)| An old SampleCollectionto be updated | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **samplecollections_post**
> SampleCollection samplecollections_post(user, sample_collection=sample_collection)

Create a SampleCollection

Create a new instance of a SampleCollection

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
api_instance = modelcatalog.SampleCollectionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
sample_collection = modelcatalog.SampleCollection() # SampleCollection | A new SampleCollectionto be created (optional)

try:
    # Create a SampleCollection
    api_response = api_instance.samplecollections_post(user, sample_collection=sample_collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleCollectionApi->samplecollections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **sample_collection** | [**SampleCollection**](SampleCollection.md)| A new SampleCollectionto be created | [optional] 

### Return type

[**SampleCollection**](SampleCollection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


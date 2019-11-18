# modelcatalog.NumericalIndexApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**numericalindexs_get**](NumericalIndexApi.md#numericalindexs_get) | **GET** /numericalindexs | List all NumericalIndex entities
[**numericalindexs_id_delete**](NumericalIndexApi.md#numericalindexs_id_delete) | **DELETE** /numericalindexs/{id} | Delete a NumericalIndex
[**numericalindexs_id_get**](NumericalIndexApi.md#numericalindexs_id_get) | **GET** /numericalindexs/{id} | Get a NumericalIndex
[**numericalindexs_id_put**](NumericalIndexApi.md#numericalindexs_id_put) | **PUT** /numericalindexs/{id} | Update a NumericalIndex
[**numericalindexs_post**](NumericalIndexApi.md#numericalindexs_post) | **POST** /numericalindexs | Create a NumericalIndex


# **numericalindexs_get**
> list[NumericalIndex] numericalindexs_get(username=username, label=label)

List all NumericalIndex entities

Gets a list of all NumericalIndex entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.NumericalIndexApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all NumericalIndex entities
    api_response = api_instance.numericalindexs_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[NumericalIndex]**](NumericalIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numericalindexs_id_delete**
> numericalindexs_id_delete(id, user)

Delete a NumericalIndex

Delete an existing NumericalIndex

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a NumericalIndex
    api_instance.numericalindexs_id_delete(id, user)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_delete: %s\n" % e)
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

# **numericalindexs_id_get**
> NumericalIndex numericalindexs_id_get(id, username=username)

Get a NumericalIndex

Gets the details of a single instance of a NumericalIndex

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.NumericalIndexApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a NumericalIndex
    api_response = api_instance.numericalindexs_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numericalindexs_id_put**
> NumericalIndex numericalindexs_id_put(id, user, numerical_index=numerical_index)

Update a NumericalIndex

Updates an existing NumericalIndex

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
numerical_index = modelcatalog.NumericalIndex() # NumericalIndex | An old NumericalIndexto be updated (optional)

try:
    # Update a NumericalIndex
    api_response = api_instance.numericalindexs_id_put(id, user, numerical_index=numerical_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **numerical_index** | [**NumericalIndex**](NumericalIndex.md)| An old NumericalIndexto be updated | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numericalindexs_post**
> NumericalIndex numericalindexs_post(user, numerical_index=numerical_index)

Create a NumericalIndex

Create a new instance of a NumericalIndex

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
api_instance = modelcatalog.NumericalIndexApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
numerical_index = modelcatalog.NumericalIndex() # NumericalIndex | A new NumericalIndexto be created (optional)

try:
    # Create a NumericalIndex
    api_response = api_instance.numericalindexs_post(user, numerical_index=numerical_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NumericalIndexApi->numericalindexs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **numerical_index** | [**NumericalIndex**](NumericalIndex.md)| A new NumericalIndexto be created | [optional] 

### Return type

[**NumericalIndex**](NumericalIndex.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


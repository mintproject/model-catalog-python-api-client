# modelcatalog.SourceCodeApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sourcecodes_get**](SourceCodeApi.md#sourcecodes_get) | **GET** /sourcecodes | List all SourceCode entities
[**sourcecodes_id_delete**](SourceCodeApi.md#sourcecodes_id_delete) | **DELETE** /sourcecodes/{id} | Delete a SourceCode
[**sourcecodes_id_get**](SourceCodeApi.md#sourcecodes_id_get) | **GET** /sourcecodes/{id} | Get a SourceCode
[**sourcecodes_id_put**](SourceCodeApi.md#sourcecodes_id_put) | **PUT** /sourcecodes/{id} | Update a SourceCode
[**sourcecodes_post**](SourceCodeApi.md#sourcecodes_post) | **POST** /sourcecodes | Create a SourceCode


# **sourcecodes_get**
> list[SourceCode] sourcecodes_get(username=username, label=label)

List all SourceCode entities

Gets a list of all SourceCode entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SourceCodeApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SourceCode entities
    api_response = api_instance.sourcecodes_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SourceCode]**](SourceCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sourcecodes_id_delete**
> sourcecodes_id_delete(id, user)

Delete a SourceCode

Delete an existing SourceCode

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SourceCode
    api_instance.sourcecodes_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_delete: %s\n" % e)
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

# **sourcecodes_id_get**
> SourceCode sourcecodes_id_get(id, username=username)

Get a SourceCode

Gets the details of a single instance of a SourceCode

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SourceCodeApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SourceCode
    api_response = api_instance.sourcecodes_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sourcecodes_id_put**
> SourceCode sourcecodes_id_put(id, user, source_code=source_code)

Update a SourceCode

Updates an existing SourceCode

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
source_code = modelcatalog.SourceCode() # SourceCode | An old SourceCodeto be updated (optional)

try:
    # Update a SourceCode
    api_response = api_instance.sourcecodes_id_put(id, user, source_code=source_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **source_code** | [**SourceCode**](SourceCode.md)| An old SourceCodeto be updated | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sourcecodes_post**
> SourceCode sourcecodes_post(user, source_code=source_code)

Create a SourceCode

Create a new instance of a SourceCode

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
api_instance = modelcatalog.SourceCodeApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
source_code = modelcatalog.SourceCode() # SourceCode | A new SourceCodeto be created (optional)

try:
    # Create a SourceCode
    api_response = api_instance.sourcecodes_post(user, source_code=source_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceCodeApi->sourcecodes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **source_code** | [**SourceCode**](SourceCode.md)| A new SourceCodeto be created | [optional] 

### Return type

[**SourceCode**](SourceCode.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


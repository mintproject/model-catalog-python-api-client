# modelcatalog.SubsidyApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subsidys_get**](SubsidyApi.md#subsidys_get) | **GET** /subsidys | List all Subsidy entities
[**subsidys_id_delete**](SubsidyApi.md#subsidys_id_delete) | **DELETE** /subsidys/{id} | Delete a Subsidy
[**subsidys_id_get**](SubsidyApi.md#subsidys_id_get) | **GET** /subsidys/{id} | Get a Subsidy
[**subsidys_id_put**](SubsidyApi.md#subsidys_id_put) | **PUT** /subsidys/{id} | Update a Subsidy
[**subsidys_post**](SubsidyApi.md#subsidys_post) | **POST** /subsidys | Create a Subsidy


# **subsidys_get**
> list[Subsidy] subsidys_get(username=username, label=label)

List all Subsidy entities

Gets a list of all Subsidy entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SubsidyApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Subsidy entities
    api_response = api_instance.subsidys_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidyApi->subsidys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Subsidy]**](Subsidy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidys_id_delete**
> subsidys_id_delete(id, user)

Delete a Subsidy

Delete an existing Subsidy

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
api_instance = modelcatalog.SubsidyApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Subsidy
    api_instance.subsidys_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SubsidyApi->subsidys_id_delete: %s\n" % e)
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

# **subsidys_id_get**
> Subsidy subsidys_id_get(id, username=username)

Get a Subsidy

Gets the details of a single instance of a Subsidy

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SubsidyApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Subsidy
    api_response = api_instance.subsidys_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidyApi->subsidys_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Subsidy**](Subsidy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidys_id_put**
> Subsidy subsidys_id_put(id, user, subsidy=subsidy)

Update a Subsidy

Updates an existing Subsidy

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
api_instance = modelcatalog.SubsidyApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
subsidy = modelcatalog.Subsidy() # Subsidy | An old Subsidyto be updated (optional)

try:
    # Update a Subsidy
    api_response = api_instance.subsidys_id_put(id, user, subsidy=subsidy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidyApi->subsidys_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **subsidy** | [**Subsidy**](Subsidy.md)| An old Subsidyto be updated | [optional] 

### Return type

[**Subsidy**](Subsidy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidys_post**
> Subsidy subsidys_post(user, subsidy=subsidy)

Create a Subsidy

Create a new instance of a Subsidy

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
api_instance = modelcatalog.SubsidyApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
subsidy = modelcatalog.Subsidy() # Subsidy | A new Subsidyto be created (optional)

try:
    # Create a Subsidy
    api_response = api_instance.subsidys_post(user, subsidy=subsidy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidyApi->subsidys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **subsidy** | [**Subsidy**](Subsidy.md)| A new Subsidyto be created | [optional] 

### Return type

[**Subsidy**](Subsidy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


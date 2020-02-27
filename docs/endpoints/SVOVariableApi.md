# modelcatalog.SVOVariableApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**svovariables_get**](SVOVariableApi.md#svovariables_get) | **GET** /svovariables | List all SVOVariable entities
[**svovariables_id_delete**](SVOVariableApi.md#svovariables_id_delete) | **DELETE** /svovariables/{id} | Delete a SVOVariable
[**svovariables_id_get**](SVOVariableApi.md#svovariables_id_get) | **GET** /svovariables/{id} | Get a SVOVariable
[**svovariables_id_put**](SVOVariableApi.md#svovariables_id_put) | **PUT** /svovariables/{id} | Update a SVOVariable
[**svovariables_post**](SVOVariableApi.md#svovariables_post) | **POST** /svovariables | Create a SVOVariable


# **svovariables_get**
> list[SVOVariable] svovariables_get(username=username, label=label)

List all SVOVariable entities

Gets a list of all SVOVariable entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SVOVariableApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SVOVariable entities
    api_response = api_instance.svovariables_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SVOVariable]**](SVOVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **svovariables_id_delete**
> svovariables_id_delete(id, user)

Delete a SVOVariable

Delete an existing SVOVariable

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
api_instance = modelcatalog.SVOVariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SVOVariable
    api_instance.svovariables_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_delete: %s\n" % e)
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

# **svovariables_id_get**
> SVOVariable svovariables_id_get(id, username=username)

Get a SVOVariable

Gets the details of a single instance of a SVOVariable

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SVOVariableApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SVOVariable
    api_response = api_instance.svovariables_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SVOVariable**](SVOVariable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **svovariables_id_put**
> SVOVariable svovariables_id_put(id, user, svo_variable=svo_variable)

Update a SVOVariable

Updates an existing SVOVariable

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
api_instance = modelcatalog.SVOVariableApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
svo_variable = modelcatalog.SVOVariable() # SVOVariable | An old SVOVariableto be updated (optional)

try:
    # Update a SVOVariable
    api_response = api_instance.svovariables_id_put(id, user, svo_variable=svo_variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **svo_variable** | [**SVOVariable**](SVOVariable.md)| An old SVOVariableto be updated | [optional] 

### Return type

[**SVOVariable**](SVOVariable.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **svovariables_post**
> SVOVariable svovariables_post(user, svo_variable=svo_variable)

Create a SVOVariable

Create a new instance of a SVOVariable

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
api_instance = modelcatalog.SVOVariableApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
svo_variable = modelcatalog.SVOVariable() # SVOVariable | A new SVOVariableto be created (optional)

try:
    # Create a SVOVariable
    api_response = api_instance.svovariables_post(user, svo_variable=svo_variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SVOVariableApi->svovariables_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **svo_variable** | [**SVOVariable**](SVOVariable.md)| A new SVOVariableto be created | [optional] 

### Return type

[**SVOVariable**](SVOVariable.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


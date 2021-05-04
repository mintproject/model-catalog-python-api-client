# modelcatalog.DataTransformationSetupApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datatransformationsetups_get**](DataTransformationSetupApi.md#datatransformationsetups_get) | **GET** /datatransformationsetups | List all instances of DataTransformationSetup
[**datatransformationsetups_id_delete**](DataTransformationSetupApi.md#datatransformationsetups_id_delete) | **DELETE** /datatransformationsetups/{id} | Delete an existing DataTransformationSetup
[**datatransformationsetups_id_get**](DataTransformationSetupApi.md#datatransformationsetups_id_get) | **GET** /datatransformationsetups/{id} | Get a single DataTransformationSetup by its id
[**datatransformationsetups_id_put**](DataTransformationSetupApi.md#datatransformationsetups_id_put) | **PUT** /datatransformationsetups/{id} | Update an existing DataTransformationSetup
[**datatransformationsetups_post**](DataTransformationSetupApi.md#datatransformationsetups_post) | **POST** /datatransformationsetups | Create one DataTransformationSetup


# **datatransformationsetups_get**
> list[DataTransformationSetup] datatransformationsetups_get(username=username, label=label, page=page, per_page=per_page)

List all instances of DataTransformationSetup

Gets a list of all instances of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DataTransformationSetupApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of DataTransformationSetup
    api_response = api_instance.datatransformationsetups_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationSetupApi->datatransformationsetups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[DataTransformationSetup]**](DataTransformationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of DataTransformationSetup. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datatransformationsetups_id_delete**
> datatransformationsetups_id_delete(id, user=user)

Delete an existing DataTransformationSetup

Delete an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DataTransformationSetup to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing DataTransformationSetup
    api_instance.datatransformationsetups_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling DataTransformationSetupApi->datatransformationsetups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformationSetup to be retrieved | 
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

# **datatransformationsetups_id_get**
> DataTransformationSetup datatransformationsetups_id_get(id, username=username)

Get a single DataTransformationSetup by its id

Gets the details of a given DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DataTransformationSetupApi()
id = 'id_example' # str | The ID of the DataTransformationSetup to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single DataTransformationSetup by its id
    api_response = api_instance.datatransformationsetups_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationSetupApi->datatransformationsetups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformationSetup to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**DataTransformationSetup**](DataTransformationSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given DataTransformationSetup |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **datatransformationsetups_id_put**
> DataTransformationSetup datatransformationsetups_id_put(id, user=user, data_transformation_setup=data_transformation_setup)

Update an existing DataTransformationSetup

Updates an existing DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationSetupApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the DataTransformationSetup to be retrieved
user = 'user_example' # str | Username (optional)
data_transformation_setup = modelcatalog.DataTransformationSetup() # DataTransformationSetup | An old DataTransformationSetupto be updated (optional)

try:
    # Update an existing DataTransformationSetup
    api_response = api_instance.datatransformationsetups_id_put(id, user=user, data_transformation_setup=data_transformation_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationSetupApi->datatransformationsetups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the DataTransformationSetup to be retrieved | 
 **user** | **str**| Username | [optional] 
 **data_transformation_setup** | [**DataTransformationSetup**](DataTransformationSetup.md)| An old DataTransformationSetupto be updated | [optional] 

### Return type

[**DataTransformationSetup**](DataTransformationSetup.md)

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

# **datatransformationsetups_post**
> DataTransformationSetup datatransformationsetups_post(user=user, data_transformation_setup=data_transformation_setup)

Create one DataTransformationSetup

Create a new instance of DataTransformationSetup (more information in https://w3id.org/okn/o/sd#DataTransformationSetup)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.8.0
configuration.host = "https://api.models.mint.isi.edu/v1.8.0"
# Create an instance of the API class
api_instance = modelcatalog.DataTransformationSetupApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
data_transformation_setup = modelcatalog.DataTransformationSetup() # DataTransformationSetup | Information about the DataTransformationSetupto be created (optional)

try:
    # Create one DataTransformationSetup
    api_response = api_instance.datatransformationsetups_post(user=user, data_transformation_setup=data_transformation_setup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTransformationSetupApi->datatransformationsetups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **data_transformation_setup** | [**DataTransformationSetup**](DataTransformationSetup.md)| Information about the DataTransformationSetupto be created | [optional] 

### Return type

[**DataTransformationSetup**](DataTransformationSetup.md)

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


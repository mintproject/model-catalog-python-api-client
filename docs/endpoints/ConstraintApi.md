# modelcatalog.ConstraintApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**constraints_get**](ConstraintApi.md#constraints_get) | **GET** /constraints | List all instances of Constraint
[**constraints_id_delete**](ConstraintApi.md#constraints_id_delete) | **DELETE** /constraints/{id} | Delete an existing Constraint
[**constraints_id_get**](ConstraintApi.md#constraints_id_get) | **GET** /constraints/{id} | Get a single Constraint by its id
[**constraints_id_put**](ConstraintApi.md#constraints_id_put) | **PUT** /constraints/{id} | Update an existing Constraint
[**constraints_post**](ConstraintApi.md#constraints_post) | **POST** /constraints | Create one Constraint


# **constraints_get**
> list[Constraint] constraints_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Constraint

Gets a list of all instances of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ConstraintApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Constraint
    api_response = api_instance.constraints_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->constraints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Constraint]**](Constraint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Constraint. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **constraints_id_delete**
> constraints_id_delete(id, user=user)

Delete an existing Constraint

Delete an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)

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
api_instance = modelcatalog.ConstraintApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Constraint to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Constraint
    api_instance.constraints_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling ConstraintApi->constraints_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Constraint to be retrieved | 
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

# **constraints_id_get**
> Constraint constraints_id_get(id, username=username)

Get a single Constraint by its id

Gets the details of a given Constraint (more information in https://w3id.org/okn/o/sd#Constraint)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.ConstraintApi()
id = 'id_example' # str | The ID of the Constraint to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Constraint by its id
    api_response = api_instance.constraints_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->constraints_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Constraint to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Constraint**](Constraint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Constraint |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **constraints_id_put**
> Constraint constraints_id_put(id, user=user, constraint=constraint)

Update an existing Constraint

Updates an existing Constraint (more information in https://w3id.org/okn/o/sd#Constraint)

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
api_instance = modelcatalog.ConstraintApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Constraint to be retrieved
user = 'user_example' # str | Username (optional)
constraint = modelcatalog.Constraint() # Constraint | An old Constraintto be updated (optional)

try:
    # Update an existing Constraint
    api_response = api_instance.constraints_id_put(id, user=user, constraint=constraint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->constraints_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Constraint to be retrieved | 
 **user** | **str**| Username | [optional] 
 **constraint** | [**Constraint**](Constraint.md)| An old Constraintto be updated | [optional] 

### Return type

[**Constraint**](Constraint.md)

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

# **constraints_post**
> Constraint constraints_post(user=user, constraint=constraint)

Create one Constraint

Create a new instance of Constraint (more information in https://w3id.org/okn/o/sd#Constraint)

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
api_instance = modelcatalog.ConstraintApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
constraint = modelcatalog.Constraint() # Constraint | Information about the Constraintto be created (optional)

try:
    # Create one Constraint
    api_response = api_instance.constraints_post(user=user, constraint=constraint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->constraints_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **constraint** | [**Constraint**](Constraint.md)| Information about the Constraintto be created | [optional] 

### Return type

[**Constraint**](Constraint.md)

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


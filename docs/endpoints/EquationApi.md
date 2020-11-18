# modelcatalog.EquationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**equations_get**](EquationApi.md#equations_get) | **GET** /equations | List all instances of Equation
[**equations_id_delete**](EquationApi.md#equations_id_delete) | **DELETE** /equations/{id} | Delete an existing Equation
[**equations_id_get**](EquationApi.md#equations_id_get) | **GET** /equations/{id} | Get a single Equation by its id
[**equations_id_put**](EquationApi.md#equations_id_put) | **PUT** /equations/{id} | Update an existing Equation
[**equations_post**](EquationApi.md#equations_post) | **POST** /equations | Create one Equation


# **equations_get**
> list[Equation] equations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Equation

Gets a list of all instances of Equation (more information in https://w3id.org/okn/o/sdm#Equation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EquationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Equation
    api_response = api_instance.equations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Equation]**](Equation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Equation. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **equations_id_delete**
> equations_id_delete(id, user)

Delete an existing Equation

Delete an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Equation to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Equation
    api_instance.equations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Equation to be retrieved | 
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

# **equations_id_get**
> Equation equations_id_get(id, username=username)

Get a single Equation by its id

Gets the details of a given Equation (more information in https://w3id.org/okn/o/sdm#Equation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.EquationApi()
id = 'id_example' # str | The ID of the Equation to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Equation by its id
    api_response = api_instance.equations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Equation to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Equation**](Equation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Equation |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **equations_id_put**
> Equation equations_id_put(id, user, equation=equation)

Update an existing Equation

Updates an existing Equation (more information in https://w3id.org/okn/o/sdm#Equation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Equation to be retrieved
user = 'user_example' # str | Username
equation = modelcatalog.Equation() # Equation | An old Equationto be updated (optional)

try:
    # Update an existing Equation
    api_response = api_instance.equations_id_put(id, user, equation=equation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Equation to be retrieved | 
 **user** | **str**| Username | 
 **equation** | [**Equation**](Equation.md)| An old Equationto be updated | [optional] 

### Return type

[**Equation**](Equation.md)

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

# **equations_post**
> Equation equations_post(user, equation=equation)

Create one Equation

Create a new instance of Equation (more information in https://w3id.org/okn/o/sdm#Equation)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.6.0
configuration.host = "https://api.models.mint.isi.edu/v1.6.0"
# Create an instance of the API class
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
equation = modelcatalog.Equation() # Equation | Information about the Equationto be created (optional)

try:
    # Create one Equation
    api_response = api_instance.equations_post(user, equation=equation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **equation** | [**Equation**](Equation.md)| Information about the Equationto be created | [optional] 

### Return type

[**Equation**](Equation.md)

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


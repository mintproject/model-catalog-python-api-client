# modelcatalog.EquationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**equations_get**](EquationApi.md#equations_get) | **GET** /equations | List all Equation entities
[**equations_id_delete**](EquationApi.md#equations_id_delete) | **DELETE** /equations/{id} | Delete a Equation
[**equations_id_get**](EquationApi.md#equations_id_get) | **GET** /equations/{id} | Get a Equation
[**equations_id_put**](EquationApi.md#equations_id_put) | **PUT** /equations/{id} | Update a Equation
[**equations_post**](EquationApi.md#equations_post) | **POST** /equations | Create a Equation


# **equations_get**
> list[Equation] equations_get(username=username, label=label)

List all Equation entities

Gets a list of all Equation entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.EquationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Equation entities
    api_response = api_instance.equations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Equation]**](Equation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **equations_id_delete**
> equations_id_delete(id, user)

Delete a Equation

Delete an existing Equation

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
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Equation
    api_instance.equations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_delete: %s\n" % e)
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

# **equations_id_get**
> Equation equations_id_get(id, username=username)

Get a Equation

Gets the details of a single instance of a Equation

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.EquationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Equation
    api_response = api_instance.equations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Equation**](Equation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **equations_id_put**
> Equation equations_id_put(id, user, equation=equation)

Update a Equation

Updates an existing Equation

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
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
equation = modelcatalog.Equation() # Equation | An old Equationto be updated (optional)

try:
    # Update a Equation
    api_response = api_instance.equations_id_put(id, user, equation=equation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **equation** | [**Equation**](Equation.md)| An old Equationto be updated | [optional] 

### Return type

[**Equation**](Equation.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **equations_post**
> Equation equations_post(user, equation=equation)

Create a Equation

Create a new instance of a Equation

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
api_instance = modelcatalog.EquationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
equation = modelcatalog.Equation() # Equation | A new Equationto be created (optional)

try:
    # Create a Equation
    api_response = api_instance.equations_post(user, equation=equation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquationApi->equations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **equation** | [**Equation**](Equation.md)| A new Equationto be created | [optional] 

### Return type

[**Equation**](Equation.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


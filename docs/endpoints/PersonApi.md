# modelcatalog.PersonApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**persons_get**](PersonApi.md#persons_get) | **GET** /persons | List all instances of Person
[**persons_id_delete**](PersonApi.md#persons_id_delete) | **DELETE** /persons/{id} | Delete an existing Person
[**persons_id_get**](PersonApi.md#persons_id_get) | **GET** /persons/{id} | Get a single Person by its id
[**persons_id_put**](PersonApi.md#persons_id_put) | **PUT** /persons/{id} | Update an existing Person
[**persons_post**](PersonApi.md#persons_post) | **POST** /persons | Create one Person


# **persons_get**
> list[Person] persons_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Person

Gets a list of all instances of Person (more information in https://w3id.org/okn/o/sd#Person)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.PersonApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Person
    api_response = api_instance.persons_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->persons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Person]**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Person. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **persons_id_delete**
> persons_id_delete(id, user)

Delete an existing Person

Delete an existing Person (more information in https://w3id.org/okn/o/sd#Person)

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
api_instance = modelcatalog.PersonApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Person to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Person
    api_instance.persons_id_delete(id, user)
except ApiException as e:
    print("Exception when calling PersonApi->persons_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Person to be retrieved | 
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

# **persons_id_get**
> Person persons_id_get(id, username=username)

Get a single Person by its id

Gets the details of a given Person (more information in https://w3id.org/okn/o/sd#Person)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.PersonApi()
id = 'id_example' # str | The ID of the Person to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Person by its id
    api_response = api_instance.persons_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->persons_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Person to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Person |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **persons_id_put**
> Person persons_id_put(id, user, person=person)

Update an existing Person

Updates an existing Person (more information in https://w3id.org/okn/o/sd#Person)

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
api_instance = modelcatalog.PersonApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Person to be retrieved
user = 'user_example' # str | Username
person = modelcatalog.Person() # Person | An old Personto be updated (optional)

try:
    # Update an existing Person
    api_response = api_instance.persons_id_put(id, user, person=person)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->persons_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Person to be retrieved | 
 **user** | **str**| Username | 
 **person** | [**Person**](Person.md)| An old Personto be updated | [optional] 

### Return type

[**Person**](Person.md)

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

# **persons_post**
> Person persons_post(user, person=person)

Create one Person

Create a new instance of Person (more information in https://w3id.org/okn/o/sd#Person)

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
api_instance = modelcatalog.PersonApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
person = modelcatalog.Person() # Person | Information about the Personto be created (optional)

try:
    # Create one Person
    api_response = api_instance.persons_post(user, person=person)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->persons_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **person** | [**Person**](Person.md)| Information about the Personto be created | [optional] 

### Return type

[**Person**](Person.md)

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


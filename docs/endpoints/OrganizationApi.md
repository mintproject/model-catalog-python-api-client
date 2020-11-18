# modelcatalog.OrganizationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_get**](OrganizationApi.md#organizations_get) | **GET** /organizations | List all instances of Organization
[**organizations_id_delete**](OrganizationApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete an existing Organization
[**organizations_id_get**](OrganizationApi.md#organizations_id_get) | **GET** /organizations/{id} | Get a single Organization by its id
[**organizations_id_put**](OrganizationApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update an existing Organization
[**organizations_post**](OrganizationApi.md#organizations_post) | **POST** /organizations | Create one Organization


# **organizations_get**
> list[Organization] organizations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Organization

Gets a list of all instances of Organization (more information in https://w3id.org/okn/o/sd#Organization)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.OrganizationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Organization
    api_response = api_instance.organizations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Organization]**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Organization. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **organizations_id_delete**
> organizations_id_delete(id, user)

Delete an existing Organization

Delete an existing Organization (more information in https://w3id.org/okn/o/sd#Organization)

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Organization to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Organization
    api_instance.organizations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization to be retrieved | 
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

# **organizations_id_get**
> Organization organizations_id_get(id, username=username)

Get a single Organization by its id

Gets the details of a given Organization (more information in https://w3id.org/okn/o/sd#Organization)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.OrganizationApi()
id = 'id_example' # str | The ID of the Organization to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Organization by its id
    api_response = api_instance.organizations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Organization |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **organizations_id_put**
> Organization organizations_id_put(id, user, organization=organization)

Update an existing Organization

Updates an existing Organization (more information in https://w3id.org/okn/o/sd#Organization)

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Organization to be retrieved
user = 'user_example' # str | Username
organization = modelcatalog.Organization() # Organization | An old Organizationto be updated (optional)

try:
    # Update an existing Organization
    api_response = api_instance.organizations_id_put(id, user, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization to be retrieved | 
 **user** | **str**| Username | 
 **organization** | [**Organization**](Organization.md)| An old Organizationto be updated | [optional] 

### Return type

[**Organization**](Organization.md)

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

# **organizations_post**
> Organization organizations_post(user, organization=organization)

Create one Organization

Create a new instance of Organization (more information in https://w3id.org/okn/o/sd#Organization)

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
organization = modelcatalog.Organization() # Organization | Information about the Organizationto be created (optional)

try:
    # Create one Organization
    api_response = api_instance.organizations_post(user, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **organization** | [**Organization**](Organization.md)| Information about the Organizationto be created | [optional] 

### Return type

[**Organization**](Organization.md)

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


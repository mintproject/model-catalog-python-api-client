# modelcatalog.OrganizationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_get**](OrganizationApi.md#organizations_get) | **GET** /organizations | List all Organization entities
[**organizations_id_delete**](OrganizationApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete a Organization
[**organizations_id_get**](OrganizationApi.md#organizations_id_get) | **GET** /organizations/{id} | Get a Organization
[**organizations_id_put**](OrganizationApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update a Organization
[**organizations_post**](OrganizationApi.md#organizations_post) | **POST** /organizations | Create a Organization


# **organizations_get**
> list[Organization] organizations_get(username=username, label=label)

List all Organization entities

Gets a list of all Organization entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.OrganizationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Organization entities
    api_response = api_instance.organizations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Organization]**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_delete**
> organizations_id_delete(id, user)

Delete a Organization

Delete an existing Organization

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Organization
    api_instance.organizations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_delete: %s\n" % e)
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

# **organizations_id_get**
> Organization organizations_id_get(id, username=username)

Get a Organization

Gets the details of a single instance of a Organization

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.OrganizationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Organization
    api_response = api_instance.organizations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_put**
> Organization organizations_id_put(id, user, organization=organization)

Update a Organization

Updates an existing Organization

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
organization = modelcatalog.Organization() # Organization | An old Organizationto be updated (optional)

try:
    # Update a Organization
    api_response = api_instance.organizations_id_put(id, user, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **organization** | [**Organization**](Organization.md)| An old Organizationto be updated | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_post**
> Organization organizations_post(user, organization=organization)

Create a Organization

Create a new instance of a Organization

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
api_instance = modelcatalog.OrganizationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
organization = modelcatalog.Organization() # Organization | A new Organizationto be created (optional)

try:
    # Create a Organization
    api_response = api_instance.organizations_post(user, organization=organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **organization** | [**Organization**](Organization.md)| A new Organizationto be created | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


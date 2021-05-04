# modelcatalog.CatalogIdentifierApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.8.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogidentifiers_get**](CatalogIdentifierApi.md#catalogidentifiers_get) | **GET** /catalogidentifiers | List all instances of CatalogIdentifier
[**catalogidentifiers_id_delete**](CatalogIdentifierApi.md#catalogidentifiers_id_delete) | **DELETE** /catalogidentifiers/{id} | Delete an existing CatalogIdentifier
[**catalogidentifiers_id_get**](CatalogIdentifierApi.md#catalogidentifiers_id_get) | **GET** /catalogidentifiers/{id} | Get a single CatalogIdentifier by its id
[**catalogidentifiers_id_put**](CatalogIdentifierApi.md#catalogidentifiers_id_put) | **PUT** /catalogidentifiers/{id} | Update an existing CatalogIdentifier
[**catalogidentifiers_post**](CatalogIdentifierApi.md#catalogidentifiers_post) | **POST** /catalogidentifiers | Create one CatalogIdentifier


# **catalogidentifiers_get**
> list[CatalogIdentifier] catalogidentifiers_get(username=username, label=label, page=page, per_page=per_page)

List all instances of CatalogIdentifier

Gets a list of all instances of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CatalogIdentifierApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of CatalogIdentifier
    api_response = api_instance.catalogidentifiers_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogIdentifierApi->catalogidentifiers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[CatalogIdentifier]**](CatalogIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of CatalogIdentifier. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **catalogidentifiers_id_delete**
> catalogidentifiers_id_delete(id, user=user)

Delete an existing CatalogIdentifier

Delete an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)

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
api_instance = modelcatalog.CatalogIdentifierApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CatalogIdentifier to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing CatalogIdentifier
    api_instance.catalogidentifiers_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling CatalogIdentifierApi->catalogidentifiers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CatalogIdentifier to be retrieved | 
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

# **catalogidentifiers_id_get**
> CatalogIdentifier catalogidentifiers_id_get(id, username=username)

Get a single CatalogIdentifier by its id

Gets the details of a given CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.CatalogIdentifierApi()
id = 'id_example' # str | The ID of the CatalogIdentifier to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single CatalogIdentifier by its id
    api_response = api_instance.catalogidentifiers_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogIdentifierApi->catalogidentifiers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CatalogIdentifier to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**CatalogIdentifier**](CatalogIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given CatalogIdentifier |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **catalogidentifiers_id_put**
> CatalogIdentifier catalogidentifiers_id_put(id, user=user, catalog_identifier=catalog_identifier)

Update an existing CatalogIdentifier

Updates an existing CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)

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
api_instance = modelcatalog.CatalogIdentifierApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the CatalogIdentifier to be retrieved
user = 'user_example' # str | Username (optional)
catalog_identifier = modelcatalog.CatalogIdentifier() # CatalogIdentifier | An old CatalogIdentifierto be updated (optional)

try:
    # Update an existing CatalogIdentifier
    api_response = api_instance.catalogidentifiers_id_put(id, user=user, catalog_identifier=catalog_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogIdentifierApi->catalogidentifiers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CatalogIdentifier to be retrieved | 
 **user** | **str**| Username | [optional] 
 **catalog_identifier** | [**CatalogIdentifier**](CatalogIdentifier.md)| An old CatalogIdentifierto be updated | [optional] 

### Return type

[**CatalogIdentifier**](CatalogIdentifier.md)

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

# **catalogidentifiers_post**
> CatalogIdentifier catalogidentifiers_post(user=user, catalog_identifier=catalog_identifier)

Create one CatalogIdentifier

Create a new instance of CatalogIdentifier (more information in https://w3id.org/okn/o/sd#CatalogIdentifier)

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
api_instance = modelcatalog.CatalogIdentifierApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
catalog_identifier = modelcatalog.CatalogIdentifier() # CatalogIdentifier | Information about the CatalogIdentifierto be created (optional)

try:
    # Create one CatalogIdentifier
    api_response = api_instance.catalogidentifiers_post(user=user, catalog_identifier=catalog_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogIdentifierApi->catalogidentifiers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **catalog_identifier** | [**CatalogIdentifier**](CatalogIdentifier.md)| Information about the CatalogIdentifierto be created | [optional] 

### Return type

[**CatalogIdentifier**](CatalogIdentifier.md)

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


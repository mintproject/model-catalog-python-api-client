# modelcatalog.InterventionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interventions_get**](InterventionApi.md#interventions_get) | **GET** /interventions | List all instances of Intervention
[**interventions_id_delete**](InterventionApi.md#interventions_id_delete) | **DELETE** /interventions/{id} | Delete an existing Intervention
[**interventions_id_get**](InterventionApi.md#interventions_id_get) | **GET** /interventions/{id} | Get a single Intervention by its id
[**interventions_id_put**](InterventionApi.md#interventions_id_put) | **PUT** /interventions/{id} | Update an existing Intervention
[**interventions_post**](InterventionApi.md#interventions_post) | **POST** /interventions | Create one Intervention


# **interventions_get**
> list[Intervention] interventions_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Intervention

Gets a list of all instances of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.InterventionApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Intervention
    api_response = api_instance.interventions_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Intervention]**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Intervention. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **interventions_id_delete**
> interventions_id_delete(id, user)

Delete an existing Intervention

Delete an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Intervention to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Intervention
    api_instance.interventions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Intervention to be retrieved | 
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

# **interventions_id_get**
> Intervention interventions_id_get(id, username=username)

Get a single Intervention by its id

Gets the details of a given Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.InterventionApi()
id = 'id_example' # str | The ID of the Intervention to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Intervention by its id
    api_response = api_instance.interventions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Intervention to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Intervention**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Intervention |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **interventions_id_put**
> Intervention interventions_id_put(id, user, intervention=intervention)

Update an existing Intervention

Updates an existing Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Intervention to be retrieved
user = 'user_example' # str | Username
intervention = modelcatalog.Intervention() # Intervention | An old Interventionto be updated (optional)

try:
    # Update an existing Intervention
    api_response = api_instance.interventions_id_put(id, user, intervention=intervention)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Intervention to be retrieved | 
 **user** | **str**| Username | 
 **intervention** | [**Intervention**](Intervention.md)| An old Interventionto be updated | [optional] 

### Return type

[**Intervention**](Intervention.md)

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

# **interventions_post**
> Intervention interventions_post(user, intervention=intervention)

Create one Intervention

Create a new instance of Intervention (more information in https://w3id.org/okn/o/sdm#Intervention)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.5.0
configuration.host = "https://api.models.mint.isi.edu/v1.5.0"
# Create an instance of the API class
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
intervention = modelcatalog.Intervention() # Intervention | Information about the Interventionto be created (optional)

try:
    # Create one Intervention
    api_response = api_instance.interventions_post(user, intervention=intervention)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **intervention** | [**Intervention**](Intervention.md)| Information about the Interventionto be created | [optional] 

### Return type

[**Intervention**](Intervention.md)

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


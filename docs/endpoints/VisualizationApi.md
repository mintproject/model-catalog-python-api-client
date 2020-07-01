# modelcatalog.VisualizationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualizations_get**](VisualizationApi.md#visualizations_get) | **GET** /visualizations | List all instances of Visualization
[**visualizations_id_delete**](VisualizationApi.md#visualizations_id_delete) | **DELETE** /visualizations/{id} | Delete an existing Visualization
[**visualizations_id_get**](VisualizationApi.md#visualizations_id_get) | **GET** /visualizations/{id} | Get a single Visualization by its id
[**visualizations_id_put**](VisualizationApi.md#visualizations_id_put) | **PUT** /visualizations/{id} | Update an existing Visualization
[**visualizations_post**](VisualizationApi.md#visualizations_post) | **POST** /visualizations | Create one Visualization


# **visualizations_get**
> list[Visualization] visualizations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Visualization

Gets a list of all instances of Visualization (more information in https://w3id.org/okn/o/sd#Visualization)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VisualizationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Visualization
    api_response = api_instance.visualizations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Visualization]**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Visualization. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **visualizations_id_delete**
> visualizations_id_delete(id, user)

Delete an existing Visualization

Delete an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization)

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Visualization to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing Visualization
    api_instance.visualizations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Visualization to be retrieved | 
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

# **visualizations_id_get**
> Visualization visualizations_id_get(id, username=username)

Get a single Visualization by its id

Gets the details of a given Visualization (more information in https://w3id.org/okn/o/sd#Visualization)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.VisualizationApi()
id = 'id_example' # str | The ID of the Visualization to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Visualization by its id
    api_response = api_instance.visualizations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Visualization to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Visualization |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **visualizations_id_put**
> Visualization visualizations_id_put(id, user, visualization=visualization)

Update an existing Visualization

Updates an existing Visualization (more information in https://w3id.org/okn/o/sd#Visualization)

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Visualization to be retrieved
user = 'user_example' # str | Username
visualization = modelcatalog.Visualization() # Visualization | An old Visualizationto be updated (optional)

try:
    # Update an existing Visualization
    api_response = api_instance.visualizations_id_put(id, user, visualization=visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Visualization to be retrieved | 
 **user** | **str**| Username | 
 **visualization** | [**Visualization**](Visualization.md)| An old Visualizationto be updated | [optional] 

### Return type

[**Visualization**](Visualization.md)

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

# **visualizations_post**
> Visualization visualizations_post(user, visualization=visualization)

Create one Visualization

Create a new instance of Visualization (more information in https://w3id.org/okn/o/sd#Visualization)

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
visualization = modelcatalog.Visualization() # Visualization | Information about the Visualizationto be created (optional)

try:
    # Create one Visualization
    api_response = api_instance.visualizations_post(user, visualization=visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **visualization** | [**Visualization**](Visualization.md)| Information about the Visualizationto be created | [optional] 

### Return type

[**Visualization**](Visualization.md)

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


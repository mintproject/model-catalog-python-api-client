# modelcatalog.VisualizationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualizations_get**](VisualizationApi.md#visualizations_get) | **GET** /visualizations | List all Visualization entities
[**visualizations_id_delete**](VisualizationApi.md#visualizations_id_delete) | **DELETE** /visualizations/{id} | Delete a Visualization
[**visualizations_id_get**](VisualizationApi.md#visualizations_id_get) | **GET** /visualizations/{id} | Get a Visualization
[**visualizations_id_put**](VisualizationApi.md#visualizations_id_put) | **PUT** /visualizations/{id} | Update a Visualization
[**visualizations_post**](VisualizationApi.md#visualizations_post) | **POST** /visualizations | Create a Visualization


# **visualizations_get**
> list[Visualization] visualizations_get(username=username, label=label)

List all Visualization entities

Gets a list of all Visualization entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.VisualizationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Visualization entities
    api_response = api_instance.visualizations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Visualization]**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualizations_id_delete**
> visualizations_id_delete(id, user)

Delete a Visualization

Delete an existing Visualization

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Visualization
    api_instance.visualizations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_delete: %s\n" % e)
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

# **visualizations_id_get**
> Visualization visualizations_id_get(id, username=username)

Get a Visualization

Gets the details of a single instance of a Visualization

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.VisualizationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Visualization
    api_response = api_instance.visualizations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualizations_id_put**
> Visualization visualizations_id_put(id, user, visualization=visualization)

Update a Visualization

Updates an existing Visualization

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
visualization = modelcatalog.Visualization() # Visualization | An old Visualizationto be updated (optional)

try:
    # Update a Visualization
    api_response = api_instance.visualizations_id_put(id, user, visualization=visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **visualization** | [**Visualization**](Visualization.md)| An old Visualizationto be updated | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visualizations_post**
> Visualization visualizations_post(user, visualization=visualization)

Create a Visualization

Create a new instance of a Visualization

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
api_instance = modelcatalog.VisualizationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
visualization = modelcatalog.Visualization() # Visualization | A new Visualizationto be created (optional)

try:
    # Create a Visualization
    api_response = api_instance.visualizations_post(user, visualization=visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisualizationApi->visualizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **visualization** | [**Visualization**](Visualization.md)| A new Visualizationto be created | [optional] 

### Return type

[**Visualization**](Visualization.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


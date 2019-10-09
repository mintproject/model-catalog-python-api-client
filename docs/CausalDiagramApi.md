# modelcatalog.CausalDiagramApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**causaldiagrams_get**](CausalDiagramApi.md#causaldiagrams_get) | **GET** /causaldiagrams | List all CausalDiagram entities
[**causaldiagrams_id_delete**](CausalDiagramApi.md#causaldiagrams_id_delete) | **DELETE** /causaldiagrams/{id} | Delete a CausalDiagram
[**causaldiagrams_id_get**](CausalDiagramApi.md#causaldiagrams_id_get) | **GET** /causaldiagrams/{id} | Get a CausalDiagram
[**causaldiagrams_id_put**](CausalDiagramApi.md#causaldiagrams_id_put) | **PUT** /causaldiagrams/{id} | Update a CausalDiagram
[**causaldiagrams_post**](CausalDiagramApi.md#causaldiagrams_post) | **POST** /causaldiagrams | Create a CausalDiagram


# **causaldiagrams_get**
> list[CausalDiagram] causaldiagrams_get(username=username, label=label)

List all CausalDiagram entities

Gets a list of all CausalDiagram entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.CausalDiagramApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all CausalDiagram entities
    api_response = api_instance.causaldiagrams_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[CausalDiagram]**](CausalDiagram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **causaldiagrams_id_delete**
> causaldiagrams_id_delete(id, user)

Delete a CausalDiagram

Delete an existing CausalDiagram

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a CausalDiagram
    api_instance.causaldiagrams_id_delete(id, user)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_delete: %s\n" % e)
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

# **causaldiagrams_id_get**
> CausalDiagram causaldiagrams_id_get(id, username=username)

Get a CausalDiagram

Gets the details of a single instance of a CausalDiagram

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.CausalDiagramApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a CausalDiagram
    api_response = api_instance.causaldiagrams_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**CausalDiagram**](CausalDiagram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **causaldiagrams_id_put**
> causaldiagrams_id_put(id, user, causal_diagram=causal_diagram)

Update a CausalDiagram

Updates an existing CausalDiagram

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
causal_diagram = modelcatalog.CausalDiagram() # CausalDiagram | An old CausalDiagramto be updated (optional)

try:
    # Update a CausalDiagram
    api_instance.causaldiagrams_id_put(id, user, causal_diagram=causal_diagram)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **causal_diagram** | [**CausalDiagram**](CausalDiagram.md)| An old CausalDiagramto be updated | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **causaldiagrams_post**
> causaldiagrams_post(user, causal_diagram=causal_diagram)

Create a CausalDiagram

Create a new instance of a CausalDiagram

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
api_instance = modelcatalog.CausalDiagramApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
causal_diagram = modelcatalog.CausalDiagram() # CausalDiagram | A new CausalDiagramto be created (optional)

try:
    # Create a CausalDiagram
    api_instance.causaldiagrams_post(user, causal_diagram=causal_diagram)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **causal_diagram** | [**CausalDiagram**](CausalDiagram.md)| A new CausalDiagramto be created | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


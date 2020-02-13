# modelcatalog.InterventionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interventions_get**](InterventionApi.md#interventions_get) | **GET** /interventions | List all Intervention entities
[**interventions_id_delete**](InterventionApi.md#interventions_id_delete) | **DELETE** /interventions/{id} | Delete a Intervention
[**interventions_id_get**](InterventionApi.md#interventions_id_get) | **GET** /interventions/{id} | Get a Intervention
[**interventions_id_put**](InterventionApi.md#interventions_id_put) | **PUT** /interventions/{id} | Update a Intervention
[**interventions_post**](InterventionApi.md#interventions_post) | **POST** /interventions | Create a Intervention


# **interventions_get**
> list[Intervention] interventions_get(username=username, label=label)

List all Intervention entities

Gets a list of all Intervention entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.InterventionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Intervention entities
    api_response = api_instance.interventions_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[Intervention]**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **interventions_id_delete**
> interventions_id_delete(id, user)

Delete a Intervention

Delete an existing Intervention

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
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Intervention
    api_instance.interventions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_delete: %s\n" % e)
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

# **interventions_id_get**
> Intervention interventions_id_get(id, username=username)

Get a Intervention

Gets the details of a single instance of a Intervention

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.InterventionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Intervention
    api_response = api_instance.interventions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**Intervention**](Intervention.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **interventions_id_put**
> Intervention interventions_id_put(id, user, intervention=intervention)

Update a Intervention

Updates an existing Intervention

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
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
intervention = modelcatalog.Intervention() # Intervention | An old Interventionto be updated (optional)

try:
    # Update a Intervention
    api_response = api_instance.interventions_id_put(id, user, intervention=intervention)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **intervention** | [**Intervention**](Intervention.md)| An old Interventionto be updated | [optional] 

### Return type

[**Intervention**](Intervention.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **interventions_post**
> Intervention interventions_post(user, intervention=intervention)

Create a Intervention

Create a new instance of a Intervention

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
api_instance = modelcatalog.InterventionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
intervention = modelcatalog.Intervention() # Intervention | A new Interventionto be created (optional)

try:
    # Create a Intervention
    api_response = api_instance.interventions_post(user, intervention=intervention)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterventionApi->interventions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **intervention** | [**Intervention**](Intervention.md)| A new Interventionto be created | [optional] 

### Return type

[**Intervention**](Intervention.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


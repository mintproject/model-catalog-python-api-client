# modelcatalog.TheoryGuidedModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**theory_guidedmodels_get**](TheoryGuidedModelApi.md#theory_guidedmodels_get) | **GET** /theory-guidedmodels | List all Theory-GuidedModel entities
[**theory_guidedmodels_id_delete**](TheoryGuidedModelApi.md#theory_guidedmodels_id_delete) | **DELETE** /theory-guidedmodels/{id} | Delete a Theory-GuidedModel
[**theory_guidedmodels_id_get**](TheoryGuidedModelApi.md#theory_guidedmodels_id_get) | **GET** /theory-guidedmodels/{id} | Get a Theory-GuidedModel
[**theory_guidedmodels_id_put**](TheoryGuidedModelApi.md#theory_guidedmodels_id_put) | **PUT** /theory-guidedmodels/{id} | Update a Theory-GuidedModel
[**theory_guidedmodels_post**](TheoryGuidedModelApi.md#theory_guidedmodels_post) | **POST** /theory-guidedmodels | Create a Theory-GuidedModel


# **theory_guidedmodels_get**
> list[TheoryGuidedModel] theory_guidedmodels_get(username=username, label=label)

List all Theory-GuidedModel entities

Gets a list of all Theory-GuidedModel entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all Theory-GuidedModel entities
    api_response = api_instance.theory_guidedmodels_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[TheoryGuidedModel]**](TheoryGuidedModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **theory_guidedmodels_id_delete**
> theory_guidedmodels_id_delete(id, user)

Delete a Theory-GuidedModel

Delete an existing Theory-GuidedModel

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
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a Theory-GuidedModel
    api_instance.theory_guidedmodels_id_delete(id, user)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_delete: %s\n" % e)
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

# **theory_guidedmodels_id_get**
> TheoryGuidedModel theory_guidedmodels_id_get(id, username=username)

Get a Theory-GuidedModel

Gets the details of a single instance of a Theory-GuidedModel

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **theory_guidedmodels_id_put**
> TheoryGuidedModel theory_guidedmodels_id_put(id, user, theory_guided_model=theory_guided_model)

Update a Theory-GuidedModel

Updates an existing Theory-GuidedModel

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
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
theory_guided_model = modelcatalog.TheoryGuidedModel() # TheoryGuidedModel | An old Theory-GuidedModelto be updated (optional)

try:
    # Update a Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_id_put(id, user, theory_guided_model=theory_guided_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **theory_guided_model** | [**TheoryGuidedModel**](TheoryGuidedModel.md)| An old Theory-GuidedModelto be updated | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **theory_guidedmodels_post**
> TheoryGuidedModel theory_guidedmodels_post(user, theory_guided_model=theory_guided_model)

Create a Theory-GuidedModel

Create a new instance of a Theory-GuidedModel

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
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
theory_guided_model = modelcatalog.TheoryGuidedModel() # TheoryGuidedModel | A new Theory-GuidedModelto be created (optional)

try:
    # Create a Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_post(user, theory_guided_model=theory_guided_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **theory_guided_model** | [**TheoryGuidedModel**](TheoryGuidedModel.md)| A new Theory-GuidedModelto be created | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


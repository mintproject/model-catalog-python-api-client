# modelcatalog.TheoryGuidedModelApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**theory_guidedmodels_get**](TheoryGuidedModelApi.md#theory_guidedmodels_get) | **GET** /theory-guidedmodels | List all instances of Theory-GuidedModel
[**theory_guidedmodels_id_delete**](TheoryGuidedModelApi.md#theory_guidedmodels_id_delete) | **DELETE** /theory-guidedmodels/{id} | Delete an existing Theory-GuidedModel
[**theory_guidedmodels_id_get**](TheoryGuidedModelApi.md#theory_guidedmodels_id_get) | **GET** /theory-guidedmodels/{id} | Get a single Theory-GuidedModel by its id
[**theory_guidedmodels_id_put**](TheoryGuidedModelApi.md#theory_guidedmodels_id_put) | **PUT** /theory-guidedmodels/{id} | Update an existing Theory-GuidedModel
[**theory_guidedmodels_post**](TheoryGuidedModelApi.md#theory_guidedmodels_post) | **POST** /theory-guidedmodels | Create one Theory-GuidedModel


# **theory_guidedmodels_get**
> list[TheoryGuidedModel] theory_guidedmodels_get(username=username, label=label, page=page, per_page=per_page)

List all instances of Theory-GuidedModel

Gets a list of all instances of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[TheoryGuidedModel]**](TheoryGuidedModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Theory-GuidedModel. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **theory_guidedmodels_id_delete**
> theory_guidedmodels_id_delete(id, user=user)

Delete an existing Theory-GuidedModel

Delete an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Theory-GuidedModel to be retrieved
user = 'user_example' # str | Username (optional)

try:
    # Delete an existing Theory-GuidedModel
    api_instance.theory_guidedmodels_id_delete(id, user=user)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Theory-GuidedModel to be retrieved | 
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

# **theory_guidedmodels_id_get**
> TheoryGuidedModel theory_guidedmodels_id_get(id, username=username)

Get a single Theory-GuidedModel by its id

Gets the details of a given Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi()
id = 'id_example' # str | The ID of the Theory-GuidedModel to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single Theory-GuidedModel by its id
    api_response = api_instance.theory_guidedmodels_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Theory-GuidedModel to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Theory-GuidedModel |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **theory_guidedmodels_id_put**
> TheoryGuidedModel theory_guidedmodels_id_put(id, user=user, theory_guided_model=theory_guided_model)

Update an existing Theory-GuidedModel

Updates an existing Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the Theory-GuidedModel to be retrieved
user = 'user_example' # str | Username (optional)
theory_guided_model = modelcatalog.TheoryGuidedModel() # TheoryGuidedModel | An old Theory-GuidedModelto be updated (optional)

try:
    # Update an existing Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_id_put(id, user=user, theory_guided_model=theory_guided_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Theory-GuidedModel to be retrieved | 
 **user** | **str**| Username | [optional] 
 **theory_guided_model** | [**TheoryGuidedModel**](TheoryGuidedModel.md)| An old Theory-GuidedModelto be updated | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

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

# **theory_guidedmodels_post**
> TheoryGuidedModel theory_guidedmodels_post(user=user, theory_guided_model=theory_guided_model)

Create one Theory-GuidedModel

Create a new instance of Theory-GuidedModel (more information in https://w3id.org/okn/o/sdm#Theory-GuidedModel)

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

# Defining host is optional and default to https://api.models.mint.isi.edu/v1.7.0
configuration.host = "https://api.models.mint.isi.edu/v1.7.0"
# Create an instance of the API class
api_instance = modelcatalog.TheoryGuidedModelApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username (optional)
theory_guided_model = modelcatalog.TheoryGuidedModel() # TheoryGuidedModel | Information about the Theory-GuidedModelto be created (optional)

try:
    # Create one Theory-GuidedModel
    api_response = api_instance.theory_guidedmodels_post(user=user, theory_guided_model=theory_guided_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TheoryGuidedModelApi->theory_guidedmodels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | [optional] 
 **theory_guided_model** | [**TheoryGuidedModel**](TheoryGuidedModel.md)| Information about the Theory-GuidedModelto be created | [optional] 

### Return type

[**TheoryGuidedModel**](TheoryGuidedModel.md)

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


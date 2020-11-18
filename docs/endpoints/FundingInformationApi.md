# modelcatalog.FundingInformationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.6.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fundinginformations_get**](FundingInformationApi.md#fundinginformations_get) | **GET** /fundinginformations | List all instances of FundingInformation
[**fundinginformations_id_delete**](FundingInformationApi.md#fundinginformations_id_delete) | **DELETE** /fundinginformations/{id} | Delete an existing FundingInformation
[**fundinginformations_id_get**](FundingInformationApi.md#fundinginformations_id_get) | **GET** /fundinginformations/{id} | Get a single FundingInformation by its id
[**fundinginformations_id_put**](FundingInformationApi.md#fundinginformations_id_put) | **PUT** /fundinginformations/{id} | Update an existing FundingInformation
[**fundinginformations_post**](FundingInformationApi.md#fundinginformations_post) | **POST** /fundinginformations | Create one FundingInformation


# **fundinginformations_get**
> list[FundingInformation] fundinginformations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of FundingInformation

Gets a list of all instances of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.FundingInformationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of FundingInformation
    api_response = api_instance.fundinginformations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[FundingInformation]**](FundingInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of FundingInformation. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **fundinginformations_id_delete**
> fundinginformations_id_delete(id, user)

Delete an existing FundingInformation

Delete an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the FundingInformation to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing FundingInformation
    api_instance.fundinginformations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FundingInformation to be retrieved | 
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

# **fundinginformations_id_get**
> FundingInformation fundinginformations_id_get(id, username=username)

Get a single FundingInformation by its id

Gets the details of a given FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.FundingInformationApi()
id = 'id_example' # str | The ID of the FundingInformation to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single FundingInformation by its id
    api_response = api_instance.fundinginformations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FundingInformation to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given FundingInformation |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **fundinginformations_id_put**
> FundingInformation fundinginformations_id_put(id, user, funding_information=funding_information)

Update an existing FundingInformation

Updates an existing FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the FundingInformation to be retrieved
user = 'user_example' # str | Username
funding_information = modelcatalog.FundingInformation() # FundingInformation | An old FundingInformationto be updated (optional)

try:
    # Update an existing FundingInformation
    api_response = api_instance.fundinginformations_id_put(id, user, funding_information=funding_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FundingInformation to be retrieved | 
 **user** | **str**| Username | 
 **funding_information** | [**FundingInformation**](FundingInformation.md)| An old FundingInformationto be updated | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

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

# **fundinginformations_post**
> FundingInformation fundinginformations_post(user, funding_information=funding_information)

Create one FundingInformation

Create a new instance of FundingInformation (more information in https://w3id.org/okn/o/sd#FundingInformation)

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
funding_information = modelcatalog.FundingInformation() # FundingInformation | Information about the FundingInformationto be created (optional)

try:
    # Create one FundingInformation
    api_response = api_instance.fundinginformations_post(user, funding_information=funding_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **funding_information** | [**FundingInformation**](FundingInformation.md)| Information about the FundingInformationto be created | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

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


# modelcatalog.FundingInformationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fundinginformations_get**](FundingInformationApi.md#fundinginformations_get) | **GET** /fundinginformations | List all FundingInformation entities
[**fundinginformations_id_delete**](FundingInformationApi.md#fundinginformations_id_delete) | **DELETE** /fundinginformations/{id} | Delete a FundingInformation
[**fundinginformations_id_get**](FundingInformationApi.md#fundinginformations_id_get) | **GET** /fundinginformations/{id} | Get a FundingInformation
[**fundinginformations_id_put**](FundingInformationApi.md#fundinginformations_id_put) | **PUT** /fundinginformations/{id} | Update a FundingInformation
[**fundinginformations_post**](FundingInformationApi.md#fundinginformations_post) | **POST** /fundinginformations | Create a FundingInformation


# **fundinginformations_get**
> list[FundingInformation] fundinginformations_get(username=username, label=label)

List all FundingInformation entities

Gets a list of all FundingInformation entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.FundingInformationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all FundingInformation entities
    api_response = api_instance.fundinginformations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[FundingInformation]**](FundingInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fundinginformations_id_delete**
> fundinginformations_id_delete(id, user)

Delete a FundingInformation

Delete an existing FundingInformation

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a FundingInformation
    api_instance.fundinginformations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_delete: %s\n" % e)
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

# **fundinginformations_id_get**
> FundingInformation fundinginformations_id_get(id, username=username)

Get a FundingInformation

Gets the details of a single instance of a FundingInformation

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.FundingInformationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a FundingInformation
    api_response = api_instance.fundinginformations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fundinginformations_id_put**
> FundingInformation fundinginformations_id_put(id, user, funding_information=funding_information)

Update a FundingInformation

Updates an existing FundingInformation

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
funding_information = modelcatalog.FundingInformation() # FundingInformation | An old FundingInformationto be updated (optional)

try:
    # Update a FundingInformation
    api_response = api_instance.fundinginformations_id_put(id, user, funding_information=funding_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **funding_information** | [**FundingInformation**](FundingInformation.md)| An old FundingInformationto be updated | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fundinginformations_post**
> FundingInformation fundinginformations_post(user, funding_information=funding_information)

Create a FundingInformation

Create a new instance of a FundingInformation

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
api_instance = modelcatalog.FundingInformationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
funding_information = modelcatalog.FundingInformation() # FundingInformation | A new FundingInformationto be created (optional)

try:
    # Create a FundingInformation
    api_response = api_instance.fundinginformations_post(user, funding_information=funding_information)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingInformationApi->fundinginformations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **funding_information** | [**FundingInformation**](FundingInformation.md)| A new FundingInformationto be created | [optional] 

### Return type

[**FundingInformation**](FundingInformation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


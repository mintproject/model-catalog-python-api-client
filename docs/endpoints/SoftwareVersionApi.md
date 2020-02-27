# modelcatalog.SoftwareVersionApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareversions_get**](SoftwareVersionApi.md#softwareversions_get) | **GET** /softwareversions | List all SoftwareVersion entities
[**softwareversions_id_delete**](SoftwareVersionApi.md#softwareversions_id_delete) | **DELETE** /softwareversions/{id} | Delete a SoftwareVersion
[**softwareversions_id_get**](SoftwareVersionApi.md#softwareversions_id_get) | **GET** /softwareversions/{id} | Get a SoftwareVersion
[**softwareversions_id_put**](SoftwareVersionApi.md#softwareversions_id_put) | **PUT** /softwareversions/{id} | Update a SoftwareVersion
[**softwareversions_post**](SoftwareVersionApi.md#softwareversions_post) | **POST** /softwareversions | Create a SoftwareVersion


# **softwareversions_get**
> list[SoftwareVersion] softwareversions_get(username=username, label=label)

List all SoftwareVersion entities

Gets a list of all SoftwareVersion entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareVersionApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SoftwareVersion entities
    api_response = api_instance.softwareversions_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SoftwareVersion]**](SoftwareVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareversions_id_delete**
> softwareversions_id_delete(id, user)

Delete a SoftwareVersion

Delete an existing SoftwareVersion

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SoftwareVersion
    api_instance.softwareversions_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_delete: %s\n" % e)
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

# **softwareversions_id_get**
> SoftwareVersion softwareversions_id_get(id, username=username)

Get a SoftwareVersion

Gets the details of a single instance of a SoftwareVersion

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareVersionApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SoftwareVersion
    api_response = api_instance.softwareversions_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareversions_id_put**
> SoftwareVersion softwareversions_id_put(id, user, software_version=software_version)

Update a SoftwareVersion

Updates an existing SoftwareVersion

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
software_version = modelcatalog.SoftwareVersion() # SoftwareVersion | An old SoftwareVersionto be updated (optional)

try:
    # Update a SoftwareVersion
    api_response = api_instance.softwareversions_id_put(id, user, software_version=software_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **software_version** | [**SoftwareVersion**](SoftwareVersion.md)| An old SoftwareVersionto be updated | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareversions_post**
> SoftwareVersion softwareversions_post(user, software_version=software_version)

Create a SoftwareVersion

Create a new instance of a SoftwareVersion

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
api_instance = modelcatalog.SoftwareVersionApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
software_version = modelcatalog.SoftwareVersion() # SoftwareVersion | A new SoftwareVersionto be created (optional)

try:
    # Create a SoftwareVersion
    api_response = api_instance.softwareversions_post(user, software_version=software_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareVersionApi->softwareversions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software_version** | [**SoftwareVersion**](SoftwareVersion.md)| A new SoftwareVersionto be created | [optional] 

### Return type

[**SoftwareVersion**](SoftwareVersion.md)

### Authorization

[BearerAuth](../#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


# modelcatalog.SoftwareConfigurationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareconfigurations_get**](SoftwareConfigurationApi.md#softwareconfigurations_get) | **GET** /softwareconfigurations | List all SoftwareConfiguration entities
[**softwareconfigurations_id_delete**](SoftwareConfigurationApi.md#softwareconfigurations_id_delete) | **DELETE** /softwareconfigurations/{id} | Delete a SoftwareConfiguration
[**softwareconfigurations_id_get**](SoftwareConfigurationApi.md#softwareconfigurations_id_get) | **GET** /softwareconfigurations/{id} | Get a SoftwareConfiguration
[**softwareconfigurations_id_put**](SoftwareConfigurationApi.md#softwareconfigurations_id_put) | **PUT** /softwareconfigurations/{id} | Update a SoftwareConfiguration
[**softwareconfigurations_post**](SoftwareConfigurationApi.md#softwareconfigurations_post) | **POST** /softwareconfigurations | Create a SoftwareConfiguration


# **softwareconfigurations_get**
> list[SoftwareConfiguration] softwareconfigurations_get(username=username, label=label)

List all SoftwareConfiguration entities

Gets a list of all SoftwareConfiguration entities

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareConfigurationApi()
username = 'username_example' # str | Username to query (optional)
label = 'label_example' # str | Filter by label (optional)

try:
    # List all SoftwareConfiguration entities
    api_response = api_instance.softwareconfigurations_get(username=username, label=label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username to query | [optional] 
 **label** | **str**| Filter by label | [optional] 

### Return type

[**list[SoftwareConfiguration]**](SoftwareConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareconfigurations_id_delete**
> softwareconfigurations_id_delete(id, user)

Delete a SoftwareConfiguration

Delete an existing SoftwareConfiguration

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username

try:
    # Delete a SoftwareConfiguration
    api_instance.softwareconfigurations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_delete: %s\n" % e)
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

# **softwareconfigurations_id_get**
> SoftwareConfiguration softwareconfigurations_id_get(id, username=username)

Get a SoftwareConfiguration

Gets the details of a single instance of a SoftwareConfiguration

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.SoftwareConfigurationApi()
id = 'id_example' # str | The ID of the resource
username = 'username_example' # str | Username to query (optional)

try:
    # Get a SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **username** | **str**| Username to query | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareconfigurations_id_put**
> SoftwareConfiguration softwareconfigurations_id_put(id, user, software_configuration=software_configuration)

Update a SoftwareConfiguration

Updates an existing SoftwareConfiguration

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the resource
user = 'user_example' # str | Username
software_configuration = modelcatalog.SoftwareConfiguration() # SoftwareConfiguration | An old SoftwareConfigurationto be updated (optional)

try:
    # Update a SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_id_put(id, user, software_configuration=software_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the resource | 
 **user** | **str**| Username | 
 **software_configuration** | [**SoftwareConfiguration**](SoftwareConfiguration.md)| An old SoftwareConfigurationto be updated | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **softwareconfigurations_post**
> SoftwareConfiguration softwareconfigurations_post(user, software_configuration=software_configuration)

Create a SoftwareConfiguration

Create a new instance of a SoftwareConfiguration

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
software_configuration = modelcatalog.SoftwareConfiguration() # SoftwareConfiguration | A new SoftwareConfigurationto be created (optional)

try:
    # Create a SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_post(user, software_configuration=software_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software_configuration** | [**SoftwareConfiguration**](SoftwareConfiguration.md)| A new SoftwareConfigurationto be created | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


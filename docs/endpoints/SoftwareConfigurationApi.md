# modelcatalog.SoftwareConfigurationApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.5.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareconfigurations_get**](SoftwareConfigurationApi.md#softwareconfigurations_get) | **GET** /softwareconfigurations | List all instances of SoftwareConfiguration
[**softwareconfigurations_id_delete**](SoftwareConfigurationApi.md#softwareconfigurations_id_delete) | **DELETE** /softwareconfigurations/{id} | Delete an existing SoftwareConfiguration
[**softwareconfigurations_id_get**](SoftwareConfigurationApi.md#softwareconfigurations_id_get) | **GET** /softwareconfigurations/{id} | Get a single SoftwareConfiguration by its id
[**softwareconfigurations_id_put**](SoftwareConfigurationApi.md#softwareconfigurations_id_put) | **PUT** /softwareconfigurations/{id} | Update an existing SoftwareConfiguration
[**softwareconfigurations_post**](SoftwareConfigurationApi.md#softwareconfigurations_post) | **POST** /softwareconfigurations | Create one SoftwareConfiguration


# **softwareconfigurations_get**
> list[SoftwareConfiguration] softwareconfigurations_get(username=username, label=label, page=page, per_page=per_page)

List all instances of SoftwareConfiguration

Gets a list of all instances of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareConfigurationApi()
username = 'username_example' # str | Name of the user graph to query (optional)
label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

try:
    # List all instances of SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_get(username=username, label=label, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Name of the user graph to query | [optional] 
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SoftwareConfiguration]**](SoftwareConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SoftwareConfiguration. |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareconfigurations_id_delete**
> softwareconfigurations_id_delete(id, user)

Delete an existing SoftwareConfiguration

Delete an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareConfiguration to be retrieved
user = 'user_example' # str | Username

try:
    # Delete an existing SoftwareConfiguration
    api_instance.softwareconfigurations_id_delete(id, user)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareConfiguration to be retrieved | 
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

# **softwareconfigurations_id_get**
> SoftwareConfiguration softwareconfigurations_id_get(id, username=username)

Get a single SoftwareConfiguration by its id

Gets the details of a given SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.SoftwareConfigurationApi()
id = 'id_example' # str | The ID of the SoftwareConfiguration to be retrieved
username = 'username_example' # str | Name of the user graph to query (optional)

try:
    # Get a single SoftwareConfiguration by its id
    api_response = api_instance.softwareconfigurations_id_get(id, username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareConfiguration to be retrieved | 
 **username** | **str**| Name of the user graph to query | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SoftwareConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **softwareconfigurations_id_put**
> SoftwareConfiguration softwareconfigurations_id_put(id, user, software_configuration=software_configuration)

Update an existing SoftwareConfiguration

Updates an existing SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
id = 'id_example' # str | The ID of the SoftwareConfiguration to be retrieved
user = 'user_example' # str | Username
software_configuration = modelcatalog.SoftwareConfiguration() # SoftwareConfiguration | An old SoftwareConfigurationto be updated (optional)

try:
    # Update an existing SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_id_put(id, user, software_configuration=software_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SoftwareConfiguration to be retrieved | 
 **user** | **str**| Username | 
 **software_configuration** | [**SoftwareConfiguration**](SoftwareConfiguration.md)| An old SoftwareConfigurationto be updated | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

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

# **softwareconfigurations_post**
> SoftwareConfiguration softwareconfigurations_post(user, software_configuration=software_configuration)

Create one SoftwareConfiguration

Create a new instance of SoftwareConfiguration (more information in https://w3id.org/okn/o/sd#SoftwareConfiguration)

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
api_instance = modelcatalog.SoftwareConfigurationApi(modelcatalog.ApiClient(configuration))
user = 'user_example' # str | Username
software_configuration = modelcatalog.SoftwareConfiguration() # SoftwareConfiguration | Information about the SoftwareConfigurationto be created (optional)

try:
    # Create one SoftwareConfiguration
    api_response = api_instance.softwareconfigurations_post(user, software_configuration=software_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareConfigurationApi->softwareconfigurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Username | 
 **software_configuration** | [**SoftwareConfiguration**](SoftwareConfiguration.md)| Information about the SoftwareConfigurationto be created | [optional] 

### Return type

[**SoftwareConfiguration**](SoftwareConfiguration.md)

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


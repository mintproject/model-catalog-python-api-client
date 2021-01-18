# modelcatalog.DefaultApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.7.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_login_post**](DefaultApi.md#user_login_post) | **POST** /user/login | 


# **user_login_post**
> str user_login_post(user=user)



Login the user

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = modelcatalog.DefaultApi()
user = modelcatalog.User() # User | User credentials (optional)

try:
    api_response = api_instance.user_login_post(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| User credentials | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * X-Rate-Limit - calls per hour allowed by the user <br>  * X-Expires-After - date in UTC when token expires <br>  |
**400** | unsuccessful operation |  -  |

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)


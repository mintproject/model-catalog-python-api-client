# modelcatalog.DefaultApi

All URIs are relative to *https://api.models.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_login_get**](DefaultApi.md#user_login_get) | **GET** /user/login | 


# **user_login_get**
> str user_login_get(username, password)



Login the user

### Example

```python
from __future__ import print_function
import time
import modelcatalog
from modelcatalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = modelcatalog.DefaultApi()
username = 'username_example' # str | The user name for login
password = 'password_example' # str | The password for login in clear text

try:
    api_response = api_instance.user_login_get(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name for login | 
 **password** | **str**| The password for login in clear text | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


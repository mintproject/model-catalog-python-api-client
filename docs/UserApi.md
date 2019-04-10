# openapi_client.UserApi

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /user | Create user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
[**get_user_by_name**](UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
[**login_user**](UserApi.md#login_user) | **GET** /user/login | Logs user into the system
[**logout_user**](UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
[**update_user**](UserApi.md#update_user) | **PUT** /user/{username} | Updated user


# **create_user**
> create_user(user)

Create user

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()
user = openapi_client.User() # User | Created user object

try:
    # Create user
    api_instance.create_user(user)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| Created user object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

Delete user

This can only be done by the logged in user.

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()
username = 'username_example' # str | The name that needs to be deleted

try:
    # Delete user
    api_instance.delete_user(username)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_name**
> User get_user_by_name(username)

Get user by user name

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()
username = 'username_example' # str | The name that needs to be fetched. Use user1 for testing.

try:
    # Get user by user name
    api_response = api_instance.get_user_by_name(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be fetched. Use user1 for testing. | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user**
> str login_user(username, password)

Logs user into the system

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()
username = 'username_example' # str | The user name for login
password = 'password_example' # str | The password for login in clear text

try:
    # Logs user into the system
    api_response = api_instance.login_user(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login_user: %s\n" % e)
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
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> logout_user()

Logs out current logged in user session

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UserApi()

try:
    # Logs out current logged in user session
    api_instance.logout_user()
except ApiException as e:
    print("Exception when calling UserApi->logout_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(username, user)

Updated user

This can only be done by the logged in user.

### Example

* Basic Authentication (BearerAuth): 
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BearerAuth
configuration = openapi_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = openapi_client.UserApi(openapi_client.ApiClient(configuration))
username = 'username_example' # str | name that need to be updated
user = openapi_client.User() # User | Updated user object

try:
    # Updated user
    api_instance.update_user(username, user)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| name that need to be updated | 
 **user** | [**User**](User.md)| Updated user object | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


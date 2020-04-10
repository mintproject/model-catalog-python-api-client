# coding: utf-8

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from modelcatalog.api_client import ApiClient
from modelcatalog.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_login_get(self, username, password, **kwargs):  # noqa: E501
        """user_login_get  # noqa: E501

        Login the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login_get(username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.user_login_get_with_http_info(username, password, **kwargs)  # noqa: E501

    def user_login_get_with_http_info(self, username, password, **kwargs):  # noqa: E501
        """user_login_get  # noqa: E501

        Login the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login_get_with_http_info(username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_login_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ApiValueError("Missing the required parameter `username` when calling `user_login_get`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ApiValueError("Missing the required parameter `password` when calling `user_login_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/login', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

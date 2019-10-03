# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mint_client.api_client import ApiClient
from mint_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SampleResourceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sampleresources_get(self, **kwargs):  # noqa: E501
        """List all SampleResource entities  # noqa: E501

        Gets a list of all SampleResource entities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username to query
        :return: list[SampleResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sampleresources_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sampleresources_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def sampleresources_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all SampleResource entities  # noqa: E501

        Gets a list of all SampleResource entities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username to query
        :return: list[SampleResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sampleresources_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

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
            '/sampleresources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SampleResource]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sampleresources_id_delete(self, id, user, **kwargs):  # noqa: E501
        """Delete a SampleResource  # noqa: E501

        Delete an existing SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_delete(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sampleresources_id_delete_with_http_info(id, user, **kwargs)  # noqa: E501
        else:
            (data) = self.sampleresources_id_delete_with_http_info(id, user, **kwargs)  # noqa: E501
            return data

    def sampleresources_id_delete_with_http_info(self, id, user, **kwargs):  # noqa: E501
        """Delete a SampleResource  # noqa: E501

        Delete an existing SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_delete_with_http_info(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sampleresources_id_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `sampleresources_id_delete`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `sampleresources_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'user' in local_var_params:
            path_params['user'] = local_var_params['user']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sampleresources/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sampleresources_id_get(self, id, **kwargs):  # noqa: E501
        """Get a SampleResource  # noqa: E501

        Gets the details of a single instance of a SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str username: Username to query
        :return: SampleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sampleresources_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.sampleresources_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def sampleresources_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a SampleResource  # noqa: E501

        Gets the details of a single instance of a SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str username: Username to query
        :return: SampleResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sampleresources_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `sampleresources_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501

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
            '/sampleresources/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SampleResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sampleresources_id_put(self, id, user, **kwargs):  # noqa: E501
        """Update a SampleResource  # noqa: E501

        Updates an existing SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_put(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :param SampleResource sample_resource: An old SampleResourceto be updated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sampleresources_id_put_with_http_info(id, user, **kwargs)  # noqa: E501
        else:
            (data) = self.sampleresources_id_put_with_http_info(id, user, **kwargs)  # noqa: E501
            return data

    def sampleresources_id_put_with_http_info(self, id, user, **kwargs):  # noqa: E501
        """Update a SampleResource  # noqa: E501

        Updates an existing SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_id_put_with_http_info(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :param SampleResource sample_resource: An old SampleResourceto be updated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'user', 'sample_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sampleresources_id_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `sampleresources_id_put`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `sampleresources_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'user' in local_var_params:
            path_params['user'] = local_var_params['user']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sample_resource' in local_var_params:
            body_params = local_var_params['sample_resource']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sampleresources/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sampleresources_post(self, user, **kwargs):  # noqa: E501
        """Create a SampleResource  # noqa: E501

        Create a new instance of a SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_post(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: Username (required)
        :param SampleResource sample_resource: A new SampleResourceto be created
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sampleresources_post_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.sampleresources_post_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def sampleresources_post_with_http_info(self, user, **kwargs):  # noqa: E501
        """Create a SampleResource  # noqa: E501

        Create a new instance of a SampleResource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sampleresources_post_with_http_info(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: Username (required)
        :param SampleResource sample_resource: A new SampleResourceto be created
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user', 'sample_resource']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sampleresources_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `sampleresources_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user' in local_var_params:
            path_params['user'] = local_var_params['user']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sample_resource' in local_var_params:
            body_params = local_var_params['sample_resource']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sampleresources', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

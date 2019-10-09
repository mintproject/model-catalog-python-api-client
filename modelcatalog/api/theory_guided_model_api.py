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

from modelcatalog.api_client import ApiClient
from modelcatalog.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TheoryGuidedModelApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def theory_guidedmodels_get(self, **kwargs):  # noqa: E501
        """List all Theory-GuidedModel entities  # noqa: E501

        Gets a list of all Theory-GuidedModel entities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username to query
        :param str label: Filter by label
        :return: list[TheoryGuidedModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.theory_guidedmodels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.theory_guidedmodels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def theory_guidedmodels_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all Theory-GuidedModel entities  # noqa: E501

        Gets a list of all Theory-GuidedModel entities  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username to query
        :param str label: Filter by label
        :return: list[TheoryGuidedModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'label']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method theory_guidedmodels_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))  # noqa: E501

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
            '/theory-guidedmodels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TheoryGuidedModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def theory_guidedmodels_id_delete(self, id, user, **kwargs):  # noqa: E501
        """Delete a Theory-GuidedModel  # noqa: E501

        Delete an existing Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_delete(id, user, async_req=True)
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
            return self.theory_guidedmodels_id_delete_with_http_info(id, user, **kwargs)  # noqa: E501
        else:
            (data) = self.theory_guidedmodels_id_delete_with_http_info(id, user, **kwargs)  # noqa: E501
            return data

    def theory_guidedmodels_id_delete_with_http_info(self, id, user, **kwargs):  # noqa: E501
        """Delete a Theory-GuidedModel  # noqa: E501

        Delete an existing Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_delete_with_http_info(id, user, async_req=True)
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
                    " to method theory_guidedmodels_id_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `theory_guidedmodels_id_delete`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `theory_guidedmodels_id_delete`")  # noqa: E501

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
            '/theory-guidedmodels/{id}', 'DELETE',
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

    def theory_guidedmodels_id_get(self, id, **kwargs):  # noqa: E501
        """Get a Theory-GuidedModel  # noqa: E501

        Gets the details of a single instance of a Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str username: Username to query
        :return: TheoryGuidedModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.theory_guidedmodels_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.theory_guidedmodels_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def theory_guidedmodels_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a Theory-GuidedModel  # noqa: E501

        Gets the details of a single instance of a Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str username: Username to query
        :return: TheoryGuidedModel
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
                    " to method theory_guidedmodels_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `theory_guidedmodels_id_get`")  # noqa: E501

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
            '/theory-guidedmodels/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TheoryGuidedModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def theory_guidedmodels_id_put(self, id, user, **kwargs):  # noqa: E501
        """Update a Theory-GuidedModel  # noqa: E501

        Updates an existing Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_put(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :param TheoryGuidedModel theory_guided_model: An old Theory-GuidedModelto be updated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.theory_guidedmodels_id_put_with_http_info(id, user, **kwargs)  # noqa: E501
        else:
            (data) = self.theory_guidedmodels_id_put_with_http_info(id, user, **kwargs)  # noqa: E501
            return data

    def theory_guidedmodels_id_put_with_http_info(self, id, user, **kwargs):  # noqa: E501
        """Update a Theory-GuidedModel  # noqa: E501

        Updates an existing Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_id_put_with_http_info(id, user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the resource (required)
        :param str user: Username (required)
        :param TheoryGuidedModel theory_guided_model: An old Theory-GuidedModelto be updated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'user', 'theory_guided_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method theory_guidedmodels_id_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `theory_guidedmodels_id_put`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `theory_guidedmodels_id_put`")  # noqa: E501

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
        if 'theory_guided_model' in local_var_params:
            body_params = local_var_params['theory_guided_model']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/theory-guidedmodels/{id}', 'PUT',
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

    def theory_guidedmodels_post(self, user, **kwargs):  # noqa: E501
        """Create a Theory-GuidedModel  # noqa: E501

        Create a new instance of a Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_post(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: Username (required)
        :param TheoryGuidedModel theory_guided_model: A new Theory-GuidedModelto be created
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.theory_guidedmodels_post_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.theory_guidedmodels_post_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def theory_guidedmodels_post_with_http_info(self, user, **kwargs):  # noqa: E501
        """Create a Theory-GuidedModel  # noqa: E501

        Create a new instance of a Theory-GuidedModel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.theory_guidedmodels_post_with_http_info(user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user: Username (required)
        :param TheoryGuidedModel theory_guided_model: A new Theory-GuidedModelto be created
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user', 'theory_guided_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method theory_guidedmodels_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ApiValueError("Missing the required parameter `user` when calling `theory_guidedmodels_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user' in local_var_params:
            path_params['user'] = local_var_params['user']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'theory_guided_model' in local_var_params:
            body_params = local_var_params['theory_guided_model']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/theory-guidedmodels', 'POST',
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

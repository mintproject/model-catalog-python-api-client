# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mint_client
from mint_client.api.standard_variable_api import StandardVariableApi  # noqa: E501
from mint_client.rest import ApiException


class TestStandardVariableApi(unittest.TestCase):
    """StandardVariableApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.standard_variable_api.StandardVariableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_standardvariables_get(self):
        """Test case for standardvariables_get

        List all StandardVariable entities  # noqa: E501
        """
        pass

    def test_standardvariables_id_delete(self):
        """Test case for standardvariables_id_delete

        Delete a StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_id_get(self):
        """Test case for standardvariables_id_get

        Get a StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_id_put(self):
        """Test case for standardvariables_id_put

        Update a StandardVariable  # noqa: E501
        """
        pass

    def test_standardvariables_post(self):
        """Test case for standardvariables_post

        Create a StandardVariable  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

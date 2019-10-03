# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.variable_presentation_api import VariablePresentationApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestVariablePresentationApi(unittest.TestCase):
    """VariablePresentationApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.variable_presentation_api.VariablePresentationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_variablepresentations_get(self):
        """Test case for variablepresentations_get

        List all VariablePresentation entities  # noqa: E501
        """
        pass

    def test_variablepresentations_id_delete(self):
        """Test case for variablepresentations_id_delete

        Delete a VariablePresentation  # noqa: E501
        """
        pass

    def test_variablepresentations_id_get(self):
        """Test case for variablepresentations_id_get

        Get a VariablePresentation  # noqa: E501
        """
        pass

    def test_variablepresentations_id_put(self):
        """Test case for variablepresentations_id_put

        Update a VariablePresentation  # noqa: E501
        """
        pass

    def test_variablepresentations_post(self):
        """Test case for variablepresentations_post

        Create a VariablePresentation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

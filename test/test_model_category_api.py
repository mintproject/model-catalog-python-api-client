# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.model_category_api import ModelCategoryApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestModelCategoryApi(unittest.TestCase):
    """ModelCategoryApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.model_category_api.ModelCategoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_modelcategorys_get(self):
        """Test case for modelcategorys_get

        List all instances of ModelCategory  # noqa: E501
        """
        pass

    def test_modelcategorys_id_delete(self):
        """Test case for modelcategorys_id_delete

        Delete an existing ModelCategory  # noqa: E501
        """
        pass

    def test_modelcategorys_id_get(self):
        """Test case for modelcategorys_id_get

        Get a single ModelCategory by its id  # noqa: E501
        """
        pass

    def test_modelcategorys_id_put(self):
        """Test case for modelcategorys_id_put

        Update an existing ModelCategory  # noqa: E501
        """
        pass

    def test_modelcategorys_post(self):
        """Test case for modelcategorys_post

        Create one ModelCategory  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
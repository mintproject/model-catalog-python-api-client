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
from mint_client.api.person_api import PersonApi  # noqa: E501
from mint_client.rest import ApiException


class TestPersonApi(unittest.TestCase):
    """PersonApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.person_api.PersonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_persons_get(self):
        """Test case for persons_get

        List all Person entities  # noqa: E501
        """
        pass

    def test_persons_id_delete(self):
        """Test case for persons_id_delete

        Delete a Person  # noqa: E501
        """
        pass

    def test_persons_id_get(self):
        """Test case for persons_id_get

        Get a Person  # noqa: E501
        """
        pass

    def test_persons_id_put(self):
        """Test case for persons_id_put

        Update a Person  # noqa: E501
        """
        pass

    def test_persons_post(self):
        """Test case for persons_post

        Create a Person  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

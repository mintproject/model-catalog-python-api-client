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
from mint_client.api.organization_api import OrganizationApi  # noqa: E501
from mint_client.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.organization_api.OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organizations_get(self):
        """Test case for organizations_get

        List all Organization entities  # noqa: E501
        """
        pass

    def test_organizations_id_delete(self):
        """Test case for organizations_id_delete

        Delete a Organization  # noqa: E501
        """
        pass

    def test_organizations_id_get(self):
        """Test case for organizations_id_get

        Get a Organization  # noqa: E501
        """
        pass

    def test_organizations_id_put(self):
        """Test case for organizations_id_put

        Update a Organization  # noqa: E501
        """
        pass

    def test_organizations_post(self):
        """Test case for organizations_post

        Create a Organization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
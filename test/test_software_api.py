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
from mint_client.api.software_api import SoftwareApi  # noqa: E501
from mint_client.rest import ApiException


class TestSoftwareApi(unittest.TestCase):
    """SoftwareApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.software_api.SoftwareApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_softwares_get(self):
        """Test case for softwares_get

        List all Software entities  # noqa: E501
        """
        pass

    def test_softwares_id_delete(self):
        """Test case for softwares_id_delete

        Delete a Software  # noqa: E501
        """
        pass

    def test_softwares_id_get(self):
        """Test case for softwares_id_get

        Get a Software  # noqa: E501
        """
        pass

    def test_softwares_id_put(self):
        """Test case for softwares_id_put

        Update a Software  # noqa: E501
        """
        pass

    def test_softwares_post(self):
        """Test case for softwares_post

        Create a Software  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

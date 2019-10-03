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
from mint_client.api.visualization_api import VisualizationApi  # noqa: E501
from mint_client.rest import ApiException


class TestVisualizationApi(unittest.TestCase):
    """VisualizationApi unit test stubs"""

    def setUp(self):
        self.api = mint_client.api.visualization_api.VisualizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_visualizations_get(self):
        """Test case for visualizations_get

        List all Visualization entities  # noqa: E501
        """
        pass

    def test_visualizations_id_delete(self):
        """Test case for visualizations_id_delete

        Delete a Visualization  # noqa: E501
        """
        pass

    def test_visualizations_id_get(self):
        """Test case for visualizations_id_get

        Get a Visualization  # noqa: E501
        """
        pass

    def test_visualizations_id_put(self):
        """Test case for visualizations_id_put

        Update a Visualization  # noqa: E501
        """
        pass

    def test_visualizations_post(self):
        """Test case for visualizations_post

        Create a Visualization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
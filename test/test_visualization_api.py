# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import modelcatalog
from modelcatalog.api.visualization_api import VisualizationApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestVisualizationApi(unittest.TestCase):
    """VisualizationApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.visualization_api.VisualizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_visualizations_get(self):
        """Test case for visualizations_get

        List all instances of Visualization  # noqa: E501
        """
        pass

    def test_visualizations_id_delete(self):
        """Test case for visualizations_id_delete

        Delete an existing Visualization  # noqa: E501
        """
        pass

    def test_visualizations_id_get(self):
        """Test case for visualizations_id_get

        Get a single Visualization by its id  # noqa: E501
        """
        pass

    def test_visualizations_id_put(self):
        """Test case for visualizations_id_put

        Update an existing Visualization  # noqa: E501
        """
        pass

    def test_visualizations_post(self):
        """Test case for visualizations_post

        Create one Visualization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

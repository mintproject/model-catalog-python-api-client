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
from modelcatalog.api.causal_diagram_api import CausalDiagramApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestCausalDiagramApi(unittest.TestCase):
    """CausalDiagramApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.causal_diagram_api.CausalDiagramApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_causaldiagrams_get(self):
        """Test case for causaldiagrams_get

        List all instances of CausalDiagram  # noqa: E501
        """
        pass

    def test_causaldiagrams_id_delete(self):
        """Test case for causaldiagrams_id_delete

        Delete an existing CausalDiagram  # noqa: E501
        """
        pass

    def test_causaldiagrams_id_get(self):
        """Test case for causaldiagrams_id_get

        Get a single CausalDiagram by its id  # noqa: E501
        """
        pass

    def test_causaldiagrams_id_put(self):
        """Test case for causaldiagrams_id_put

        Update an existing CausalDiagram  # noqa: E501
        """
        pass

    def test_causaldiagrams_post(self):
        """Test case for causaldiagrams_post

        Create one CausalDiagram  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

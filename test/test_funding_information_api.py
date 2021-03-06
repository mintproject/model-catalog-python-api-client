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
from modelcatalog.api.funding_information_api import FundingInformationApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestFundingInformationApi(unittest.TestCase):
    """FundingInformationApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.funding_information_api.FundingInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fundinginformations_get(self):
        """Test case for fundinginformations_get

        List all instances of FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_id_delete(self):
        """Test case for fundinginformations_id_delete

        Delete an existing FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_id_get(self):
        """Test case for fundinginformations_id_get

        Get a single FundingInformation by its id  # noqa: E501
        """
        pass

    def test_fundinginformations_id_put(self):
        """Test case for fundinginformations_id_put

        Update an existing FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_post(self):
        """Test case for fundinginformations_post

        Create one FundingInformation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

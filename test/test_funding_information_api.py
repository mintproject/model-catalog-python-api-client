# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.1.0
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

        List all FundingInformation entities  # noqa: E501
        """
        pass

    def test_fundinginformations_id_delete(self):
        """Test case for fundinginformations_id_delete

        Delete a FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_id_get(self):
        """Test case for fundinginformations_id_get

        Get a FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_id_put(self):
        """Test case for fundinginformations_id_put

        Update a FundingInformation  # noqa: E501
        """
        pass

    def test_fundinginformations_post(self):
        """Test case for fundinginformations_post

        Create a FundingInformation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

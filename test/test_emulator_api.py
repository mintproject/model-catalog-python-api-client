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
from modelcatalog.api.emulator_api import EmulatorApi  # noqa: E501
from modelcatalog.rest import ApiException


class TestEmulatorApi(unittest.TestCase):
    """EmulatorApi unit test stubs"""

    def setUp(self):
        self.api = modelcatalog.api.emulator_api.EmulatorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_emulators_get(self):
        """Test case for emulators_get

        List all instances of Emulator  # noqa: E501
        """
        pass

    def test_emulators_id_delete(self):
        """Test case for emulators_id_delete

        Delete an existing Emulator  # noqa: E501
        """
        pass

    def test_emulators_id_get(self):
        """Test case for emulators_id_get

        Get a single Emulator by its id  # noqa: E501
        """
        pass

    def test_emulators_id_put(self):
        """Test case for emulators_id_put

        Update an existing Emulator  # noqa: E501
        """
        pass

    def test_emulators_post(self):
        """Test case for emulators_post

        Create one Emulator  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

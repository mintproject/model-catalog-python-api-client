# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FundingInformation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'funding_source': 'list[Organization]',
        'funding_grant': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'funding_source': 'fundingSource',
        'funding_grant': 'fundingGrant'
    }

    def __init__(self, description=None, id=None, label=None, type=None, funding_source=None, funding_grant=None):  # noqa: E501
        """FundingInformation - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self._funding_source = None
        self._funding_grant = None
        self.discriminator = None

        if description is not None:
            self.description = description
        else:
            if hasattr(self, '_description'): del self._description
            if hasattr(self.attribute_map, 'description'): del self.attribute_map['description']
            if hasattr(self.openapi_types, 'description'): del self.openapi_types['description']
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        else:
            if hasattr(self, '_label'): del self._label
            if hasattr(self.attribute_map, 'label'): del self.attribute_map['label']
            if hasattr(self.openapi_types, 'label'): del self.openapi_types['label']
        if type is not None:
            self.type = type
        else:
            if hasattr(self, '_type'): del self._type
            if hasattr(self.attribute_map, 'type'): del self.attribute_map['type']
            if hasattr(self.openapi_types, 'type'): del self.openapi_types['type']
        if funding_source is not None:
            self.funding_source = funding_source
        else:
            if hasattr(self, '_funding_source'): del self._funding_source
            if hasattr(self.attribute_map, 'funding_source'): del self.attribute_map['funding_source']
            if hasattr(self.openapi_types, 'funding_source'): del self.openapi_types['funding_source']
        if funding_grant is not None:
            self.funding_grant = funding_grant
        else:
            if hasattr(self, '_funding_grant'): del self._funding_grant
            if hasattr(self.attribute_map, 'funding_grant'): del self.attribute_map['funding_grant']
            if hasattr(self.openapi_types, 'funding_grant'): del self.openapi_types['funding_grant']

    @property
    def description(self):
        """Gets the description of this FundingInformation.  # noqa: E501


        :return: The description of this FundingInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FundingInformation.


        :param description: The description of this FundingInformation.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this FundingInformation.  # noqa: E501


        :return: The id of this FundingInformation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FundingInformation.


        :param id: The id of this FundingInformation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this FundingInformation.  # noqa: E501


        :return: The label of this FundingInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FundingInformation.


        :param label: The label of this FundingInformation.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this FundingInformation.  # noqa: E501


        :return: The type of this FundingInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FundingInformation.


        :param type: The type of this FundingInformation.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def funding_source(self):
        """Gets the funding_source of this FundingInformation.  # noqa: E501


        :return: The funding_source of this FundingInformation.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._funding_source

    @funding_source.setter
    def funding_source(self, funding_source):
        """Sets the funding_source of this FundingInformation.


        :param funding_source: The funding_source of this FundingInformation.  # noqa: E501
        :type: list[Organization]
        """

        self._funding_source = funding_source

    @property
    def funding_grant(self):
        """Gets the funding_grant of this FundingInformation.  # noqa: E501


        :return: The funding_grant of this FundingInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._funding_grant

    @funding_grant.setter
    def funding_grant(self, funding_grant):
        """Sets the funding_grant of this FundingInformation.


        :param funding_grant: The funding_grant of this FundingInformation.  # noqa: E501
        :type: list[str]
        """

        self._funding_grant = funding_grant

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
            else:
                continue                
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FundingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
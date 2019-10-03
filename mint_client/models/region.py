# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Region(object):
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
        'geo': 'list[object]',
        'id': 'str',
        'label': 'str',
        'type': 'list[str]'
    }

    attribute_map = {
        'geo': 'geo',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, geo=None, id=None, label=None, type=None):  # noqa: E501
        """Region - a model defined in OpenAPI"""  # noqa: E501

        self._geo = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        if geo is not None:
            self.geo = geo
        else:
            if hasattr(self, '_geo'): del self._geo
            if hasattr(self.attribute_map, 'geo'): del self.attribute_map['geo']
            if hasattr(self.openapi_types, 'geo'): del self.openapi_types['geo']
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

    @property
    def geo(self):
        """Gets the geo of this Region.  # noqa: E501


        :return: The geo of this Region.  # noqa: E501
        :rtype: list[object]
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """Sets the geo of this Region.


        :param geo: The geo of this Region.  # noqa: E501
        :type: list[object]
        """

        self._geo = geo

    @property
    def id(self):
        """Gets the id of this Region.  # noqa: E501


        :return: The id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.


        :param id: The id of this Region.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Region.  # noqa: E501


        :return: The label of this Region.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Region.


        :param label: The label of this Region.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Region.  # noqa: E501


        :return: The type of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Region.


        :param type: The type of this Region.  # noqa: E501
        :type: list[str]
        """

        self._type = type

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
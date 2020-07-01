# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.5.0
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
        'description': 'list[str]',
        'part_of': 'list[Region]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'geo': 'geo',
        'description': 'description',
        'part_of': 'partOf',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, geo=None, description=None, part_of=None, id=None, label=None, type=None):  # noqa: E501
        """Region - a model defined in OpenAPI"""  # noqa: E501

        self._geo = None
        self._description = None
        self._part_of = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.geo = geo
        self.description = description
        self.part_of = part_of
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def geo(self):
        """Gets the geo of this Region.  # noqa: E501

        Specific coordinates or shape associated with a region  # noqa: E501

        :return: The geo of this Region.  # noqa: E501
        :rtype: list[object]
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """Sets the geo of this Region.

        Specific coordinates or shape associated with a region  # noqa: E501

        :param geo: The geo of this Region.  # noqa: E501
        :type: list[object]
        """

        self._geo = geo

    @property
    def description(self):
        """Gets the description of this Region.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Region.

        small description  # noqa: E501

        :param description: The description of this Region.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def part_of(self):
        """Gets the part_of of this Region.  # noqa: E501

        Indicates whether a region is part of another region  # noqa: E501

        :return: The part_of of this Region.  # noqa: E501
        :rtype: list[Region]
        """
        return self._part_of

    @part_of.setter
    def part_of(self, part_of):
        """Sets the part_of of this Region.

        Indicates whether a region is part of another region  # noqa: E501

        :param part_of: The part_of of this Region.  # noqa: E501
        :type: list[Region]
        """

        self._part_of = part_of

    @property
    def id(self):
        """Gets the id of this Region.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Region.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Region.

        identifier  # noqa: E501

        :param id: The id of this Region.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Region.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Region.

        short description of the resource  # noqa: E501

        :param label: The label of this Region.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Region.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Region.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Region.

        type of the resource  # noqa: E501

        :param type: The type of this Region.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
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

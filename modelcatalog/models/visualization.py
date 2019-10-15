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


class Visualization(object):
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
        'has_format': 'list[str]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'was_derived_from_software': 'list[Software]'
    }

    attribute_map = {
        'has_format': 'hasFormat',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'was_derived_from_software': 'wasDerivedFromSoftware'
    }

    def __init__(self, has_format=None, description=None, id=None, label=None, type=None, was_derived_from_software=None):  # noqa: E501
        """Visualization - a model defined in OpenAPI"""  # noqa: E501

        self._has_format = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self._was_derived_from_software = None
        self.discriminator = None

        if has_format is not None:
            self.has_format = has_format
        else:
            if hasattr(self, '_has_format'): del self._has_format
            if hasattr(self.attribute_map, 'has_format'): del self.attribute_map['has_format']
            if hasattr(self.openapi_types, 'has_format'): del self.openapi_types['has_format']
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
        if was_derived_from_software is not None:
            self.was_derived_from_software = was_derived_from_software
        else:
            if hasattr(self, '_was_derived_from_software'): del self._was_derived_from_software
            if hasattr(self.attribute_map, 'was_derived_from_software'): del self.attribute_map['was_derived_from_software']
            if hasattr(self.openapi_types, 'was_derived_from_software'): del self.openapi_types['was_derived_from_software']

    @property
    def has_format(self):
        """Gets the has_format of this Visualization.  # noqa: E501


        :return: The has_format of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this Visualization.


        :param has_format: The has_format of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._has_format = has_format

    @property
    def description(self):
        """Gets the description of this Visualization.  # noqa: E501


        :return: The description of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Visualization.


        :param description: The description of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Visualization.  # noqa: E501


        :return: The id of this Visualization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Visualization.


        :param id: The id of this Visualization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Visualization.  # noqa: E501


        :return: The label of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Visualization.


        :param label: The label of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Visualization.  # noqa: E501


        :return: The type of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Visualization.


        :param type: The type of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def was_derived_from_software(self):
        """Gets the was_derived_from_software of this Visualization.  # noqa: E501


        :return: The was_derived_from_software of this Visualization.  # noqa: E501
        :rtype: list[Software]
        """
        return self._was_derived_from_software

    @was_derived_from_software.setter
    def was_derived_from_software(self, was_derived_from_software):
        """Sets the was_derived_from_software of this Visualization.


        :param was_derived_from_software: The was_derived_from_software of this Visualization.  # noqa: E501
        :type: list[Software]
        """

        self._was_derived_from_software = was_derived_from_software

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
        if not isinstance(other, Visualization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

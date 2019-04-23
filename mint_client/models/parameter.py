# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about     Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: 0.0.2
    Contact: mosorio@isi.edu
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Parameter(object):
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
        'id': 'str',
        'type': 'list[str]',
        'label': 'str',
        'description': 'str',
        'has_default_value': 'str',
        'has_data_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'label': 'label',
        'description': 'description',
        'has_default_value': 'hasDefaultValue',
        'has_data_type': 'hasDataType'
    }

    def __init__(self, id=None, type=None, label=None, description=None, has_default_value=None, has_data_type=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._label = None
        self._description = None
        self._has_default_value = None
        self._has_data_type = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        else:
            if hasattr(self, type): del self._type
            if hasattr(self, self.attribute_map['type']): del self.attribute_map['type']
            if hasattr(self, self.openapi_types['type']): del self.openapi_types['type']
        if label is not None:
            self.label = label
        else:
            if hasattr(self, label): del self._label
            if hasattr(self, self.attribute_map['label']): del self.attribute_map['label']
            if hasattr(self, self.openapi_types['label']): del self.openapi_types['label']
        if description is not None:
            self.description = description
        else:
            if hasattr(self, description): del self._description
            if hasattr(self, self.attribute_map['description']): del self.attribute_map['description']
            if hasattr(self, self.openapi_types['description']): del self.openapi_types['description']
        if has_default_value is not None:
            self.has_default_value = has_default_value
        else:
            if hasattr(self, has_default_value): del self._has_default_value
            if hasattr(self, self.attribute_map['has_default_value']): del self.attribute_map['has_default_value']
            if hasattr(self, self.openapi_types['has_default_value']): del self.openapi_types['has_default_value']
        if has_data_type is not None:
            self.has_data_type = has_data_type
        else:
            if hasattr(self, has_data_type): del self._has_data_type
            if hasattr(self, self.attribute_map['has_data_type']): del self.attribute_map['has_data_type']
            if hasattr(self, self.openapi_types['has_data_type']): del self.openapi_types['has_data_type']

    @property
    def id(self):
        """Gets the id of this Parameter.  # noqa: E501


        :return: The id of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Parameter.


        :param id: The id of this Parameter.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Parameter.  # noqa: E501


        :return: The type of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.


        :param type: The type of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this Parameter.  # noqa: E501


        :return: The label of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Parameter.


        :param label: The label of this Parameter.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this Parameter.  # noqa: E501


        :return: The description of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.


        :param description: The description of this Parameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def has_default_value(self):
        """Gets the has_default_value of this Parameter.  # noqa: E501


        :return: The has_default_value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this Parameter.


        :param has_default_value: The has_default_value of this Parameter.  # noqa: E501
        :type: str
        """

        self._has_default_value = has_default_value

    @property
    def has_data_type(self):
        """Gets the has_data_type of this Parameter.  # noqa: E501


        :return: The has_data_type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._has_data_type

    @has_data_type.setter
    def has_data_type(self, has_data_type):
        """Sets the has_data_type of this Parameter.


        :param has_data_type: The has_data_type of this Parameter.  # noqa: E501
        :type: str
        """

        self._has_data_type = has_data_type

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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

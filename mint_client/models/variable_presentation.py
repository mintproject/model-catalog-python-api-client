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


class VariablePresentation(object):
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
        'has_long_name': 'str',
        'has_short_name': 'str',
        'has_standard_variable': 'list[DatasetSpecification]',
        'has_relevance_level': 'int',
        'uses_unit': 'Unit'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'label': 'label',
        'description': 'description',
        'has_long_name': 'hasLongName',
        'has_short_name': 'hasShortName',
        'has_standard_variable': 'hasStandardVariable',
        'has_relevance_level': 'hasRelevanceLevel',
        'uses_unit': 'usesUnit'
    }

    def __init__(self, id=None, type=None, label=None, description=None, has_long_name=None, has_short_name=None, has_standard_variable=None, has_relevance_level=None, uses_unit=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._label = None
        self._description = None
        self._has_long_name = None
        self._has_short_name = None
        self._has_standard_variable = None
        self._has_relevance_level = None
        self._uses_unit = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        else:
            del self._type
            del self.attribute_map['type']
            del self.openapi_types['type']
        if label is not None:
            self.label = label
        else:
            del self._label
            del self.attribute_map['label']
            del self.openapi_types['label']
        if description is not None:
            self.description = description
        else:
            del self._description
            del self.attribute_map['description']
            del self.openapi_types['description']
        if has_long_name is not None:
            self.has_long_name = has_long_name
        else:
            del self._has_long_name
            del self.attribute_map['has_long_name']
            del self.openapi_types['has_long_name']
        if has_short_name is not None:
            self.has_short_name = has_short_name
        else:
            del self._has_short_name
            del self.attribute_map['has_short_name']
            del self.openapi_types['has_short_name']
        if has_standard_variable is not None:
            self.has_standard_variable = has_standard_variable
        else:
            del self._has_standard_variable
            del self.attribute_map['has_standard_variable']
            del self.openapi_types['has_standard_variable']
        if has_relevance_level is not None:
            self.has_relevance_level = has_relevance_level
        else:
            del self._has_relevance_level
            del self.attribute_map['has_relevance_level']
            del self.openapi_types['has_relevance_level']
        if uses_unit is not None:
            self.uses_unit = uses_unit

    @property
    def id(self):
        """Gets the id of this VariablePresentation.  # noqa: E501


        :return: The id of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariablePresentation.


        :param id: The id of this VariablePresentation.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this VariablePresentation.  # noqa: E501


        :return: The type of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariablePresentation.


        :param type: The type of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this VariablePresentation.  # noqa: E501


        :return: The label of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.


        :param label: The label of this VariablePresentation.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this VariablePresentation.  # noqa: E501


        :return: The description of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablePresentation.


        :param description: The description of this VariablePresentation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.  # noqa: E501


        :return: The has_long_name of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.


        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type: str
        """

        self._has_long_name = has_long_name

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.  # noqa: E501


        :return: The has_short_name of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.


        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type: str
        """

        self._has_short_name = has_short_name

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.  # noqa: E501


        :return: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :rtype: list[DatasetSpecification]
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.


        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type: list[DatasetSpecification]
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_relevance_level(self):
        """Gets the has_relevance_level of this VariablePresentation.  # noqa: E501


        :return: The has_relevance_level of this VariablePresentation.  # noqa: E501
        :rtype: int
        """
        return self._has_relevance_level

    @has_relevance_level.setter
    def has_relevance_level(self, has_relevance_level):
        """Sets the has_relevance_level of this VariablePresentation.


        :param has_relevance_level: The has_relevance_level of this VariablePresentation.  # noqa: E501
        :type: int
        """

        self._has_relevance_level = has_relevance_level

    @property
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.  # noqa: E501


        :return: The uses_unit of this VariablePresentation.  # noqa: E501
        :rtype: Unit
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.


        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type: Unit
        """

        self._uses_unit = uses_unit

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
        if not isinstance(other, VariablePresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

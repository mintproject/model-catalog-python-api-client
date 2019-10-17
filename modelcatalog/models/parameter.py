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
        'has_default_value': 'list[str]',
        'has_maximum_accepted_value': 'list[str]',
        'description': 'list[str]',
        'has_data_type': 'list[str]',
        'has_fixed_value': 'list[str]',
        'has_presentation': 'list[VariablePresentation]',
        'label': 'list[str]',
        'type': 'list[str]',
        'has_minimum_accepted_value': 'list[str]',
        'adjusts_variable': 'list[object]',
        'position': 'list[float]',
        'id': 'str',
        'uses_unit': 'list[object]'
    }

    attribute_map = {
        'has_default_value': 'hasDefaultValue',
        'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
        'description': 'description',
        'has_data_type': 'hasDataType',
        'has_fixed_value': 'hasFixedValue',
        'has_presentation': 'hasPresentation',
        'label': 'label',
        'type': 'type',
        'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
        'adjusts_variable': 'adjustsVariable',
        'position': 'position',
        'id': 'id',
        'uses_unit': 'usesUnit'
    }

    def __init__(self, has_default_value=None, has_maximum_accepted_value=None, description=None, has_data_type=None, has_fixed_value=None, has_presentation=None, label=None, type=None, has_minimum_accepted_value=None, adjusts_variable=None, position=None, id=None, uses_unit=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI"""  # noqa: E501

        self._has_default_value = None
        self._has_maximum_accepted_value = None
        self._description = None
        self._has_data_type = None
        self._has_fixed_value = None
        self._has_presentation = None
        self._label = None
        self._type = None
        self._has_minimum_accepted_value = None
        self._adjusts_variable = None
        self._position = None
        self._id = None
        self._uses_unit = None
        self.discriminator = None

        if has_default_value is not None:
            self.has_default_value = has_default_value
        else:
            if hasattr(self, '_has_default_value'): del self._has_default_value
            if hasattr(self.attribute_map, 'has_default_value'): del self.attribute_map['has_default_value']
            if hasattr(self.openapi_types, 'has_default_value'): del self.openapi_types['has_default_value']
        if has_maximum_accepted_value is not None:
            self.has_maximum_accepted_value = has_maximum_accepted_value
        else:
            if hasattr(self, '_has_maximum_accepted_value'): del self._has_maximum_accepted_value
            if hasattr(self.attribute_map, 'has_maximum_accepted_value'): del self.attribute_map['has_maximum_accepted_value']
            if hasattr(self.openapi_types, 'has_maximum_accepted_value'): del self.openapi_types['has_maximum_accepted_value']
        if description is not None:
            self.description = description
        else:
            if hasattr(self, '_description'): del self._description
            if hasattr(self.attribute_map, 'description'): del self.attribute_map['description']
            if hasattr(self.openapi_types, 'description'): del self.openapi_types['description']
        if has_data_type is not None:
            self.has_data_type = has_data_type
        else:
            if hasattr(self, '_has_data_type'): del self._has_data_type
            if hasattr(self.attribute_map, 'has_data_type'): del self.attribute_map['has_data_type']
            if hasattr(self.openapi_types, 'has_data_type'): del self.openapi_types['has_data_type']
        if has_fixed_value is not None:
            self.has_fixed_value = has_fixed_value
        else:
            if hasattr(self, '_has_fixed_value'): del self._has_fixed_value
            if hasattr(self.attribute_map, 'has_fixed_value'): del self.attribute_map['has_fixed_value']
            if hasattr(self.openapi_types, 'has_fixed_value'): del self.openapi_types['has_fixed_value']
        if has_presentation is not None:
            self.has_presentation = has_presentation
        else:
            if hasattr(self, '_has_presentation'): del self._has_presentation
            if hasattr(self.attribute_map, 'has_presentation'): del self.attribute_map['has_presentation']
            if hasattr(self.openapi_types, 'has_presentation'): del self.openapi_types['has_presentation']
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
        if has_minimum_accepted_value is not None:
            self.has_minimum_accepted_value = has_minimum_accepted_value
        else:
            if hasattr(self, '_has_minimum_accepted_value'): del self._has_minimum_accepted_value
            if hasattr(self.attribute_map, 'has_minimum_accepted_value'): del self.attribute_map['has_minimum_accepted_value']
            if hasattr(self.openapi_types, 'has_minimum_accepted_value'): del self.openapi_types['has_minimum_accepted_value']
        if adjusts_variable is not None:
            self.adjusts_variable = adjusts_variable
        else:
            if hasattr(self, '_adjusts_variable'): del self._adjusts_variable
            if hasattr(self.attribute_map, 'adjusts_variable'): del self.attribute_map['adjusts_variable']
            if hasattr(self.openapi_types, 'adjusts_variable'): del self.openapi_types['adjusts_variable']
        if position is not None:
            self.position = position
        else:
            if hasattr(self, '_position'): del self._position
            if hasattr(self.attribute_map, 'position'): del self.attribute_map['position']
            if hasattr(self.openapi_types, 'position'): del self.openapi_types['position']
        if id is not None:
            self.id = id
        if uses_unit is not None:
            self.uses_unit = uses_unit
        else:
            if hasattr(self, '_uses_unit'): del self._uses_unit
            if hasattr(self.attribute_map, 'uses_unit'): del self.attribute_map['uses_unit']
            if hasattr(self.openapi_types, 'uses_unit'): del self.openapi_types['uses_unit']

    @property
    def has_default_value(self):
        """Gets the has_default_value of this Parameter.  # noqa: E501


        :return: The has_default_value of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this Parameter.


        :param has_default_value: The has_default_value of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._has_default_value = has_default_value

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this Parameter.  # noqa: E501


        :return: The has_maximum_accepted_value of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this Parameter.


        :param has_maximum_accepted_value: The has_maximum_accepted_value of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def description(self):
        """Gets the description of this Parameter.  # noqa: E501


        :return: The description of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Parameter.


        :param description: The description of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def has_data_type(self):
        """Gets the has_data_type of this Parameter.  # noqa: E501


        :return: The has_data_type of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_data_type

    @has_data_type.setter
    def has_data_type(self, has_data_type):
        """Sets the has_data_type of this Parameter.


        :param has_data_type: The has_data_type of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._has_data_type = has_data_type

    @property
    def has_fixed_value(self):
        """Gets the has_fixed_value of this Parameter.  # noqa: E501


        :return: The has_fixed_value of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_fixed_value

    @has_fixed_value.setter
    def has_fixed_value(self, has_fixed_value):
        """Sets the has_fixed_value of this Parameter.


        :param has_fixed_value: The has_fixed_value of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._has_fixed_value = has_fixed_value

    @property
    def has_presentation(self):
        """Gets the has_presentation of this Parameter.  # noqa: E501


        :return: The has_presentation of this Parameter.  # noqa: E501
        :rtype: list[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this Parameter.


        :param has_presentation: The has_presentation of this Parameter.  # noqa: E501
        :type: list[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def label(self):
        """Gets the label of this Parameter.  # noqa: E501


        :return: The label of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Parameter.


        :param label: The label of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._label = label

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
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this Parameter.  # noqa: E501


        :return: The has_minimum_accepted_value of this Parameter.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this Parameter.


        :param has_minimum_accepted_value: The has_minimum_accepted_value of this Parameter.  # noqa: E501
        :type: list[str]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def adjusts_variable(self):
        """Gets the adjusts_variable of this Parameter.  # noqa: E501


        :return: The adjusts_variable of this Parameter.  # noqa: E501
        :rtype: list[object]
        """
        return self._adjusts_variable

    @adjusts_variable.setter
    def adjusts_variable(self, adjusts_variable):
        """Sets the adjusts_variable of this Parameter.


        :param adjusts_variable: The adjusts_variable of this Parameter.  # noqa: E501
        :type: list[object]
        """

        self._adjusts_variable = adjusts_variable

    @property
    def position(self):
        """Gets the position of this Parameter.  # noqa: E501


        :return: The position of this Parameter.  # noqa: E501
        :rtype: list[float]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Parameter.


        :param position: The position of this Parameter.  # noqa: E501
        :type: list[float]
        """

        self._position = position

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

        self._id = id

    @property
    def uses_unit(self):
        """Gets the uses_unit of this Parameter.  # noqa: E501


        :return: The uses_unit of this Parameter.  # noqa: E501
        :rtype: list[object]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this Parameter.


        :param uses_unit: The uses_unit of this Parameter.  # noqa: E501
        :type: list[object]
        """

        self._uses_unit = uses_unit

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
        if not isinstance(other, Parameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

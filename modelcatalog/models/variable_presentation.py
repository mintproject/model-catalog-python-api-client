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
        'has_default_value': 'list[object]',
        'has_short_name': 'list[str]',
        'has_minimum_accepted_value': 'list[object]',
        'has_standard_variable': 'list[StandardVariable]',
        'has_maximum_accepted_value': 'list[object]',
        'has_constraint': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'part_of_dataset': 'list[DatasetSpecification]',
        'type': 'list[str]',
        'uses_unit': 'list[object]',
        'has_long_name': 'list[str]'
    }

    attribute_map = {
        'has_default_value': 'hasDefaultValue',
        'has_short_name': 'hasShortName',
        'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
        'has_standard_variable': 'hasStandardVariable',
        'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
        'has_constraint': 'hasConstraint',
        'id': 'id',
        'label': 'label',
        'part_of_dataset': 'partOfDataset',
        'type': 'type',
        'uses_unit': 'usesUnit',
        'has_long_name': 'hasLongName'
    }

    def __init__(self, has_default_value=None, has_short_name=None, has_minimum_accepted_value=None, has_standard_variable=None, has_maximum_accepted_value=None, has_constraint=None, id=None, label=None, part_of_dataset=None, type=None, uses_unit=None, has_long_name=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI"""  # noqa: E501

        self._has_default_value = None
        self._has_short_name = None
        self._has_minimum_accepted_value = None
        self._has_standard_variable = None
        self._has_maximum_accepted_value = None
        self._has_constraint = None
        self._id = None
        self._label = None
        self._part_of_dataset = None
        self._type = None
        self._uses_unit = None
        self._has_long_name = None
        self.discriminator = None

        if has_default_value is not None:
            self.has_default_value = has_default_value
        else:
            if hasattr(self, '_has_default_value'): del self._has_default_value
            if hasattr(self.attribute_map, 'has_default_value'): del self.attribute_map['has_default_value']
            if hasattr(self.openapi_types, 'has_default_value'): del self.openapi_types['has_default_value']
        if has_short_name is not None:
            self.has_short_name = has_short_name
        else:
            if hasattr(self, '_has_short_name'): del self._has_short_name
            if hasattr(self.attribute_map, 'has_short_name'): del self.attribute_map['has_short_name']
            if hasattr(self.openapi_types, 'has_short_name'): del self.openapi_types['has_short_name']
        if has_minimum_accepted_value is not None:
            self.has_minimum_accepted_value = has_minimum_accepted_value
        else:
            if hasattr(self, '_has_minimum_accepted_value'): del self._has_minimum_accepted_value
            if hasattr(self.attribute_map, 'has_minimum_accepted_value'): del self.attribute_map['has_minimum_accepted_value']
            if hasattr(self.openapi_types, 'has_minimum_accepted_value'): del self.openapi_types['has_minimum_accepted_value']
        if has_standard_variable is not None:
            self.has_standard_variable = has_standard_variable
        else:
            if hasattr(self, '_has_standard_variable'): del self._has_standard_variable
            if hasattr(self.attribute_map, 'has_standard_variable'): del self.attribute_map['has_standard_variable']
            if hasattr(self.openapi_types, 'has_standard_variable'): del self.openapi_types['has_standard_variable']
        if has_maximum_accepted_value is not None:
            self.has_maximum_accepted_value = has_maximum_accepted_value
        else:
            if hasattr(self, '_has_maximum_accepted_value'): del self._has_maximum_accepted_value
            if hasattr(self.attribute_map, 'has_maximum_accepted_value'): del self.attribute_map['has_maximum_accepted_value']
            if hasattr(self.openapi_types, 'has_maximum_accepted_value'): del self.openapi_types['has_maximum_accepted_value']
        if has_constraint is not None:
            self.has_constraint = has_constraint
        else:
            if hasattr(self, '_has_constraint'): del self._has_constraint
            if hasattr(self.attribute_map, 'has_constraint'): del self.attribute_map['has_constraint']
            if hasattr(self.openapi_types, 'has_constraint'): del self.openapi_types['has_constraint']
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        else:
            if hasattr(self, '_label'): del self._label
            if hasattr(self.attribute_map, 'label'): del self.attribute_map['label']
            if hasattr(self.openapi_types, 'label'): del self.openapi_types['label']
        if part_of_dataset is not None:
            self.part_of_dataset = part_of_dataset
        else:
            if hasattr(self, '_part_of_dataset'): del self._part_of_dataset
            if hasattr(self.attribute_map, 'part_of_dataset'): del self.attribute_map['part_of_dataset']
            if hasattr(self.openapi_types, 'part_of_dataset'): del self.openapi_types['part_of_dataset']
        if type is not None:
            self.type = type
        else:
            if hasattr(self, '_type'): del self._type
            if hasattr(self.attribute_map, 'type'): del self.attribute_map['type']
            if hasattr(self.openapi_types, 'type'): del self.openapi_types['type']
        if uses_unit is not None:
            self.uses_unit = uses_unit
        else:
            if hasattr(self, '_uses_unit'): del self._uses_unit
            if hasattr(self.attribute_map, 'uses_unit'): del self.attribute_map['uses_unit']
            if hasattr(self.openapi_types, 'uses_unit'): del self.openapi_types['uses_unit']
        if has_long_name is not None:
            self.has_long_name = has_long_name
        else:
            if hasattr(self, '_has_long_name'): del self._has_long_name
            if hasattr(self.attribute_map, 'has_long_name'): del self.attribute_map['has_long_name']
            if hasattr(self.openapi_types, 'has_long_name'): del self.openapi_types['has_long_name']

    @property
    def has_default_value(self):
        """Gets the has_default_value of this VariablePresentation.  # noqa: E501


        :return: The has_default_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this VariablePresentation.


        :param has_default_value: The has_default_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_default_value = has_default_value

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.  # noqa: E501


        :return: The has_short_name of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.


        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._has_short_name = has_short_name

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this VariablePresentation.  # noqa: E501


        :return: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this VariablePresentation.


        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.  # noqa: E501


        :return: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :rtype: list[StandardVariable]
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.


        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type: list[StandardVariable]
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this VariablePresentation.  # noqa: E501


        :return: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this VariablePresentation.


        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def has_constraint(self):
        """Gets the has_constraint of this VariablePresentation.  # noqa: E501


        :return: The has_constraint of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_constraint

    @has_constraint.setter
    def has_constraint(self, has_constraint):
        """Sets the has_constraint of this VariablePresentation.


        :param has_constraint: The has_constraint of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._has_constraint = has_constraint

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

        self._id = id

    @property
    def label(self):
        """Gets the label of this VariablePresentation.  # noqa: E501


        :return: The label of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.


        :param label: The label of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def part_of_dataset(self):
        """Gets the part_of_dataset of this VariablePresentation.  # noqa: E501


        :return: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :rtype: list[DatasetSpecification]
        """
        return self._part_of_dataset

    @part_of_dataset.setter
    def part_of_dataset(self, part_of_dataset):
        """Sets the part_of_dataset of this VariablePresentation.


        :param part_of_dataset: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :type: list[DatasetSpecification]
        """

        self._part_of_dataset = part_of_dataset

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
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.  # noqa: E501


        :return: The uses_unit of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.


        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._uses_unit = uses_unit

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.  # noqa: E501


        :return: The has_long_name of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.


        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._has_long_name = has_long_name

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
        if not isinstance(other, VariablePresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

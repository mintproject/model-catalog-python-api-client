# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.8.0
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
        'description': 'list[str]',
        'part_of_dataset': 'list[DatasetSpecification]',
        'id': 'str',
        'label': 'list[str]',
        'uses_unit': 'list[Unit]',
        'type': 'list[str]',
        'has_long_name': 'list[str]'
    }

    attribute_map = {
        'has_default_value': 'hasDefaultValue',
        'has_short_name': 'hasShortName',
        'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
        'has_standard_variable': 'hasStandardVariable',
        'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
        'description': 'description',
        'part_of_dataset': 'partOfDataset',
        'id': 'id',
        'label': 'label',
        'uses_unit': 'usesUnit',
        'type': 'type',
        'has_long_name': 'hasLongName'
    }

    def __init__(self, has_default_value=None, has_short_name=None, has_minimum_accepted_value=None, has_standard_variable=None, has_maximum_accepted_value=None, description=None, part_of_dataset=None, id=None, label=None, uses_unit=None, type=None, has_long_name=None):  # noqa: E501
        """VariablePresentation - a model defined in OpenAPI"""  # noqa: E501

        self._has_default_value = None
        self._has_short_name = None
        self._has_minimum_accepted_value = None
        self._has_standard_variable = None
        self._has_maximum_accepted_value = None
        self._description = None
        self._part_of_dataset = None
        self._id = None
        self._label = None
        self._uses_unit = None
        self._type = None
        self._has_long_name = None
        self.discriminator = None

        self.has_default_value = has_default_value
        self.has_short_name = has_short_name
        self.has_minimum_accepted_value = has_minimum_accepted_value
        self.has_standard_variable = has_standard_variable
        self.has_maximum_accepted_value = has_maximum_accepted_value
        self.description = description
        self.part_of_dataset = part_of_dataset
        if id is not None:
            self.id = id
        self.label = label
        self.uses_unit = uses_unit
        self.type = type
        self.has_long_name = has_long_name

    @property
    def has_default_value(self):
        """Gets the has_default_value of this VariablePresentation.  # noqa: E501

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_default_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this VariablePresentation.

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_default_value: The has_default_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_default_value = has_default_value

    @property
    def has_short_name(self):
        """Gets the has_short_name of this VariablePresentation.  # noqa: E501

        A short name (e.g., temperature) capturing the high-level concept of the variable  # noqa: E501

        :return: The has_short_name of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_short_name

    @has_short_name.setter
    def has_short_name(self, has_short_name):
        """Sets the has_short_name of this VariablePresentation.

        A short name (e.g., temperature) capturing the high-level concept of the variable  # noqa: E501

        :param has_short_name: The has_short_name of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._has_short_name = has_short_name

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this VariablePresentation.  # noqa: E501

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this VariablePresentation.

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_minimum_accepted_value: The has_minimum_accepted_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def has_standard_variable(self):
        """Gets the has_standard_variable of this VariablePresentation.  # noqa: E501

        the standard name of a variable  # noqa: E501

        :return: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :rtype: list[StandardVariable]
        """
        return self._has_standard_variable

    @has_standard_variable.setter
    def has_standard_variable(self, has_standard_variable):
        """Sets the has_standard_variable of this VariablePresentation.

        the standard name of a variable  # noqa: E501

        :param has_standard_variable: The has_standard_variable of this VariablePresentation.  # noqa: E501
        :type: list[StandardVariable]
        """

        self._has_standard_variable = has_standard_variable

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this VariablePresentation.  # noqa: E501

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this VariablePresentation.

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_maximum_accepted_value: The has_maximum_accepted_value of this VariablePresentation.  # noqa: E501
        :type: list[object]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def description(self):
        """Gets the description of this VariablePresentation.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablePresentation.

        small description  # noqa: E501

        :param description: The description of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def part_of_dataset(self):
        """Gets the part_of_dataset of this VariablePresentation.  # noqa: E501

        Associates a presentation with a dataset where the presentation occurs  # noqa: E501

        :return: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :rtype: list[DatasetSpecification]
        """
        return self._part_of_dataset

    @part_of_dataset.setter
    def part_of_dataset(self, part_of_dataset):
        """Sets the part_of_dataset of this VariablePresentation.

        Associates a presentation with a dataset where the presentation occurs  # noqa: E501

        :param part_of_dataset: The part_of_dataset of this VariablePresentation.  # noqa: E501
        :type: list[DatasetSpecification]
        """

        self._part_of_dataset = part_of_dataset

    @property
    def id(self):
        """Gets the id of this VariablePresentation.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this VariablePresentation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariablePresentation.

        identifier  # noqa: E501

        :param id: The id of this VariablePresentation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this VariablePresentation.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VariablePresentation.

        short description of the resource  # noqa: E501

        :param label: The label of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def uses_unit(self):
        """Gets the uses_unit of this VariablePresentation.  # noqa: E501

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :return: The uses_unit of this VariablePresentation.  # noqa: E501
        :rtype: list[Unit]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this VariablePresentation.

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :param uses_unit: The uses_unit of this VariablePresentation.  # noqa: E501
        :type: list[Unit]
        """

        self._uses_unit = uses_unit

    @property
    def type(self):
        """Gets the type of this VariablePresentation.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariablePresentation.

        type of the resource  # noqa: E501

        :param type: The type of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_long_name(self):
        """Gets the has_long_name of this VariablePresentation.  # noqa: E501

        Properties that relate the variable representation to its long name. The long name is useful for context (e.g., precipitation is less ambiguous than P) but not as precise as the standard name.  # noqa: E501

        :return: The has_long_name of this VariablePresentation.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_long_name

    @has_long_name.setter
    def has_long_name(self, has_long_name):
        """Sets the has_long_name of this VariablePresentation.

        Properties that relate the variable representation to its long name. The long name is useful for context (e.g., precipitation is less ambiguous than P) but not as precise as the standard name.  # noqa: E501

        :param has_long_name: The has_long_name of this VariablePresentation.  # noqa: E501
        :type: list[str]
        """

        self._has_long_name = has_long_name

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

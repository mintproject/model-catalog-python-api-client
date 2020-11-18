# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CatalogIdentifier(object):
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
        'has_maximum_accepted_value': 'list[object]',
        'description': 'list[str]',
        'has_data_type': 'list[str]',
        'has_fixed_value': 'list[object]',
        'has_presentation': 'list[VariablePresentation]',
        'label': 'list[str]',
        'recommended_increment': 'list[float]',
        'type': 'list[str]',
        'has_minimum_accepted_value': 'list[object]',
        'has_accepted_values': 'list[str]',
        'adjusts_variable': 'list[Variable]',
        'relevant_for_intervention': 'list[Intervention]',
        'position': 'list[int]',
        'id': 'str',
        'uses_unit': 'list[Unit]',
        'has_step_size': 'list[float]'
    }

    attribute_map = {
        'has_default_value': 'hasDefaultValue',
        'has_maximum_accepted_value': 'hasMaximumAcceptedValue',
        'description': 'description',
        'has_data_type': 'hasDataType',
        'has_fixed_value': 'hasFixedValue',
        'has_presentation': 'hasPresentation',
        'label': 'label',
        'recommended_increment': 'recommendedIncrement',
        'type': 'type',
        'has_minimum_accepted_value': 'hasMinimumAcceptedValue',
        'has_accepted_values': 'hasAcceptedValues',
        'adjusts_variable': 'adjustsVariable',
        'relevant_for_intervention': 'relevantForIntervention',
        'position': 'position',
        'id': 'id',
        'uses_unit': 'usesUnit',
        'has_step_size': 'hasStepSize'
    }

    def __init__(self, has_default_value=None, has_maximum_accepted_value=None, description=None, has_data_type=None, has_fixed_value=None, has_presentation=None, label=None, recommended_increment=None, type=None, has_minimum_accepted_value=None, has_accepted_values=None, adjusts_variable=None, relevant_for_intervention=None, position=None, id=None, uses_unit=None, has_step_size=None):  # noqa: E501
        """CatalogIdentifier - a model defined in OpenAPI"""  # noqa: E501

        self._has_default_value = None
        self._has_maximum_accepted_value = None
        self._description = None
        self._has_data_type = None
        self._has_fixed_value = None
        self._has_presentation = None
        self._label = None
        self._recommended_increment = None
        self._type = None
        self._has_minimum_accepted_value = None
        self._has_accepted_values = None
        self._adjusts_variable = None
        self._relevant_for_intervention = None
        self._position = None
        self._id = None
        self._uses_unit = None
        self._has_step_size = None
        self.discriminator = None

        self.has_default_value = has_default_value
        self.has_maximum_accepted_value = has_maximum_accepted_value
        self.description = description
        self.has_data_type = has_data_type
        self.has_fixed_value = has_fixed_value
        self.has_presentation = has_presentation
        self.label = label
        self.recommended_increment = recommended_increment
        self.type = type
        self.has_minimum_accepted_value = has_minimum_accepted_value
        self.has_accepted_values = has_accepted_values
        self.adjusts_variable = adjusts_variable
        self.relevant_for_intervention = relevant_for_intervention
        self.position = position
        if id is not None:
            self.id = id
        self.uses_unit = uses_unit
        self.has_step_size = has_step_size

    @property
    def has_default_value(self):
        """Gets the has_default_value of this CatalogIdentifier.  # noqa: E501

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_default_value of this CatalogIdentifier.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this CatalogIdentifier.

        Default accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_default_value: The has_default_value of this CatalogIdentifier.  # noqa: E501
        :type: list[object]
        """

        self._has_default_value = has_default_value

    @property
    def has_maximum_accepted_value(self):
        """Gets the has_maximum_accepted_value of this CatalogIdentifier.  # noqa: E501

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_maximum_accepted_value of this CatalogIdentifier.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_maximum_accepted_value

    @has_maximum_accepted_value.setter
    def has_maximum_accepted_value(self, has_maximum_accepted_value):
        """Sets the has_maximum_accepted_value of this CatalogIdentifier.

        Maximum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_maximum_accepted_value: The has_maximum_accepted_value of this CatalogIdentifier.  # noqa: E501
        :type: list[object]
        """

        self._has_maximum_accepted_value = has_maximum_accepted_value

    @property
    def description(self):
        """Gets the description of this CatalogIdentifier.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this CatalogIdentifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CatalogIdentifier.

        small description  # noqa: E501

        :param description: The description of this CatalogIdentifier.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def has_data_type(self):
        """Gets the has_data_type of this CatalogIdentifier.  # noqa: E501

        Property that indicates the data type of a parameter  # noqa: E501

        :return: The has_data_type of this CatalogIdentifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_data_type

    @has_data_type.setter
    def has_data_type(self, has_data_type):
        """Sets the has_data_type of this CatalogIdentifier.

        Property that indicates the data type of a parameter  # noqa: E501

        :param has_data_type: The has_data_type of this CatalogIdentifier.  # noqa: E501
        :type: list[str]
        """

        self._has_data_type = has_data_type

    @property
    def has_fixed_value(self):
        """Gets the has_fixed_value of this CatalogIdentifier.  # noqa: E501

        Value of a parameter in a software setup.  # noqa: E501

        :return: The has_fixed_value of this CatalogIdentifier.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_fixed_value

    @has_fixed_value.setter
    def has_fixed_value(self, has_fixed_value):
        """Sets the has_fixed_value of this CatalogIdentifier.

        Value of a parameter in a software setup.  # noqa: E501

        :param has_fixed_value: The has_fixed_value of this CatalogIdentifier.  # noqa: E501
        :type: list[object]
        """

        self._has_fixed_value = has_fixed_value

    @property
    def has_presentation(self):
        """Gets the has_presentation of this CatalogIdentifier.  # noqa: E501

        Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it.  # noqa: E501

        :return: The has_presentation of this CatalogIdentifier.  # noqa: E501
        :rtype: list[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this CatalogIdentifier.

        Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it.  # noqa: E501

        :param has_presentation: The has_presentation of this CatalogIdentifier.  # noqa: E501
        :type: list[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def label(self):
        """Gets the label of this CatalogIdentifier.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this CatalogIdentifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CatalogIdentifier.

        short description of the resource  # noqa: E501

        :param label: The label of this CatalogIdentifier.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def recommended_increment(self):
        """Gets the recommended_increment of this CatalogIdentifier.  # noqa: E501

        Value that represents how a parameter should be incremented on each iteration of a software component execution. This value is important when preparing execution ensembles automatically, e.g., simulating crop production varying the parameter \"fertilizer amount\" in increments of 10%.  # noqa: E501

        :return: The recommended_increment of this CatalogIdentifier.  # noqa: E501
        :rtype: list[float]
        """
        return self._recommended_increment

    @recommended_increment.setter
    def recommended_increment(self, recommended_increment):
        """Sets the recommended_increment of this CatalogIdentifier.

        Value that represents how a parameter should be incremented on each iteration of a software component execution. This value is important when preparing execution ensembles automatically, e.g., simulating crop production varying the parameter \"fertilizer amount\" in increments of 10%.  # noqa: E501

        :param recommended_increment: The recommended_increment of this CatalogIdentifier.  # noqa: E501
        :type: list[float]
        """

        self._recommended_increment = recommended_increment

    @property
    def type(self):
        """Gets the type of this CatalogIdentifier.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this CatalogIdentifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CatalogIdentifier.

        type of the resource  # noqa: E501

        :param type: The type of this CatalogIdentifier.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_minimum_accepted_value(self):
        """Gets the has_minimum_accepted_value of this CatalogIdentifier.  # noqa: E501

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :return: The has_minimum_accepted_value of this CatalogIdentifier.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_minimum_accepted_value

    @has_minimum_accepted_value.setter
    def has_minimum_accepted_value(self, has_minimum_accepted_value):
        """Sets the has_minimum_accepted_value of this CatalogIdentifier.

        Minimum accepted value of a variable presentation (or a parameter)  # noqa: E501

        :param has_minimum_accepted_value: The has_minimum_accepted_value of this CatalogIdentifier.  # noqa: E501
        :type: list[object]
        """

        self._has_minimum_accepted_value = has_minimum_accepted_value

    @property
    def has_accepted_values(self):
        """Gets the has_accepted_values of this CatalogIdentifier.  # noqa: E501

        Property that constraints which values are accepted for a parameter. For example, the name of a crop can only be \"Maize\" or \"Sorghum\"  # noqa: E501

        :return: The has_accepted_values of this CatalogIdentifier.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_accepted_values

    @has_accepted_values.setter
    def has_accepted_values(self, has_accepted_values):
        """Sets the has_accepted_values of this CatalogIdentifier.

        Property that constraints which values are accepted for a parameter. For example, the name of a crop can only be \"Maize\" or \"Sorghum\"  # noqa: E501

        :param has_accepted_values: The has_accepted_values of this CatalogIdentifier.  # noqa: E501
        :type: list[str]
        """

        self._has_accepted_values = has_accepted_values

    @property
    def adjusts_variable(self):
        """Gets the adjusts_variable of this CatalogIdentifier.  # noqa: E501

        Property that links parameter with the variable they adjust. This property can be used when parameters quantify variables without directly representing them. For example, a \"fertilizer percentage adjustment\" parameter can quantify a \"fertilizer price\" variable  # noqa: E501

        :return: The adjusts_variable of this CatalogIdentifier.  # noqa: E501
        :rtype: list[Variable]
        """
        return self._adjusts_variable

    @adjusts_variable.setter
    def adjusts_variable(self, adjusts_variable):
        """Sets the adjusts_variable of this CatalogIdentifier.

        Property that links parameter with the variable they adjust. This property can be used when parameters quantify variables without directly representing them. For example, a \"fertilizer percentage adjustment\" parameter can quantify a \"fertilizer price\" variable  # noqa: E501

        :param adjusts_variable: The adjusts_variable of this CatalogIdentifier.  # noqa: E501
        :type: list[Variable]
        """

        self._adjusts_variable = adjusts_variable

    @property
    def relevant_for_intervention(self):
        """Gets the relevant_for_intervention of this CatalogIdentifier.  # noqa: E501

        Description not available  # noqa: E501

        :return: The relevant_for_intervention of this CatalogIdentifier.  # noqa: E501
        :rtype: list[Intervention]
        """
        return self._relevant_for_intervention

    @relevant_for_intervention.setter
    def relevant_for_intervention(self, relevant_for_intervention):
        """Sets the relevant_for_intervention of this CatalogIdentifier.

        Description not available  # noqa: E501

        :param relevant_for_intervention: The relevant_for_intervention of this CatalogIdentifier.  # noqa: E501
        :type: list[Intervention]
        """

        self._relevant_for_intervention = relevant_for_intervention

    @property
    def position(self):
        """Gets the position of this CatalogIdentifier.  # noqa: E501

        Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution  # noqa: E501

        :return: The position of this CatalogIdentifier.  # noqa: E501
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CatalogIdentifier.

        Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution  # noqa: E501

        :param position: The position of this CatalogIdentifier.  # noqa: E501
        :type: list[int]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this CatalogIdentifier.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this CatalogIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CatalogIdentifier.

        identifier  # noqa: E501

        :param id: The id of this CatalogIdentifier.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uses_unit(self):
        """Gets the uses_unit of this CatalogIdentifier.  # noqa: E501

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :return: The uses_unit of this CatalogIdentifier.  # noqa: E501
        :rtype: list[Unit]
        """
        return self._uses_unit

    @uses_unit.setter
    def uses_unit(self, uses_unit):
        """Sets the uses_unit of this CatalogIdentifier.

        Property used to link a variable presentation or time interval to the unit they are represented in  # noqa: E501

        :param uses_unit: The uses_unit of this CatalogIdentifier.  # noqa: E501
        :type: list[Unit]
        """

        self._uses_unit = uses_unit

    @property
    def has_step_size(self):
        """Gets the has_step_size of this CatalogIdentifier.  # noqa: E501

        Property that determines what are the increments (step size) that are commonly used to vary a parameter. This is commonly used for automatically setting up software tests. For example, if I want to set up a model and try 30 reasonable values on a parameter, I may use the default value and the step size to create the appropriate increments. If the step size is 0.1 and the default value is 0, then I will will be able to create setups: 0, 0.1, 0.2...2.9,3  # noqa: E501

        :return: The has_step_size of this CatalogIdentifier.  # noqa: E501
        :rtype: list[float]
        """
        return self._has_step_size

    @has_step_size.setter
    def has_step_size(self, has_step_size):
        """Sets the has_step_size of this CatalogIdentifier.

        Property that determines what are the increments (step size) that are commonly used to vary a parameter. This is commonly used for automatically setting up software tests. For example, if I want to set up a model and try 30 reasonable values on a parameter, I may use the default value and the step size to create the appropriate increments. If the step size is 0.1 and the default value is 0, then I will will be able to create setups: 0, 0.1, 0.2...2.9,3  # noqa: E501

        :param has_step_size: The has_step_size of this CatalogIdentifier.  # noqa: E501
        :type: list[float]
        """

        self._has_step_size = has_step_size

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
        if not isinstance(other, CatalogIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

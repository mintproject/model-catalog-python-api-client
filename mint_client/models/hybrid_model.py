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


class HybridModel(object):
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
        'has_grid': 'list[Grid]',
        'has_explanation_diagram': 'list[object]',
        'has_equation': 'list[Equation]',
        'id': 'str',
        'label': 'str',
        'type': 'list[str]',
        'has_model_category': 'list[str]'
    }

    attribute_map = {
        'has_grid': 'hasGrid',
        'has_explanation_diagram': 'hasExplanationDiagram',
        'has_equation': 'hasEquation',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'has_model_category': 'hasModelCategory'
    }

    def __init__(self, has_grid=None, has_explanation_diagram=None, has_equation=None, id=None, label=None, type=None, has_model_category=None):  # noqa: E501
        """HybridModel - a model defined in OpenAPI"""  # noqa: E501

        self._has_grid = None
        self._has_explanation_diagram = None
        self._has_equation = None
        self._id = None
        self._label = None
        self._type = None
        self._has_model_category = None
        self.discriminator = None

        if has_grid is not None:
            self.has_grid = has_grid
        else:
            if hasattr(self, '_has_grid'): del self._has_grid
            if hasattr(self.attribute_map, 'has_grid'): del self.attribute_map['has_grid']
            if hasattr(self.openapi_types, 'has_grid'): del self.openapi_types['has_grid']
        if has_explanation_diagram is not None:
            self.has_explanation_diagram = has_explanation_diagram
        else:
            if hasattr(self, '_has_explanation_diagram'): del self._has_explanation_diagram
            if hasattr(self.attribute_map, 'has_explanation_diagram'): del self.attribute_map['has_explanation_diagram']
            if hasattr(self.openapi_types, 'has_explanation_diagram'): del self.openapi_types['has_explanation_diagram']
        if has_equation is not None:
            self.has_equation = has_equation
        else:
            if hasattr(self, '_has_equation'): del self._has_equation
            if hasattr(self.attribute_map, 'has_equation'): del self.attribute_map['has_equation']
            if hasattr(self.openapi_types, 'has_equation'): del self.openapi_types['has_equation']
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
        if has_model_category is not None:
            self.has_model_category = has_model_category
        else:
            if hasattr(self, '_has_model_category'): del self._has_model_category
            if hasattr(self.attribute_map, 'has_model_category'): del self.attribute_map['has_model_category']
            if hasattr(self.openapi_types, 'has_model_category'): del self.openapi_types['has_model_category']

    @property
    def has_grid(self):
        """Gets the has_grid of this HybridModel.  # noqa: E501


        :return: The has_grid of this HybridModel.  # noqa: E501
        :rtype: list[Grid]
        """
        return self._has_grid

    @has_grid.setter
    def has_grid(self, has_grid):
        """Sets the has_grid of this HybridModel.


        :param has_grid: The has_grid of this HybridModel.  # noqa: E501
        :type: list[Grid]
        """

        self._has_grid = has_grid

    @property
    def has_explanation_diagram(self):
        """Gets the has_explanation_diagram of this HybridModel.  # noqa: E501


        :return: The has_explanation_diagram of this HybridModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_explanation_diagram

    @has_explanation_diagram.setter
    def has_explanation_diagram(self, has_explanation_diagram):
        """Sets the has_explanation_diagram of this HybridModel.


        :param has_explanation_diagram: The has_explanation_diagram of this HybridModel.  # noqa: E501
        :type: list[object]
        """

        self._has_explanation_diagram = has_explanation_diagram

    @property
    def has_equation(self):
        """Gets the has_equation of this HybridModel.  # noqa: E501


        :return: The has_equation of this HybridModel.  # noqa: E501
        :rtype: list[Equation]
        """
        return self._has_equation

    @has_equation.setter
    def has_equation(self, has_equation):
        """Sets the has_equation of this HybridModel.


        :param has_equation: The has_equation of this HybridModel.  # noqa: E501
        :type: list[Equation]
        """

        self._has_equation = has_equation

    @property
    def id(self):
        """Gets the id of this HybridModel.  # noqa: E501


        :return: The id of this HybridModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HybridModel.


        :param id: The id of this HybridModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this HybridModel.  # noqa: E501


        :return: The label of this HybridModel.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this HybridModel.


        :param label: The label of this HybridModel.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this HybridModel.  # noqa: E501


        :return: The type of this HybridModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HybridModel.


        :param type: The type of this HybridModel.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_model_category(self):
        """Gets the has_model_category of this HybridModel.  # noqa: E501


        :return: The has_model_category of this HybridModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_model_category

    @has_model_category.setter
    def has_model_category(self, has_model_category):
        """Sets the has_model_category of this HybridModel.


        :param has_model_category: The has_model_category of this HybridModel.  # noqa: E501
        :type: list[str]
        """

        self._has_model_category = has_model_category

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
        if not isinstance(other, HybridModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.3.0/index-en.html](https://w3id.org/okn/o/sdm)  # noqa: E501

    OpenAPI spec version: v1.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DatasetSpecification(object):
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
        'has_dimensionality': 'list[int]',
        'has_format': 'list[str]',
        'has_file_structure': 'list[object]',
        'description': 'list[str]',
        'has_presentation': 'list[VariablePresentation]',
        'position': 'list[int]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'has_fixed_resource': 'list[SampleResource]'
    }

    attribute_map = {
        'has_dimensionality': 'hasDimensionality',
        'has_format': 'hasFormat',
        'has_file_structure': 'hasFileStructure',
        'description': 'description',
        'has_presentation': 'hasPresentation',
        'position': 'position',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'has_fixed_resource': 'hasFixedResource'
    }

    def __init__(self, has_dimensionality=None, has_format=None, has_file_structure=None, description=None, has_presentation=None, position=None, id=None, label=None, type=None, has_fixed_resource=None):  # noqa: E501
        """DatasetSpecification - a model defined in OpenAPI"""  # noqa: E501

        self._has_dimensionality = None
        self._has_format = None
        self._has_file_structure = None
        self._description = None
        self._has_presentation = None
        self._position = None
        self._id = None
        self._label = None
        self._type = None
        self._has_fixed_resource = None
        self.discriminator = None

        if has_dimensionality is not None:
            self.has_dimensionality = has_dimensionality
        else:
            if hasattr(self, '_has_dimensionality'): del self._has_dimensionality
            if hasattr(self.attribute_map, 'has_dimensionality'): del self.attribute_map['has_dimensionality']
            if hasattr(self.openapi_types, 'has_dimensionality'): del self.openapi_types['has_dimensionality']
        if has_format is not None:
            self.has_format = has_format
        else:
            if hasattr(self, '_has_format'): del self._has_format
            if hasattr(self.attribute_map, 'has_format'): del self.attribute_map['has_format']
            if hasattr(self.openapi_types, 'has_format'): del self.openapi_types['has_format']
        if has_file_structure is not None:
            self.has_file_structure = has_file_structure
        else:
            if hasattr(self, '_has_file_structure'): del self._has_file_structure
            if hasattr(self.attribute_map, 'has_file_structure'): del self.attribute_map['has_file_structure']
            if hasattr(self.openapi_types, 'has_file_structure'): del self.openapi_types['has_file_structure']
        if description is not None:
            self.description = description
        else:
            if hasattr(self, '_description'): del self._description
            if hasattr(self.attribute_map, 'description'): del self.attribute_map['description']
            if hasattr(self.openapi_types, 'description'): del self.openapi_types['description']
        if has_presentation is not None:
            self.has_presentation = has_presentation
        else:
            if hasattr(self, '_has_presentation'): del self._has_presentation
            if hasattr(self.attribute_map, 'has_presentation'): del self.attribute_map['has_presentation']
            if hasattr(self.openapi_types, 'has_presentation'): del self.openapi_types['has_presentation']
        if position is not None:
            self.position = position
        else:
            if hasattr(self, '_position'): del self._position
            if hasattr(self.attribute_map, 'position'): del self.attribute_map['position']
            if hasattr(self.openapi_types, 'position'): del self.openapi_types['position']
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
        if has_fixed_resource is not None:
            self.has_fixed_resource = has_fixed_resource
        else:
            if hasattr(self, '_has_fixed_resource'): del self._has_fixed_resource
            if hasattr(self.attribute_map, 'has_fixed_resource'): del self.attribute_map['has_fixed_resource']
            if hasattr(self.openapi_types, 'has_fixed_resource'): del self.openapi_types['has_fixed_resource']

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this DatasetSpecification.  # noqa: E501


        :return: The has_dimensionality of this DatasetSpecification.  # noqa: E501
        :rtype: list[int]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this DatasetSpecification.


        :param has_dimensionality: The has_dimensionality of this DatasetSpecification.  # noqa: E501
        :type: list[int]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_format(self):
        """Gets the has_format of this DatasetSpecification.  # noqa: E501


        :return: The has_format of this DatasetSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this DatasetSpecification.


        :param has_format: The has_format of this DatasetSpecification.  # noqa: E501
        :type: list[str]
        """

        self._has_format = has_format

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this DatasetSpecification.  # noqa: E501


        :return: The has_file_structure of this DatasetSpecification.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this DatasetSpecification.


        :param has_file_structure: The has_file_structure of this DatasetSpecification.  # noqa: E501
        :type: list[object]
        """

        self._has_file_structure = has_file_structure

    @property
    def description(self):
        """Gets the description of this DatasetSpecification.  # noqa: E501


        :return: The description of this DatasetSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetSpecification.


        :param description: The description of this DatasetSpecification.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def has_presentation(self):
        """Gets the has_presentation of this DatasetSpecification.  # noqa: E501


        :return: The has_presentation of this DatasetSpecification.  # noqa: E501
        :rtype: list[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this DatasetSpecification.


        :param has_presentation: The has_presentation of this DatasetSpecification.  # noqa: E501
        :type: list[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def position(self):
        """Gets the position of this DatasetSpecification.  # noqa: E501


        :return: The position of this DatasetSpecification.  # noqa: E501
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DatasetSpecification.


        :param position: The position of this DatasetSpecification.  # noqa: E501
        :type: list[int]
        """

        self._position = position

    @property
    def id(self):
        """Gets the id of this DatasetSpecification.  # noqa: E501


        :return: The id of this DatasetSpecification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetSpecification.


        :param id: The id of this DatasetSpecification.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this DatasetSpecification.  # noqa: E501


        :return: The label of this DatasetSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DatasetSpecification.


        :param label: The label of this DatasetSpecification.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this DatasetSpecification.  # noqa: E501


        :return: The type of this DatasetSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DatasetSpecification.


        :param type: The type of this DatasetSpecification.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this DatasetSpecification.  # noqa: E501


        :return: The has_fixed_resource of this DatasetSpecification.  # noqa: E501
        :rtype: list[SampleResource]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this DatasetSpecification.


        :param has_fixed_resource: The has_fixed_resource of this DatasetSpecification.  # noqa: E501
        :type: list[SampleResource]
        """

        self._has_fixed_resource = has_fixed_resource

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
        if not isinstance(other, DatasetSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

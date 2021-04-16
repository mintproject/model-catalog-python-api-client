# coding: utf-8

"""
    Model Catalog

    This is the API of the Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.7.0
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
        'description': 'list[str]',
        'had_primary_source': 'list[object]',
        'has_format': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'value': 'list[object]',
        'was_derived_from_software': 'list[Software]'
    }

    attribute_map = {
        'description': 'description',
        'had_primary_source': 'hadPrimarySource',
        'has_format': 'hasFormat',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'value': 'value',
        'was_derived_from_software': 'wasDerivedFromSoftware'
    }

    def __init__(self, description=None, had_primary_source=None, has_format=None, id=None, label=None, type=None, value=None, was_derived_from_software=None):  # noqa: E501
        """Visualization - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._had_primary_source = None
        self._has_format = None
        self._id = None
        self._label = None
        self._type = None
        self._value = None
        self._was_derived_from_software = None
        self.discriminator = None

        self.description = description
        self.had_primary_source = had_primary_source
        self.has_format = has_format
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.value = value
        self.was_derived_from_software = was_derived_from_software

    @property
    def description(self):
        """Gets the description of this Visualization.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Visualization.

        small description  # noqa: E501

        :param description: The description of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def had_primary_source(self):
        """Gets the had_primary_source of this Visualization.  # noqa: E501

        Property to identify the original source of the information of the annotated resource. It could be a web page, an organization, a person, some experiment notes, etc.  # noqa: E501

        :return: The had_primary_source of this Visualization.  # noqa: E501
        :rtype: list[object]
        """
        return self._had_primary_source

    @had_primary_source.setter
    def had_primary_source(self, had_primary_source):
        """Sets the had_primary_source of this Visualization.

        Property to identify the original source of the information of the annotated resource. It could be a web page, an organization, a person, some experiment notes, etc.  # noqa: E501

        :param had_primary_source: The had_primary_source of this Visualization.  # noqa: E501
        :type: list[object]
        """

        self._had_primary_source = had_primary_source

    @property
    def has_format(self):
        """Gets the has_format of this Visualization.  # noqa: E501

        Format followed by a file. For example, txt, nc, etc.  # noqa: E501

        :return: The has_format of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this Visualization.

        Format followed by a file. For example, txt, nc, etc.  # noqa: E501

        :param has_format: The has_format of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._has_format = has_format

    @property
    def id(self):
        """Gets the id of this Visualization.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Visualization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Visualization.

        identifier  # noqa: E501

        :param id: The id of this Visualization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Visualization.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Visualization.

        short description of the resource  # noqa: E501

        :param label: The label of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Visualization.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Visualization.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Visualization.

        type of the resource  # noqa: E501

        :param type: The type of this Visualization.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this Visualization.  # noqa: E501

        Value associated to the described entity  # noqa: E501

        :return: The value of this Visualization.  # noqa: E501
        :rtype: list[object]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Visualization.

        Value associated to the described entity  # noqa: E501

        :param value: The value of this Visualization.  # noqa: E501
        :type: list[object]
        """

        self._value = value

    @property
    def was_derived_from_software(self):
        """Gets the was_derived_from_software of this Visualization.  # noqa: E501

        Property that identifies the software used to create a visualization  # noqa: E501

        :return: The was_derived_from_software of this Visualization.  # noqa: E501
        :rtype: list[Software]
        """
        return self._was_derived_from_software

    @was_derived_from_software.setter
    def was_derived_from_software(self, was_derived_from_software):
        """Sets the was_derived_from_software of this Visualization.

        Property that identifies the software used to create a visualization  # noqa: E501

        :param was_derived_from_software: The was_derived_from_software of this Visualization.  # noqa: E501
        :type: list[Software]
        """

        self._was_derived_from_software = was_derived_from_software

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
        if not isinstance(other, Visualization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

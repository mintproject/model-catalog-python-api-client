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


class SampleExecution(object):
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
        'has_execution_command': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'has_execution_command': 'hasExecutionCommand',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, description=None, has_execution_command=None, id=None, label=None, type=None):  # noqa: E501
        """SampleExecution - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._has_execution_command = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.has_execution_command = has_execution_command
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def description(self):
        """Gets the description of this SampleExecution.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this SampleExecution.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleExecution.

        small description  # noqa: E501

        :param description: The description of this SampleExecution.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def has_execution_command(self):
        """Gets the has_execution_command of this SampleExecution.  # noqa: E501

        Execution instructions on how to run the image  # noqa: E501

        :return: The has_execution_command of this SampleExecution.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_execution_command

    @has_execution_command.setter
    def has_execution_command(self, has_execution_command):
        """Sets the has_execution_command of this SampleExecution.

        Execution instructions on how to run the image  # noqa: E501

        :param has_execution_command: The has_execution_command of this SampleExecution.  # noqa: E501
        :type: list[str]
        """

        self._has_execution_command = has_execution_command

    @property
    def id(self):
        """Gets the id of this SampleExecution.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this SampleExecution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleExecution.

        identifier  # noqa: E501

        :param id: The id of this SampleExecution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SampleExecution.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this SampleExecution.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SampleExecution.

        short description of the resource  # noqa: E501

        :param label: The label of this SampleExecution.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SampleExecution.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this SampleExecution.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SampleExecution.

        type of the resource  # noqa: E501

        :param type: The type of this SampleExecution.  # noqa: E501
        :type: list[str]
        """

        self._type = type

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
        if not isinstance(other, SampleExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

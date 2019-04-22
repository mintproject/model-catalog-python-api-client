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


class ModelVersion(object):
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
        'label': 'str',
        'type': 'list[str]',
        'has_documentation': 'list[str]',
        'has_version_id': 'str',
        'has_configuration': 'list[ModelConfiguration]'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'has_documentation': 'hasDocumentation',
        'has_version_id': 'hasVersionId',
        'has_configuration': 'hasConfiguration'
    }

    def __init__(self, id=None, label=None, type=None, has_documentation=None, has_version_id=None, has_configuration=None):  # noqa: E501
        """ModelVersion - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._label = None
        self._type = None
        self._has_documentation = None
        self._has_version_id = None
        self._has_configuration = None
        self.discriminator = None

        self.id = id
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if has_documentation is not None:
            self.has_documentation = has_documentation
        if has_version_id is not None:
            self.has_version_id = has_version_id
        if has_configuration is not None:
            self.has_configuration = has_configuration

    @property
    def id(self):
        """Gets the id of this ModelVersion.  # noqa: E501


        :return: The id of this ModelVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelVersion.


        :param id: The id of this ModelVersion.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this ModelVersion.  # noqa: E501


        :return: The label of this ModelVersion.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelVersion.


        :param label: The label of this ModelVersion.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ModelVersion.  # noqa: E501


        :return: The type of this ModelVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelVersion.


        :param type: The type of this ModelVersion.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_documentation(self):
        """Gets the has_documentation of this ModelVersion.  # noqa: E501


        :return: The has_documentation of this ModelVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this ModelVersion.


        :param has_documentation: The has_documentation of this ModelVersion.  # noqa: E501
        :type: list[str]
        """

        self._has_documentation = has_documentation

    @property
    def has_version_id(self):
        """Gets the has_version_id of this ModelVersion.  # noqa: E501


        :return: The has_version_id of this ModelVersion.  # noqa: E501
        :rtype: str
        """
        return self._has_version_id

    @has_version_id.setter
    def has_version_id(self, has_version_id):
        """Sets the has_version_id of this ModelVersion.


        :param has_version_id: The has_version_id of this ModelVersion.  # noqa: E501
        :type: str
        """

        self._has_version_id = has_version_id

    @property
    def has_configuration(self):
        """Gets the has_configuration of this ModelVersion.  # noqa: E501


        :return: The has_configuration of this ModelVersion.  # noqa: E501
        :rtype: list[ModelConfiguration]
        """
        return self._has_configuration

    @has_configuration.setter
    def has_configuration(self, has_configuration):
        """Sets the has_configuration of this ModelVersion.


        :param has_configuration: The has_configuration of this ModelVersion.  # noqa: E501
        :type: list[ModelConfiguration]
        """

        self._has_configuration = has_configuration

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
        if not isinstance(other, ModelVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
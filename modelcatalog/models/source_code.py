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


class SourceCode(object):
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
        'license': 'list[str]',
        'programming_language': 'list[str]',
        'description': 'list[str]',
        'code_repository': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'license': 'license',
        'programming_language': 'programmingLanguage',
        'description': 'description',
        'code_repository': 'codeRepository',
        'id': 'id',
        'label': 'label',
        'type': 'type'
    }

    def __init__(self, license=None, programming_language=None, description=None, code_repository=None, id=None, label=None, type=None):  # noqa: E501
        """SourceCode - a model defined in OpenAPI"""  # noqa: E501

        self._license = None
        self._programming_language = None
        self._description = None
        self._code_repository = None
        self._id = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.license = license
        self.programming_language = programming_language
        self.description = description
        self.code_repository = code_repository
        if id is not None:
            self.id = id
        self.label = label
        self.type = type

    @property
    def license(self):
        """Gets the license of this SourceCode.  # noqa: E501

        License of a software component or its source code  # noqa: E501

        :return: The license of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this SourceCode.

        License of a software component or its source code  # noqa: E501

        :param license: The license of this SourceCode.  # noqa: E501
        :type: list[str]
        """

        self._license = license

    @property
    def programming_language(self):
        """Gets the programming_language of this SourceCode.  # noqa: E501

        Language used to code a software component  # noqa: E501

        :return: The programming_language of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._programming_language

    @programming_language.setter
    def programming_language(self, programming_language):
        """Sets the programming_language of this SourceCode.

        Language used to code a software component  # noqa: E501

        :param programming_language: The programming_language of this SourceCode.  # noqa: E501
        :type: list[str]
        """

        self._programming_language = programming_language

    @property
    def description(self):
        """Gets the description of this SourceCode.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SourceCode.

        small description  # noqa: E501

        :param description: The description of this SourceCode.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def code_repository(self):
        """Gets the code_repository of this SourceCode.  # noqa: E501

        URL to the code repository of a software component  # noqa: E501

        :return: The code_repository of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._code_repository

    @code_repository.setter
    def code_repository(self, code_repository):
        """Sets the code_repository of this SourceCode.

        URL to the code repository of a software component  # noqa: E501

        :param code_repository: The code_repository of this SourceCode.  # noqa: E501
        :type: list[str]
        """

        self._code_repository = code_repository

    @property
    def id(self):
        """Gets the id of this SourceCode.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this SourceCode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceCode.

        identifier  # noqa: E501

        :param id: The id of this SourceCode.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SourceCode.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SourceCode.

        short description of the resource  # noqa: E501

        :param label: The label of this SourceCode.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SourceCode.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this SourceCode.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceCode.

        type of the resource  # noqa: E501

        :param type: The type of this SourceCode.  # noqa: E501
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
        if not isinstance(other, SourceCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class Person(object):
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
        'identifier': 'list[str]',
        'website': 'list[str]',
        'description': 'list[str]',
        'id': 'str',
        'label': 'list[str]',
        'type': 'list[str]',
        'email': 'list[str]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'website': 'website',
        'description': 'description',
        'id': 'id',
        'label': 'label',
        'type': 'type',
        'email': 'email'
    }

    def __init__(self, identifier=None, website=None, description=None, id=None, label=None, type=None, email=None):  # noqa: E501
        """Person - a model defined in OpenAPI"""  # noqa: E501

        self._identifier = None
        self._website = None
        self._description = None
        self._id = None
        self._label = None
        self._type = None
        self._email = None
        self.discriminator = None

        self.identifier = identifier
        self.website = website
        self.description = description
        if id is not None:
            self.id = id
        self.label = label
        self.type = type
        self.email = email

    @property
    def identifier(self):
        """Gets the identifier of this Person.  # noqa: E501

        Identifier of the resource being described  # noqa: E501

        :return: The identifier of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Person.

        Identifier of the resource being described  # noqa: E501

        :param identifier: The identifier of this Person.  # noqa: E501
        :type: list[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Person.  # noqa: E501

        Website of the software  # noqa: E501

        :return: The website of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Person.

        Website of the software  # noqa: E501

        :param website: The website of this Person.  # noqa: E501
        :type: list[str]
        """

        self._website = website

    @property
    def description(self):
        """Gets the description of this Person.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Person.

        small description  # noqa: E501

        :param description: The description of this Person.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Person.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this Person.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.

        identifier  # noqa: E501

        :param id: The id of this Person.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Person.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Person.

        short description of the resource  # noqa: E501

        :param label: The label of this Person.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Person.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Person.

        type of the resource  # noqa: E501

        :param type: The type of this Person.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def email(self):
        """Gets the email of this Person.  # noqa: E501

        Email of a person  # noqa: E501

        :return: The email of this Person.  # noqa: E501
        :rtype: list[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Person.

        Email of a person  # noqa: E501

        :param email: The email of this Person.  # noqa: E501
        :type: list[str]
        """

        self._email = email

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
        if not isinstance(other, Person):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

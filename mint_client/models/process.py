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


class Process(object):
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
        'type': 'list[str]',
        'label': 'str',
        'influences': 'list[Process]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'label': 'label',
        'influences': 'influences'
    }

    def __init__(self, id=None, type=None, label=None, influences=None):  # noqa: E501
        """Process - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._type = None
        self._label = None
        self._influences = None
        self.discriminator = None

        self.id = id
        if type is not None:
            self.type = type
        else:
            del self._type
            del self.attribute_map['type']
            del self.openapi_types['type']
        if label is not None:
            self.label = label
        else:
            del self._label
            del self.attribute_map['label']
            del self.openapi_types['label']
        if influences is not None:
            self.influences = influences
        else:
            del self._influences
            del self.attribute_map['influences']
            del self.openapi_types['influences']

    @property
    def id(self):
        """Gets the id of this Process.  # noqa: E501


        :return: The id of this Process.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Process.


        :param id: The id of this Process.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Process.  # noqa: E501


        :return: The type of this Process.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Process.


        :param type: The type of this Process.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this Process.  # noqa: E501


        :return: The label of this Process.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Process.


        :param label: The label of this Process.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def influences(self):
        """Gets the influences of this Process.  # noqa: E501

        Property that describe the causal relationship between two processes, two variables, a process and a variable or a variable and a process  # noqa: E501

        :return: The influences of this Process.  # noqa: E501
        :rtype: list[Process]
        """
        return self._influences

    @influences.setter
    def influences(self, influences):
        """Sets the influences of this Process.

        Property that describe the causal relationship between two processes, two variables, a process and a variable or a variable and a process  # noqa: E501

        :param influences: The influences of this Process.  # noqa: E501
        :type: list[Process]
        """

        self._influences = influences

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
        if not isinstance(other, Process):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

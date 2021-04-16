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


class PointBasedGrid(object):
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
        'has_coordinate_system': 'list[str]',
        'has_data_transformation': 'list[DataTransformation]',
        'has_data_transformation_setup': 'list[DataTransformationSetup]',
        'has_dimension': 'list[str]',
        'has_dimensionality': 'list[int]',
        'has_file_structure': 'list[object]',
        'has_fixed_resource': 'list[SampleResource]',
        'has_format': 'list[str]',
        'has_presentation': 'list[VariablePresentation]',
        'has_shape': 'list[str]',
        'has_spatial_resolution': 'list[str]',
        'id': 'str',
        'is_transformed_from': 'list[DatasetSpecification]',
        'label': 'list[str]',
        'path_location': 'list[str]',
        'position': 'list[int]',
        'type': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'has_coordinate_system': 'hasCoordinateSystem',
        'has_data_transformation': 'hasDataTransformation',
        'has_data_transformation_setup': 'hasDataTransformationSetup',
        'has_dimension': 'hasDimension',
        'has_dimensionality': 'hasDimensionality',
        'has_file_structure': 'hasFileStructure',
        'has_fixed_resource': 'hasFixedResource',
        'has_format': 'hasFormat',
        'has_presentation': 'hasPresentation',
        'has_shape': 'hasShape',
        'has_spatial_resolution': 'hasSpatialResolution',
        'id': 'id',
        'is_transformed_from': 'isTransformedFrom',
        'label': 'label',
        'path_location': 'pathLocation',
        'position': 'position',
        'type': 'type'
    }

    def __init__(self, description=None, has_coordinate_system=None, has_data_transformation=None, has_data_transformation_setup=None, has_dimension=None, has_dimensionality=None, has_file_structure=None, has_fixed_resource=None, has_format=None, has_presentation=None, has_shape=None, has_spatial_resolution=None, id=None, is_transformed_from=None, label=None, path_location=None, position=None, type=None):  # noqa: E501
        """PointBasedGrid - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._has_coordinate_system = None
        self._has_data_transformation = None
        self._has_data_transformation_setup = None
        self._has_dimension = None
        self._has_dimensionality = None
        self._has_file_structure = None
        self._has_fixed_resource = None
        self._has_format = None
        self._has_presentation = None
        self._has_shape = None
        self._has_spatial_resolution = None
        self._id = None
        self._is_transformed_from = None
        self._label = None
        self._path_location = None
        self._position = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.has_coordinate_system = has_coordinate_system
        self.has_data_transformation = has_data_transformation
        self.has_data_transformation_setup = has_data_transformation_setup
        self.has_dimension = has_dimension
        self.has_dimensionality = has_dimensionality
        self.has_file_structure = has_file_structure
        self.has_fixed_resource = has_fixed_resource
        self.has_format = has_format
        self.has_presentation = has_presentation
        self.has_shape = has_shape
        self.has_spatial_resolution = has_spatial_resolution
        if id is not None:
            self.id = id
        self.is_transformed_from = is_transformed_from
        self.label = label
        self.path_location = path_location
        self.position = position
        self.type = type

    @property
    def description(self):
        """Gets the description of this PointBasedGrid.  # noqa: E501

        small description  # noqa: E501

        :return: The description of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PointBasedGrid.

        small description  # noqa: E501

        :param description: The description of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def has_coordinate_system(self):
        """Gets the has_coordinate_system of this PointBasedGrid.  # noqa: E501

        Coordinate system used in a grid  # noqa: E501

        :return: The has_coordinate_system of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_coordinate_system

    @has_coordinate_system.setter
    def has_coordinate_system(self, has_coordinate_system):
        """Sets the has_coordinate_system of this PointBasedGrid.

        Coordinate system used in a grid  # noqa: E501

        :param has_coordinate_system: The has_coordinate_system of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._has_coordinate_system = has_coordinate_system

    @property
    def has_data_transformation(self):
        """Gets the has_data_transformation of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_data_transformation of this PointBasedGrid.  # noqa: E501
        :rtype: list[DataTransformation]
        """
        return self._has_data_transformation

    @has_data_transformation.setter
    def has_data_transformation(self, has_data_transformation):
        """Sets the has_data_transformation of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_data_transformation: The has_data_transformation of this PointBasedGrid.  # noqa: E501
        :type: list[DataTransformation]
        """

        self._has_data_transformation = has_data_transformation

    @property
    def has_data_transformation_setup(self):
        """Gets the has_data_transformation_setup of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_data_transformation_setup of this PointBasedGrid.  # noqa: E501
        :rtype: list[DataTransformationSetup]
        """
        return self._has_data_transformation_setup

    @has_data_transformation_setup.setter
    def has_data_transformation_setup(self, has_data_transformation_setup):
        """Sets the has_data_transformation_setup of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_data_transformation_setup: The has_data_transformation_setup of this PointBasedGrid.  # noqa: E501
        :type: list[DataTransformationSetup]
        """

        self._has_data_transformation_setup = has_data_transformation_setup

    @property
    def has_dimension(self):
        """Gets the has_dimension of this PointBasedGrid.  # noqa: E501

        Dimension of the grid (2D, 3D)  # noqa: E501

        :return: The has_dimension of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_dimension

    @has_dimension.setter
    def has_dimension(self, has_dimension):
        """Sets the has_dimension of this PointBasedGrid.

        Dimension of the grid (2D, 3D)  # noqa: E501

        :param has_dimension: The has_dimension of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._has_dimension = has_dimension

    @property
    def has_dimensionality(self):
        """Gets the has_dimensionality of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_dimensionality of this PointBasedGrid.  # noqa: E501
        :rtype: list[int]
        """
        return self._has_dimensionality

    @has_dimensionality.setter
    def has_dimensionality(self, has_dimensionality):
        """Sets the has_dimensionality of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_dimensionality: The has_dimensionality of this PointBasedGrid.  # noqa: E501
        :type: list[int]
        """

        self._has_dimensionality = has_dimensionality

    @property
    def has_file_structure(self):
        """Gets the has_file_structure of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_file_structure of this PointBasedGrid.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_file_structure

    @has_file_structure.setter
    def has_file_structure(self, has_file_structure):
        """Sets the has_file_structure of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_file_structure: The has_file_structure of this PointBasedGrid.  # noqa: E501
        :type: list[object]
        """

        self._has_file_structure = has_file_structure

    @property
    def has_fixed_resource(self):
        """Gets the has_fixed_resource of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_fixed_resource of this PointBasedGrid.  # noqa: E501
        :rtype: list[SampleResource]
        """
        return self._has_fixed_resource

    @has_fixed_resource.setter
    def has_fixed_resource(self, has_fixed_resource):
        """Sets the has_fixed_resource of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_fixed_resource: The has_fixed_resource of this PointBasedGrid.  # noqa: E501
        :type: list[SampleResource]
        """

        self._has_fixed_resource = has_fixed_resource

    @property
    def has_format(self):
        """Gets the has_format of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_format of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_format

    @has_format.setter
    def has_format(self, has_format):
        """Sets the has_format of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_format: The has_format of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._has_format = has_format

    @property
    def has_presentation(self):
        """Gets the has_presentation of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The has_presentation of this PointBasedGrid.  # noqa: E501
        :rtype: list[VariablePresentation]
        """
        return self._has_presentation

    @has_presentation.setter
    def has_presentation(self, has_presentation):
        """Sets the has_presentation of this PointBasedGrid.

        Description not available  # noqa: E501

        :param has_presentation: The has_presentation of this PointBasedGrid.  # noqa: E501
        :type: list[VariablePresentation]
        """

        self._has_presentation = has_presentation

    @property
    def has_shape(self):
        """Gets the has_shape of this PointBasedGrid.  # noqa: E501

        Grids may be: rectangular, triangular, hexagonal, hybrid, unstructured, block structure, etc.  # noqa: E501

        :return: The has_shape of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_shape

    @has_shape.setter
    def has_shape(self, has_shape):
        """Sets the has_shape of this PointBasedGrid.

        Grids may be: rectangular, triangular, hexagonal, hybrid, unstructured, block structure, etc.  # noqa: E501

        :param has_shape: The has_shape of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._has_shape = has_shape

    @property
    def has_spatial_resolution(self):
        """Gets the has_spatial_resolution of this PointBasedGrid.  # noqa: E501

        Spatial resolution of a grid (e.g., 50m)  # noqa: E501

        :return: The has_spatial_resolution of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_spatial_resolution

    @has_spatial_resolution.setter
    def has_spatial_resolution(self, has_spatial_resolution):
        """Sets the has_spatial_resolution of this PointBasedGrid.

        Spatial resolution of a grid (e.g., 50m)  # noqa: E501

        :param has_spatial_resolution: The has_spatial_resolution of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._has_spatial_resolution = has_spatial_resolution

    @property
    def id(self):
        """Gets the id of this PointBasedGrid.  # noqa: E501

        identifier  # noqa: E501

        :return: The id of this PointBasedGrid.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PointBasedGrid.

        identifier  # noqa: E501

        :param id: The id of this PointBasedGrid.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_transformed_from(self):
        """Gets the is_transformed_from of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The is_transformed_from of this PointBasedGrid.  # noqa: E501
        :rtype: list[DatasetSpecification]
        """
        return self._is_transformed_from

    @is_transformed_from.setter
    def is_transformed_from(self, is_transformed_from):
        """Sets the is_transformed_from of this PointBasedGrid.

        Description not available  # noqa: E501

        :param is_transformed_from: The is_transformed_from of this PointBasedGrid.  # noqa: E501
        :type: list[DatasetSpecification]
        """

        self._is_transformed_from = is_transformed_from

    @property
    def label(self):
        """Gets the label of this PointBasedGrid.  # noqa: E501

        short description of the resource  # noqa: E501

        :return: The label of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PointBasedGrid.

        short description of the resource  # noqa: E501

        :param label: The label of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def path_location(self):
        """Gets the path_location of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The path_location of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._path_location

    @path_location.setter
    def path_location(self, path_location):
        """Sets the path_location of this PointBasedGrid.

        Description not available  # noqa: E501

        :param path_location: The path_location of this PointBasedGrid.  # noqa: E501
        :type: list[str]
        """

        self._path_location = path_location

    @property
    def position(self):
        """Gets the position of this PointBasedGrid.  # noqa: E501

        Description not available  # noqa: E501

        :return: The position of this PointBasedGrid.  # noqa: E501
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PointBasedGrid.

        Description not available  # noqa: E501

        :param position: The position of this PointBasedGrid.  # noqa: E501
        :type: list[int]
        """

        self._position = position

    @property
    def type(self):
        """Gets the type of this PointBasedGrid.  # noqa: E501

        type of the resource  # noqa: E501

        :return: The type of this PointBasedGrid.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PointBasedGrid.

        type of the resource  # noqa: E501

        :param type: The type of this PointBasedGrid.  # noqa: E501
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
        if not isinstance(other, PointBasedGrid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

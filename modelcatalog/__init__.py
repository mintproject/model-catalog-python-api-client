# coding: utf-8

# flake8: noqa

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.3.0/index-en.html](https://w3id.org/okn/o/sdm)  # noqa: E501

    OpenAPI spec version: v1.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.7.3"

# import apis into sdk package
from modelcatalog.api.causal_diagram_api import CausalDiagramApi
from modelcatalog.api.configuration_setup_api import ConfigurationSetupApi
from modelcatalog.api.dataset_specification_api import DatasetSpecificationApi
from modelcatalog.api.empirical_model_api import EmpiricalModelApi
from modelcatalog.api.emulator_api import EmulatorApi
from modelcatalog.api.equation_api import EquationApi
from modelcatalog.api.farming_practices_api import FarmingPracticesApi
from modelcatalog.api.funding_information_api import FundingInformationApi
from modelcatalog.api.geo_coordinates_api import GeoCoordinatesApi
from modelcatalog.api.geo_shape_api import GeoShapeApi
from modelcatalog.api.grid_api import GridApi
from modelcatalog.api.hybrid_model_api import HybridModelApi
from modelcatalog.api.icasa_variable_api import ICASAVariableApi
from modelcatalog.api.image_api import ImageApi
from modelcatalog.api.intervention_api import InterventionApi
from modelcatalog.api.model_api import ModelApi
from modelcatalog.api.model_configuration_api import ModelConfigurationApi
from modelcatalog.api.model_configuration_setup_api import ModelConfigurationSetupApi
from modelcatalog.api.numerical_index_api import NumericalIndexApi
from modelcatalog.api.organization_api import OrganizationApi
from modelcatalog.api.parameter_api import ParameterApi
from modelcatalog.api.person_api import PersonApi
from modelcatalog.api.point_based_grid_api import PointBasedGridApi
from modelcatalog.api.process_api import ProcessApi
from modelcatalog.api.region_api import RegionApi
from modelcatalog.api.svo_variable_api import SVOVariableApi
from modelcatalog.api.sample_collection_api import SampleCollectionApi
from modelcatalog.api.sample_execution_api import SampleExecutionApi
from modelcatalog.api.sample_resource_api import SampleResourceApi
from modelcatalog.api.software_api import SoftwareApi
from modelcatalog.api.software_configuration_api import SoftwareConfigurationApi
from modelcatalog.api.software_image_api import SoftwareImageApi
from modelcatalog.api.software_version_api import SoftwareVersionApi
from modelcatalog.api.source_code_api import SourceCodeApi
from modelcatalog.api.spatial_resolution_api import SpatialResolutionApi
from modelcatalog.api.spatially_distributed_grid_api import SpatiallyDistributedGridApi
from modelcatalog.api.standard_variable_api import StandardVariableApi
from modelcatalog.api.subsidy_api import SubsidyApi
from modelcatalog.api.theory_guided_model_api import TheoryGuidedModelApi
from modelcatalog.api.time_interval_api import TimeIntervalApi
from modelcatalog.api.unit_api import UnitApi
from modelcatalog.api.variable_api import VariableApi
from modelcatalog.api.variable_presentation_api import VariablePresentationApi
from modelcatalog.api.visualization_api import VisualizationApi
from modelcatalog.api.default_api import DefaultApi

# import ApiClient
from modelcatalog.api_client import ApiClient
from modelcatalog.configuration import Configuration
from modelcatalog.exceptions import OpenApiException
from modelcatalog.exceptions import ApiTypeError
from modelcatalog.exceptions import ApiValueError
from modelcatalog.exceptions import ApiKeyError
from modelcatalog.exceptions import ApiException
# import models into sdk package
from modelcatalog.models.causal_diagram import CausalDiagram
from modelcatalog.models.configuration_setup import ConfigurationSetup
from modelcatalog.models.dataset_specification import DatasetSpecification
from modelcatalog.models.empirical_model import EmpiricalModel
from modelcatalog.models.emulator import Emulator
from modelcatalog.models.equation import Equation
from modelcatalog.models.farming_practices import FarmingPractices
from modelcatalog.models.funding_information import FundingInformation
from modelcatalog.models.geo_coordinates import GeoCoordinates
from modelcatalog.models.geo_shape import GeoShape
from modelcatalog.models.grid import Grid
from modelcatalog.models.hybrid_model import HybridModel
from modelcatalog.models.icasa_variable import ICASAVariable
from modelcatalog.models.image import Image
from modelcatalog.models.intervention import Intervention
from modelcatalog.models.model import Model
from modelcatalog.models.model_configuration import ModelConfiguration
from modelcatalog.models.model_configuration_setup import ModelConfigurationSetup
from modelcatalog.models.numerical_index import NumericalIndex
from modelcatalog.models.organization import Organization
from modelcatalog.models.parameter import Parameter
from modelcatalog.models.person import Person
from modelcatalog.models.point_based_grid import PointBasedGrid
from modelcatalog.models.process import Process
from modelcatalog.models.region import Region
from modelcatalog.models.svo_variable import SVOVariable
from modelcatalog.models.sample_collection import SampleCollection
from modelcatalog.models.sample_execution import SampleExecution
from modelcatalog.models.sample_resource import SampleResource
from modelcatalog.models.software import Software
from modelcatalog.models.software_configuration import SoftwareConfiguration
from modelcatalog.models.software_image import SoftwareImage
from modelcatalog.models.software_version import SoftwareVersion
from modelcatalog.models.source_code import SourceCode
from modelcatalog.models.spatial_resolution import SpatialResolution
from modelcatalog.models.spatially_distributed_grid import SpatiallyDistributedGrid
from modelcatalog.models.standard_variable import StandardVariable
from modelcatalog.models.subsidy import Subsidy
from modelcatalog.models.theory_guided_model import TheoryGuidedModel
from modelcatalog.models.time_interval import TimeInterval
from modelcatalog.models.unit import Unit
from modelcatalog.models.user import User
from modelcatalog.models.variable import Variable
from modelcatalog.models.variable_presentation import VariablePresentation
from modelcatalog.models.visualization import Visualization


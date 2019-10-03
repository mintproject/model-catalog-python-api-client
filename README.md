# mint-api
This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.0.0
- Package version: 1.0.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install mint-api
```
(you may need to run `pip` with root permission: `sudo pip install mint-api`)

Then import the package:
```python
import mint_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mint_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mint_client
from mint_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = mint_client.CausalDiagramApi(mint_client.ApiClient(configuration))
username = 'username_example' # str | Username to query (optional)

try:
    # List all CausalDiagram entities
    api_response = api_instance.causaldiagrams_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CausalDiagramApi->causaldiagrams_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.models.mint.isi.edu/v1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CausalDiagramApi* | [**causaldiagrams_get**](docs/CausalDiagramApi.md#causaldiagrams_get) | **GET** /causaldiagrams | List all CausalDiagram entities
*CausalDiagramApi* | [**causaldiagrams_id_delete**](docs/CausalDiagramApi.md#causaldiagrams_id_delete) | **DELETE** /causaldiagrams/{id} | Delete a CausalDiagram
*CausalDiagramApi* | [**causaldiagrams_id_get**](docs/CausalDiagramApi.md#causaldiagrams_id_get) | **GET** /causaldiagrams/{id} | Get a CausalDiagram
*CausalDiagramApi* | [**causaldiagrams_id_put**](docs/CausalDiagramApi.md#causaldiagrams_id_put) | **PUT** /causaldiagrams/{id} | Update a CausalDiagram
*CausalDiagramApi* | [**causaldiagrams_post**](docs/CausalDiagramApi.md#causaldiagrams_post) | **POST** /causaldiagrams | Create a CausalDiagram
*DatasetSpecificationApi* | [**datasetspecifications_get**](docs/DatasetSpecificationApi.md#datasetspecifications_get) | **GET** /datasetspecifications | List all DatasetSpecification entities
*DatasetSpecificationApi* | [**datasetspecifications_id_delete**](docs/DatasetSpecificationApi.md#datasetspecifications_id_delete) | **DELETE** /datasetspecifications/{id} | Delete a DatasetSpecification
*DatasetSpecificationApi* | [**datasetspecifications_id_get**](docs/DatasetSpecificationApi.md#datasetspecifications_id_get) | **GET** /datasetspecifications/{id} | Get a DatasetSpecification
*DatasetSpecificationApi* | [**datasetspecifications_id_put**](docs/DatasetSpecificationApi.md#datasetspecifications_id_put) | **PUT** /datasetspecifications/{id} | Update a DatasetSpecification
*DatasetSpecificationApi* | [**datasetspecifications_post**](docs/DatasetSpecificationApi.md#datasetspecifications_post) | **POST** /datasetspecifications | Create a DatasetSpecification
*EmpiricalModelApi* | [**empiricalmodels_get**](docs/EmpiricalModelApi.md#empiricalmodels_get) | **GET** /empiricalmodels | List all EmpiricalModel entities
*EmpiricalModelApi* | [**empiricalmodels_id_delete**](docs/EmpiricalModelApi.md#empiricalmodels_id_delete) | **DELETE** /empiricalmodels/{id} | Delete a EmpiricalModel
*EmpiricalModelApi* | [**empiricalmodels_id_get**](docs/EmpiricalModelApi.md#empiricalmodels_id_get) | **GET** /empiricalmodels/{id} | Get a EmpiricalModel
*EmpiricalModelApi* | [**empiricalmodels_id_put**](docs/EmpiricalModelApi.md#empiricalmodels_id_put) | **PUT** /empiricalmodels/{id} | Update a EmpiricalModel
*EmpiricalModelApi* | [**empiricalmodels_post**](docs/EmpiricalModelApi.md#empiricalmodels_post) | **POST** /empiricalmodels | Create a EmpiricalModel
*EmulatorApi* | [**emulators_get**](docs/EmulatorApi.md#emulators_get) | **GET** /emulators | List all Emulator entities
*EmulatorApi* | [**emulators_id_delete**](docs/EmulatorApi.md#emulators_id_delete) | **DELETE** /emulators/{id} | Delete a Emulator
*EmulatorApi* | [**emulators_id_get**](docs/EmulatorApi.md#emulators_id_get) | **GET** /emulators/{id} | Get a Emulator
*EmulatorApi* | [**emulators_id_put**](docs/EmulatorApi.md#emulators_id_put) | **PUT** /emulators/{id} | Update a Emulator
*EmulatorApi* | [**emulators_post**](docs/EmulatorApi.md#emulators_post) | **POST** /emulators | Create a Emulator
*EquationApi* | [**equations_get**](docs/EquationApi.md#equations_get) | **GET** /equations | List all Equation entities
*EquationApi* | [**equations_id_delete**](docs/EquationApi.md#equations_id_delete) | **DELETE** /equations/{id} | Delete a Equation
*EquationApi* | [**equations_id_get**](docs/EquationApi.md#equations_id_get) | **GET** /equations/{id} | Get a Equation
*EquationApi* | [**equations_id_put**](docs/EquationApi.md#equations_id_put) | **PUT** /equations/{id} | Update a Equation
*EquationApi* | [**equations_post**](docs/EquationApi.md#equations_post) | **POST** /equations | Create a Equation
*GeoCoordinatesApi* | [**geocoordinatess_get**](docs/GeoCoordinatesApi.md#geocoordinatess_get) | **GET** /geocoordinatess | List all GeoCoordinates entities
*GeoCoordinatesApi* | [**geocoordinatess_id_delete**](docs/GeoCoordinatesApi.md#geocoordinatess_id_delete) | **DELETE** /geocoordinatess/{id} | Delete a GeoCoordinates
*GeoCoordinatesApi* | [**geocoordinatess_id_get**](docs/GeoCoordinatesApi.md#geocoordinatess_id_get) | **GET** /geocoordinatess/{id} | Get a GeoCoordinates
*GeoCoordinatesApi* | [**geocoordinatess_id_put**](docs/GeoCoordinatesApi.md#geocoordinatess_id_put) | **PUT** /geocoordinatess/{id} | Update a GeoCoordinates
*GeoCoordinatesApi* | [**geocoordinatess_post**](docs/GeoCoordinatesApi.md#geocoordinatess_post) | **POST** /geocoordinatess | Create a GeoCoordinates
*GeoShapeApi* | [**geoshapes_get**](docs/GeoShapeApi.md#geoshapes_get) | **GET** /geoshapes | List all GeoShape entities
*GeoShapeApi* | [**geoshapes_id_delete**](docs/GeoShapeApi.md#geoshapes_id_delete) | **DELETE** /geoshapes/{id} | Delete a GeoShape
*GeoShapeApi* | [**geoshapes_id_get**](docs/GeoShapeApi.md#geoshapes_id_get) | **GET** /geoshapes/{id} | Get a GeoShape
*GeoShapeApi* | [**geoshapes_id_put**](docs/GeoShapeApi.md#geoshapes_id_put) | **PUT** /geoshapes/{id} | Update a GeoShape
*GeoShapeApi* | [**geoshapes_post**](docs/GeoShapeApi.md#geoshapes_post) | **POST** /geoshapes | Create a GeoShape
*GridApi* | [**grids_get**](docs/GridApi.md#grids_get) | **GET** /grids | List all Grid entities
*GridApi* | [**grids_id_delete**](docs/GridApi.md#grids_id_delete) | **DELETE** /grids/{id} | Delete a Grid
*GridApi* | [**grids_id_get**](docs/GridApi.md#grids_id_get) | **GET** /grids/{id} | Get a Grid
*GridApi* | [**grids_id_put**](docs/GridApi.md#grids_id_put) | **PUT** /grids/{id} | Update a Grid
*GridApi* | [**grids_post**](docs/GridApi.md#grids_post) | **POST** /grids | Create a Grid
*HybridModelApi* | [**hybridmodels_get**](docs/HybridModelApi.md#hybridmodels_get) | **GET** /hybridmodels | List all HybridModel entities
*HybridModelApi* | [**hybridmodels_id_delete**](docs/HybridModelApi.md#hybridmodels_id_delete) | **DELETE** /hybridmodels/{id} | Delete a HybridModel
*HybridModelApi* | [**hybridmodels_id_get**](docs/HybridModelApi.md#hybridmodels_id_get) | **GET** /hybridmodels/{id} | Get a HybridModel
*HybridModelApi* | [**hybridmodels_id_put**](docs/HybridModelApi.md#hybridmodels_id_put) | **PUT** /hybridmodels/{id} | Update a HybridModel
*HybridModelApi* | [**hybridmodels_post**](docs/HybridModelApi.md#hybridmodels_post) | **POST** /hybridmodels | Create a HybridModel
*ICASAVariableApi* | [**icasavariables_get**](docs/ICASAVariableApi.md#icasavariables_get) | **GET** /icasavariables | List all ICASAVariable entities
*ICASAVariableApi* | [**icasavariables_id_delete**](docs/ICASAVariableApi.md#icasavariables_id_delete) | **DELETE** /icasavariables/{id} | Delete a ICASAVariable
*ICASAVariableApi* | [**icasavariables_id_get**](docs/ICASAVariableApi.md#icasavariables_id_get) | **GET** /icasavariables/{id} | Get a ICASAVariable
*ICASAVariableApi* | [**icasavariables_id_put**](docs/ICASAVariableApi.md#icasavariables_id_put) | **PUT** /icasavariables/{id} | Update a ICASAVariable
*ICASAVariableApi* | [**icasavariables_post**](docs/ICASAVariableApi.md#icasavariables_post) | **POST** /icasavariables | Create a ICASAVariable
*ImageApi* | [**images_get**](docs/ImageApi.md#images_get) | **GET** /images | List all Image entities
*ImageApi* | [**images_id_delete**](docs/ImageApi.md#images_id_delete) | **DELETE** /images/{id} | Delete a Image
*ImageApi* | [**images_id_get**](docs/ImageApi.md#images_id_get) | **GET** /images/{id} | Get a Image
*ImageApi* | [**images_id_put**](docs/ImageApi.md#images_id_put) | **PUT** /images/{id} | Update a Image
*ImageApi* | [**images_post**](docs/ImageApi.md#images_post) | **POST** /images | Create a Image
*ModelApi* | [**models_get**](docs/ModelApi.md#models_get) | **GET** /models | List all Model entities
*ModelApi* | [**models_id_delete**](docs/ModelApi.md#models_id_delete) | **DELETE** /models/{id} | Delete a Model
*ModelApi* | [**models_id_get**](docs/ModelApi.md#models_id_get) | **GET** /models/{id} | Get a Model
*ModelApi* | [**models_id_put**](docs/ModelApi.md#models_id_put) | **PUT** /models/{id} | Update a Model
*ModelApi* | [**models_post**](docs/ModelApi.md#models_post) | **POST** /models | Create a Model
*ModelConfigurationApi* | [**modelconfigurations_get**](docs/ModelConfigurationApi.md#modelconfigurations_get) | **GET** /modelconfigurations | List all ModelConfiguration entities
*ModelConfigurationApi* | [**modelconfigurations_id_delete**](docs/ModelConfigurationApi.md#modelconfigurations_id_delete) | **DELETE** /modelconfigurations/{id} | Delete a ModelConfiguration
*ModelConfigurationApi* | [**modelconfigurations_id_get**](docs/ModelConfigurationApi.md#modelconfigurations_id_get) | **GET** /modelconfigurations/{id} | Get a ModelConfiguration
*ModelConfigurationApi* | [**modelconfigurations_id_put**](docs/ModelConfigurationApi.md#modelconfigurations_id_put) | **PUT** /modelconfigurations/{id} | Update a ModelConfiguration
*ModelConfigurationApi* | [**modelconfigurations_post**](docs/ModelConfigurationApi.md#modelconfigurations_post) | **POST** /modelconfigurations | Create a ModelConfiguration
*OrganizationApi* | [**organizations_get**](docs/OrganizationApi.md#organizations_get) | **GET** /organizations | List all Organization entities
*OrganizationApi* | [**organizations_id_delete**](docs/OrganizationApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete a Organization
*OrganizationApi* | [**organizations_id_get**](docs/OrganizationApi.md#organizations_id_get) | **GET** /organizations/{id} | Get a Organization
*OrganizationApi* | [**organizations_id_put**](docs/OrganizationApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update a Organization
*OrganizationApi* | [**organizations_post**](docs/OrganizationApi.md#organizations_post) | **POST** /organizations | Create a Organization
*ParameterApi* | [**parameters_get**](docs/ParameterApi.md#parameters_get) | **GET** /parameters | List all Parameter entities
*ParameterApi* | [**parameters_id_delete**](docs/ParameterApi.md#parameters_id_delete) | **DELETE** /parameters/{id} | Delete a Parameter
*ParameterApi* | [**parameters_id_get**](docs/ParameterApi.md#parameters_id_get) | **GET** /parameters/{id} | Get a Parameter
*ParameterApi* | [**parameters_id_put**](docs/ParameterApi.md#parameters_id_put) | **PUT** /parameters/{id} | Update a Parameter
*ParameterApi* | [**parameters_post**](docs/ParameterApi.md#parameters_post) | **POST** /parameters | Create a Parameter
*PersonApi* | [**persons_get**](docs/PersonApi.md#persons_get) | **GET** /persons | List all Person entities
*PersonApi* | [**persons_id_delete**](docs/PersonApi.md#persons_id_delete) | **DELETE** /persons/{id} | Delete a Person
*PersonApi* | [**persons_id_get**](docs/PersonApi.md#persons_id_get) | **GET** /persons/{id} | Get a Person
*PersonApi* | [**persons_id_put**](docs/PersonApi.md#persons_id_put) | **PUT** /persons/{id} | Update a Person
*PersonApi* | [**persons_post**](docs/PersonApi.md#persons_post) | **POST** /persons | Create a Person
*PointBasedGridApi* | [**pointbasedgrids_get**](docs/PointBasedGridApi.md#pointbasedgrids_get) | **GET** /pointbasedgrids | List all PointBasedGrid entities
*PointBasedGridApi* | [**pointbasedgrids_id_delete**](docs/PointBasedGridApi.md#pointbasedgrids_id_delete) | **DELETE** /pointbasedgrids/{id} | Delete a PointBasedGrid
*PointBasedGridApi* | [**pointbasedgrids_id_get**](docs/PointBasedGridApi.md#pointbasedgrids_id_get) | **GET** /pointbasedgrids/{id} | Get a PointBasedGrid
*PointBasedGridApi* | [**pointbasedgrids_id_put**](docs/PointBasedGridApi.md#pointbasedgrids_id_put) | **PUT** /pointbasedgrids/{id} | Update a PointBasedGrid
*PointBasedGridApi* | [**pointbasedgrids_post**](docs/PointBasedGridApi.md#pointbasedgrids_post) | **POST** /pointbasedgrids | Create a PointBasedGrid
*ProcessApi* | [**processs_get**](docs/ProcessApi.md#processs_get) | **GET** /processs | List all Process entities
*ProcessApi* | [**processs_id_delete**](docs/ProcessApi.md#processs_id_delete) | **DELETE** /processs/{id} | Delete a Process
*ProcessApi* | [**processs_id_get**](docs/ProcessApi.md#processs_id_get) | **GET** /processs/{id} | Get a Process
*ProcessApi* | [**processs_id_put**](docs/ProcessApi.md#processs_id_put) | **PUT** /processs/{id} | Update a Process
*ProcessApi* | [**processs_post**](docs/ProcessApi.md#processs_post) | **POST** /processs | Create a Process
*RegionApi* | [**regions_get**](docs/RegionApi.md#regions_get) | **GET** /regions | List all Region entities
*RegionApi* | [**regions_id_delete**](docs/RegionApi.md#regions_id_delete) | **DELETE** /regions/{id} | Delete a Region
*RegionApi* | [**regions_id_get**](docs/RegionApi.md#regions_id_get) | **GET** /regions/{id} | Get a Region
*RegionApi* | [**regions_id_put**](docs/RegionApi.md#regions_id_put) | **PUT** /regions/{id} | Update a Region
*RegionApi* | [**regions_post**](docs/RegionApi.md#regions_post) | **POST** /regions | Create a Region
*SVOVariableApi* | [**svovariables_get**](docs/SVOVariableApi.md#svovariables_get) | **GET** /svovariables | List all SVOVariable entities
*SVOVariableApi* | [**svovariables_id_delete**](docs/SVOVariableApi.md#svovariables_id_delete) | **DELETE** /svovariables/{id} | Delete a SVOVariable
*SVOVariableApi* | [**svovariables_id_get**](docs/SVOVariableApi.md#svovariables_id_get) | **GET** /svovariables/{id} | Get a SVOVariable
*SVOVariableApi* | [**svovariables_id_put**](docs/SVOVariableApi.md#svovariables_id_put) | **PUT** /svovariables/{id} | Update a SVOVariable
*SVOVariableApi* | [**svovariables_post**](docs/SVOVariableApi.md#svovariables_post) | **POST** /svovariables | Create a SVOVariable
*SampleExecutionApi* | [**sampleexecutions_get**](docs/SampleExecutionApi.md#sampleexecutions_get) | **GET** /sampleexecutions | List all SampleExecution entities
*SampleExecutionApi* | [**sampleexecutions_id_delete**](docs/SampleExecutionApi.md#sampleexecutions_id_delete) | **DELETE** /sampleexecutions/{id} | Delete a SampleExecution
*SampleExecutionApi* | [**sampleexecutions_id_get**](docs/SampleExecutionApi.md#sampleexecutions_id_get) | **GET** /sampleexecutions/{id} | Get a SampleExecution
*SampleExecutionApi* | [**sampleexecutions_id_put**](docs/SampleExecutionApi.md#sampleexecutions_id_put) | **PUT** /sampleexecutions/{id} | Update a SampleExecution
*SampleExecutionApi* | [**sampleexecutions_post**](docs/SampleExecutionApi.md#sampleexecutions_post) | **POST** /sampleexecutions | Create a SampleExecution
*SampleResourceApi* | [**sampleresources_get**](docs/SampleResourceApi.md#sampleresources_get) | **GET** /sampleresources | List all SampleResource entities
*SampleResourceApi* | [**sampleresources_id_delete**](docs/SampleResourceApi.md#sampleresources_id_delete) | **DELETE** /sampleresources/{id} | Delete a SampleResource
*SampleResourceApi* | [**sampleresources_id_get**](docs/SampleResourceApi.md#sampleresources_id_get) | **GET** /sampleresources/{id} | Get a SampleResource
*SampleResourceApi* | [**sampleresources_id_put**](docs/SampleResourceApi.md#sampleresources_id_put) | **PUT** /sampleresources/{id} | Update a SampleResource
*SampleResourceApi* | [**sampleresources_post**](docs/SampleResourceApi.md#sampleresources_post) | **POST** /sampleresources | Create a SampleResource
*SoftwareApi* | [**softwares_get**](docs/SoftwareApi.md#softwares_get) | **GET** /softwares | List all Software entities
*SoftwareApi* | [**softwares_id_delete**](docs/SoftwareApi.md#softwares_id_delete) | **DELETE** /softwares/{id} | Delete a Software
*SoftwareApi* | [**softwares_id_get**](docs/SoftwareApi.md#softwares_id_get) | **GET** /softwares/{id} | Get a Software
*SoftwareApi* | [**softwares_id_put**](docs/SoftwareApi.md#softwares_id_put) | **PUT** /softwares/{id} | Update a Software
*SoftwareApi* | [**softwares_post**](docs/SoftwareApi.md#softwares_post) | **POST** /softwares | Create a Software
*SoftwareConfigurationApi* | [**softwareconfigurations_get**](docs/SoftwareConfigurationApi.md#softwareconfigurations_get) | **GET** /softwareconfigurations | List all SoftwareConfiguration entities
*SoftwareConfigurationApi* | [**softwareconfigurations_id_delete**](docs/SoftwareConfigurationApi.md#softwareconfigurations_id_delete) | **DELETE** /softwareconfigurations/{id} | Delete a SoftwareConfiguration
*SoftwareConfigurationApi* | [**softwareconfigurations_id_get**](docs/SoftwareConfigurationApi.md#softwareconfigurations_id_get) | **GET** /softwareconfigurations/{id} | Get a SoftwareConfiguration
*SoftwareConfigurationApi* | [**softwareconfigurations_id_put**](docs/SoftwareConfigurationApi.md#softwareconfigurations_id_put) | **PUT** /softwareconfigurations/{id} | Update a SoftwareConfiguration
*SoftwareConfigurationApi* | [**softwareconfigurations_post**](docs/SoftwareConfigurationApi.md#softwareconfigurations_post) | **POST** /softwareconfigurations | Create a SoftwareConfiguration
*SoftwareImageApi* | [**softwareimages_get**](docs/SoftwareImageApi.md#softwareimages_get) | **GET** /softwareimages | List all SoftwareImage entities
*SoftwareImageApi* | [**softwareimages_id_delete**](docs/SoftwareImageApi.md#softwareimages_id_delete) | **DELETE** /softwareimages/{id} | Delete a SoftwareImage
*SoftwareImageApi* | [**softwareimages_id_get**](docs/SoftwareImageApi.md#softwareimages_id_get) | **GET** /softwareimages/{id} | Get a SoftwareImage
*SoftwareImageApi* | [**softwareimages_id_put**](docs/SoftwareImageApi.md#softwareimages_id_put) | **PUT** /softwareimages/{id} | Update a SoftwareImage
*SoftwareImageApi* | [**softwareimages_post**](docs/SoftwareImageApi.md#softwareimages_post) | **POST** /softwareimages | Create a SoftwareImage
*SoftwareVersionApi* | [**softwareversions_get**](docs/SoftwareVersionApi.md#softwareversions_get) | **GET** /softwareversions | List all SoftwareVersion entities
*SoftwareVersionApi* | [**softwareversions_id_delete**](docs/SoftwareVersionApi.md#softwareversions_id_delete) | **DELETE** /softwareversions/{id} | Delete a SoftwareVersion
*SoftwareVersionApi* | [**softwareversions_id_get**](docs/SoftwareVersionApi.md#softwareversions_id_get) | **GET** /softwareversions/{id} | Get a SoftwareVersion
*SoftwareVersionApi* | [**softwareversions_id_put**](docs/SoftwareVersionApi.md#softwareversions_id_put) | **PUT** /softwareversions/{id} | Update a SoftwareVersion
*SoftwareVersionApi* | [**softwareversions_post**](docs/SoftwareVersionApi.md#softwareversions_post) | **POST** /softwareversions | Create a SoftwareVersion
*SourceCodeApi* | [**sourcecodes_get**](docs/SourceCodeApi.md#sourcecodes_get) | **GET** /sourcecodes | List all SourceCode entities
*SourceCodeApi* | [**sourcecodes_id_delete**](docs/SourceCodeApi.md#sourcecodes_id_delete) | **DELETE** /sourcecodes/{id} | Delete a SourceCode
*SourceCodeApi* | [**sourcecodes_id_get**](docs/SourceCodeApi.md#sourcecodes_id_get) | **GET** /sourcecodes/{id} | Get a SourceCode
*SourceCodeApi* | [**sourcecodes_id_put**](docs/SourceCodeApi.md#sourcecodes_id_put) | **PUT** /sourcecodes/{id} | Update a SourceCode
*SourceCodeApi* | [**sourcecodes_post**](docs/SourceCodeApi.md#sourcecodes_post) | **POST** /sourcecodes | Create a SourceCode
*SpatialResolutionApi* | [**spatialresolutions_get**](docs/SpatialResolutionApi.md#spatialresolutions_get) | **GET** /spatialresolutions | List all SpatialResolution entities
*SpatialResolutionApi* | [**spatialresolutions_id_delete**](docs/SpatialResolutionApi.md#spatialresolutions_id_delete) | **DELETE** /spatialresolutions/{id} | Delete a SpatialResolution
*SpatialResolutionApi* | [**spatialresolutions_id_get**](docs/SpatialResolutionApi.md#spatialresolutions_id_get) | **GET** /spatialresolutions/{id} | Get a SpatialResolution
*SpatialResolutionApi* | [**spatialresolutions_id_put**](docs/SpatialResolutionApi.md#spatialresolutions_id_put) | **PUT** /spatialresolutions/{id} | Update a SpatialResolution
*SpatialResolutionApi* | [**spatialresolutions_post**](docs/SpatialResolutionApi.md#spatialresolutions_post) | **POST** /spatialresolutions | Create a SpatialResolution
*SpatiallyDistributedGridApi* | [**spatiallydistributedgrids_get**](docs/SpatiallyDistributedGridApi.md#spatiallydistributedgrids_get) | **GET** /spatiallydistributedgrids | List all SpatiallyDistributedGrid entities
*SpatiallyDistributedGridApi* | [**spatiallydistributedgrids_id_delete**](docs/SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_delete) | **DELETE** /spatiallydistributedgrids/{id} | Delete a SpatiallyDistributedGrid
*SpatiallyDistributedGridApi* | [**spatiallydistributedgrids_id_get**](docs/SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_get) | **GET** /spatiallydistributedgrids/{id} | Get a SpatiallyDistributedGrid
*SpatiallyDistributedGridApi* | [**spatiallydistributedgrids_id_put**](docs/SpatiallyDistributedGridApi.md#spatiallydistributedgrids_id_put) | **PUT** /spatiallydistributedgrids/{id} | Update a SpatiallyDistributedGrid
*SpatiallyDistributedGridApi* | [**spatiallydistributedgrids_post**](docs/SpatiallyDistributedGridApi.md#spatiallydistributedgrids_post) | **POST** /spatiallydistributedgrids | Create a SpatiallyDistributedGrid
*StandardVariableApi* | [**standardvariables_get**](docs/StandardVariableApi.md#standardvariables_get) | **GET** /standardvariables | List all StandardVariable entities
*StandardVariableApi* | [**standardvariables_id_delete**](docs/StandardVariableApi.md#standardvariables_id_delete) | **DELETE** /standardvariables/{id} | Delete a StandardVariable
*StandardVariableApi* | [**standardvariables_id_get**](docs/StandardVariableApi.md#standardvariables_id_get) | **GET** /standardvariables/{id} | Get a StandardVariable
*StandardVariableApi* | [**standardvariables_id_put**](docs/StandardVariableApi.md#standardvariables_id_put) | **PUT** /standardvariables/{id} | Update a StandardVariable
*StandardVariableApi* | [**standardvariables_post**](docs/StandardVariableApi.md#standardvariables_post) | **POST** /standardvariables | Create a StandardVariable
*TheoryGuidedModelApi* | [**theory_guidedmodels_get**](docs/TheoryGuidedModelApi.md#theory_guidedmodels_get) | **GET** /theory-guidedmodels | List all Theory-GuidedModel entities
*TheoryGuidedModelApi* | [**theory_guidedmodels_id_delete**](docs/TheoryGuidedModelApi.md#theory_guidedmodels_id_delete) | **DELETE** /theory-guidedmodels/{id} | Delete a Theory-GuidedModel
*TheoryGuidedModelApi* | [**theory_guidedmodels_id_get**](docs/TheoryGuidedModelApi.md#theory_guidedmodels_id_get) | **GET** /theory-guidedmodels/{id} | Get a Theory-GuidedModel
*TheoryGuidedModelApi* | [**theory_guidedmodels_id_put**](docs/TheoryGuidedModelApi.md#theory_guidedmodels_id_put) | **PUT** /theory-guidedmodels/{id} | Update a Theory-GuidedModel
*TheoryGuidedModelApi* | [**theory_guidedmodels_post**](docs/TheoryGuidedModelApi.md#theory_guidedmodels_post) | **POST** /theory-guidedmodels | Create a Theory-GuidedModel
*TimeIntervalApi* | [**timeintervals_get**](docs/TimeIntervalApi.md#timeintervals_get) | **GET** /timeintervals | List all TimeInterval entities
*TimeIntervalApi* | [**timeintervals_id_delete**](docs/TimeIntervalApi.md#timeintervals_id_delete) | **DELETE** /timeintervals/{id} | Delete a TimeInterval
*TimeIntervalApi* | [**timeintervals_id_get**](docs/TimeIntervalApi.md#timeintervals_id_get) | **GET** /timeintervals/{id} | Get a TimeInterval
*TimeIntervalApi* | [**timeintervals_id_put**](docs/TimeIntervalApi.md#timeintervals_id_put) | **PUT** /timeintervals/{id} | Update a TimeInterval
*TimeIntervalApi* | [**timeintervals_post**](docs/TimeIntervalApi.md#timeintervals_post) | **POST** /timeintervals | Create a TimeInterval
*UnitApi* | [**units_get**](docs/UnitApi.md#units_get) | **GET** /units | List all Unit entities
*UnitApi* | [**units_id_delete**](docs/UnitApi.md#units_id_delete) | **DELETE** /units/{id} | Delete a Unit
*UnitApi* | [**units_id_get**](docs/UnitApi.md#units_id_get) | **GET** /units/{id} | Get a Unit
*UnitApi* | [**units_id_put**](docs/UnitApi.md#units_id_put) | **PUT** /units/{id} | Update a Unit
*UnitApi* | [**units_post**](docs/UnitApi.md#units_post) | **POST** /units | Create a Unit
*VariableApi* | [**variables_get**](docs/VariableApi.md#variables_get) | **GET** /variables | List all Variable entities
*VariableApi* | [**variables_id_delete**](docs/VariableApi.md#variables_id_delete) | **DELETE** /variables/{id} | Delete a Variable
*VariableApi* | [**variables_id_get**](docs/VariableApi.md#variables_id_get) | **GET** /variables/{id} | Get a Variable
*VariableApi* | [**variables_id_put**](docs/VariableApi.md#variables_id_put) | **PUT** /variables/{id} | Update a Variable
*VariableApi* | [**variables_post**](docs/VariableApi.md#variables_post) | **POST** /variables | Create a Variable
*VariablePresentationApi* | [**variablepresentations_get**](docs/VariablePresentationApi.md#variablepresentations_get) | **GET** /variablepresentations | List all VariablePresentation entities
*VariablePresentationApi* | [**variablepresentations_id_delete**](docs/VariablePresentationApi.md#variablepresentations_id_delete) | **DELETE** /variablepresentations/{id} | Delete a VariablePresentation
*VariablePresentationApi* | [**variablepresentations_id_get**](docs/VariablePresentationApi.md#variablepresentations_id_get) | **GET** /variablepresentations/{id} | Get a VariablePresentation
*VariablePresentationApi* | [**variablepresentations_id_put**](docs/VariablePresentationApi.md#variablepresentations_id_put) | **PUT** /variablepresentations/{id} | Update a VariablePresentation
*VariablePresentationApi* | [**variablepresentations_post**](docs/VariablePresentationApi.md#variablepresentations_post) | **POST** /variablepresentations | Create a VariablePresentation
*VisualizationApi* | [**visualizations_get**](docs/VisualizationApi.md#visualizations_get) | **GET** /visualizations | List all Visualization entities
*VisualizationApi* | [**visualizations_id_delete**](docs/VisualizationApi.md#visualizations_id_delete) | **DELETE** /visualizations/{id} | Delete a Visualization
*VisualizationApi* | [**visualizations_id_get**](docs/VisualizationApi.md#visualizations_id_get) | **GET** /visualizations/{id} | Get a Visualization
*VisualizationApi* | [**visualizations_id_put**](docs/VisualizationApi.md#visualizations_id_put) | **PUT** /visualizations/{id} | Update a Visualization
*VisualizationApi* | [**visualizations_post**](docs/VisualizationApi.md#visualizations_post) | **POST** /visualizations | Create a Visualization
*DefaultApi* | [**user_login_get**](docs/DefaultApi.md#user_login_get) | **GET** /user/login | 


## Documentation For Models

 - [CausalDiagram](docs/CausalDiagram.md)
 - [DatasetSpecification](docs/DatasetSpecification.md)
 - [EmpiricalModel](docs/EmpiricalModel.md)
 - [Emulator](docs/Emulator.md)
 - [Equation](docs/Equation.md)
 - [GeoCoordinates](docs/GeoCoordinates.md)
 - [GeoShape](docs/GeoShape.md)
 - [Grid](docs/Grid.md)
 - [HybridModel](docs/HybridModel.md)
 - [ICASAVariable](docs/ICASAVariable.md)
 - [Image](docs/Image.md)
 - [Model](docs/Model.md)
 - [ModelConfiguration](docs/ModelConfiguration.md)
 - [Organization](docs/Organization.md)
 - [Parameter](docs/Parameter.md)
 - [Person](docs/Person.md)
 - [PointBasedGrid](docs/PointBasedGrid.md)
 - [Process](docs/Process.md)
 - [Region](docs/Region.md)
 - [SVOVariable](docs/SVOVariable.md)
 - [SampleExecution](docs/SampleExecution.md)
 - [SampleResource](docs/SampleResource.md)
 - [Software](docs/Software.md)
 - [SoftwareConfiguration](docs/SoftwareConfiguration.md)
 - [SoftwareImage](docs/SoftwareImage.md)
 - [SoftwareVersion](docs/SoftwareVersion.md)
 - [SourceCode](docs/SourceCode.md)
 - [SpatialResolution](docs/SpatialResolution.md)
 - [SpatiallyDistributedGrid](docs/SpatiallyDistributedGrid.md)
 - [StandardVariable](docs/StandardVariable.md)
 - [TheoryGuidedModel](docs/TheoryGuidedModel.md)
 - [TimeInterval](docs/TimeInterval.md)
 - [Unit](docs/Unit.md)
 - [User](docs/User.md)
 - [Variable](docs/Variable.md)
 - [VariablePresentation](docs/VariablePresentation.md)
 - [Visualization](docs/Visualization.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (JWT)


## Author





# mint-api
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mintproject/MINT-ModelCatalogAPI-client/v1.0.3?filepath=notebook-example-how-to-use.ipynb)

This is MINT Model Catalog You can find out more about     Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.2
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

configuration = mint_client.Configuration()
# Configure Bearer authorization (JWT): BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = mint_client.DatasetspecificationApi(mint_client.ApiClient(configuration))
dataset_specification = mint_client.DatasetSpecification() # DatasetSpecification | A new `datasetspecification` to be created.

try:
    # Create a datasetspecification
    api_instance.create_data_set(dataset_specification)
except ApiException as e:
    print("Exception when calling DatasetspecificationApi->create_data_set: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.models.mint.isi.edu/v0.0.2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatasetspecificationApi* | [**create_data_set**](docs/DatasetspecificationApi.md#create_data_set) | **POST** /datasetspecifications | Create a datasetspecification
*DatasetspecificationApi* | [**get_data_sets**](docs/DatasetspecificationApi.md#get_data_sets) | **GET** /datasetspecifications | List All datasetspecifications
*ModelApi* | [**create_model**](docs/ModelApi.md#create_model) | **POST** /models | Create a model
*ModelApi* | [**delete_model**](docs/ModelApi.md#delete_model) | **DELETE** /model/{id} | Delete a Model
*ModelApi* | [**get_model**](docs/ModelApi.md#get_model) | **GET** /model/{id} | Get a Model
*ModelApi* | [**get_models**](docs/ModelApi.md#get_models) | **GET** /models | List All models
*ModelApi* | [**update_model**](docs/ModelApi.md#update_model) | **PUT** /model/{id} | Update a Model
*ModelconfigurationApi* | [**create_inputs_by_modelconfiguration**](docs/ModelconfigurationApi.md#create_inputs_by_modelconfiguration) | **POST** /modelconfiguration/{id}/inputs | Creates a new instance of a &#x60;DatasetSpecification&#x60; related as Input.
*ModelconfigurationApi* | [**create_model_configuration**](docs/ModelconfigurationApi.md#create_model_configuration) | **POST** /modelconfigurations | Create a model configuration
*ModelconfigurationApi* | [**create_outputs_by_modelconfiguration**](docs/ModelconfigurationApi.md#create_outputs_by_modelconfiguration) | **POST** /modelconfiguration/{id}/outputs | Create the output of a model configuration
*ModelconfigurationApi* | [**create_parameters_by_modelconfiguration**](docs/ModelconfigurationApi.md#create_parameters_by_modelconfiguration) | **POST** /modelconfiguration/{id}/parameters | Create the inputs of a model configuration
*ModelconfigurationApi* | [**delete_model_configuration**](docs/ModelconfigurationApi.md#delete_model_configuration) | **DELETE** /modelconfiguration/{id} | Delete a ModelConfiguration
*ModelconfigurationApi* | [**get_inputs_by_modelconfiguration**](docs/ModelconfigurationApi.md#get_inputs_by_modelconfiguration) | **GET** /modelconfiguration/{id}/inputs | Get the inputs of a model configuration
*ModelconfigurationApi* | [**get_model_configuration**](docs/ModelconfigurationApi.md#get_model_configuration) | **GET** /modelconfiguration/{id} | Get modelconfiguration
*ModelconfigurationApi* | [**get_model_configurations**](docs/ModelconfigurationApi.md#get_model_configurations) | **GET** /modelconfigurations | List modelconfiguration
*ModelconfigurationApi* | [**get_outputs_by_modelconfiguration**](docs/ModelconfigurationApi.md#get_outputs_by_modelconfiguration) | **GET** /modelconfiguration/{id}/outputs | Get the outputs of a model configuration
*ModelconfigurationApi* | [**get_parameters_by_modelconfiguration**](docs/ModelconfigurationApi.md#get_parameters_by_modelconfiguration) | **GET** /modelconfiguration/{id}/parameters | Get the parameters of a model configuration
*ModelconfigurationApi* | [**update_model_configuration**](docs/ModelconfigurationApi.md#update_model_configuration) | **PUT** /modelconfiguration/{id} | Update model configuration
*ModelversionApi* | [**create_model_version**](docs/ModelversionApi.md#create_model_version) | **POST** /modelversions | Create a ModelVersion
*ModelversionApi* | [**delete_model_version**](docs/ModelversionApi.md#delete_model_version) | **DELETE** /modelversion/{id} | Delete a ModelVersion
*ModelversionApi* | [**get_model_version**](docs/ModelversionApi.md#get_model_version) | **GET** /modelversion/{id} | Get a ModelVersion
*ModelversionApi* | [**get_model_versions**](docs/ModelversionApi.md#get_model_versions) | **GET** /modelversions | List All ModelVersions
*ModelversionApi* | [**update_model_version**](docs/ModelversionApi.md#update_model_version) | **PUT** /modelversion/{id} | Update a ModelVersion
*ParameterApi* | [**create_parameter**](docs/ParameterApi.md#create_parameter) | **POST** /parameters | Create a Parameter
*ParameterApi* | [**get_parameters**](docs/ParameterApi.md#get_parameters) | **GET** /parameters | List All Parameters
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user
*VariablespresentationsApi* | [**datasetspecification_id_variablepresentations_get**](docs/VariablespresentationsApi.md#datasetspecification_id_variablepresentations_get) | **GET** /datasetspecification/{id}/variablepresentations | List variable presentations related with a datasetspecification


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [CAG](docs/CAG.md)
 - [DatasetSpecification](docs/DatasetSpecification.md)
 - [Model](docs/Model.md)
 - [ModelConfiguration](docs/ModelConfiguration.md)
 - [ModelVersion](docs/ModelVersion.md)
 - [Parameter](docs/Parameter.md)
 - [Process](docs/Process.md)
 - [StandardVariable](docs/StandardVariable.md)
 - [TimeInterval](docs/TimeInterval.md)
 - [Unit](docs/Unit.md)
 - [User](docs/User.md)
 - [VariablePresentation](docs/VariablePresentation.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (JWT)


## Author

mosorio@isi.edu



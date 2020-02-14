# Quickstart
This page describes how to easily retrieve model information from the MINT model catalog.

!!! info "Terminology"
    For more information about the terms used in this page (model, model version), please see [https://mintproject.readthedocs.io/en/latest/modelcatalog/#overview](https://mintproject.readthedocs.io/en/latest/modelcatalog/#overview)

## Models

### List all models

```python
# create an instance of the API class
username="mint@isi.edu"
api_instance = modelcatalog.ModelApi()
try:
    # List all Model entities
    models = api_instance.models_get(username=username)
except ApiException as e:
    print("Exception when calling ModelApi->models_get: %s\n" % e)
```

### Response

A Model contains information such as description, documentation, authors and license. For more information about the properties of a model see: [**list[Model]**](../endpoints/Model)

### Search a model

You can search a model by using free text, which we will match against the model name, description and keywords. For example, let's search all the models by the word: `agriculture`

```python
# create an instance of the API class
username="mint@isi.edu"
label="agriculture"
api_instance = modelcatalog.ModelApi()
try:
    # List all Model entities
    models = api_instance.models_get(username=username, label=label)
except ApiException as e:
    print("Exception when calling ModelApi->models_get: %s\n" % e)
```

#### Response

We found 2 models.

!!! warning
    For readibility purposes, we are displaying the id and description in the table below. The real output is a JSON file which contains a full description of the model.
    
| Property    | Value                                                                                                                                                                                                                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description | ['Cycles simulates the productivity and the water,carbon and nitrogen balance of soil-crop systems subject to climate conditions and a large array of management constraints. Overall the model is set up to be daily. Some processes such as water balance are temporally nested (subdaily)\n.'] |
| id          | https://w3id.org/okn/i/mint/CYCLES          |


| Property    | Value|
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description | ['Decision Support System for Agrotechnology Transfer (DSSAT) is software application program that comprises dynamic crop growth simulation models for over 40 crops. DSSAT is supported by a range of utilities and applications for weather, soil, genetic, crop management and observational experimental data. Includes example data sets for all crop models. The crop simulation models simulate growth, development and yield as a function of the soil-plant-atmosphere dynamics (https://dssat.net/. 2019)'] |
| id          | https://w3id.org/okn/i/mint/DSSAT   |


### Get metadata from a model

You can use the python client to easily retrieve basic metadata of a model. For example, let's retrieve the description, author and versions of the `CYCLES` model.

```
model_id = "CYCLES"
try:
    # Get a Model
    model = api_instance.models_id_get(model_id, username=username)
    pprint(model)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_get: %s\n" % e)
```

#### Response


!!! warning
    For readibility purposes, we are only displaying the id, description, authors and versions of the model
    
| Property           | Value                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| has_version        |  https://w3id.org/okn/i/mint/cycles_v0.9.3_alpha, https://w3id.org/okn/i/mint/cycles_v0.10.2_alpha, 'https://w3id.org/okn/i/mint/cycles_v0.9.4_alpha
| description        | Cycles simulates the productivity and the water,carbon and nitrogen balance of soil-crop systems subject to climate conditions and a large array of management constraints. Overall the model is set up to be daily. Some processes such as water balance are temporally nested (subdaily)   |
| has_contact_person | https://w3id.org/okn/i/mint/kemanian_armen               |
| id                 | https://w3id.org/okn/i/mint/CYCLES    |

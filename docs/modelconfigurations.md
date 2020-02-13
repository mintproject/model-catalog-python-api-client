# Searching model configurations


### Search a model configuration by text

You can search a model by a free text. Let's search all the models by the text: `agriculture`

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

We found 7 model configurations. A ModelConfiguration contains information such as description, parameters, inputs, outputs, region. For more information, go to: [**[ModelConfiguration]**](../endpoints/ModelConfiguration)

!!! warning
    We are displaying only the id and description in a table for visualization purposes. The real output is a JSON.

| Property    | Value                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/DSSAT_cfg_simple                                                    |
| description | ['DSSAT simple working configuration that accepts changes in weather; soil moisture and maize'] |


| Property    | Value                                           |
|-------------|-------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/cycles              |
| description | ['Cycles (version 0.9.3) simple configuration'] |


| Property    | Value                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/cycles-0.10.2-alpha-collection                                                                                                 |
| description | ['Cycles configuration (version 0.10.2) for grouped weather and soil files and exposing additional parameters such as weeds fraction and fertilizer rate'] |


| Property    | Value                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/cycles-0.9.4-alpha                                                                     |
| description | ['Cycles configuration (version 0.9.4) exposing additional parameters such as weeds fraction and fertilizer rate'] |


| Property    | Value                                                                          |
|-------------|--------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/cycles_multiple_points                             |
| description | ['Cycles (version 0.9.3) configuration to run the model with multiple points'] |


| Property    | Value                                                                                                                                                                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/economic-v7                                                                                                                                                                                                                                                  |
| description | ['Aggregate crop supply response model (version 7). Based on the Agricultural Sample Survey reports (AgSS), from 2009-2018 (http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA/ethiopia)\nThe price index still comes from the World Food Programme report.'] |


| Property    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id          | https://w3id.org/okn/i/mint/economicGambella-v6.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| description | ['Aggregate crop supply response model. Based on the Agricultural Sample Survey reports (AgSS), two crops are harvested in this region: maize and sorghum, so this model includes only 2 crops. Land use, production and yield level data comes from Agss report 2014 (http://surveys.worldbank.org/lsms/programs/integrated-surveys-agriculture-ISA/ethiopia)\n\nThe price index still comes from the World Food Programme report, which included Gambella and its own set of prices.\n\nThe Nitrogen application rate is set to a low value because farmers in Gambella utilize very low level of fertilizer.  \nAll other parameters, have been approximate based the South Sudan model calibration.'] |



### Obtain the information for execution

Let's use the **ModelConfiguration**: cycles-0.9.4-alpha

```python
# create an instance of the API class
api_instance = modelcatalog.ModelConfigurationApi()
resource_id = 'cycles-0.9.4-alpha' # str | The ID of the resource

try:
    # Get a ModelConfiguration
    resource = api_instance.custom_modelconfigurations_id_get(resource_id, username=username)
except ApiException as e:
    print("Exception when calling ModelConfigurationApi->custom_modelconfigurations_id_get: %s\n" % e)
pprint(resource)
```

#### Display the parameters

```
parameters = resource.has_parameter
```


!!! warning
    This resource has 8 parameters but we're showing only two.

| Property                | Value                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| adjustsVariable         | ['https://w3id.org/okn/i/mint/cycles_mass']                                                                                                                                     |
| description             | ['Mass of nitrogen fertilizer added each year (kg/ha). The model will multiply the mass by the concentration of the fertilizer (0.32). Teff crops should not surpass 320kg/ha'] |
| hasDataType             | ['float']                                                                                                                                                                       |
| hasDefaultValue         | ['0']                                                                                                                                                                           |
| hasMaximumAcceptedValue | ['1250']                                                                                                                                                                        |
| hasMinimumAcceptedValue | ['0']                                                                                                                                                                           |
| id                      | https://w3id.org/okn/i/mint/cycles-0.9.4-alpha_fertilizer_rate                                                                                                                  |
| label                   | ['fertilizer_rate']                                                                                                                                                             |
| position                | ['6']                                                                                                                                                                           |
| usesUnit                | ['https://w3id.org/okn/i/mint/kg_ha_1M_L_2']                                                                                                                                    |


| Property        | Value                                                        |
|-----------------|--------------------------------------------------------------|
| description     | ['Use forcing data from a hydrology model (when available)'] |
| hasDataType     | ['boolean']                                                  |
| hasDefaultValue | ['FALSE']                                                    |
| id              | https://w3id.org/okn/i/mint/cycles-0.9.4-alpha_use_forcing   |
| label           | ['use_forcing']                                              |
| position        | ['8']                                                        |



#### Display the inputs

```
inputs = resource.has_input
```

!!! warning
    This resource has 3 inputs but we're showing only one.

| Property          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description       | ['Cycles soil description file. Soil files typically have a suffix of .soil, but any naming convention can be used as long as it matches the soil file name listed in the control file. The soil file starts with three lines at the beginning with the keyword tags CURVE_NUMBER, SLOPE, and TOTAL_LAYERS, with each keyword followed by a tab-delimited value.']                                                                     |
| hasDimensionality | ['0']                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| hasFormat         | ['soil']                                                                                                                                                                                                                                                                                                                                                                                                                               |
| hasPresentation   | ['https://w3id.org/okn/i/mint/cycles_bd', 'https://w3id.org/okn/i/mint/cycles_som', 'https://w3id.org/okn/i/mint/cycles_dz', 'https://w3id.org/okn/i/mint/cycles_rv', 'https://w3id.org/okn/i/mint/cycles_smc', 'https://w3id.org/okn/i/mint/cycles_clay', 'https://w3id.org/okn/i/mint/cycles_cn', 'https://w3id.org/okn/i/mint/cycles_layer', 'https://w3id.org/okn/i/mint/cycles_silt', 'https://w3id.org/okn/i/mint/cycles_slope'] |
| id                | https://w3id.org/okn/i/mint/cycles-0.9.4-alpha_soil                                                                                                                                                                                                                                                                                                                                                                                    |
| label             | ['cycles_soil']                                                                                                                                                                                                                                                                                                                                                                                                                        |
| position          | ['2']                                                                                                                                                                                                                                                                                                                                                                                                                                  |
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

#### Display the outputs


```
output = resource.has_output
```


!!! warning
    This resource has four outputs but we're showing only one.


| Property          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description       | ['Results in this file are for the sum of all layers in the soil profile, including surface residues']                                                                                                                                                                                                                                                                                                                                                                                                        |
| hasDimensionality | ['0']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| hasFormat         | ['dat']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| hasPresentation   | ['https://w3id.org/okn/i/mint/cycles_res_c_decomp', 'https://w3id.org/okn/i/mint/cycles_humified_c2', 'https://w3id.org/okn/i/mint/cycles_final_c', 'https://w3id.org/okn/i/mint/cycles_res_biomass_in', 'https://w3id.org/okn/i/mint/cycles_c_diff', 'https://w3id.org/okn/i/mint/cycles_respired_c', 'https://w3id.org/okn/i/mint/cycles_init_c_mass', 'https://w3id.org/okn/i/mint/cycles_root_c_decomp', 'https://w3id.org/okn/i/mint/cycles_root_biomass_in', 'https://w3id.org/okn/i/mint/cycles_year'] |
| id                | https://w3id.org/okn/i/mint/cycles-0.9.4-alpha_soilProfile                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| label             | ['cycles_soilProfile']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| position          | ['1']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
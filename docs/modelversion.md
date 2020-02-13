# Software Version

### List the SoftwareVersion of a Model

```python
# create an instance of the API class
username="mint@isi.edu"
api_instance = modelcatalog.ModelApi()
model_id = "CYCLES"
try:
    # Get a Model
    model = api_instance.models_id_get(model_id, username=username)
    pprint(model)
except ApiException as e:
    print("Exception when calling ModelApi->models_id_get: %s\n" % e)

```

### Response

The model `CYCLES` has three SoftwareVersion

```
https://w3id.org/okn/i/mint/cycles_v0.9.3_alpha
https://w3id.org/okn/i/mint/cycles_v0.10.2_alpha
https://w3id.org/okn/i/mint/cycles_v0.9.4_alpha
```

### Get information of a SoftwareVersion

```python
api_instance = modelcatalog.SoftwareVersionApi()
software_version_id = 'cycles_v0.9.4_alpha' # str | The ID of the resource

try:
    # Get a SoftwareImage
    software_version = api_instance.softwareversions_id_get(software_version_id, username=username)
    pprint(software_version)
except ApiException as e:
    print("Exception when calling SoftwareImageApi->softwareimages_id_get: %s\n" % e)
```

 For more information, go to [**ModelVersion**](../endpoints/ModelVersion)

#### Response

The **SoftwareVersion** has one **ModelConfiguration**: cycles-0.9.4-alpha


!!! warning
    We are displaying only the id and description in a table for visualization purposes. The real output is a JSON.
    
| Property          | Value                                                                                                                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description       | ['Version 0.9.4 of Cycles allowing exposing multiple parameters']                                                                                                                                                                |
| id                | https://w3id.org/okn/i/mint/cycles_v0.9.4_alpha                                                                                                                                                                                  |
| has_configuration | [ 'id': 'https://w3id.org/okn/i/mint/cycles-0.9.4-alpha', 'label': ['Cycles configuration (v0.9.4) exposing weed fraction and fertilizer rate']}] |

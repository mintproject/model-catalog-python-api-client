# DatasetSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_dimensionality** | **list[int]** | Property to indicate dimensionality of the input or output of a dataset specification | [optional] 
**has_format** | **list[str]** | Format followed by a file. For example, txt, nc, etc. | [optional] 
**path_location** | **list[str]** | Property that indicates the relative path of an input or output with respect to the folder structure of the executable.   For example, let&#39;s assume we have an input that has to exist in the folder &#x60;/datasets&#x60; or the executable will not work. This property ensures that this knowledge is captured for a given software component execution.  In this case the property would capture this as follows:  &#x60;&#x60;&#x60; :input_prep a sd:DatasetSpecification . :input_prep rdfs:label \&quot;precipitation file\&quot; . :input_precip sd:pathLocation \&quot;/datasets/\&quot;. &#x60;&#x60;&#x60; | [optional] 
**has_file_structure** | **list[object]** | Relates a dataset specification to the data structure definition | [optional] 
**description** | **list[str]** | small description | [optional] 
**has_data_transformation** | [**list[DataTransformation]**](DataTransformation.md) | Property that associates an input/output with their corresponding data transformation. | [optional] 
**has_presentation** | [**list[VariablePresentation]**](VariablePresentation.md) | Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it. | [optional] 
**label** | **list[str]** | short description of the resource | [optional] 
**type** | **list[str]** | type of the resource | [optional] 
**has_fixed_resource** | [**list[SampleResource]**](SampleResource.md) | Property that links a parameter or an input to a fixed value. For example, in a given configuration a parameter with the planting date for a model could be fixed to avoid the user changing it for that region. | [optional] 
**has_data_transformation_setup** | [**list[DataTransformationSetup]**](DataTransformationSetup.md) | Property to link an input/output dataset to the specific data transformation (with URLs | [optional] 
**position** | **list[int]** | Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution | [optional] 
**id** | **str** | identifier | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)



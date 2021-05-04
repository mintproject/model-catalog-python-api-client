# VariablePresentation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_default_value** | [**list[AnyOfURIbooleanDateTimefloatintegerstring]**](AnyOfURIbooleanDateTimefloatintegerstring.md) | Default accepted value of a variable presentation (or a parameter) | [optional] 
**has_short_name** | **list[str]** | A short name (e.g., temperature) capturing the high-level concept of the variable | [optional] 
**has_minimum_accepted_value** | [**list[AnyOfDateTimefloatinteger]**](AnyOfDateTimefloatinteger.md) | Minimum accepted value of a variable presentation (or a parameter) | [optional] 
**has_standard_variable** | [**list[StandardVariable]**](StandardVariable.md) | the standard name of a variable | [optional] 
**has_maximum_accepted_value** | [**list[AnyOfDateTimefloatinteger]**](AnyOfDateTimefloatinteger.md) | Maximum accepted value of a variable presentation (or a parameter) | [optional] 
**description** | **list[str]** | small description | [optional] 
**part_of_dataset** | [**list[DatasetSpecification]**](DatasetSpecification.md) | Associates a presentation with a dataset where the presentation occurs | [optional] 
**id** | **str** | identifier | [optional] 
**label** | **list[str]** | short description of the resource | [optional] 
**uses_unit** | [**list[Unit]**](Unit.md) | Property used to link a variable presentation or time interval to the unit they are represented in | [optional] 
**type** | **list[str]** | type of the resource | [optional] 
**has_long_name** | **list[str]** | Properties that relate the variable representation to its long name. The long name is useful for context (e.g., precipitation is less ambiguous than P) but not as precise as the standard name. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)



# Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_default_value** | **list[object]** | Default accepted value of a variable presentation (or a parameter) | [optional] 
**has_maximum_accepted_value** | **list[object]** | Maximum accepted value of a variable presentation (or a parameter) | [optional] 
**description** | **list[str]** | small description | [optional] 
**has_data_type** | **list[str]** | Property that indicates the data type of a parameter | [optional] 
**has_fixed_value** | **list[object]** | Value of a parameter in a software setup. | [optional] 
**has_presentation** | [**list[VariablePresentation]**](VariablePresentation.md) | Property that links an instance of a dataset (or a dataset specification) to the presentation of a variable contained (or expected to be contained) on it. | [optional] 
**label** | **list[str]** | short description of the resource | [optional] 
**recommended_increment** | **list[float]** | Value that represents how a parameter should be incremented on each iteration of a software component execution. This value is important when preparing execution ensembles automatically, e.g., simulating crop production varying the parameter \&quot;fertilizer amount\&quot; in increments of 10%. | [optional] 
**type** | **list[str]** | type of the resource | [optional] 
**has_minimum_accepted_value** | **list[object]** | Minimum accepted value of a variable presentation (or a parameter) | [optional] 
**has_accepted_values** | **list[str]** | Property that constraints which values are accepted for a parameter. For example, the name of a crop can only be \&quot;Maize\&quot; or \&quot;Sorghum\&quot; | [optional] 
**adjusts_variable** | [**list[Variable]**](Variable.md) | Property that links parameter with the variable they adjust. This property can be used when parameters quantify variables without directly representing them. For example, a \&quot;fertilizer percentage adjustment\&quot; parameter can quantify a \&quot;fertilizer price\&quot; variable | [optional] 
**relevant_for_intervention** | [**list[Intervention]**](Intervention.md) | Description not available | [optional] 
**position** | **list[int]** | Position of the parameter or input/output in the model configuration. This property is needed to know how to organize the I/O of the component on execution | [optional] 
**id** | **str** | identifier | [optional] 
**uses_unit** | [**list[Unit]**](Unit.md) | Property used to link a variable presentation or time interval to the unit they are represented in | [optional] 
**has_step_size** | **list[float]** | Property that determines what are the increments (step size) that are commonly used to vary a parameter. This is commonly used for automatically setting up software tests. For example, if I want to set up a model and try 30 reasonable values on a parameter, I may use the default value and the step size to create the appropriate increments. If the step size is 0.1 and the default value is 0, then I will will be able to create setups: 0, 0.1, 0.2...2.9,3 | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)



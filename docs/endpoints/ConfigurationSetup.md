# ConfigurationSetup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_download_instructions** | **list[str]** | Instructions needed to download a software component. The difference with &#x60;hasDownloadURL&#x60; is that this property captures the human readable instructions required to download software. For example, sometimes an authentication is needed, users need to fill in a form, etc. | [optional] 
**keywords** | **list[str]** | Keywords associated with a software component | [optional] 
**has_documentation** | **list[str]** | Pointer to the documentation of the model | [optional] 
**has_implementation_script_location** | **list[str]** | Property that points to the main runnable script for the current function | [optional] 
**software_requirements** | **list[str]** | Software requirements needed to install a software component | [optional] 
**has_download_url** | **list[str]** | Download URL where to obtain the source/executable of the software | [optional] 
**type** | **list[str]** | type of the resource | [optional] 
**has_installation_instructions** | **list[str]** | Instructions required to install this particular piece of software. Installation instructions usually are available in a human-readable manner. | [optional] 
**compatible_visualization_software** | [**list[Software]**](Software.md) | Property that links a software component to other useful software that canbe used to visualize its outputs | [optional] 
**copyright_holder** | [**list[AnyOfOrganizationPerson]**](AnyOfOrganizationPerson.md) | Copyright holder for a software component | [optional] 
**has_faq** | **list[str]** | Frequently asked questions about a software | [optional] 
**logo** | [**list[Image]**](Image.md) | Property that links to the image used as logo for a software component | [optional] 
**has_contact_person** | [**list[AnyOfOrganizationPerson]**](AnyOfOrganizationPerson.md) | Contact person responsible for a software component | [optional] 
**tag** | **list[str]** | Tag used to annotate a version or a software configuration. This annotation is useful to show which version is the latest, or which version is deprecated. Supported tags are: \&quot;latest\&quot;, \&quot;deprecated\&quot; | [optional] 
**id** | **str** | identifier | [optional] 
**identifier** | **list[str]** | Identifier of the resource being described | [optional] 
**has_sample_execution** | [**list[SampleExecution]**](SampleExecution.md) | Property pointing to a sample execution of a software configuration | [optional] 
**has_sample_result** | [**list[SampleResource]**](SampleResource.md) | Property designed to link a software configuration to a sample resource resulting from its execution | [optional] 
**author** | [**list[AnyOfOrganizationPerson]**](AnyOfOrganizationPerson.md) | The creator of a software component | [optional] 
**was_derived_from_setup** | [**list[ConfigurationSetup]**](ConfigurationSetup.md) | Property that links a setup to a previous version of that setup. This property is needed (for example) when creating snapshots of setups. | [optional] 
**has_constraint** | [**list[Constraint]**](Constraint.md) | Constraint or rule associated to a software configuration. For example: \&quot;This model accepts only monthly data\&quot;, or \&quot;all inputs of this model configuration must share the same location\&quot;. More structured restrictions, such as Jena rules or SWRL rules may also be captured with this property | [optional] 
**has_build_file** | **list[str]** | A file (e.g., Dockerfile) with executable instructions indicating how a Software Image or a Software component is built | [optional] 
**short_description** | **list[str]** | A summarized description of the resource | [optional] 
**has_execution_command** | **list[str]** | Execution instructions on how to run the image | [optional] 
**date_published** | **list[str]** | Date when a software component was published | [optional] 
**license** | **list[str]** | License of a software component or its source code | [optional] 
**has_source_code** | [**list[SourceCode]**](SourceCode.md) | Property designed to link a software with its software source code (which may reside in a code repository such as GitHub) | [optional] 
**has_setup** | [**list[ConfigurationSetup]**](ConfigurationSetup.md) | Property used to define configurations with some fixed resources and values. The rationale of this property is to allow predefined configurations | [optional] 
**has_example** | **list[str]** | An example explaining a scenario where the software component was used in plain language. | [optional] 
**publisher** | [**list[AnyOfOrganizationPerson]**](AnyOfOrganizationPerson.md) | Publisher organization or person responsible for a software component | [optional] 
**has_output** | [**list[DatasetSpecification]**](DatasetSpecification.md) | Property that expresses what are the outputs of a model | [optional] 
**status** | **list[str]** | Data property to indicate the status of a configuration setups. For example, to indicate that a setup has been executed in a platform, that the setup should notbe shown to users (it&#39;s an auxiliary setup), etc. | [optional] 
**doi** | **list[str]** | Digital Object Identifier associated with a software component | [optional] 
**has_funding** | [**list[FundingInformation]**](FundingInformation.md) | Property that links a software project to its funding information | [optional] 
**has_component_location** | **list[str]** | Location of the aggregation of all the files needed to execute the component. Usually a zip file including the run script and support scripts, including specification files | [optional] 
**support_details** | **list[str]** | Property to link details, such as mailing lists in case a contact person is not provided | [optional] 
**has_version** | [**list[SoftwareVersion]**](SoftwareVersion.md) | Property designed to link a software component with its corresponding versions | [optional] 
**has_typical_data_source** | **list[str]** | Typical data sources that are used by a software component | [optional] 
**description** | **list[str]** | small description | [optional] 
**reference_publication** | **list[str]** | Main publication to cite for this software component | [optional] 
**screenshot** | [**list[Image]**](Image.md) | Image illustrating a snapshot of the target software | [optional] 
**had_primary_source** | **list[object]** | Property to identify the original source of the information of the annotated resource. It could be a web page, an organization, a person, some experiment notes, etc. | [optional] 
**issue_tracker** | **list[str]** | Pointer to the issue tracker of a software component | [optional] 
**has_software_image** | [**list[SoftwareImage]**](SoftwareImage.md) | Function to link a function with its corresponding container | [optional] 
**date_created** | **list[str]** | Date when a software component was created | [optional] 
**contributor** | [**list[Person]**](Person.md) | Contributor to a software component | [optional] 
**has_purpose** | **list[str]** | Objective or main functionality that can be achieved by running this software | [optional] 
**has_executable_instructions** | **list[str]** | Instructions that indicate how a software component should be executed. The difference with &#x60;hasExecutionCommand&#x60; is that the execution instructions aim to be human-readable, and have explanations between the different commands and instructions | [optional] 
**has_sample_visualization** | [**list[Visualization]**](Visualization.md) | A typical sample visualization of the softwware outputs | [optional] 
**memory_requirements** | **list[str]** | Memory requirements of a software | [optional] 
**website** | **list[str]** | Website of the software | [optional] 
**citation** | **list[str]** | How to cite this software | [optional] 
**processor_requirements** | **list[str]** | Processor requirements of a software component | [optional] 
**adjustable_parameter** | [**list[Parameter]**](Parameter.md) | Parameter that can be adjusted in a configuration setup | [optional] 
**has_usage_notes** | **list[str]** | Property that describes the usage considerations of a particular software. These notes capture the rationale of for that software configuration, along with an explanation for sample inputs, things to consider when running the model with data, etc. | [optional] 
**has_support_script_location** | **list[str]** | Property that links to the location of scripts that may be used from the main runnable script. | [optional] 
**readme** | **list[str]** | URl to the readme file of a software component | [optional] 
**label** | **list[str]** | short description of the resource | [optional] 
**has_assumption** | **list[str]** | Assumptions of a software, e.g. the solver being used for a particular model, the source of the data (e.g., all data must have a given resolution), etc. | [optional] 
**has_parameter** | [**list[Parameter]**](Parameter.md) | Property that indicates the parameters of a model configuration | [optional] 
**operating_systems** | **list[str]** | Operating systems under which a software component can operate | [optional] 
**has_executable_notebook** | **list[str]** | Property that links a software component with an executable notebook (e.g., Jupyter notebook) that illustrates how to use it in an executable manner. | [optional] 
**useful_for_calculating_index** | [**list[NumericalIndex]**](NumericalIndex.md) | Property that indicates that a software component (or any of its outputs) can be used to calculate a particular index. The rationale for this property is that indices are usually calculated by applying post-processing steps to the outputs of a software component. | [optional] 
**has_input** | [**list[DatasetSpecification]**](DatasetSpecification.md) | Property that links a model configuration to the input types expected by it. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)



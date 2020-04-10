# coding: utf-8

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SoftwareImage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'has_funding': 'list[FundingInformation]',
        'keywords': 'list[str]',
        'has_documentation': 'list[str]',
        'support_details': 'list[str]',
        'software_requirements': 'list[str]',
        'has_version': 'list[SoftwareVersion]',
        'has_typical_data_source': 'list[str]',
        'has_download_url': 'list[str]',
        'description': 'list[str]',
        'reference_publication': 'list[str]',
        'screenshot': 'list[Image]',
        'type': 'list[str]',
        'has_installation_instructions': 'list[str]',
        'had_primary_source': 'list[object]',
        'date_created': 'list[str]',
        'contributor': 'list[Person]',
        'compatible_visualization_software': 'list[Software]',
        'has_faq': 'list[str]',
        'logo': 'list[Image]',
        'has_contact_person': 'list[object]',
        'has_purpose': 'list[str]',
        'id': 'str',
        'has_sample_visualization': 'list[Visualization]',
        'identifier': 'list[str]',
        'memory_requirements': 'list[str]',
        'website': 'list[str]',
        'citation': 'list[str]',
        'author': 'list[object]',
        'processor_requirements': 'list[str]',
        'has_usage_notes': 'list[str]',
        'short_description': 'list[str]',
        'label': 'list[str]',
        'has_execution_command': 'list[str]',
        'has_assumption': 'list[str]',
        'date_published': 'list[str]',
        'operating_systems': 'list[str]',
        'license': 'list[str]',
        'has_source_code': 'list[SourceCode]',
        'has_example': 'list[str]',
        'publisher': 'list[object]'
    }

    attribute_map = {
        'has_funding': 'hasFunding',
        'keywords': 'keywords',
        'has_documentation': 'hasDocumentation',
        'support_details': 'supportDetails',
        'software_requirements': 'softwareRequirements',
        'has_version': 'hasVersion',
        'has_typical_data_source': 'hasTypicalDataSource',
        'has_download_url': 'hasDownloadURL',
        'description': 'description',
        'reference_publication': 'referencePublication',
        'screenshot': 'screenshot',
        'type': 'type',
        'has_installation_instructions': 'hasInstallationInstructions',
        'had_primary_source': 'hadPrimarySource',
        'date_created': 'dateCreated',
        'contributor': 'contributor',
        'compatible_visualization_software': 'compatibleVisualizationSoftware',
        'has_faq': 'hasFAQ',
        'logo': 'logo',
        'has_contact_person': 'hasContactPerson',
        'has_purpose': 'hasPurpose',
        'id': 'id',
        'has_sample_visualization': 'hasSampleVisualization',
        'identifier': 'identifier',
        'memory_requirements': 'memoryRequirements',
        'website': 'website',
        'citation': 'citation',
        'author': 'author',
        'processor_requirements': 'processorRequirements',
        'has_usage_notes': 'hasUsageNotes',
        'short_description': 'shortDescription',
        'label': 'label',
        'has_execution_command': 'hasExecutionCommand',
        'has_assumption': 'hasAssumption',
        'date_published': 'datePublished',
        'operating_systems': 'operatingSystems',
        'license': 'license',
        'has_source_code': 'hasSourceCode',
        'has_example': 'hasExample',
        'publisher': 'publisher'
    }

    def __init__(self, has_funding=None, keywords=None, has_documentation=None, support_details=None, software_requirements=None, has_version=None, has_typical_data_source=None, has_download_url=None, description=None, reference_publication=None, screenshot=None, type=None, has_installation_instructions=None, had_primary_source=None, date_created=None, contributor=None, compatible_visualization_software=None, has_faq=None, logo=None, has_contact_person=None, has_purpose=None, id=None, has_sample_visualization=None, identifier=None, memory_requirements=None, website=None, citation=None, author=None, processor_requirements=None, has_usage_notes=None, short_description=None, label=None, has_execution_command=None, has_assumption=None, date_published=None, operating_systems=None, license=None, has_source_code=None, has_example=None, publisher=None):  # noqa: E501
        """SoftwareImage - a model defined in OpenAPI"""  # noqa: E501

        self._has_funding = None
        self._keywords = None
        self._has_documentation = None
        self._support_details = None
        self._software_requirements = None
        self._has_version = None
        self._has_typical_data_source = None
        self._has_download_url = None
        self._description = None
        self._reference_publication = None
        self._screenshot = None
        self._type = None
        self._has_installation_instructions = None
        self._had_primary_source = None
        self._date_created = None
        self._contributor = None
        self._compatible_visualization_software = None
        self._has_faq = None
        self._logo = None
        self._has_contact_person = None
        self._has_purpose = None
        self._id = None
        self._has_sample_visualization = None
        self._identifier = None
        self._memory_requirements = None
        self._website = None
        self._citation = None
        self._author = None
        self._processor_requirements = None
        self._has_usage_notes = None
        self._short_description = None
        self._label = None
        self._has_execution_command = None
        self._has_assumption = None
        self._date_published = None
        self._operating_systems = None
        self._license = None
        self._has_source_code = None
        self._has_example = None
        self._publisher = None
        self.discriminator = None

        self.has_funding = has_funding
        self.keywords = keywords
        self.has_documentation = has_documentation
        self.support_details = support_details
        self.software_requirements = software_requirements
        self.has_version = has_version
        self.has_typical_data_source = has_typical_data_source
        self.has_download_url = has_download_url
        self.description = description
        self.reference_publication = reference_publication
        self.screenshot = screenshot
        self.type = type
        self.has_installation_instructions = has_installation_instructions
        self.had_primary_source = had_primary_source
        self.date_created = date_created
        self.contributor = contributor
        self.compatible_visualization_software = compatible_visualization_software
        self.has_faq = has_faq
        self.logo = logo
        self.has_contact_person = has_contact_person
        self.has_purpose = has_purpose
        if id is not None:
            self.id = id
        self.has_sample_visualization = has_sample_visualization
        self.identifier = identifier
        self.memory_requirements = memory_requirements
        self.website = website
        self.citation = citation
        self.author = author
        self.processor_requirements = processor_requirements
        self.has_usage_notes = has_usage_notes
        self.short_description = short_description
        self.label = label
        self.has_execution_command = has_execution_command
        self.has_assumption = has_assumption
        self.date_published = date_published
        self.operating_systems = operating_systems
        self.license = license
        self.has_source_code = has_source_code
        self.has_example = has_example
        self.publisher = publisher

    @property
    def has_funding(self):
        """Gets the has_funding of this SoftwareImage.  # noqa: E501


        :return: The has_funding of this SoftwareImage.  # noqa: E501
        :rtype: list[FundingInformation]
        """
        return self._has_funding

    @has_funding.setter
    def has_funding(self, has_funding):
        """Sets the has_funding of this SoftwareImage.


        :param has_funding: The has_funding of this SoftwareImage.  # noqa: E501
        :type: list[FundingInformation]
        """

        self._has_funding = has_funding

    @property
    def keywords(self):
        """Gets the keywords of this SoftwareImage.  # noqa: E501


        :return: The keywords of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this SoftwareImage.


        :param keywords: The keywords of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def has_documentation(self):
        """Gets the has_documentation of this SoftwareImage.  # noqa: E501


        :return: The has_documentation of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this SoftwareImage.


        :param has_documentation: The has_documentation of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_documentation = has_documentation

    @property
    def support_details(self):
        """Gets the support_details of this SoftwareImage.  # noqa: E501


        :return: The support_details of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._support_details

    @support_details.setter
    def support_details(self, support_details):
        """Sets the support_details of this SoftwareImage.


        :param support_details: The support_details of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._support_details = support_details

    @property
    def software_requirements(self):
        """Gets the software_requirements of this SoftwareImage.  # noqa: E501


        :return: The software_requirements of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._software_requirements

    @software_requirements.setter
    def software_requirements(self, software_requirements):
        """Sets the software_requirements of this SoftwareImage.


        :param software_requirements: The software_requirements of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._software_requirements = software_requirements

    @property
    def has_version(self):
        """Gets the has_version of this SoftwareImage.  # noqa: E501


        :return: The has_version of this SoftwareImage.  # noqa: E501
        :rtype: list[SoftwareVersion]
        """
        return self._has_version

    @has_version.setter
    def has_version(self, has_version):
        """Sets the has_version of this SoftwareImage.


        :param has_version: The has_version of this SoftwareImage.  # noqa: E501
        :type: list[SoftwareVersion]
        """

        self._has_version = has_version

    @property
    def has_typical_data_source(self):
        """Gets the has_typical_data_source of this SoftwareImage.  # noqa: E501


        :return: The has_typical_data_source of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_typical_data_source

    @has_typical_data_source.setter
    def has_typical_data_source(self, has_typical_data_source):
        """Sets the has_typical_data_source of this SoftwareImage.


        :param has_typical_data_source: The has_typical_data_source of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_typical_data_source = has_typical_data_source

    @property
    def has_download_url(self):
        """Gets the has_download_url of this SoftwareImage.  # noqa: E501


        :return: The has_download_url of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_download_url

    @has_download_url.setter
    def has_download_url(self, has_download_url):
        """Sets the has_download_url of this SoftwareImage.


        :param has_download_url: The has_download_url of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_download_url = has_download_url

    @property
    def description(self):
        """Gets the description of this SoftwareImage.  # noqa: E501


        :return: The description of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SoftwareImage.


        :param description: The description of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def reference_publication(self):
        """Gets the reference_publication of this SoftwareImage.  # noqa: E501


        :return: The reference_publication of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._reference_publication

    @reference_publication.setter
    def reference_publication(self, reference_publication):
        """Sets the reference_publication of this SoftwareImage.


        :param reference_publication: The reference_publication of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._reference_publication = reference_publication

    @property
    def screenshot(self):
        """Gets the screenshot of this SoftwareImage.  # noqa: E501


        :return: The screenshot of this SoftwareImage.  # noqa: E501
        :rtype: list[Image]
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this SoftwareImage.


        :param screenshot: The screenshot of this SoftwareImage.  # noqa: E501
        :type: list[Image]
        """

        self._screenshot = screenshot

    @property
    def type(self):
        """Gets the type of this SoftwareImage.  # noqa: E501


        :return: The type of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SoftwareImage.


        :param type: The type of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_installation_instructions(self):
        """Gets the has_installation_instructions of this SoftwareImage.  # noqa: E501


        :return: The has_installation_instructions of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_installation_instructions

    @has_installation_instructions.setter
    def has_installation_instructions(self, has_installation_instructions):
        """Sets the has_installation_instructions of this SoftwareImage.


        :param has_installation_instructions: The has_installation_instructions of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_installation_instructions = has_installation_instructions

    @property
    def had_primary_source(self):
        """Gets the had_primary_source of this SoftwareImage.  # noqa: E501


        :return: The had_primary_source of this SoftwareImage.  # noqa: E501
        :rtype: list[object]
        """
        return self._had_primary_source

    @had_primary_source.setter
    def had_primary_source(self, had_primary_source):
        """Sets the had_primary_source of this SoftwareImage.


        :param had_primary_source: The had_primary_source of this SoftwareImage.  # noqa: E501
        :type: list[object]
        """

        self._had_primary_source = had_primary_source

    @property
    def date_created(self):
        """Gets the date_created of this SoftwareImage.  # noqa: E501


        :return: The date_created of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SoftwareImage.


        :param date_created: The date_created of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._date_created = date_created

    @property
    def contributor(self):
        """Gets the contributor of this SoftwareImage.  # noqa: E501


        :return: The contributor of this SoftwareImage.  # noqa: E501
        :rtype: list[Person]
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this SoftwareImage.


        :param contributor: The contributor of this SoftwareImage.  # noqa: E501
        :type: list[Person]
        """

        self._contributor = contributor

    @property
    def compatible_visualization_software(self):
        """Gets the compatible_visualization_software of this SoftwareImage.  # noqa: E501


        :return: The compatible_visualization_software of this SoftwareImage.  # noqa: E501
        :rtype: list[Software]
        """
        return self._compatible_visualization_software

    @compatible_visualization_software.setter
    def compatible_visualization_software(self, compatible_visualization_software):
        """Sets the compatible_visualization_software of this SoftwareImage.


        :param compatible_visualization_software: The compatible_visualization_software of this SoftwareImage.  # noqa: E501
        :type: list[Software]
        """

        self._compatible_visualization_software = compatible_visualization_software

    @property
    def has_faq(self):
        """Gets the has_faq of this SoftwareImage.  # noqa: E501


        :return: The has_faq of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_faq

    @has_faq.setter
    def has_faq(self, has_faq):
        """Sets the has_faq of this SoftwareImage.


        :param has_faq: The has_faq of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_faq = has_faq

    @property
    def logo(self):
        """Gets the logo of this SoftwareImage.  # noqa: E501


        :return: The logo of this SoftwareImage.  # noqa: E501
        :rtype: list[Image]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this SoftwareImage.


        :param logo: The logo of this SoftwareImage.  # noqa: E501
        :type: list[Image]
        """

        self._logo = logo

    @property
    def has_contact_person(self):
        """Gets the has_contact_person of this SoftwareImage.  # noqa: E501


        :return: The has_contact_person of this SoftwareImage.  # noqa: E501
        :rtype: list[object]
        """
        return self._has_contact_person

    @has_contact_person.setter
    def has_contact_person(self, has_contact_person):
        """Sets the has_contact_person of this SoftwareImage.


        :param has_contact_person: The has_contact_person of this SoftwareImage.  # noqa: E501
        :type: list[object]
        """

        self._has_contact_person = has_contact_person

    @property
    def has_purpose(self):
        """Gets the has_purpose of this SoftwareImage.  # noqa: E501


        :return: The has_purpose of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_purpose

    @has_purpose.setter
    def has_purpose(self, has_purpose):
        """Sets the has_purpose of this SoftwareImage.


        :param has_purpose: The has_purpose of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_purpose = has_purpose

    @property
    def id(self):
        """Gets the id of this SoftwareImage.  # noqa: E501


        :return: The id of this SoftwareImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoftwareImage.


        :param id: The id of this SoftwareImage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def has_sample_visualization(self):
        """Gets the has_sample_visualization of this SoftwareImage.  # noqa: E501


        :return: The has_sample_visualization of this SoftwareImage.  # noqa: E501
        :rtype: list[Visualization]
        """
        return self._has_sample_visualization

    @has_sample_visualization.setter
    def has_sample_visualization(self, has_sample_visualization):
        """Sets the has_sample_visualization of this SoftwareImage.


        :param has_sample_visualization: The has_sample_visualization of this SoftwareImage.  # noqa: E501
        :type: list[Visualization]
        """

        self._has_sample_visualization = has_sample_visualization

    @property
    def identifier(self):
        """Gets the identifier of this SoftwareImage.  # noqa: E501


        :return: The identifier of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SoftwareImage.


        :param identifier: The identifier of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._identifier = identifier

    @property
    def memory_requirements(self):
        """Gets the memory_requirements of this SoftwareImage.  # noqa: E501


        :return: The memory_requirements of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._memory_requirements

    @memory_requirements.setter
    def memory_requirements(self, memory_requirements):
        """Sets the memory_requirements of this SoftwareImage.


        :param memory_requirements: The memory_requirements of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._memory_requirements = memory_requirements

    @property
    def website(self):
        """Gets the website of this SoftwareImage.  # noqa: E501


        :return: The website of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this SoftwareImage.


        :param website: The website of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._website = website

    @property
    def citation(self):
        """Gets the citation of this SoftwareImage.  # noqa: E501


        :return: The citation of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this SoftwareImage.


        :param citation: The citation of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._citation = citation

    @property
    def author(self):
        """Gets the author of this SoftwareImage.  # noqa: E501


        :return: The author of this SoftwareImage.  # noqa: E501
        :rtype: list[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this SoftwareImage.


        :param author: The author of this SoftwareImage.  # noqa: E501
        :type: list[object]
        """

        self._author = author

    @property
    def processor_requirements(self):
        """Gets the processor_requirements of this SoftwareImage.  # noqa: E501


        :return: The processor_requirements of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._processor_requirements

    @processor_requirements.setter
    def processor_requirements(self, processor_requirements):
        """Sets the processor_requirements of this SoftwareImage.


        :param processor_requirements: The processor_requirements of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._processor_requirements = processor_requirements

    @property
    def has_usage_notes(self):
        """Gets the has_usage_notes of this SoftwareImage.  # noqa: E501


        :return: The has_usage_notes of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_usage_notes

    @has_usage_notes.setter
    def has_usage_notes(self, has_usage_notes):
        """Sets the has_usage_notes of this SoftwareImage.


        :param has_usage_notes: The has_usage_notes of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_usage_notes = has_usage_notes

    @property
    def short_description(self):
        """Gets the short_description of this SoftwareImage.  # noqa: E501


        :return: The short_description of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this SoftwareImage.


        :param short_description: The short_description of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._short_description = short_description

    @property
    def label(self):
        """Gets the label of this SoftwareImage.  # noqa: E501


        :return: The label of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SoftwareImage.


        :param label: The label of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def has_execution_command(self):
        """Gets the has_execution_command of this SoftwareImage.  # noqa: E501


        :return: The has_execution_command of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_execution_command

    @has_execution_command.setter
    def has_execution_command(self, has_execution_command):
        """Sets the has_execution_command of this SoftwareImage.


        :param has_execution_command: The has_execution_command of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_execution_command = has_execution_command

    @property
    def has_assumption(self):
        """Gets the has_assumption of this SoftwareImage.  # noqa: E501


        :return: The has_assumption of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_assumption

    @has_assumption.setter
    def has_assumption(self, has_assumption):
        """Sets the has_assumption of this SoftwareImage.


        :param has_assumption: The has_assumption of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_assumption = has_assumption

    @property
    def date_published(self):
        """Gets the date_published of this SoftwareImage.  # noqa: E501


        :return: The date_published of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this SoftwareImage.


        :param date_published: The date_published of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._date_published = date_published

    @property
    def operating_systems(self):
        """Gets the operating_systems of this SoftwareImage.  # noqa: E501


        :return: The operating_systems of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this SoftwareImage.


        :param operating_systems: The operating_systems of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._operating_systems = operating_systems

    @property
    def license(self):
        """Gets the license of this SoftwareImage.  # noqa: E501


        :return: The license of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this SoftwareImage.


        :param license: The license of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._license = license

    @property
    def has_source_code(self):
        """Gets the has_source_code of this SoftwareImage.  # noqa: E501


        :return: The has_source_code of this SoftwareImage.  # noqa: E501
        :rtype: list[SourceCode]
        """
        return self._has_source_code

    @has_source_code.setter
    def has_source_code(self, has_source_code):
        """Sets the has_source_code of this SoftwareImage.


        :param has_source_code: The has_source_code of this SoftwareImage.  # noqa: E501
        :type: list[SourceCode]
        """

        self._has_source_code = has_source_code

    @property
    def has_example(self):
        """Gets the has_example of this SoftwareImage.  # noqa: E501


        :return: The has_example of this SoftwareImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_example

    @has_example.setter
    def has_example(self, has_example):
        """Sets the has_example of this SoftwareImage.


        :param has_example: The has_example of this SoftwareImage.  # noqa: E501
        :type: list[str]
        """

        self._has_example = has_example

    @property
    def publisher(self):
        """Gets the publisher of this SoftwareImage.  # noqa: E501


        :return: The publisher of this SoftwareImage.  # noqa: E501
        :rtype: list[object]
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this SoftwareImage.


        :param publisher: The publisher of this SoftwareImage.  # noqa: E501
        :type: list[object]
        """

        self._publisher = publisher

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SoftwareImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

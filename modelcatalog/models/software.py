# coding: utf-8

"""
    Model Catalog

    This is MINT Model Catalog You can find out more about Model Catalog at [https://w3id.org/mint/modelCatalog/](https://w3id.org/mint/modelCatalog/)  # noqa: E501

    OpenAPI spec version: v1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Software(object):
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
        'keywords': 'list[str]',
        'has_documentation': 'list[str]',
        'software_requirements': 'list[str]',
        'has_version': 'list[SoftwareVersion]',
        'has_typical_data_source': 'list[str]',
        'has_download_url': 'list[str]',
        'description': 'list[str]',
        'reference_publication': 'list[str]',
        'screenshot': 'list[Image]',
        'type': 'list[str]',
        'has_installation_instructions': 'list[str]',
        'date_created': 'list[str]',
        'contributor': 'list[Person]',
        'has_faq': 'list[str]',
        'has_contact_person': 'list[Person]',
        'logo': 'list[Image]',
        'has_purpose': 'list[str]',
        'id': 'str',
        'has_sample_visualization': 'list[Visualization]',
        'memory_requirements': 'list[str]',
        'identifier': 'list[str]',
        'website': 'list[str]',
        'citation': 'list[str]',
        'author': 'list[object]',
        'processor_requirements': 'list[str]',
        'short_description': 'list[str]',
        'label': 'list[str]',
        'has_assumption': 'list[str]',
        'date_published': 'list[str]',
        'operating_systems': 'list[str]',
        'license': 'list[str]',
        'has_source_code': 'list[SourceCode]',
        'publisher': 'list[object]',
        'funding_source': 'list[Organization]'
    }

    attribute_map = {
        'keywords': 'keywords',
        'has_documentation': 'hasDocumentation',
        'software_requirements': 'softwareRequirements',
        'has_version': 'hasVersion',
        'has_typical_data_source': 'hasTypicalDataSource',
        'has_download_url': 'hasDownloadURL',
        'description': 'description',
        'reference_publication': 'referencePublication',
        'screenshot': 'screenshot',
        'type': 'type',
        'has_installation_instructions': 'hasInstallationInstructions',
        'date_created': 'dateCreated',
        'contributor': 'contributor',
        'has_faq': 'hasFAQ',
        'has_contact_person': 'hasContactPerson',
        'logo': 'logo',
        'has_purpose': 'hasPurpose',
        'id': 'id',
        'has_sample_visualization': 'hasSampleVisualization',
        'memory_requirements': 'memoryRequirements',
        'identifier': 'identifier',
        'website': 'website',
        'citation': 'citation',
        'author': 'author',
        'processor_requirements': 'processorRequirements',
        'short_description': 'shortDescription',
        'label': 'label',
        'has_assumption': 'hasAssumption',
        'date_published': 'datePublished',
        'operating_systems': 'operatingSystems',
        'license': 'license',
        'has_source_code': 'hasSourceCode',
        'publisher': 'publisher',
        'funding_source': 'fundingSource'
    }

    def __init__(self, keywords=None, has_documentation=None, software_requirements=None, has_version=None, has_typical_data_source=None, has_download_url=None, description=None, reference_publication=None, screenshot=None, type=None, has_installation_instructions=None, date_created=None, contributor=None, has_faq=None, has_contact_person=None, logo=None, has_purpose=None, id=None, has_sample_visualization=None, memory_requirements=None, identifier=None, website=None, citation=None, author=None, processor_requirements=None, short_description=None, label=None, has_assumption=None, date_published=None, operating_systems=None, license=None, has_source_code=None, publisher=None, funding_source=None):  # noqa: E501
        """Software - a model defined in OpenAPI"""  # noqa: E501

        self._keywords = None
        self._has_documentation = None
        self._software_requirements = None
        self._has_version = None
        self._has_typical_data_source = None
        self._has_download_url = None
        self._description = None
        self._reference_publication = None
        self._screenshot = None
        self._type = None
        self._has_installation_instructions = None
        self._date_created = None
        self._contributor = None
        self._has_faq = None
        self._has_contact_person = None
        self._logo = None
        self._has_purpose = None
        self._id = None
        self._has_sample_visualization = None
        self._memory_requirements = None
        self._identifier = None
        self._website = None
        self._citation = None
        self._author = None
        self._processor_requirements = None
        self._short_description = None
        self._label = None
        self._has_assumption = None
        self._date_published = None
        self._operating_systems = None
        self._license = None
        self._has_source_code = None
        self._publisher = None
        self._funding_source = None
        self.discriminator = None

        if keywords is not None:
            self.keywords = keywords
        else:
            if hasattr(self, '_keywords'): del self._keywords
            if hasattr(self.attribute_map, 'keywords'): del self.attribute_map['keywords']
            if hasattr(self.openapi_types, 'keywords'): del self.openapi_types['keywords']
        if has_documentation is not None:
            self.has_documentation = has_documentation
        else:
            if hasattr(self, '_has_documentation'): del self._has_documentation
            if hasattr(self.attribute_map, 'has_documentation'): del self.attribute_map['has_documentation']
            if hasattr(self.openapi_types, 'has_documentation'): del self.openapi_types['has_documentation']
        if software_requirements is not None:
            self.software_requirements = software_requirements
        else:
            if hasattr(self, '_software_requirements'): del self._software_requirements
            if hasattr(self.attribute_map, 'software_requirements'): del self.attribute_map['software_requirements']
            if hasattr(self.openapi_types, 'software_requirements'): del self.openapi_types['software_requirements']
        if has_version is not None:
            self.has_version = has_version
        else:
            if hasattr(self, '_has_version'): del self._has_version
            if hasattr(self.attribute_map, 'has_version'): del self.attribute_map['has_version']
            if hasattr(self.openapi_types, 'has_version'): del self.openapi_types['has_version']
        if has_typical_data_source is not None:
            self.has_typical_data_source = has_typical_data_source
        else:
            if hasattr(self, '_has_typical_data_source'): del self._has_typical_data_source
            if hasattr(self.attribute_map, 'has_typical_data_source'): del self.attribute_map['has_typical_data_source']
            if hasattr(self.openapi_types, 'has_typical_data_source'): del self.openapi_types['has_typical_data_source']
        if has_download_url is not None:
            self.has_download_url = has_download_url
        else:
            if hasattr(self, '_has_download_url'): del self._has_download_url
            if hasattr(self.attribute_map, 'has_download_url'): del self.attribute_map['has_download_url']
            if hasattr(self.openapi_types, 'has_download_url'): del self.openapi_types['has_download_url']
        if description is not None:
            self.description = description
        else:
            if hasattr(self, '_description'): del self._description
            if hasattr(self.attribute_map, 'description'): del self.attribute_map['description']
            if hasattr(self.openapi_types, 'description'): del self.openapi_types['description']
        if reference_publication is not None:
            self.reference_publication = reference_publication
        else:
            if hasattr(self, '_reference_publication'): del self._reference_publication
            if hasattr(self.attribute_map, 'reference_publication'): del self.attribute_map['reference_publication']
            if hasattr(self.openapi_types, 'reference_publication'): del self.openapi_types['reference_publication']
        if screenshot is not None:
            self.screenshot = screenshot
        else:
            if hasattr(self, '_screenshot'): del self._screenshot
            if hasattr(self.attribute_map, 'screenshot'): del self.attribute_map['screenshot']
            if hasattr(self.openapi_types, 'screenshot'): del self.openapi_types['screenshot']
        if type is not None:
            self.type = type
        else:
            if hasattr(self, '_type'): del self._type
            if hasattr(self.attribute_map, 'type'): del self.attribute_map['type']
            if hasattr(self.openapi_types, 'type'): del self.openapi_types['type']
        if has_installation_instructions is not None:
            self.has_installation_instructions = has_installation_instructions
        else:
            if hasattr(self, '_has_installation_instructions'): del self._has_installation_instructions
            if hasattr(self.attribute_map, 'has_installation_instructions'): del self.attribute_map['has_installation_instructions']
            if hasattr(self.openapi_types, 'has_installation_instructions'): del self.openapi_types['has_installation_instructions']
        if date_created is not None:
            self.date_created = date_created
        else:
            if hasattr(self, '_date_created'): del self._date_created
            if hasattr(self.attribute_map, 'date_created'): del self.attribute_map['date_created']
            if hasattr(self.openapi_types, 'date_created'): del self.openapi_types['date_created']
        if contributor is not None:
            self.contributor = contributor
        else:
            if hasattr(self, '_contributor'): del self._contributor
            if hasattr(self.attribute_map, 'contributor'): del self.attribute_map['contributor']
            if hasattr(self.openapi_types, 'contributor'): del self.openapi_types['contributor']
        if has_faq is not None:
            self.has_faq = has_faq
        else:
            if hasattr(self, '_has_faq'): del self._has_faq
            if hasattr(self.attribute_map, 'has_faq'): del self.attribute_map['has_faq']
            if hasattr(self.openapi_types, 'has_faq'): del self.openapi_types['has_faq']
        if has_contact_person is not None:
            self.has_contact_person = has_contact_person
        else:
            if hasattr(self, '_has_contact_person'): del self._has_contact_person
            if hasattr(self.attribute_map, 'has_contact_person'): del self.attribute_map['has_contact_person']
            if hasattr(self.openapi_types, 'has_contact_person'): del self.openapi_types['has_contact_person']
        if logo is not None:
            self.logo = logo
        else:
            if hasattr(self, '_logo'): del self._logo
            if hasattr(self.attribute_map, 'logo'): del self.attribute_map['logo']
            if hasattr(self.openapi_types, 'logo'): del self.openapi_types['logo']
        if has_purpose is not None:
            self.has_purpose = has_purpose
        else:
            if hasattr(self, '_has_purpose'): del self._has_purpose
            if hasattr(self.attribute_map, 'has_purpose'): del self.attribute_map['has_purpose']
            if hasattr(self.openapi_types, 'has_purpose'): del self.openapi_types['has_purpose']
        if id is not None:
            self.id = id
        if has_sample_visualization is not None:
            self.has_sample_visualization = has_sample_visualization
        else:
            if hasattr(self, '_has_sample_visualization'): del self._has_sample_visualization
            if hasattr(self.attribute_map, 'has_sample_visualization'): del self.attribute_map['has_sample_visualization']
            if hasattr(self.openapi_types, 'has_sample_visualization'): del self.openapi_types['has_sample_visualization']
        if memory_requirements is not None:
            self.memory_requirements = memory_requirements
        else:
            if hasattr(self, '_memory_requirements'): del self._memory_requirements
            if hasattr(self.attribute_map, 'memory_requirements'): del self.attribute_map['memory_requirements']
            if hasattr(self.openapi_types, 'memory_requirements'): del self.openapi_types['memory_requirements']
        if identifier is not None:
            self.identifier = identifier
        else:
            if hasattr(self, '_identifier'): del self._identifier
            if hasattr(self.attribute_map, 'identifier'): del self.attribute_map['identifier']
            if hasattr(self.openapi_types, 'identifier'): del self.openapi_types['identifier']
        if website is not None:
            self.website = website
        else:
            if hasattr(self, '_website'): del self._website
            if hasattr(self.attribute_map, 'website'): del self.attribute_map['website']
            if hasattr(self.openapi_types, 'website'): del self.openapi_types['website']
        if citation is not None:
            self.citation = citation
        else:
            if hasattr(self, '_citation'): del self._citation
            if hasattr(self.attribute_map, 'citation'): del self.attribute_map['citation']
            if hasattr(self.openapi_types, 'citation'): del self.openapi_types['citation']
        if author is not None:
            self.author = author
        else:
            if hasattr(self, '_author'): del self._author
            if hasattr(self.attribute_map, 'author'): del self.attribute_map['author']
            if hasattr(self.openapi_types, 'author'): del self.openapi_types['author']
        if processor_requirements is not None:
            self.processor_requirements = processor_requirements
        else:
            if hasattr(self, '_processor_requirements'): del self._processor_requirements
            if hasattr(self.attribute_map, 'processor_requirements'): del self.attribute_map['processor_requirements']
            if hasattr(self.openapi_types, 'processor_requirements'): del self.openapi_types['processor_requirements']
        if short_description is not None:
            self.short_description = short_description
        else:
            if hasattr(self, '_short_description'): del self._short_description
            if hasattr(self.attribute_map, 'short_description'): del self.attribute_map['short_description']
            if hasattr(self.openapi_types, 'short_description'): del self.openapi_types['short_description']
        if label is not None:
            self.label = label
        else:
            if hasattr(self, '_label'): del self._label
            if hasattr(self.attribute_map, 'label'): del self.attribute_map['label']
            if hasattr(self.openapi_types, 'label'): del self.openapi_types['label']
        if has_assumption is not None:
            self.has_assumption = has_assumption
        else:
            if hasattr(self, '_has_assumption'): del self._has_assumption
            if hasattr(self.attribute_map, 'has_assumption'): del self.attribute_map['has_assumption']
            if hasattr(self.openapi_types, 'has_assumption'): del self.openapi_types['has_assumption']
        if date_published is not None:
            self.date_published = date_published
        else:
            if hasattr(self, '_date_published'): del self._date_published
            if hasattr(self.attribute_map, 'date_published'): del self.attribute_map['date_published']
            if hasattr(self.openapi_types, 'date_published'): del self.openapi_types['date_published']
        if operating_systems is not None:
            self.operating_systems = operating_systems
        else:
            if hasattr(self, '_operating_systems'): del self._operating_systems
            if hasattr(self.attribute_map, 'operating_systems'): del self.attribute_map['operating_systems']
            if hasattr(self.openapi_types, 'operating_systems'): del self.openapi_types['operating_systems']
        if license is not None:
            self.license = license
        else:
            if hasattr(self, '_license'): del self._license
            if hasattr(self.attribute_map, 'license'): del self.attribute_map['license']
            if hasattr(self.openapi_types, 'license'): del self.openapi_types['license']
        if has_source_code is not None:
            self.has_source_code = has_source_code
        else:
            if hasattr(self, '_has_source_code'): del self._has_source_code
            if hasattr(self.attribute_map, 'has_source_code'): del self.attribute_map['has_source_code']
            if hasattr(self.openapi_types, 'has_source_code'): del self.openapi_types['has_source_code']
        if publisher is not None:
            self.publisher = publisher
        else:
            if hasattr(self, '_publisher'): del self._publisher
            if hasattr(self.attribute_map, 'publisher'): del self.attribute_map['publisher']
            if hasattr(self.openapi_types, 'publisher'): del self.openapi_types['publisher']
        if funding_source is not None:
            self.funding_source = funding_source
        else:
            if hasattr(self, '_funding_source'): del self._funding_source
            if hasattr(self.attribute_map, 'funding_source'): del self.attribute_map['funding_source']
            if hasattr(self.openapi_types, 'funding_source'): del self.openapi_types['funding_source']

    @property
    def keywords(self):
        """Gets the keywords of this Software.  # noqa: E501


        :return: The keywords of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Software.


        :param keywords: The keywords of this Software.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def has_documentation(self):
        """Gets the has_documentation of this Software.  # noqa: E501


        :return: The has_documentation of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_documentation

    @has_documentation.setter
    def has_documentation(self, has_documentation):
        """Sets the has_documentation of this Software.


        :param has_documentation: The has_documentation of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_documentation = has_documentation

    @property
    def software_requirements(self):
        """Gets the software_requirements of this Software.  # noqa: E501


        :return: The software_requirements of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._software_requirements

    @software_requirements.setter
    def software_requirements(self, software_requirements):
        """Sets the software_requirements of this Software.


        :param software_requirements: The software_requirements of this Software.  # noqa: E501
        :type: list[str]
        """

        self._software_requirements = software_requirements

    @property
    def has_version(self):
        """Gets the has_version of this Software.  # noqa: E501


        :return: The has_version of this Software.  # noqa: E501
        :rtype: list[SoftwareVersion]
        """
        return self._has_version

    @has_version.setter
    def has_version(self, has_version):
        """Sets the has_version of this Software.


        :param has_version: The has_version of this Software.  # noqa: E501
        :type: list[SoftwareVersion]
        """

        self._has_version = has_version

    @property
    def has_typical_data_source(self):
        """Gets the has_typical_data_source of this Software.  # noqa: E501


        :return: The has_typical_data_source of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_typical_data_source

    @has_typical_data_source.setter
    def has_typical_data_source(self, has_typical_data_source):
        """Sets the has_typical_data_source of this Software.


        :param has_typical_data_source: The has_typical_data_source of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_typical_data_source = has_typical_data_source

    @property
    def has_download_url(self):
        """Gets the has_download_url of this Software.  # noqa: E501


        :return: The has_download_url of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_download_url

    @has_download_url.setter
    def has_download_url(self, has_download_url):
        """Sets the has_download_url of this Software.


        :param has_download_url: The has_download_url of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_download_url = has_download_url

    @property
    def description(self):
        """Gets the description of this Software.  # noqa: E501


        :return: The description of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Software.


        :param description: The description of this Software.  # noqa: E501
        :type: list[str]
        """

        self._description = description

    @property
    def reference_publication(self):
        """Gets the reference_publication of this Software.  # noqa: E501


        :return: The reference_publication of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._reference_publication

    @reference_publication.setter
    def reference_publication(self, reference_publication):
        """Sets the reference_publication of this Software.


        :param reference_publication: The reference_publication of this Software.  # noqa: E501
        :type: list[str]
        """

        self._reference_publication = reference_publication

    @property
    def screenshot(self):
        """Gets the screenshot of this Software.  # noqa: E501


        :return: The screenshot of this Software.  # noqa: E501
        :rtype: list[Image]
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this Software.


        :param screenshot: The screenshot of this Software.  # noqa: E501
        :type: list[Image]
        """

        self._screenshot = screenshot

    @property
    def type(self):
        """Gets the type of this Software.  # noqa: E501


        :return: The type of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Software.


        :param type: The type of this Software.  # noqa: E501
        :type: list[str]
        """

        self._type = type

    @property
    def has_installation_instructions(self):
        """Gets the has_installation_instructions of this Software.  # noqa: E501


        :return: The has_installation_instructions of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_installation_instructions

    @has_installation_instructions.setter
    def has_installation_instructions(self, has_installation_instructions):
        """Sets the has_installation_instructions of this Software.


        :param has_installation_instructions: The has_installation_instructions of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_installation_instructions = has_installation_instructions

    @property
    def date_created(self):
        """Gets the date_created of this Software.  # noqa: E501


        :return: The date_created of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Software.


        :param date_created: The date_created of this Software.  # noqa: E501
        :type: list[str]
        """

        self._date_created = date_created

    @property
    def contributor(self):
        """Gets the contributor of this Software.  # noqa: E501


        :return: The contributor of this Software.  # noqa: E501
        :rtype: list[Person]
        """
        return self._contributor

    @contributor.setter
    def contributor(self, contributor):
        """Sets the contributor of this Software.


        :param contributor: The contributor of this Software.  # noqa: E501
        :type: list[Person]
        """

        self._contributor = contributor

    @property
    def has_faq(self):
        """Gets the has_faq of this Software.  # noqa: E501


        :return: The has_faq of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_faq

    @has_faq.setter
    def has_faq(self, has_faq):
        """Sets the has_faq of this Software.


        :param has_faq: The has_faq of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_faq = has_faq

    @property
    def has_contact_person(self):
        """Gets the has_contact_person of this Software.  # noqa: E501


        :return: The has_contact_person of this Software.  # noqa: E501
        :rtype: list[Person]
        """
        return self._has_contact_person

    @has_contact_person.setter
    def has_contact_person(self, has_contact_person):
        """Sets the has_contact_person of this Software.


        :param has_contact_person: The has_contact_person of this Software.  # noqa: E501
        :type: list[Person]
        """

        self._has_contact_person = has_contact_person

    @property
    def logo(self):
        """Gets the logo of this Software.  # noqa: E501


        :return: The logo of this Software.  # noqa: E501
        :rtype: list[Image]
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Software.


        :param logo: The logo of this Software.  # noqa: E501
        :type: list[Image]
        """

        self._logo = logo

    @property
    def has_purpose(self):
        """Gets the has_purpose of this Software.  # noqa: E501


        :return: The has_purpose of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_purpose

    @has_purpose.setter
    def has_purpose(self, has_purpose):
        """Sets the has_purpose of this Software.


        :param has_purpose: The has_purpose of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_purpose = has_purpose

    @property
    def id(self):
        """Gets the id of this Software.  # noqa: E501


        :return: The id of this Software.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Software.


        :param id: The id of this Software.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def has_sample_visualization(self):
        """Gets the has_sample_visualization of this Software.  # noqa: E501


        :return: The has_sample_visualization of this Software.  # noqa: E501
        :rtype: list[Visualization]
        """
        return self._has_sample_visualization

    @has_sample_visualization.setter
    def has_sample_visualization(self, has_sample_visualization):
        """Sets the has_sample_visualization of this Software.


        :param has_sample_visualization: The has_sample_visualization of this Software.  # noqa: E501
        :type: list[Visualization]
        """

        self._has_sample_visualization = has_sample_visualization

    @property
    def memory_requirements(self):
        """Gets the memory_requirements of this Software.  # noqa: E501


        :return: The memory_requirements of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._memory_requirements

    @memory_requirements.setter
    def memory_requirements(self, memory_requirements):
        """Sets the memory_requirements of this Software.


        :param memory_requirements: The memory_requirements of this Software.  # noqa: E501
        :type: list[str]
        """

        self._memory_requirements = memory_requirements

    @property
    def identifier(self):
        """Gets the identifier of this Software.  # noqa: E501


        :return: The identifier of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Software.


        :param identifier: The identifier of this Software.  # noqa: E501
        :type: list[str]
        """

        self._identifier = identifier

    @property
    def website(self):
        """Gets the website of this Software.  # noqa: E501


        :return: The website of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Software.


        :param website: The website of this Software.  # noqa: E501
        :type: list[str]
        """

        self._website = website

    @property
    def citation(self):
        """Gets the citation of this Software.  # noqa: E501


        :return: The citation of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """Sets the citation of this Software.


        :param citation: The citation of this Software.  # noqa: E501
        :type: list[str]
        """

        self._citation = citation

    @property
    def author(self):
        """Gets the author of this Software.  # noqa: E501


        :return: The author of this Software.  # noqa: E501
        :rtype: list[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Software.


        :param author: The author of this Software.  # noqa: E501
        :type: list[object]
        """

        self._author = author

    @property
    def processor_requirements(self):
        """Gets the processor_requirements of this Software.  # noqa: E501


        :return: The processor_requirements of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._processor_requirements

    @processor_requirements.setter
    def processor_requirements(self, processor_requirements):
        """Sets the processor_requirements of this Software.


        :param processor_requirements: The processor_requirements of this Software.  # noqa: E501
        :type: list[str]
        """

        self._processor_requirements = processor_requirements

    @property
    def short_description(self):
        """Gets the short_description of this Software.  # noqa: E501


        :return: The short_description of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this Software.


        :param short_description: The short_description of this Software.  # noqa: E501
        :type: list[str]
        """

        self._short_description = short_description

    @property
    def label(self):
        """Gets the label of this Software.  # noqa: E501


        :return: The label of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Software.


        :param label: The label of this Software.  # noqa: E501
        :type: list[str]
        """

        self._label = label

    @property
    def has_assumption(self):
        """Gets the has_assumption of this Software.  # noqa: E501


        :return: The has_assumption of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._has_assumption

    @has_assumption.setter
    def has_assumption(self, has_assumption):
        """Sets the has_assumption of this Software.


        :param has_assumption: The has_assumption of this Software.  # noqa: E501
        :type: list[str]
        """

        self._has_assumption = has_assumption

    @property
    def date_published(self):
        """Gets the date_published of this Software.  # noqa: E501


        :return: The date_published of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this Software.


        :param date_published: The date_published of this Software.  # noqa: E501
        :type: list[str]
        """

        self._date_published = date_published

    @property
    def operating_systems(self):
        """Gets the operating_systems of this Software.  # noqa: E501


        :return: The operating_systems of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this Software.


        :param operating_systems: The operating_systems of this Software.  # noqa: E501
        :type: list[str]
        """

        self._operating_systems = operating_systems

    @property
    def license(self):
        """Gets the license of this Software.  # noqa: E501


        :return: The license of this Software.  # noqa: E501
        :rtype: list[str]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Software.


        :param license: The license of this Software.  # noqa: E501
        :type: list[str]
        """

        self._license = license

    @property
    def has_source_code(self):
        """Gets the has_source_code of this Software.  # noqa: E501


        :return: The has_source_code of this Software.  # noqa: E501
        :rtype: list[SourceCode]
        """
        return self._has_source_code

    @has_source_code.setter
    def has_source_code(self, has_source_code):
        """Sets the has_source_code of this Software.


        :param has_source_code: The has_source_code of this Software.  # noqa: E501
        :type: list[SourceCode]
        """

        self._has_source_code = has_source_code

    @property
    def publisher(self):
        """Gets the publisher of this Software.  # noqa: E501


        :return: The publisher of this Software.  # noqa: E501
        :rtype: list[object]
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Software.


        :param publisher: The publisher of this Software.  # noqa: E501
        :type: list[object]
        """

        self._publisher = publisher

    @property
    def funding_source(self):
        """Gets the funding_source of this Software.  # noqa: E501


        :return: The funding_source of this Software.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._funding_source

    @funding_source.setter
    def funding_source(self, funding_source):
        """Sets the funding_source of this Software.


        :param funding_source: The funding_source of this Software.  # noqa: E501
        :type: list[Organization]
        """

        self._funding_source = funding_source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
            else:
                continue                
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
        if not isinstance(other, Software):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Model Catalog

    This is the API of the  Software Description Ontology at [https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.3.0/index-en.html](https://w3id.org/okn/o/sdm)  # noqa: E501

    OpenAPI spec version: v1.3.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "modelcatalog-api"
VERSION = "1.7.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Model Catalog",
    author_email="",
    url="https://pypi.org/project/modelcatalog-api/",
    keywords=["OpenAPI", "OpenAPI-Generator", "Model Catalog"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the API of the  Software Description Ontology at [https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.3.0/index-en.html](https://w3id.org/okn/o/sdm)  # noqa: E501
    """
)

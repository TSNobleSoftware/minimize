from setuptools import setup, find_packages
from pathlib import Path

version = "0.0.1"
here = Path(__file__).parent.resolve()

with open(here.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(here.joinpath("requirements.txt"), encoding="utf-8") as f:
    requirements = f.readlines()

setup(
    name="PACKAGE_NAME",
    version=version,
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="Url to the repo",
    author="NAME",
    author_email="CONTACT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Any other classifiers..."
    ],
    keywords=["Relevant", "keywords", "go", "here"],
    packages=find_packages(),
    python_requires="Supported versions e.g. >=3.5",
    install_requires=[requirements],
    project_urls={
        "Bug Reports": "Url to issues section of the repo",
        "Source": "Url to the repo",
    }
)

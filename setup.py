from setuptools import setup, find_packages
from pathlib import Path

version = "0.0.2"
here = Path(__file__).parent.resolve()

with open(here.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(here.joinpath("requirements.txt"), encoding="utf-8") as f:
    requirements = f.readlines()

setup(
    name="python-minimize",
    version=version,
    description="Reduce the size of MicroPython projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TSNobleSoftware/minimize",
    author="Tom Noble",
    author_email="t.s.noble@outlook.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: MicroPython",
    ],
    keywords=["python", "micropython", "cli"],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[requirements],
    project_urls={
        "Bug Reports": "https://github.com/TSNobleSoftware/minimize/issues",
        "Source": "https://github.com/TSNobleSoftware/minimize",
    }
)

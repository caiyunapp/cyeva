import setuptools
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, "README.md"), "r") as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, "requirements/requirements.txt")
with open(requirements_path) as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cyeva",
    version="0.1.0-beta",
    author="caiyunapp",
    author_email="oss@caiyunapp.com",
    description="A package to evaluate of forecast",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    package_data={"": ["*.csv", "*.config", "*.nl", "*.json"]},
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Framework :: Sphinx"
    ],
    python_requires=">=3.7"
)

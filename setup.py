import setuptools
import os
from .cyeva import __version__

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, "README.md"), "r") as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, "requirements/requirements.txt")
with open(requirements_path) as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cyeva",
    version=__version__,
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
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7"
)

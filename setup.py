import setuptools
import os
import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r", encoding="utf8") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(FILE_PATH, "README.md"), "r", encoding="utf8") as fh:
    long_description = fh.read()

requirements_path = os.path.join(FILE_PATH, "requirements/requirements.txt")
with open(requirements_path, encoding="utf8") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cyeva",
    author="caiyunapp",
    version=get_version("cyeva/__init__.py"),
    author_email="oss@caiyunapp.com",
    description="A package to evaluate weather forecast correction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caiyunapp/cyeva",
    include_package_data=True,
    package_data={"": ["*.csv", "*.config", "*.nl", "*.json"]},
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
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
        "Framework :: Sphinx",
    ],
    python_requires=">=3.7",
)

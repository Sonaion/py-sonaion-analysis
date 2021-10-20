import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-sonaion-analysis",
    version="0.0.2",
    description="Library for creating visualiziations and analysations of REyeker, REyeker 2.0, Eyetracking, EEG and Behavioral Data.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sonaion/py-sonaion-analysis",
    author="Jonas Mucke",
    author_email="jonas.mucke@web.com",
    license="BSD 3-Clause",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["sonaion_analysis"],
    include_package_data=True,
    install_requires=[""],
)
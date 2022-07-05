from setuptools import setup

NAME="Housing_predictor"
VERSION="0.0.1"
AUTHOR="GSSV"
DESCRIPTION="lets wait for the code"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements():
    with open("REQUIREMENT_FILE_NAME") as required_file:
        return required_file.readlines()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    intall_requi=get_requirements()
)
from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List:
    """
    :param file_path:
    :return: requirements -> list of requirements
    """
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readline()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Nattapong',
    author_email='natt.nawarat@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)

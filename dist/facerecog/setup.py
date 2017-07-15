from os import path
from setuptools import setup, find_packages

project_name = 'facerecog'

setup(
    name=project_name,
    version='0.0.1',
    description='PyQt OpenCV Face Recognition Widget',
    url='https://github.com/benhoff/blog',
    license='GPL3',
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    packages = [project_name],
    package_data={'': '*.xml'},
    install_requires=[
        'PyQt5',
        'numpy',
        ],

    extras_require={
        'dev': ['twine'],
        'cv': ['opencv-python'],
    }
)

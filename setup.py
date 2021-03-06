from setuptools import find_packages, setup

setup(
    name="blog",
    version='0.0.1',
    description='blog',
    url='https://github.com/benhoff/blog',
    license='GPL3',
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    packages= find_packages(), # exclude=['docs', 'tests']
    install_requires=[
        'pelican',
        'typogrify',
        'jupyter',
        'Markdown',
        'ghp-import',
        'wheel',
        ],

    extras_require={
        'dev': ['flake8', 'twine'],
        'vim': ['jedi',],
    }
)

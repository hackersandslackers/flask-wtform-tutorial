"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-WTF Tutorial',
    version='0.0.1',
    description='Tutorial to implement forms in your Flask app.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/flask-wtform-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Flask Flask-WTF Forms',
    packages=find_packages(),
    install_requires=['Flask',
                      'Flask-WTF'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run=wsgi:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/flask-wtform-tutorial/issues',
        'Source': 'https://github.com/toddbirchard/flask-wtform-tutorial/',
    },
)

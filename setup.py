from setuptools import setup, find_packages
    
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name = 'disney_movies',
    version = '0.0.1',
    description = 'This package is used for gathering and analyzing data on Disney movies and their ratings.',
    author = 'Daisy Harris, Olivia Hanks',
    author_email = 'dasharon@byu.edu',
    packages = find_packages(),
    install_requires = parse_requirements('requirements.txt'),
    package_data = {'disney_movies': ['datasets/*.csv']},
    long_description = long_description
)

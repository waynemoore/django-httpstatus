from setuptools import setup, find_packages

setup(
    name = "django-httpstatus",
    version = "0.1",
    url = 'http://github.com/shroomling/django-httpstatus',
    license = 'BSD',
    description = 'Django Helper Exceptions for generating HTTP error responses',
    author = 'Wayne Moore',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)

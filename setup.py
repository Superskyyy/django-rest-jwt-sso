# coding: utf-8
import os
from setuptools import find_packages, setup
import rest_framework_jwt_sso


INSTALL_REQUIRES = ["PyJWT>1.5", "Django>3", "djangorestframework>3", "cryptography>2.5", "PyNaCl>1.2"]


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="django-rest-jwt-sso",
    version=rest_framework_jwt_sso.VERSION,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    license="MIT License",
    description="Yet another SSO solution for Django REST Framework",
    long_description=README,
    url="https://github.com/iqueensu/django-rest-jwt-sso",
    author="Somion",
    author_email="calibur.tonyt@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=INSTALL_REQUIRES,
)

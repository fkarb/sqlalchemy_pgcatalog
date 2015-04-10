"""
Setup for sqlalchemy_pgcatalog
"""

from setuptools import find_packages, setup

setup_params = dict(
    name="sqlalchemy_pgcatalog",
    description="SQLAlchemy definitions for PostgreSQL catalog tables",
    packages=find_packages(),
    version = "0.1.0",
    install_requires = ["sqlalchemy>=0.7.0"],
)

if __name__ == '__main__':
    setup(**setup_params)

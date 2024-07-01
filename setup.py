from setuptools import setup, find_packages

# setup(name="octo", packages=["octo"])
setup(
    name="octo",
    packages=find_packages(include=["octo", "octo.*"]),
)

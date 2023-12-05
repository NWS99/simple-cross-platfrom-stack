from setuptools import setup, find_packages

setup(
    name="simple-cross-platfrom-stack",
    version="0.1",
    packages=find_packages(),
    scripts=["scripts/frontend/main.py"]
)
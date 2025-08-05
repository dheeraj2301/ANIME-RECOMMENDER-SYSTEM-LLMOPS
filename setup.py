from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="LLMOPS-4",
    version="0.1",
    author="Dheeraj",
    packages=find_packages(),
    install_requires=requirements
)
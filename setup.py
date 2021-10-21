from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy"]

setup(
    name="StockOptionOptimizer",
    version="0.0.1",
    author='Christos Grigoras',
    author_email='chris.grigoras@gmail.com',
    description='Stock Option Optimizer',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ChristosGrigoras/Stock-Option-Optimizer",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

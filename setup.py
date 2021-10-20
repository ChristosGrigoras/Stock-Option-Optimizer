from setuptools import setup

setup(
    name='StockOptionOptimizer',
    url='https://github.com/ChristosGrigoras/Stock-Option-Optimizer',
    author='Christos Grigoras',
    author_email='chris.grigoras@gmail.com',
    packages=['sooptimizer'],
    install_requires=['numpy'],
    version='0.1',
    license='MIT',
    description='Stock Option Optimizer',
    long_description=open('README.txt').read(),
)

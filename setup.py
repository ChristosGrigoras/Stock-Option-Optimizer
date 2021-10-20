from setuptools import setup

setup(
    name='Stock-Option-Optimizer',
    url='https://github.com/ChristosGrigoras/Stock-Option-Optimizer',
    author='Christos Grigoras',
    author_email='cgrigoras@gmail.com',
    packages=['optimizer'],
    install_requires=['numpy'],
    version='0.1',
    license='MIT',
    description='Stock Option Optimizer',
    long_description=open('README.txt').read(),
)

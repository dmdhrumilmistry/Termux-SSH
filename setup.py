from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'Termux-SSH',
    version = '1.0.0',
    license='MIT License',
    description = 'Termux SSH helps you to setup SSH server on termux application on android, which helps you to execute tasks remotely through terminal/cmd/powershell/termux.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['wheel', 'colorama', 'prettytable'],
)
import platform
from pathlib import Path

from setuptools import find_packages, setup
from distutils.version import StrictVersion


if StrictVersion(platform.python_version()) < StrictVersion('3.0.0'):
    raise Exception("`t99-mailgun` support python version >= 3.0.0 only.")

setup(
    name='mailgun',
    version='1.0.0',
    description=(
        'Flask Mailgun for Python web framework'
    ),
    long_description=Path(__file__).parent.joinpath('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    packages=find_packages(),
    package_data={
        't99': ['mailgun/*'],
    },
    install_requires=[],
    url='https://github.com/1099policy-packages/flask-mailgun',
    author='Ray Ventura',
    author_email='ray@1099policy.com',
)
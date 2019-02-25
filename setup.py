from setuptools import setup, find_packages
from os import path
from io import open

setup(
    name='py3_openstudio_linux_sdk',
    version='2.7.0',
    description='OpenStudio python bindings.',
    long_description="""
    """,
    long_description_content_type='text/markdown',
    url='https://github.com/arif-hanif/py3-openstudio-linux-sdk',
    author='Arif Hanif',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='openstudio py3 setuptools development',
    packages=find_packages(include=['py3_openstudio_linux_sdk']),
    include_package_data=True,
    install_requires=[
        "pytest>=3.5.1",
    ],
)

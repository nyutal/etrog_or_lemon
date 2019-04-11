# Created by @nyutal on 20/01/2019
from setuptools import setup, find_packages


install_requires = [
    'fastai',
    'torch',
    'torchvision',
    'starlette',
    'uvicorn',
    'aiohttp',
    'python-multipart',
]

setup_requires = []
tests_require = []


setup(
    name= 'etrog_or_lemon',
    description='web app to classify etrog vs. lemon',
    version='1.0.0',
    packages=find_packages('./src'),
    package_dir={'':'src'},
    author='Nadav Yutal',
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
)


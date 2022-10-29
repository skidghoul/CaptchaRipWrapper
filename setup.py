import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name                        = 'captcha.rip',
    version                     = '1.0.0',
    packages                    = find_packages(),
    include_package_data        = True,
    license                     = 'MIT License',
    description                 = 'A Python Library that UNOFFICIALLY wraps the captcha solving service, captcharip.',
    keywords      = 'captcha.rip',
    url           = 'https://discord.gg/capthas',
    author        = 'sillyrayman',
    author_email  = 'fanboys@fbi.ac',
    classifiers   = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)

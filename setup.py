# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


install_requires = [
    'requests',
]

extra_require = {
}


def set_entry_points():
    r = {}
    r['console_scripts'] = [
        'pyarchappl-get=archappl.scripts.get:main',
    ]
    return r


setup(
    name='phantasyRestClient',
    version='0.1',
    description='Python interface to PHANTASY-REST',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/phantasy-project/phantasy-rest-client",
    author='Tong Zhang',
    author_email='zhangt@frib.msu.edu',
    packages=find_packages(),
    include_package_data=True,
    # entry_points=set_entry_points(),
    install_requires=install_requires,
    extra_require=extra_require,
    license='GPL3+',
    keywords="PHANTASY",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

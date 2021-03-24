from setuptools import find_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='django-getpaid',
    description='Multi-broker payment processor for django',
    long_description=long_description,
    version='2.2.2-dev1',
    packages=find_packages(),
    url='https://github.com/cypreess/django-getpaid',
    license='MIT',
    author='Krzysztof Dorosz',
    author_email='cypreess@gmail.com',
    include_package_data=True,
    install_requires=[
        'typing_extensions>=3.7.0,<4.0',
    ],
    extras_require={
        'payu': [
            'django-celery>=3.0.11',
        ],
        'przelewy24': [
            'django-celery>=3.0.11',
            'pytz',
        ],
        'moip': [
            'requests',
            'lxml'
        ],
        'paymill': [
            'pymill',
        ]
    },

)

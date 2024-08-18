from setuptools import setup, find_packages

setup(
    name='MockOrderDataGenerator',
    version='1.1.0',
    description='A package for generating and processing test data with geographical and route calculations.',
    author='eventually',
    author_email='ferry792351742@gmail.com',
     url='https://github.com/eventually11/MockOrderDataGenerator',
    packages=find_packages(where="src"),
    package_dir={"": "src"},  
    install_requires=[
        'requests',
        'pandas',
        'Faker',
        'hypothesis'
    ],
    entry_points={
        'console_scripts': [
            'run_script=scripts.run_script:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
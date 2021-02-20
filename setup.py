from setuptools import setup

requirements = []


setup(
    name='Kadal',
    author='SynderBlack',
    version="0.2.6",
    packages=['kadal'],
    license='MIT',
    description='Async wrapper for the Anilist API',
    url='https://github.com/SynderBlack/Kadal',
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'multio': [
            'multio',
            'asks'
        ],
        'asyncio': [
            'aiohttp'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only"
    ]
)

from setuptools import setup, find_packages


setup(
    name='fingerprints',
    version='0.5.1',
    description="A library to generate entity fingerprints.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='names people companies normalisation',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/pudo/fingerprints',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={
        '': ['fingerprints/data/types.yml']
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'normality>=0.4.0',
        'unidecode',
        'pyyaml',
        'six'
    ],
    tests_require=[
        'nose',
        'coverage',
        'wheel'
    ],
    entry_points={
    }
)

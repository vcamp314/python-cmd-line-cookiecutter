import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{cookiecutter.pkg_name}}",
    version="0.0.1",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    description="template for future packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['{{cookiecutter.pkg_name}} = {{cookiecutter.file_name}}.__main__:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)

{{cookiecutter.pkg_name}} Package
=================================
This is a template package structure for future packages.
Replace this text with your project's description.

Note: All  below commands should be executed from root (directory of this readme)

Production Use
---------------
+++++++++++++
Installation
+++++++++++++
Installing package with dependencies (update accordingly for actual github link/PyPI)::

    $ python3 -m pip install git+https://github.com/user/{{cookiecutter.pkg_name}}

++++++
Usage
++++++
How to run (template example, to be replaced with actual project's example)

Default run example::

    $ {{cookiecutter.pkg_name}}

Positional argument example::

    $ {{cookiecutter.pkg_name}} pos

Positional and optional argument example::

    $ {{cookiecutter.pkg_name}} opt-pos -t "example optional text"


Development
---------------
++++++
Setup
++++++
Installing package with dependencies::

    $ python3 -m pip install -r requirements.txt

+++++++
Running
+++++++
How to run (template example, to be replaced with actual project's example)

Default run example::

    $ python3 -m {{cookiecutter.pkg_name}}

Positional argument example::

    $ python3 -m {{cookiecutter.pkg_name}} pos

Positional and optional argument example::

    $ python3 -m {{cookiecutter.pkg_name}} opt-pos -t "example optional text"

++++++++
Testing
++++++++
how to run unit tests including doctests::

    $ py.test



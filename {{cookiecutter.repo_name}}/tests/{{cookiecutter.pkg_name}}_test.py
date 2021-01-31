import os
import pytest
from .context import {{cookiecutter.pkg_name}}

# the below two lines are for pip installing with test option and the tests will open files:
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(CURRENT_DIR)


def test_{{cookiecutter.pkg_name}}():
    assert 1 == 1

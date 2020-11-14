"""
The test script for class StandardForm
"""


from src.StandardForm import StandardForm
from numpy import *

A = array([
    [0.0, 1.0],
    [1.0, 1.0],
    [1.0, 0.0],
    [1.0, -1.0]
])
b = array([[6.0], [8.0], [4.0], [2.0]])
c = array([4, 1])

standard_form = StandardForm(A, b, c)


def test_instantiate():
    assert isinstance(standard_form, StandardForm)


def test_getA():
    assert standard_form.get_A()[0, 0] == 0
    assert standard_form.get_A()[0, 1] == 1
    assert standard_form.get_A()[1, 0] == 1
    assert standard_form.get_A()[1, 1] == 1
    assert standard_form.get_A()[2, 0] == 1
    assert standard_form.get_A()[2, 1] == 0
    assert standard_form.get_A()[3, 0] == 1
    assert standard_form.get_A()[3, 1] == -1


def test_get_c():
    assert standard_form.get_c()[0] == 4
    assert standard_form.get_c()[1] == 1


def test_get_b():
    assert standard_form.get_b()[0] == 6
    assert standard_form.get_b()[1] == 8
    assert standard_form.get_b()[2] == 4
    assert standard_form.get_b()[3] == 2

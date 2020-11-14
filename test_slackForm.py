"""
The test script for class SlackForm
"""


from src.SlackForm import SlackForm
from numpy import *

N = {1, 2}
B = {3, 4}
A = array([[1, -1], [2, 1]])
b = array([[1], [2]])
c = array([5, -3])
v = 0

slack_form = SlackForm(N, B, A, b, c, v)


def test_instantiate():
    assert isinstance(slack_form, SlackForm)


def test_getA():
    assert slack_form.get_A()[0, 0] == 1
    assert slack_form.get_A()[0, 1] == -1
    assert slack_form.get_A()[1, 0] == 2
    assert slack_form.get_A()[1, 1] == 1


def test_getN():
    assert slack_form.get_N() == {1, 2}


def test_getB():
    assert slack_form.get_B() == {3, 4}


def test_get_c():
    assert slack_form.get_c()[0] == 5
    assert slack_form.get_c()[1] == -3


def test_get_b():
    assert slack_form.get_b()[0] == 1
    assert slack_form.get_b()[1] == 2


def test_get_v():
    assert slack_form.get_v() == 0

"""
The test script for class Simplex
"""


from src.Simplex import Simplex


sim = Simplex()


def test_instantiate():
    assert isinstance(sim, Simplex)

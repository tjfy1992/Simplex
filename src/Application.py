"""
The class of example inputs. Uncomment each input to use it as input.
Run this file to get the results.
"""


from numpy import *
from src.Simplex import Simplex
from src.StandardForm import StandardForm

simplex = Simplex()

"""
Sample input 1
maximize: z = 4x1 + x2
subject to:
    x2 <= 6
    x1 + x2 <= 8
    x1 <= 4
    x1 - x2 <= 2
    x1, x2, x3, x4 >= 0
"""
A = array([
    [0.0, 1.0],
    [1.0, 1.0],
    [1.0, 0.0],
    [1.0, -1.0]
])
b = array([[6.0], [8.0], [4.0], [2.0]])
c = array([4, 1])
standard_form = StandardForm(A, b, c)
simplex.simplex(standard_form)


"""
Sample input 2
maximize x1 + 2x2
subject to:
    -x1 + x2 <= 3
    x1 + 3x2 <= 13
    x1 - x2 <= 1
    x1, x2 >= 0
"""
# A = array([
#     [-1.0, 1.0],
#     [1.0, 3.0],
#     [1.0, -1.0]
# ])
# b = array([[3.0], [13.0], [1.0]])
# c = array([1, 2])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 3
maximize: 5x1 + 4x2 + 3x3
subject to:
    2x1 + 3x2 + x3 <= 5
    4x1 + x2 + 2x3 <= 11
    3x1 + 4x2 + 2x3 <= 8
"""
# A = array([
#     [2.0, 3.0, 1.0],
#     [4.0, 1.0, 2.0],
#     [3.0, 4.0, 2.0]
# ])
# b = array([[5.0], [11.0], [8.0]])
# c = array([5, 4, 3])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 4
maximize: 5x1 - 3x2
subject to:
    x1 - x2 <= 1
    2x1 + x2 <= 2
    x1, x2 >= 0
"""
# A = array([
#     [1.0, -1.0],
#     [2.0, 1.0]
# ])
# b = array([[1.0], [2.0]])
# c = array([5, -3])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 5
An example that requires auxiliary LP
maximize: 2x1 - x2
subject to:
    2x1 - x2 <= 2
    x1 - 5x2 <= -4
    x1, x2 >= 0
"""
# A = array([
#     [2.0, -1.0],
#     [1.0, -5.0],
# ])
# b = array([[2.0], [-4.0]])
# c = array([2, -1])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 6
Another example which requires auxiliary LP
maximize: 2x1 - 3x2
subject to:
    2x1 - x2 <= 2
    x1 - 5x2 <= -4
    x1, x2 >= 0
"""
# A = array([
#     [2.0, -1.0],
#     [1.0, -5.0],
# ])
# b = array([[2.0], [-4.0]])
# c = array([2, -3])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)

"""
Sample input 7
maximize: 10000*y1 + 30000*y2
subject to:
    2*y1 + 20*y2 <= 1
    7.5*y1 + 5*y2 <= 1
    3* y1 + 10 * y2 <= 1
    y1, y2 >= 0
"""
# A = array([
#     [2.0, 20.0],
#     [7.5, 5.0],
#     [3.0, 10.0]
# ])
# b = array([[1.0], [1.0], [1.0]])
# c = array([10000, 30000])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 8
maximize: 2x1 + 4x2 + 6x3 + 2x4
subject to:
    x1 - x2 + 2x3 + x4 <= 1
    -2x1 + x2 + x4 <= 2
    x1 + x2 + x3 + x4 <= 1
    x1, x2, x3, x4 >= 0
"""
# A = array([
#     [1.0, -1.0, 2.0, 1.0],
#     [-2.0, 1.0, 0.0, 1.0],
#     [1.0, 1.0, 1.0, 1.0]
# ])
# b = array([[1.0], [2.0], [1.0]])
# c = array([2, 4, 6, 2])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 9
An example in which all variables in b are negative
maximize: 2x1 - 3x2
subject to:
    2x1 - x2 <= -2
    x1 - 5x2 <= -4
    x1, x2 >= 0
"""
# A = array([
#     [2.0, -1.0],
#     [1.0, -5.0],
# ])
# b = array([[-2.0], [-4.0]])
# c = array([2, -3])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)


"""
Sample input 10
Maximize: x1 + x7 + x10
    Subject to:
        x1 <= 10
        x2 <= 9
        x3 <= 10
        x4 <= 4
        x5 <= 15
        x6 <= 15
        x7 <= 5
        x8 <= 8
        x9 <= 10
        x10 <= 15
        x11 <= 4
        x12 <= 6
        x13 <= 15
        x14 <= 10
        x15 <= 16
        -x1 + x2 + x4 + x5 <= 0
        x1 - x2 – x4 – x5 <= 0
        -x2 + x3 + x6 <= 0
        x2 – x3 – x6 <= 0
        -x4 - x7 + x8 + x11 - x12 <= 0
        x4 + x7 - x8 - x11 + x12 <= 0
        -x5 - x6 - x8 + x9 + x13 <= 0
        x5 + x6 + x8 – x9 – x13 <= 0
        -x10 - x11 + x15 <= 0
        x10 + x11 – x15 <= 0
        x12 - x13 + x14 - x15 <= 0
        -x12 + x13 – x14 + x15 <= 0
        X1, x2, …, x15 >= 0
"""
# A = array([
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [-1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 1, -1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 1, -1, 0, 0, -1, 1, 0, 0, 0],
#     [0, 0, 0, 0, -1, -1, 0, -1, 1, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, -1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, -1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 1]
# ])
#
# b = array([[10.0],
#            [9.0],
#            [10.0],
#            [4.0],
#            [15.0],
#            [15.0],
#            [5.0],
#            [8.0],
#            [10.0],
#            [15.0],
#            [4.0],
#            [6.0],
#            [15.0],
#            [10.0],
#            [16.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0],
#            [0.0]
# ])
# c = array([1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0])
# standard_form = StandardForm(A, b, c)
# simplex.simplex(standard_form)

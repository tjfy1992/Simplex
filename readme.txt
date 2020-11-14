src/SlackForm.py: The class of slack form
src/StandardForm.py: The class of standard form
src/Simplex.py: The class which implements Simplex Algorithm.
test_simplex.py: Test script for class Simplex
test_slackForm.py: Test script for class SlackForm
test_standardForm.py: Test script for class StandardForm.

To run the pytest, in the console, input "pytest -v". The test scripts are files starting with "test_".

To run a sample input, simply uncomment the corresponding code block. To make the output easy to read, running multiple sample
inputs is not recommended. Right-click on Application.py, and click "Run Application", the result will be shown in the terminal.

An example input is as following:
For the following LP in standard form:
maximize: z = 4x1 + x2
subject to:
    x2 <= 6
    x1 + x2 <= 8
    x1 <= 4
    x1 - x2 <= 2
    x1, x2, x3, x4 >= 0
/------------------------example input-------------------------/
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
/------------------------example input-------------------------/
Please make sure the input is in correct format of a standard form, otherwise the program will report an exception.
The output of the above example is as following:
/------------------------example output-------------------------/
basic solution:
[ 4.000000  4.000000  2.000000  0.000000  0.000000  2.000000]
final slack form:
A:  [[ 1.000000 -1.000000]
 [ 1.000000 -0.000000]
 [-1.000000  1.000000]
 [-2.000000  1.000000]]
b:  [ 2.000000  4.000000  4.000000  2.000000]
c:  [-3.000000 -1.000000]
N:  [5, 4]
B:  [3, 1, 2, 6]
v:  20.0
/------------------------example output-------------------------/
It first prints out the basic solution. For the above one, we can see the basic solution is
x1 = 4, x2 = 4, x3 = 2, x4 = 0, x5 = 0, x6 = 2
The indices of variables in basic solution are in increasing order. The simplex algorithm should only return only x1 and x2,
but to make it clear, I print all the variables out.
And then it prints out the final slack form. The v = 20 is the maximized objective value.
Please notice that the indices in B and N may not be in an order. For the above one, the slack form is:
maximize: z = -3 * x5 - x4
subject to:
    x3 = 2 - x5 + x4
    x1 = 4 - x5
    x2 = 4 + x5 - x4
    x6 = 2 + 2*x5 - x4
    x1, x2, x3, x4, x5, x6 >= 0
The values in the output will have 6 digits after the dot, if it is a float variable. Since N and B stores the index of variables,
the values within them are stored as integers.
There maybe a variable which is -0.000000. It can be regarded as 0.000000.

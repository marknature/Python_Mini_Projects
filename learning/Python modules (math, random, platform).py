# The function returns an alphabetically sorted list
# dir(module)
import math
for name in dir(math):
  print(name, end="∖t")

dir(math)

# returns True
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

'''
sinh(x) → the hyperbolic sine;
cosh(x) → the hyperbolic cosine;
tanh(x) → the hyperbolic tangent;
asinh(x) → the hyperbolic arcsine;
acosh(x) → the hyperbolic arccosine;
atanh(x) → the hyperbolic arctangent;
pi → a constant with a value that is an approximation of π;
radians(x) → a function that converts x from degrees to radians;
degrees(x) → acting in the other direction (from radians to degrees);
e → a constant with a value that is an approximation of Euler's number (e);
exp(x) → finding the value of ex;
log(x) → the natural logarithm of x;
log(x, b) → the logarithm of x to base b;
log10(x) → the decimal logarithm of x (more precise than log(x, 10));
log2(x) → the binary logarithm of x (more precise than log(x, 2));
pow(x, y) → finding the value of xy (mind the domains);
ceil(x) → the ceiling of x (the smallest integer greater than or equal to x);
floor(x) → the floor of x (the largest integer less than or equal to x);
trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor);
factorial(x) → returns x! (x has to be an integral and not a negative);
hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise).
'''

from math import e, exp, log
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


# The random function
# roduces a float number x coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0).
from random import random
for i in range(5):
    print(random())


# The seed function
# The seed() function is able to directly set the generator's seed.
''' We'll show you two of its variants:
seed() - sets the seed with the current time;
seed(int_value) - sets the seed with the integer value int_value. '''

from random import random, seed
seed(0)
for i in range(5):
    print(random())

# The randrange and randint functions
''' If you want integer random values, one of the following functions would fit better:
- randrange(end)
- randrange(beg, end)
- randrange(beg, end, step)
- randint(left, right)
The first three invocations will generate an integer taken (pseudorandomly) from the range (respectively):
- range(end)
- range(beg, end)
- range(beg, end, step)
Note the implicit right-sided exclusion!
The last function is an equivalent of randrange(left, right+1) - it generates the integer value i, which falls in the range [left, right] (no exclusion on the right side).
'''
from random import randrange, randint
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

for i in range(10):
    print(randint(1, 10), end=',')

# The choice and sample functions
# choice(sequence)
# sample(sequence, elements_to_choose)
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

# The platform function
# platform(aliased = False, terse = False)
from platform import platform 
print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine
print(machine())

# The processor function
from platform import processor
print(processor())

# The system function
from platform import system
print(system())

# The version function
from platform import version
print(version())

# The python_implementation and the python_version_tuple functions
from platform import python_implementation, python_version_tuple
print(python_implementation())
for atr in python_version_tuple():
    print(atr)

'''
1. A function named dir() can show you a list of the entities contained inside an imported module. For example:
import os
dir(os)
prints out the list of all the os module's facilities you can use in your code.
2. The math module couples more than 50 symbols (functions and constants) that perform mathematical operations (like sine(), pow(), factorial()) or providing important values (like π and the Euler symbol e).
3. The random module groups more than 60 entities designed to help you use pseudo-random numbers. Don't forget the prefix "random", as there is no such thing as a real random number when it comes to generating them using the computer's algorithms.
4. The platform module contains about 70 functions which let you dive into the underlaying layers of the OS and hardware. Using them allows you to get to know more about the environment in which your code is executed.
5. Python Module Index https://docs.python.org/3/py-modindex.html is a community-driven directory of modules available in the Python universe. If you want to find a module fitting your needs, start your search there.
'''

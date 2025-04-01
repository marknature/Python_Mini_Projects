# How do you divide a piece of software into separate but cooperating parts? This is the question. Modules are the answer.

# Importing a module
import math, sys #import more than one module by listing the modules after the import keyword

# A namespace is a space (understood in a non-physical context) in which some names exist and the names don't conflict with each other (i.e., there are not two different objects of the same name).
# Namespace
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# In the second method, the import's syntax precisely points out which module's entity (or entities) are acceptable in the code:
from math import pi

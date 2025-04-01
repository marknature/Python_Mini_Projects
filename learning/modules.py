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
print(math.e)

from math import sin, pi
print(sin(pi/2))
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))

'''
In the third method, the import's syntax is a more aggressive form of the previously presented one:
from module import *
As you can see, the name of an entity (or the list of entities' names) is replaced with a single asterisk (*).
Such an instruction imports all entities from the indicated module.
'''

import module as alias
# If you use the import module variant and you don't like a particular module's name (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) you can give it any name you like - this is called aliasing.

'''
Aliasing
If you need to change the word math, you can introduce your own name, just like in the example:
import math as m
print(m.sin(m.pi/2))
Note: after successful execution of an aliased import, the original module name becomes inaccessible and must not be used.
In turn, when you use the from module import name variant and you need to change the entity's name, you make an alias for the entity. This will cause the name to be replaced by the alias you choose.
This is how it can be done:
from module import name as alias
As previously, the original (unaliased) name becomes inaccessible.
The phrase name as alias can be repeated - use commas to separate the multiplied phrases, like this:
from module import n as a, m as b, o as c
The example may look a bit weird, but it works:
from math import pi as PI, sin as sine
print(sine(PI/2))
Now you're familiar with the basics of using modules. Let us show you some modules and some of their useful entities.
'''

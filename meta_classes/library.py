"""
How to be sure, that user that will use this class will implement necessary methods
e.g. bar
There are 3 answers to this
1. build_class - not used much, but good to know it's there
2. meta_classes
3. using __init_subclass__ method - the best way
"""


# 1.
"""
class Base:
    def foo(self):
        return self.bar()

old_bc = __build_class__


def my_bc(fun, name, base=None, **kw):
    if base is Base:
        print('check if bar method defined!')
    if base is not None:
        return old_bc(fun, name, base, **kw)
    return old_bc(fun, name, **kw)

import builtins
builtins.__build_class__ = my_bc
"""

# 2.


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError("User class missing bar method")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()


# 3.

class Base:
    def foo(self):
        return self.bar()

    def __init_subclass__(cls, **kwargs):
        print('init subclass... check if bar defined')
        return super().__init_subclass__(cls, **kwargs)

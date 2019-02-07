from library import Base

"""
To be sure that foo method from the Base class is not deleted. Check before runtime.
"""

assert hasattr(Base, 'foo'), "you broke it!"

class ExtendBase(Base):
    def poop(self):
        return self.foo()

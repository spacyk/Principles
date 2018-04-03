from library import Base

assert hasattr(Base, 'foo'), "you broke it!"

class ExtendBase(Base):
    def poop(self):
        return self.foo()

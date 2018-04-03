class Polynomial():
    def __init__(self, *args, **kwargs):
        self.coeffs = args

    def __repr__(self):
        return f'Polynomial({self.coeffs})'




class AbstractClass(object):
    """
    This stupid example shows how you can instantiate object,
    and return different value, in this case you need to call __init__ method manualy,
    because init is called only when the instance object is returned from __new__ method.
    """
    def __new__(cls, a, b):
        instance = super(AbstractClass, cls).__new__(cls)
        instance.__init__(a, b)
        return 3

    def __init__(self, a, b):
        print "Initializing Instance", a, b



def main():
    a = Polynomial(2,3,4)
    print(a)


    b = AbstractClass(2, 3)

if __name__=="__main__":
    main()


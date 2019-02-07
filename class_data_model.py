class Polynomial():
    """
    Data model methods defines some behavior you want to implement for the class instance
    https://docs.python.org/3/reference/datamodel.html
    There is always top level function or top level syntax -> corresponding __
    Data model is a way to implement protocols
    """
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f'Polynomial(*{self.coeffs})'

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)




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
        print("Initializing Instance", a, b)



def main():
    a = Polynomial(2,3,4)
    b = Polynomial(2,3,4)
    print(a + b)


    #b = AbstractClass(2, 3)

if __name__=="__main__":
    main()


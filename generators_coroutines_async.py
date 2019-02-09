from time import sleep

"""
Generators
You don't need to define class with __iter__ and __next__ methods to have generator.
You just need to yield values as in compute function.
"""


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration
        sleep(.5)
        return rv


def compute():
    for i in range(10):
        sleep(.5)
        yield i


def test_generators():
    for val in Compute():
        print(val)

    for val in compute():
        print(val)


""""""

# Example of basic async understanding
async def coro():
    await other_coro()
    sync()

def sync():
    """
    Await other_coro() is one the most reasons why people create new async version of libraries, also reason for Quart
    as Flask was not able
    :return:
    """
    other_coro()  # Creates coroutine, but doesn't run it
    await other_coro() # Syntax error




"""
Coroutines explained a bit
Type of the function will be still generator object, but this also waits for input through send
corou is ran by __next__() and it will 
when yielding values you just use next, when wating for values, you use send
Generators give execution to the next code, doesn't wait for this
When closed it generates GeneratorExit exception
"""
# Python3 program for demonstrating
# coroutine execution

def print_name(prefix):
    def print_name(prefix):
        print("Searching prefix:{}".format(prefix))
        try:
            while True:
                name = (yield)
                if prefix in name:
                    print(name)
        except GeneratorExit:
            print("Closing coroutine!!")


if __name__ == "__main__"""
    # calling coroutine, nothing will happen
    corou = print_name("Dear")

    # This will start execution of coroutine and
    # Prints first line "Searchig prefix..."
    # and advance execution to the first yield expression
    corou.__next__()

    # sending inputs
    corou.send("Atul")
    corou.send("Dear Atul")
    corou.close()


"""
Example with chaining, code from:
https://www.geeksforgeeks.org/coroutine-in-python/
"""
# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and
    feed it to pattern_filter coroutine
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    '''
    Act as a sink, simply print the
    received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
pf.close()
pt.close()


"""
Yield and yield from
"""
def iterable1():
    yield 1
    yield 2

def iterable2():
    yield from iterable1()
    yield 3

assert list(iterable2) == [1, 2, 3]

"""
From what I see now asyncio just adds interface to easily work with coroutines
You can await another coroutine function without all the manual things written in up examples
"""
"""
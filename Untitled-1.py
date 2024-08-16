def add(x, y):
    return x + y 
def test_add():
    results = add(1, 2)
    assert results == 3


def subtract(x, y):
    return x - y
def test_subtract():
    results = subtract(10, 7)
    assert results == 3

def multiply(x, y):
    return x * y
def test_multiply():
    results = multiply(2, 3)
    assert results == 6

def divide(x, y):
    return x / y
def test_divide():
    results = divide(6, 2)
    assert results == 3
def test_divide_by_zero():
    results = divide(99, 0)
    assert type(results) == str    

def square(x):
    return x ** 2
def test_square():
    results = square(3)
    assert results == 9

def power(x, y):
        return x ** y    
def test_power():
    results = power(3, 2)
    assert results == 9

    results = power(3, 3)
    assert results == 27

def sqrt(x):
    return
def test_sqrt():
    results = sqrt(9)
    assert results == 3
    results = sqrt(16)
    assert results == 4

    


    
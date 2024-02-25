'''My Calculator Test'''
# import sys
# sys.path.append('/Users/francycamacho/Desktop/is601/projectSetup2')


from calculator import add, subtract, multiply
#import calculator as calc

def test_addition():
    '''Test that addition function works '''
    assert add(2,2) == 4
    print("works ")

def test_subtraction():
    '''Test that subtraction function works '''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,2) == 4

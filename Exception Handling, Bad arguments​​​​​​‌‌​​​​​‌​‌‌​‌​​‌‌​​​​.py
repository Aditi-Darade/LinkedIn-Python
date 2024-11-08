# Python code​​​​​​‌‌​​​​​‌​‌‌​‌​​‌‌​​​​‌​‌‌ below
class NonIntArgumnetException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if item is not int:
                raise NonIntArgumnetException()
        return func(*args)
    return wrapper


# This is how your code will be called.
# Your answer should be the largest value in the numbers list.
# You can edit this code to try different testing cases.

@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumnetException as e:
    print('Hooray!')
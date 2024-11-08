# Factorial 222222222222222222222222222222222222222222222222
def factorial(num):
    # Your code goes here.
    if type(num) != int:
        return None
    if(num<0):
        return None
    else:
        sum = 1
        while num != 0:
            sum = sum * num;
            num = num - 1;    
        return sum

number = 5
result = factorial(number)
print(result)

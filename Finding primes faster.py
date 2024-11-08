def allPrimesUpTo(num):
    # Your code goes here.
    list = [2]
    for numb in range(3,num):
        notPrime = False   
        for val in list :
            if (numb % val == 0):
                notPrime = True
                break
        if (notPrime == False):
            list.append(numb)                     
    return list

num = 100
print(allPrimesUpTo(num))
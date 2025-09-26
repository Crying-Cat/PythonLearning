def factorial(val):
    if(val<=1):
        return 1
    return val*factorial(val-1)

print(factorial(5))

def fibonnaci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonnaci(n-2)+fibonnaci(n-1)
for i in range(10):
    print(fibonnaci(i))
print(fibonnaci(20))
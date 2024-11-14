def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f    
x=int(input("enter the value: "))
answer=factorial(x)
print(answer)
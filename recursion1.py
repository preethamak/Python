
def factorial(x):
    if x==0:
        return 1
    return x*factorial(x-1)
x=int(input("enter the element: "))
answer=factorial(x)
print(answer)
lst=[1,2,3,4,5,6,7,8,9]
even= list(filter(lambda n: n%2==0, lst))
print(even)
double=list(map(lambda n: n+2, even))
print(double)
from functools import reduce
count = reduce(lambda x,y:x/y, even)
print(int(count))
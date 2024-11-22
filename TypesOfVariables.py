class smith:
    average= 67                     #class variables(fixed)
    def __init__(self):
        self.runs=9880             #instance variables(not fixed)
        self.centuries=32

s1=smith()
s2=smith()
smith.average=70

print(s1.average, s1.runs, s1.centuries)
print(s2.average, s2.runs, s2.centuries)


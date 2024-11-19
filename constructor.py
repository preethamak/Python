class define:
    def __init__(self):
        self.name='preetham'
        self.age='17'

    def update(self):
     self.age=30
    
    def compare(self,c2):
        if self.age == self.age:
            return True
        else:
             return False
c1=define()
c1.age=25
c2=define()
c2.name='preetham ak'    

if c1.compare(c2):
    print("they are same ")
else:
    print("they are not same ")

print(c1.name)        
print(c2.name)    
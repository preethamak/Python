class student:
    school='ak'
    def __init__(self,m1,m2,m3):            #instance function(a normal function)
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3    
    
    @classmethod              #class function(should pass arguments while calling)
    def info(cls):
       cls.school
    print(school)

    @staticmethod
    def give():                                     #static function(not changeable)
        print("hlo")    
    
s1 = student(50,100,70)    
s2 = student(99, 98, 98) 

print("avg of s1 is: ", s1.avg())
print()
print("avg of s2 is: ",s2.avg())
print()
student.info()

student.give()
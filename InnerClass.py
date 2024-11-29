class student():
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno

    class laptop:
        def __init__(self):
            self.laptop = 'hp'
            self.ram= 8
            print(self.laptop)


s1=student('preetham', 2)
s2=student('prajwal', 3)

print(s1)
print(s2)

student.laptop()
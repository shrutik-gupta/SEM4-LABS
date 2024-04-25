class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    
    def average(self):
        sum=0
        for element in self.marks:
            sum+=element
        average_marks= sum/3
        return average_marks

s1 = Student("Shrutik",[55,56,57])
print(s1.average())
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
    # def __str__(self):
    #     return f"Student {self.name}, has these grades: {self.grades}"

    def __repr__(self):
        return f"<Person('{self.name}',{self.grades})>"


student = Student("Rolf", (90, 90, 80, 70, 50))
print(student.average())
print(student)

class Student:
    def __init__ (self, name, points=0):
        self.name = name
        self.points = points
    
    def add_points(self, add_point):
        self.points += add_point
        return add_point

    def has_passed(self):
        if self.points >= 50:
            return True
        else:
            return False

student1 = Student("Alexander", 99)
student2 = Student("Vincent", 60)
student3 = Student("Anton", 78)
student4 = Student("kalle", 22)
student5 = Student("Carl-Johan", 2)
student6 = Student("Chrille", 0)
student_list = [student1, student2, student3, student4, student5, student6]

for student in student_list:
    #print(f"{student.name}: {student.points} points")
    if student.has_passed() == True:
        print(f"{student.name} has {student.points}| Passed!")
    else:
        print(f"{student.name} has {student.points}| Failed!")

          
'''
add_points = int(input("Lägg in hur mycket poäng studenten ska få: "))
student1.add_points(add_points)
student1.has_passed()
has_passed = student1.has_passed()

if has_passed == True:
    print("Studenten är godkänd!")
else:
    print("Studenten är underkänd")
    '''

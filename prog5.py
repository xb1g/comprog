class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def getID(self):
        return self.student_id

    def setID(self, student_id):
        self.student_id = student_id

    def getName(self):
        return self.name

    def setFavoriteCourse(self, course):
        self.favorite_course = course

    def getFavoriteCourse(self):
        return self.favorite_course

# Q3: Course Class
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

# Q1
print("\nQ1 Create student object")
big = Student('Bunyasit', "6658049556")
print(big.name)
print(big.student_id)

# Q2
print("\nQ2: getName() method")
print(big.getName())

# Q3
print("\nQ3: Create course object")
prog = Course('Introduction to Computer Programming', "5602102")
print(prog.course_name)
print(prog.course_id)

# Q4

big.setFavoriteCourse(prog)

print("\nQ4: Favorite course")
print(big.getFavoriteCourse().course_name)


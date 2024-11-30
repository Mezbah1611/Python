class Department:
    Name = " "
    def display_name(self):
        print("HI! Mezbah")

class Teacher(Department):
    def Schedule_class(self):
        print("Schedule Class Strat")
    def grade_Student(self):
        print("Your Grade is low")
    def display_name(self):
        super().display_name()

class Author:
    def write_Article(self):
        print("Write an Article")
    def publish_Blog(self):
        print("Please publish a blog")
class TeacherAuthor(Teacher,Author):
    pass

t = TeacherAuthor()
t.display_name()
t.Schedule_class()
t.grade_Student()
t.write_Article()
t.publish_Blog()
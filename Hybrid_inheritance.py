class School:

    def func1(self):
        print("This function is in School")

class Student1(School):

    def func2(self):
        print("This function is in Student 1.")

class Student2(School):

    def func3(self):
        print("This function is in Student 2.")

class Student3(Student1, School):
    
    def func4(self):
        print("This function is in Student 3.")
         

object = Student3()
object.func1()
object.func2()

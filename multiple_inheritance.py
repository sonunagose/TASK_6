class Mother:
    MotherName = " "

    def Mother(self):
        print(self.MotherName)

class Father:
    FatherName = " "

    def Father(self):
        print(self.FatherName) 

class Son(Mother, Father):

    def parent(self):
        print("Father : " , self.FatherName)
        print("Mother : ", self. MotherName)

s1 = Son()
s1.FatherName = "RAM"
s1.MotherName = "SITA"
s1.parent()
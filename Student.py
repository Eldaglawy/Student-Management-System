class Student (object):
    def __init__(self, name= "Mohamed" ,ID= 320210100, dbirth = "15-4-2000", nat= "Egyptian", gender= "Male", GPA= 3.7):
        self.name = name
        self.ID = ID
        self.dbirth = dbirth
        self.nat = nat
        self.gender = gender
        self.GPA = GPA
        
        
    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getDbirth(self):
        return self.dbirth

    def getNat(self):
        return self.nat

    def getGender(self):
        return self.gender

    def getGPA(self):
        return self.GPA
    
    
    def setName(self, name):
        self.name=name

    def setID(self, ID):
        self.ID= ID

    def setDbirth(self, dbirth):
        self.dbirth = dbirth

    def setNat(self, nat):
        self.nat = nat

    def setGender(self, gender):
        self.gender = gender

    def setGPA(self, GPA):
        self.GPA = GPA
    
    def description (self):
        return f"Hello I'm a Student, my name is {self.name}, my ID is {self.ID}, my GPA is {self.GPA}, and I'm {self.nat}"



        
        
        
        
        
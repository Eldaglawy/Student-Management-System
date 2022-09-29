from Student import *

class Worker (Student):
    def __init__ (self, name= " Mohamed" ,ID= 320210100, dbirth = "19-5-2003", nat= "Egyptian", gender= "Male", salary= 100, working_hours =8, job_title= "Worker"):
        
        Student.__init__ (self, name= " Ali" ,ID= 320210100, dbirth = "15-4-2000", nat= "Egyptian", gender= "Male")
        self.salary=salary
        self.working_hours= working_hours
        self.job_title = job_title
     
    def setSalary(self, salary):
        self.salary = salary
    
    def setWorking_hours(self, working_hours):
        self.working_hours = working_hours
        
    def setJob_title(self, job_title):
        self.job_title = job_title
        
        
    def getSalary(self):
        return self.salary
    def getID(self):
        return self.ID
    def getWorking_hours(self):
        return self.working_hours
    def getJob_title(self):
        return self.job_title
    def description (self):
        return f"Hello I'm a Worker, my name is {self.name}, my ID is {self.ID}, my salary is {self.salary}, and my Job title is {self.job_title}"
my_worker= Worker()
print (my_worker.description())
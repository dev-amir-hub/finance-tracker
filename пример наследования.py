class Empoyee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary=salary
    def work(self):
        print(f'{self.name} is working')
class Developer(Empoyee):
        def __init__(self,name,salary,language):
            super().__init__(name,salary)
            self.language=language
        def code(self):
            print(f"{self.name} is coding in {self.language}")
class Manager(Empoyee):
        def __init__(self,name,salary,team_size):
            super().__init__(name,salary)
            self.team_size=team_size
        def manage(self):
            print(f'{self.name} is managung {self.team_size} people')
dev = Developer("Amir", 100000, "Python")
dev.work()
dev.code()

manager = Manager("John", 150000, 10)
manager.work()
manager.manage()
class Task:
    def __init__ (self,name,description,deadline,state):
        self.name=name
        self.description=description
        self.deadline=deadline
        self.state=state

class TaskManager(Task):
    def add(self):
        print("Task ADDED")

    def remove(self):
        print("Task REMOVED")

    def noted(self):
        print("Task NOTED")

task1=Task("METRIX","so cool",7,"funny")
taskmanager1=TaskManager("METRIX","so cool",7,"funny")
task1.name()
taskmanager1.add()

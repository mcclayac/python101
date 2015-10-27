#!/usr/bin/env python3
import abc

class User(object):

    name = ""


    def __init__(self, name):
        self.name = name




    def printName(self):
        print("Name  = " + self.name)

brian = User("brian")
brian.printName()




class Programmer(User):
    count = 0

    def __init__(self, name, years):
        super(Programmer, self).__init__(name)
        self.years = years

    def doPython(self):
        print("Programming Python", self.name, ' - ' , self.years)

    @classmethod
    def classMethod(cls):
        print(Programmer.count)

    @staticmethod
    def filerInt(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


brian = User("brian")
brian.printName()

diana = Programmer("Diana", 21)
diana.printName()
diana.doPython()



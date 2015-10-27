#!/usr/bin/env python3




class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()

#redcar.__updateSoftware()  not accesible from object.

class Car2(object):

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

redcar = Car2()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private

redcar.setMaxSpeed(35)
redcar.drive()

# Type	Description
# public methods	accessible from anywhere
# private methods	accessible only in their own class. starts with two underscores
# public variables	accessible from anywhere
# private variables	 accesible only in their own class or by a method if defined. starts with two underscores





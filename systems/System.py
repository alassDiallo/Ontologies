from devices.Device import *

class System():
    def __init__(self,name):
        self.idSys = name
        self.devices=set()

#This methods allows to add a new devices in na system
    def addDevice(self,d:Device):
       self.devices.add(d.id)


    def __str__(self):
      return f"{self.idSys}"
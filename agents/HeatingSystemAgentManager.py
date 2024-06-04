from agents.MyAgent import MyAgent
from devices.Device import Device
from systems.System import System
#from environment import Environment
class HeatingSystemAgentManager(MyAgent):
    def __init__(self,id,env,mangedSysteme:System=None,location=""):
        super().__init__(id,env,managedSystem=mangedSysteme,location=location)
        self.preferenceTemperature = 20
        self.state = True
    
    def automaticRegulation(self,device:Device):
        if self.env.temperatureGlobalMinim  <= device.temp <= self.env.temperatureGlobalMax:
            if  device.temp > self.preferenceTemperature:
                print("temperature elevée")
                while device.temp > self.preferenceTemperature:
                    print(f"temperature recueillie = {device.temp} --- temperature normal = {self.preferenceTemperature}")
                    #self.decreasePreferedTemperature()
                    self.decreaseHeatingPower()
                    device.temp-=1
                    print(device.temp)
            elif device.temp < self.preferenceTemperature:
                print("temperature basse")
                while device.temp < self.preferenceTemperature :
                    print(f"temperature recueillie = {device.temp} --- temperature normal = {self.preferenceTemperature}")
                #self.increasePreferedTemperature()
                    self.increaseHeatingPower()
                    device.temp+=1
                    print(device.temp)
        else:
            if device.temp < self.env.temperatureGlobalMinim:
                print("temperature trés basse")
                while device.temp < self.preferenceTemperature :
                    self.increaseHeatingPower()
                    device.temp+=1
                    print(device.temp)
            elif device.temp > self.env.temperatureGlobalMax:
                print("temperature trés élevée")
                while device.temp > self.preferenceTemperature :
                    self.decreaseHeatingPower()
                    device.temp-=1
                    print(device.temp)

    def increasePreferedTemperature(self):
        if self.preferenceTemperature < self.env.temperatureGlobalMax:
            self.preferenceTemperature = self.preferenceTemperature + 1

    def decreasePreferedTemperature(self):
        if self.preferenceTemperature > self.env.temperatureGlobalMinim:
            self.preferenceTemperature = self.preferenceTemperature - 1

    def increaseHeatingPower(self):
        print("I increase the heating power")

    def decreaseHeatingPower(self):
        print("I decrease the heating power")
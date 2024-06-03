from agents.MyAgent import MyAgent
from devices.Device import Device
from systems.System import System
#from environment import Environment
class HeatingSystemAgentManager(MyAgent):
    def __init__(self,id,mangedSysteme:System=None,location=""):
        super().__init__(id,managedSystem=mangedSysteme,location=location)
        self.preferenceTemperature = 19
    
    def automationRegulation(self,device:Device):
        if device.temp > self.preferenceTemperature and   (env.temperatureGlobalMinim  <= self.preferenceTemperature <= env.temperatureGlobalMax):
            print("temperature elevée")
            while device.temp > self.preferenceTemperature:
                print(f"temperature recueillie = {device.temp} --- temperature normal = {self.preferenceTemperature}")
                #self.decreasePreferedTemperature()
                device.temp-=1
                print(device.temp)
        else :
            print("temperature basse")
            while device.temp < self.preferenceTemperature:
                print(f"temperature recueillie = {device.temp} --- temperature normal = {self.preferenceTemperature}")
            #self.increasePreferedTemperature()
                device.temp+=1
                print(device.temp)


    def increasePreferedTemperature(self):
        self.preferenceTemperature = self.preferenceTemperature + 1

    def decreasePreferedTemperature(self):
        self.preferenceTemperature = self.preferenceTemperature - 1
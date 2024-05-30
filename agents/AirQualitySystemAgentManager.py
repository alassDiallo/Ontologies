from agents.MyAgent import MyAgent
from devices.Device import Device
from systems.System import System

class AirQualitySystemAgentManager(MyAgent):
    def __init__(self,id,mangedSysteme:System=None,location=""):
        super().__init__(id,managedSystem=mangedSysteme,location=location)

    def automationRegulation(self,device:Device):
        pass
       
from agents.MyAgent import MyAgent
from devices.Device import Device
from systems.System import System

class AirQualitySystemAgentManager(MyAgent):
    def __init__(self,id,env,mangedSysteme:System=None,location=""):
        super().__init__(id,env,managedSystem=mangedSysteme,location=location)

    def automaticRegulation(self,device:Device):
        pass
       
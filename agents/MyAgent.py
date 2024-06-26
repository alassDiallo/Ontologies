from devices.Device import Device
from systems.System import System
from abc import abstractmethod

class MyAgent:
    def __init__(self,id,env,managedSystem:System=None,location=None):
        self.id=id
        self.managedSystem=managedSystem
        self.location=location
        self.mailBox = []
        self.env = env

    def sendMessage(self,idReceiver,textContent):
        pass

    def receiveMessage(self):
        pass

    def act(self):
        pass

    def __str__(self):
      return f"{self.id} manages {self.managedSystem}"
    
    @abstractmethod
    def automaticRegulation(self,device:Device):
        pass
    
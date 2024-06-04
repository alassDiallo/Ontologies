
from agents.MyAgent import MyAgent
from devices.Device import Device
from systems.System import System
class LightingSystemAgentManager(MyAgent):
    def __init__(self,id,env,managedSystem:System=None,location=""):
        super().__init__(id,env,managedSystem=managedSystem,location=location)
        self.state = False

    def automaticRegulation(self,device:Device):
        print("Lightining agent")

    def turnOnOf(self):
        self.state = not self.state
        if self.state:
            print("turn off")
        else:
            print("turn on")

from systems.System import System

class LightingSystem(System):
    def __init__(self,id):
        super().__init__(id)
        self.idSys = id
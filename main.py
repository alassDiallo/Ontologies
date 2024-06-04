

import time
from threading import Timer
from environment import Environment
from request import requestData

#this method initialise the environment from the data in the Ontology
def loadEnvironment():
    env = Environment()
    env.configEnv()
    print(env)
    return (env,env.setAgents)


def setInterval(agents,env):
    delay = 30
    
    print('I print in intervals!')
    requestData(agents,env)
    time.sleep(delay)
    
    setInterval(agents,env)

def main():
    delay = 10.0
    env,agents = loadEnvironment()
    devices = set()
    for a in agents:
        if agents[a].managedSystem is not None:
            devices.update(agents[a].managedSystem.devices)
    
    print(devices)
    """t = Timer(delay,requestData,args=(agents,))
    t.start()"""
    #setInterval(agents=agents)

    requestData(agents,env)


if __name__ == "__main__":
    main()
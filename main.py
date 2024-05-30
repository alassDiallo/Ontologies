

from environment import Environment
from request import requestData

#this method initialise the environment from the data in the Ontology
def loadEnvironment():
    env = Environment()
    env.configEnv()
    print(env)
    return (env,env.setAgents)



def main():
    env,agents = loadEnvironment()
    devices = set()
    for a in agents:
        if agents[a].managedSystem is not None:
            devices.update(agents[a].managedSystem.devices)
    
    print(devices)
    requestData(agents)


if __name__ == "__main__":
    main()
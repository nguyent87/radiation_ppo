import numpy as np
import gym

from gym_rad_search import gym_rad_search


class UniformSearchAgent(object):
    def __init__(self):
        pass

    def step(self):
        act = 0
        return act

agent = UniformSearchAgent() 
env_name = 'gym_rad_search:RadSearch-v0'
init_dims = {'bbox':[[0.0,0.0],[2700.0,0.0],[2700.0,2700.0],[0.0,2700.0]], #Dimensions of the search area
             'area_obs':[200.0,500.0], #Obstruction area, only relevant when obstructions are present
             'obstruct':0}

robust_seed = 321342 #Change to get new starting environment conditons
rng = np.random.default_rng(robust_seed)
init_dims['seed'] = rng

env = gym.make(env_name,**init_dims) #Create gym environment
o, _, _, _ = env.reset(), 0, 0, 0
N = 120 #maximum number of steps in the environment

for n in range(N):
    a = agent.step() #Agent takes an action
    o, _, d, _ = env.step(a) #Update the environment state relative to the agent action 
    o[1:3] = o[1:3] * init_dims['bbox'][2][0] #restore original detector coordinates in cm

    if d:
        print('Found the source!')
        break


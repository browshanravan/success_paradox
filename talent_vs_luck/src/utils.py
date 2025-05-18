import numpy as np


class UniformAgent:
    def __init__(self, low=0, high=1):
        self.low= low
        self.high= high
    
    def pull(self):
        return np.random.uniform(low= self.low, high= self.high)




class GaussianAgent:
    def __init__(self, loc=0.5, scale=0.1):
        self.loc= loc
        self.scale= scale
    
    def pull(self):
        return np.random.normal(loc=self.loc, scale=self.scale, size=500)
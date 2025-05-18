import numpy as np
import matplotlib.pyplot as plt


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
        return np.abs(np.random.normal(loc=self.loc, scale=self.scale))



class MonteCarlo:
    def __init__(self, agent_type, total_number_of_participants, required_number_of_participants):
        self.total_number_of_participants= total_number_of_participants
        self.required_number_of_participants= required_number_of_participants
        self.percentage_talent_contribution= np.linspace(start= 1, stop= 0.5, num= 10)
        if agent_type == "UniformAgent":
            self.agent= [UniformAgent() for _ in range(self.total_number_of_participants)]
        if agent_type == "GaussianAgent":
            self.agent= [GaussianAgent() for _ in range(self.total_number_of_participants)]
    

    def adjusted_talent_luck(self, percentage_talent, percentage_luck):
        talent= percentage_talent * np.array([i.pull() for i in self.agent])
        luck= percentage_luck * np.array([i.pull() for i in self.agent])
        return talent, luck
    

    def simulation(self):
        numbers_picked= []
        for percentage_talent in self.percentage_talent_contribution:
            talent, luck= self.adjusted_talent_luck(percentage_talent= percentage_talent, percentage_luck= 1-percentage_talent)
            total_percentage= talent + luck
            agent_total_score= dict(zip(range(self.total_number_of_participants), total_percentage))
            agent_talent_score= dict(zip(range(self.total_number_of_participants), talent))
            ranked_agent_total_score= dict(sorted(agent_total_score.items(), reverse=True, key= lambda x: x[1]))
            ranked_agent_talent_score= dict(sorted(agent_talent_score.items(), reverse=True, key= lambda x: x[1]))
            overlap= len(
                set(list(ranked_agent_total_score.keys())[:self.required_number_of_participants]).intersection(
                    list(ranked_agent_talent_score.keys())[:self.required_number_of_participants]
                    ))
            numbers_picked.append(overlap)
        
        return dict(zip(self.percentage_talent_contribution.tolist(), numbers_picked))



def plot_data(dataframe):

    plt.plot(dataframe)
    plt.gca().invert_xaxis()
    plt.xlabel("% Talent Contribution")
    plt.ylabel("# of Participants Selected")

    plt.tight_layout()
    plt.show()
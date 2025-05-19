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
        self.percentage_talent_contribution= np.linspace(start= 1, stop= 0.95, num= 10)
        if agent_type == "UniformAgent":
            self.talent= [UniformAgent() for _ in range(self.total_number_of_participants)]
            self.luck= [UniformAgent() for _ in range(self.total_number_of_participants)]
        if agent_type == "GaussianAgent":
            self.talent= [GaussianAgent() for _ in range(self.total_number_of_participants)]
            self.luck= [GaussianAgent() for _ in range(self.total_number_of_participants)]
    

    def adjusted_talent_luck(self, percentage_talent, percentage_luck):
        talent= percentage_talent * np.array([i.pull() for i in self.talent])
        luck= percentage_luck * np.array([i.pull() for i in self.luck])
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



def plot_data(data):

    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['ytick.left'] = False

    plt.plot(data, color="tab:orange", linewidth=1, marker="o", markersize=6, ls="--", markeredgecolor="w", markeredgewidth=1.3)
    plt.gca().invert_xaxis()
    plt.xlabel("% Talent Contribution")
    plt.ylabel("# of Participants Selected")

    for x,y in zip(data.index, data.values):

        label = "{:.2f}".format(y)

        plt.annotate(label,
                    (x,y),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center'
                    )

    plt.tight_layout()
    plt.show()
from success_paradox.src.utils import (
    MonteCarlo,
    plot_data,
)
import pandas as pd
import concurrent.futures



agent_type= ["UniformAgent", "GaussianAgent"][0]
total_number_of_participants= 12000
required_number_of_participants= 10
number_of_simulations= 100


# #This is for a single run
# montecarlo= MonteCarlo(
#     agent_type= agent_type, 
#     total_number_of_participants= total_number_of_participants,
#     required_number_of_participants= required_number_of_participants,
#     ).simulation()

# print(montecarlo)



args = (agent_type, total_number_of_participants, required_number_of_participants)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(MonteCarlo, *args) for _ in range(number_of_simulations)]
    results = [f.result().simulation() for f in concurrent.futures.as_completed(futures)]

df= pd.DataFrame(data= results).mean()

plot_data(data=df)
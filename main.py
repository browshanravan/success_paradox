from success_paradox.src.utils import (
    MonteCarlo,
    run_parallel_monte_carlo_simulation,
    plot_data,
)
import pandas as pd
import concurrent.futures


agent_type= ["UniformAgent", "GaussianAgent"][0]
total_number_of_participants= 12000
required_number_of_participants= 10
number_of_simulations= 100


# #This is for a single run using the class option
# montecarlo= MonteCarlo(
#     agent_type= agent_type, 
#     total_number_of_participants= total_number_of_participants,
#     required_number_of_participants= required_number_of_participants,
#     ).simulation()

# print(montecarlo)



#This is for a running the simulations in parallel using the function approach
args = (agent_type, total_number_of_participants, required_number_of_participants)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(run_parallel_monte_carlo_simulation, *args) for _ in range(number_of_simulations)]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]

df= pd.DataFrame(data= results).mean()

plot_data(data=df)
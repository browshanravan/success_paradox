from talent_vs_luck.src.utils import (
    UniformAgent,
    GaussianAgent
)
import pandas as pd
import matplotlib.pyplot as plt


num= GaussianAgent()
pd.Series(data=num.pull()).plot(kind="hist")
plt.tight_layout()
plt.show()
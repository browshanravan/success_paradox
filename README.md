# success_paradox

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

This project was inspired by [Is Success Luck or Hard Work?](https://www.youtube.com/watch?v=3LopI4YeC4I) video by `Veritasium`.

A Monte Carlo and agent-based exploration into how much luck versus talent contributes to success.

---

## About This Project

This Python package simulates populations of “agents” endowed with talent and luck scores drawn from statistical distributions. By varying the percentage of success attributed to talent versus luck, it measures how often the most “successful” agents (by combined score) overlap with the most talented agents. The goal is to illustrate the sometimes counterintuitive interplay between chance and skill in real-world success.

---

## Project Description

- **Agent Types**  
  - **UniformAgent**  
    Draws talent or luck uniformly from [0, 1].  
  - **GaussianAgent**  
    Draws from a normal distribution centered at 0.5 (σ = 0.1), truncated to non-negative values.

- **Monte Carlo Simulation**  
  - For a given total population size _N_ and number of “winners” _k_, the simulation runs through a series of scenarios where talent contribution ranges from 100 % down to 95 %.  
  - In each scenario:  
    1. Each agent’s talent and luck scores are sampled.  
    2. A combined score = (talent × p) + (luck × (1 – p)) is computed for each agent.  
    3. Agents are ranked by combined score and by raw talent; the top _k_ in each ranking are compared.  
    4. The overlap count (how many of the top _k_ by combined score are also top _k_ by talent) is recorded.  
  - Repeats the above for multiple independent simulations and averages the overlap counts to smooth out randomness.

- **Visualization**  
  - Plots average overlap (# of truly talented winners) vs. talent’s percentage contribution, illustrating how increasing or decreasing the role of luck changes the alignment between raw talent and observed success.

---

## Features

- Choice of uniform or Gaussian-distributed agents  
- Customizable population size, number of winners, and simulation count  
- Parallelised Monte Carlo runs via Python’s `concurrent.futures`  
- Publication-quality matplotlib plots with clean, minimalist style  
- Ready-to-use devcontainer for reproducible environments  

---

## Getting Started

### Prerequisites

- Python 3.10  
- git (to clone the repo)  

### Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/browshanravan/success_paradox.git
   cd success_paradox
   ```

2. Install Python dependencies  
   ```bash
   pip install -r requirements.txt
   ```

---

## Quick Start

Run a batch of Monte Carlo simulations and view the plot:

```bash
python main.py
```

By default, `main.py` will:

1. Use `UniformAgent` (change to `"GaussianAgent"` in `main.py` to switch)  
2. Simulate 100 independent runs on 12 000 agents, selecting the top 10 winners each time  
3. Compute and average the overlap counts  
4. Display a plot of “# of Truly Talented Winners” vs “% Talent Contribution”

To customize simulation parameters, edit the variables at the top of `main.py`:

```python
agent_type = ["UniformAgent", "GaussianAgent"][0]
total_number_of_participants = 12000
required_number_of_participants = 10
number_of_simulations = 100
```

---

## Development with Dev Container

This project includes a VS Code devcontainer for zero-setup development:

1. Install [VS Code](https://code.visualstudio.com/) and the [Dev Containers](https://code.visualstudio.com/docs/remote/containers) extension.  
2. Reopen this folder in the container:  
   ```text
   Command Palette → Remote-Containers: Reopen in Container
   ```  
3. The container builds using Python 3.10 and installs necessary tools automatically.  

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/my-improvement`)  
3. Commit your changes (`git commit -am 'Add awesome feature'`)  
4. Push to your branch (`git push origin feature/my-improvement`)  
5. Open a Pull Request  

Please ensure your code follows PEP 8 style and includes appropriate tests or examples.

---

## File Structure

```
.
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
└── success_paradox/
    └── src/
        └── utils.py
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
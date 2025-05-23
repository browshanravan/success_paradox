# success_paradox
A Monte Carlo and agent based exploration into how much luck plays a role in success

## About this project
Some time ago I came across [Is Success Luck or Hard Work?](https://www.youtube.com/watch?v=3LopI4YeC4I) video by `Veritasium`.

It puts forward and interesting question, namely, how influential is talent/luck in success?

This project employes `OOP`, `Monte Carlo` and `Agentic` simulation methodology to see how much talent/luck plays a role in success.

The crux of this project comes down to every person having a luck score and a talent score. 

These scores come from either a `uniform` or `normal` distribution. The ploted data shows how many people are selected (successful) as their percentage talent contribution changes.

The observations suggest the luck/talent contribution to success can vary depending on the distribution those scores come from.

You can change `agent_type` argument in `main.py` to see the effect.

## Getting started

You can pull this package and run it in devcontainers in your VSCode.

Otherwise run the app by installing `python 3.10` using conda.

The easiest way to run the app is to go to the local directory of this repo and execute:

```console
pip3 install -r requirements.txt
```
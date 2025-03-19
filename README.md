## Twitch Modbot vs. Spambot Simulation (EECS-4461 Winter 2025 Group 5)

This repo is the group project of EECS-4461 Winter 2025 group 5
This project explores the ongoing battle between Twitch mod bots and spambots using Agent-Based Modeling (ABM). On live-streaming platforms like Twitch, chat rooms serve as primary spaces for interaction, but they are also vulnerable to spambot invasions. Mod bots work to enforce chat rules by filtering messages, issuing warnings, and blocking spambots, while spambots continuously evolve to bypass detection through message manipulation and human-like behavior. Our project models these interactions using agent-based simulations to understand the dynamics of AI-vs-AI moderation and AI-to-human interactions. The research findings can contribute to better automated moderation strategies, improved spam detection, and enhanced user experiences on live-streaming and social media platforms.

## Section A: Overview of the Current Implementation StateS

The simulation is built using the Epstein Civil Violence Model, modified to represent the battle between modbots and spambots in Twitch chat rooms.

Implemented Features:

✔ Spambots: Can either remain quiet (avoiding detection) or actively post spam.

✔ Modbots: Patrol the chat, identifying and banning spambots based on their intelligence.

✔ Audience Members: React to spam and may participate in conversations.

✔ Dynamic Agent Behavior: Spambots and modbots make real-time decisions based on environmental factors.

✔ Interactive Visualization: Includes a color-coded grid, pie chart, and line graph showing live simulation data.

## Section B: How to Run the Simulation

Installation Steps

1. Clone the repository:

   git clone https://github.com/Peterayade/EECS-4461-Project.git

   cd EECS-4461-Project

2. Install dependencies:

   pip install -r requirements.txt
   (If using pipenv, run pipenv install instead.)

3. Run the simulation:

   solara run src/app.py

   or, if running without visualization:

   python src/main.py

## Section C: Limitations & Planned Improvements

Current Limitations

- High-IQ spambots evade detection too easily, leading to persistent spam.

- Spam activity fluctuates unexpectedly, possibly due to previously banned spambots returning.

- Modbots struggle with clustered spambots, affecting moderation efficiency.

Planned Improvements

1. Permanent Ban Mechanism: Implement a system where spambots exceeding a threshold number of bans will be permanently removed, aligning with real-world moderation strategies on Twitch.

2. Audience Experience System: Introduce a user experience metric where excessive spam exposure or false bans negatively impact audience retention, simulating engagement shifts.

3. Dynamic Learning Mechanism: Enable mod bots and spambots to adjust their IQ dynamically over time, simulating AI adaptation to changing moderation tactics.

## Summary

This model is based on Joshua Epstein's simulation of how civil unrest grows and is suppressed. Citizen agents wander the grid randomly, and are endowed with individual risk aversion and hardship levels; there is also a universal regime legitimacy value. There are also Cop agents, who work on behalf of the regime. Cops arrest Citizens who are actively rebelling; Citizens decide whether to rebel based on their hardship and the regime legitimacy, and their perceived probability of arrest.

The model generates mass uprising as self-reinforcing processes: if enough agents are rebelling, the probability of any individual agent being arrested is reduced, making more agents more likely to join the uprising. However, the more rebelling Citizens the Cops arrest, the less likely additional agents become to join.

## How to Run

To run the model interactively, in this directory, run the following command

```
    $ solara run app.py
```

## Files

* ``model.py``: Core model code.
* ``agent.py``: Agent classes.
* ``app.py``: Sets up the interactive visualization.
* ``Epstein Civil Violence.ipynb``: Jupyter notebook conducting some preliminary analysis of the model.

## Further Reading

This model is based adapted from:

[Epstein, J. “Modeling civil violence: An agent-based computational approach”, Proceedings of the National Academy of Sciences, Vol. 99, Suppl. 3, May 14, 2002](http://www.pnas.org/content/99/suppl.3/7243.short)

A similar model is also included with NetLogo:

Wilensky, U. (2004). NetLogo Rebellion model. http://ccl.northwestern.edu/netlogo/models/Rebellion. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

For additional guidance on setting up Mesa, refer to the official tutorial:
[Mesa Introduction & Setup Guide](https://mesa.readthedocs.io/stable/tutorials/intro_tutorial.html)

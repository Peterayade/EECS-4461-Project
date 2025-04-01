[A. Overview of the phenomenon modeled]
Our project simulates the adversarial relationship between Spambot and Modbot in live streaming platforms such as Twitch and their impact on the audience. Spambot evades detection by imitating human behavior, while Modbot continuously learns and improves its own strategies to maintain order in the chat room. This interaction not only affects the credibility of platform content and user experience, but also exposes the limitations of current automated governance mechanisms, such as algorithmic bias, false blocking, and infringement of user privacy. To make matters more complicated, when the audience is affected by a large amount of spam, it may mistakenly participate in the spread, further disrupting the stability of the system. To deeply analyze these complex behaviors, we use the Agent-Based Modeling (ABM) method based on the Epstein Civil Violence Model mesa model to model Spambot, Modbot, and Audience as agents with local rules and adaptive behaviors, which can capture the interactions and dynamic evolution processes in the system. Our simulation explains the impact of AI on platforms such as Twitch in reality.

[B.How to run the simulation]
1.Setup the environment and install required modules()
Create and activate a virtual environment. Python version 3.11 or higher is required.
Install Mesa:
pip install --upgrade mesa[rec]

Install Jupyter notebook (optional):
pip install jupyter

Install Seaborn (which is used for data visualization):
pip install seaborn

2.Download the twitch_streaming_simulation folder and extract it

3.Open your terminal and change the address to where you put the twitch_streaming_simulation folder
eg:       
 cd (where you put the folder)\twitch_streaming_simulation  

4.input the following command in the terminal
solara run app.py

5.If the prototype doesn't open shortly, there is a link in the terminal that should generate after following the instructions, copy and paste it into your browser, and the prototype should run

6.You can drag the visual component to the position you want

[C.Key findings of observations]
Through this simulation, we deeply observed the interaction between Spambot, Modbot and Audience in Twitch live broadcast rooms, as well as the impact of different parameters on system dynamics. We found that the stability and volatility of the model are affected by multiple variables, but the three most significant factors are registration difficulty, Spambot ratio, and the number of bans allowed before an account is permanently banned.

First, the higher the registration difficulty, the higher the cost of creating an account for Spambots, which makes them more cautious in their behavior. This not only speeds up the system to reach a stable state, but also reduces the frequency and amplitude of subsequent sudden large fluctuations. At the same time, high registration difficulty also means that the total number of permanently banned accounts is relatively small. Second, the level of Spambot ratio directly determines the scope of false information dissemination in the system. When the Spambot ratio is low, Audience is more difficult to be misled, the system takes less time to stabilize, and sudden dynamics are rarer. The last key parameter - "number of bans before being permanently banned" - has the most dramatic impact on the system's dynamics. When the value is small, Modbot can quickly identify and handle illegal accounts, thereby greatly shortening the time required for the system to stabilize and significantly reducing the amplitude and frequency of subsequent fluctuations; the opposite is true.

In addition, other parameters such as vision and IQ also affect the speed at which the system tends to stabilize, but the effect is relatively small. When the IQ of Spambot is significantly higher than that of Modbot, Modbot needs more time to adapt and learn, further delaying the arrival of stability.

We also observed that even after the system reaches a relatively stable state, there will still be regular and large fluctuations. This phenomenon may occur because multiple accounts are unbanned at the same time, or a large number of Spambots are active at the same time, triggering a chain reaction of Audience, resulting in an explosive growth of Spam information in a short period of time. This kind of sudden dynamics was not expected in the early stage of model design, showing the complex and dynamic behavior patterns in virtual communities.

In summary, this model effectively reveals how different management strategies and environmental settings affect the interactive order and fluctuation characteristics of virtual communities, and has certain value for real-life simulation and theoretical discussion.

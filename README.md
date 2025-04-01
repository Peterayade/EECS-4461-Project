§A. Overview of the current implementation state. At present, our simulation system has been successfully built and can effectively simulate the interaction process between Spambot, Modbot and the audience in the Twitch chat room. The whole simulation is based on the transformation of the Epstein Civil Violence Mesa Model, which realizes the dynamic interaction of different types of agents. Spambot's behavior is affected by spam demand, registration difficulty and risk control awareness. They will choose when to post spam, while Modbot determines whether to ban by comparing the field of view and IQ. The behaviour of the audience depends on the proportion of spam in the chat environment, and they may become passive spammers.

§B. How to run the simulation

1. Setup the environment and install the required modules. Create and activate a virtual environment. Python version 3.11 or higher is required.

Install Mesa: pip install --upgrade mesa[rec]

Install Jupyter notebook (optional): pip install jupyter

Install Seaborn (which is used for data visualization): pip install seaborn

2. Download the twitch_streaming_simulation folder and extract it

3. Open your terminal and change the address to where you put the twitch_streaming_simulation folder eg: cd (where you put the folder)\twitch_streaming_simulation

4. Input the following command in the terminal solara run app.py

5. If the prototype doesn't open shortly, there is a link in the terminal that should generate after following the instructions, copy and paste it into your browser, and the prototype should run

6. You can drag the visual component to the position you want

§C. Limitations and planned improvements for the next phase: Although the current simulation system can better present the interaction between AI audit and spam dissemination in the Twitch chat environment, it still has certain limitations. The current ban mechanism does not have the function of a permanent ban, which allows Spambot to continue to be active after the ban period ends, thus causing periodic spam surges. At the same time, the audience experience has not been quantified. Although the existing model can show the audience's reaction to the spam environment, it fails to introduce a feedback mechanism for the decline of user retention or engagement. Finally, the intelligence level of Modbot AI and Spambot AI is still static; that is, it is set from the beginning and will not change. This fails to reflect the learning ability of AI in reality.

The next stage of improvement will focus on these issues. We plan to introduce a permanent ban mechanism and add a ban threshold to ensure that Spambots that have been banned too many times cannot continue to enter the chat room, so as to be more in line with the operation of real platforms. At the same time, we will increase the simulation of audience loss due to misbanning or excessive spam messages to improve the model's fit to real social platforms. In addition, we hope to make AI's learning ability dynamic so that its behaviour changes over time.

from agents import (
    Citizen,
    CitizenState,
    Cop,
)
from model import EpsteinCivilViolence
from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)
import solara
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mesa.visualization.utils import update_counter

@solara.component
def PieChart(model):
    update_counter.get()


    df = model.datacollector.get_model_vars_dataframe()
    if df.empty:
        return solara.Text("No data collected yet.")

    data = df.iloc[-1]
    labels = ["Active", "SPAMBOT Quiet", "Banned", "Audience Quiet"]
    sizes = [data["active"], data["spambot_quiet"], data["banned"], data["audience_quiet"]]
    colors = ["#FE6100", "#648FFF", "#808080", "#33f561"]


    if sum(sizes) == 0:
        return solara.Text("No agents available.")


    fig = Figure()
    ax = fig.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.axis("equal")

    return solara.FigureMatplotlib(fig)



COP_COLOR = "#000000"

agent_colors = {
    CitizenState.ACTIVE: "#FE6100",
    CitizenState.SPAMBOT_QUIET: "#648FFF",
    CitizenState.BANNED: "#808080",
    CitizenState.AUDIENCE_QUIET:"#33f561",
}


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "size": 50,
    }

    if isinstance(agent, Citizen):
        portrayal["color"] = agent_colors[agent.state]
    elif isinstance(agent, Cop):
        portrayal["color"] = COP_COLOR

    return portrayal


def post_process(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.get_figure().set_size_inches(10, 10)


model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "height": 40,
    "width": 40,
    "citizen_density": Slider("Initial Agent Density", 0.7, 0.0, 0.9, 0.1),
    "spambot_ratio": Slider("spambot ratio", 70, 0, 90, 10),
    "cop_density": Slider("Initial Modbot Density", 0.04, 0.0, 0.1, 0.01),
    "citizen_vision": Slider("Spambot Vision", 7, 1, 10, 1),
    "cop_vision": Slider("Modbot Vision", 7, 1, 10, 1),
    "legitimacy": Slider("Registeration difficulty", 0.82, 0.0, 1, 0.01),
    "max_jail_term": Slider("Max ban time", 30, 0, 50, 1),
    "spambot_iq": Slider("Spambot IQ Range", 0.7, 0.0, 0.9, 0.1),
    "modbot_iq": Slider("Modbot IQ", 0.7, 0.0, 0.9, 0.1),
    "ban_forever_time": Slider("Times of ban before forever ban", 7, 1, 10, 1),
}

space_component = make_space_component(
    citizen_cop_portrayal, post_process=post_process, draw_grid=False
)

chart_component = make_plot_component(
    {state.name.lower(): agent_colors[state] for state in CitizenState}
)

epstein_model = EpsteinCivilViolence()
pie_component = PieChart

page = SolaraViz(
    epstein_model,
    components=[space_component, chart_component,pie_component],
    model_params=model_params,
    name="Twitch Streaming Simulation",
)
page  # noqa

import pandas as pd
import matplotlib.pyplot as plt

from ctg_viz.plots.boxplots import boxplot_por_objetivo, violin_swarm


def test_boxplot_por_objetivo():
    df = pd.DataFrame({"f": [1, 2], "t": ["a", "b"]})
    ax = boxplot_por_objetivo(df, "f", "t")
    assert isinstance(ax, plt.Axes)


def test_violin_swarm():
    df = pd.DataFrame({"f": [1, 2], "t": ["a", "b"]})
    ax = violin_swarm(df, "f", "t")
    assert isinstance(ax, plt.Axes)

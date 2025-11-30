import pandas as pd
import matplotlib.pyplot as plt

from ctg_viz.plots.barplots import barras_horizontales, dotplot_dos_grupos


def test_barras_horizontales():
    df = pd.DataFrame({"c": ["a", "b", "a"]})
    ax = barras_horizontales(df, "c")
    assert isinstance(ax, plt.Axes)


def test_dotplot_dos_grupos():
    df = pd.DataFrame({"v": [1, 2], "g": ["x", "y"]})
    ax = dotplot_dos_grupos(df, "v", "g")
    assert isinstance(ax, plt.Axes)

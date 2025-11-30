import pandas as pd
import matplotlib.pyplot as plt

from ctg_viz.plots.histograms import histograma_kde


def test_histograma_kde():
    df = pd.DataFrame({"v": [1, 2, 2, 3], "g": ["a", "a", "b", "b"]})
    ax = histograma_kde(df, "v", "g")
    assert isinstance(ax, plt.Axes)

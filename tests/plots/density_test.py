import pandas as pd
import matplotlib.pyplot as plt

from ctg_viz.plots.density import densidad_por_clase


def test_densidad_por_clase():
    df = pd.DataFrame({"v": [1, 2, 3], "c": ["a", "a", "b"]})
    ax = densidad_por_clase(df, "v", "c")
    assert isinstance(ax, plt.Axes)

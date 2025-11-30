import pandas as pd
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

from ctg_viz.plots.heatmap import mapa_correlacion


def test_mapa_correlacion_con_numericas():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })

    fig, ax = plt.subplots()
    resultado = mapa_correlacion(df, ax=ax)

    assert resultado is ax


def test_mapa_correlacion_sin_numericas():
    df = pd.DataFrame({
        "x": ["a", "b", "c"],
        "y": ["d", "e", "f"]
    })

    fig, ax = plt.subplots()
    resultado = mapa_correlacion(df, ax=ax)

    assert len(ax.texts) == 1
    assert "No hay columnas numéricas" in ax.texts[0].get_text()


def test_mapa_correlacion_crea_ax_cuando_no_se_pasa():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })

    plt.figure()
    ax = mapa_correlacion(df)

    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.figure is plt.gcf()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def boxplot_por_objetivo(
    df: pd.DataFrame,
    columna: str,
    objetivo: str,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()

    sns.boxplot(data=df, x=objetivo, y=columna, ax=ax)
    return ax


def violin_swarm(
    df: pd.DataFrame,
    columna: str,
    objetivo: str,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()

    sns.violinplot(data=df, x=objetivo, y=columna, inner=None, ax=ax)
    sns.swarmplot(data=df, x=objetivo, y=columna, color="k", size=3, ax=ax)
    return ax

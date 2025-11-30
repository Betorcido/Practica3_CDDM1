import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def histograma_kde(
    df: pd.DataFrame,
    columna: str,
    grupo: str | None = None,
    bins: int = 30,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()

    sns.histplot(df, x=columna, hue=grupo, bins=bins, kde=True, stat="density", ax=ax)
    return ax

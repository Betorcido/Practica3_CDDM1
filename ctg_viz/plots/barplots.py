import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def barras_horizontales(
    df: pd.DataFrame, columna: str, ax: plt.Axes | None = None
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()
    orden = df[columna].value_counts().index
    sns.countplot(data=df, y=columna, order=orden, ax=ax)
    return ax


def dotplot_dos_grupos(
    df: pd.DataFrame, valor: str, grupo: str, ax: plt.Axes | None = None
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()
    sns.stripplot(data=df, x=grupo, y=valor, dodge=True, jitter=True, ax=ax)
    return ax

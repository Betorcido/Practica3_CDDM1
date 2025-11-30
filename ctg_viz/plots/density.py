import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def densidad_por_clase(
    df: pd.DataFrame, valor: str, clase: str, ax: plt.Axes | None = None
) -> plt.Axes:
    if ax is None:
        _, ax = plt.subplots()

    sns.kdeplot(data=df, x=valor, hue=clase, common_norm=False, fill=False, ax=ax)
    return ax

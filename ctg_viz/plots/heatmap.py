import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from ..utils import es_numerica, completitud, clasificar_columna


def mapa_correlacion(
    df: pd.DataFrame,
    metodo: str = "pearson",
    mostrar: bool = True,
    ax: plt.Axes | None = None,
) -> plt.Axes:

    import seaborn as sns
    import matplotlib.pyplot as plt

    if ax is None:
        fig = plt.gcf()             
        ax = fig.add_subplot(111)

    df_num = df.select_dtypes(include="number")
    df_num = df_num.loc[:, df_num.std() > 0]

    if df_num.empty or df_num.shape[1] == 0:
        ax.text(
            0.5, 0.5,
            "No hay columnas numéricas válidas para correlación",
            ha='center', va='center', fontsize=14
        )
        return ax

    corr = df_num.corr(method=metodo)

    sns.heatmap(
        corr,
        cmap="viridis",
        annot=False,
        square=True,
        ax=ax,
        cbar_kws={"shrink": 0.8},
        linewidths=0.2,
        linecolor="white",
    )

    return ax
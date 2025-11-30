from typing import Optional
import numpy as np
import pandas as pd


def eliminar_columnas_nulos_altos(df: pd.DataFrame, umbral: float = 0.2) -> pd.DataFrame:
    proporciones = df.isna().mean()
    columnas = proporciones[proporciones <= umbral].index
    return df[columnas].copy()


def imputar_faltantes(
    df: pd.DataFrame,
    usar_mediana: bool = True,
    usar_knn: bool = False,
    n_vecinos: int = 5,
    random_state: Optional[int] = None,
) -> pd.DataFrame:
    resultado = df.copy()
    cols_num = resultado.select_dtypes(include=[np.number]).columns.tolist()
    cols_cat = resultado.select_dtypes(exclude=[np.number]).columns.tolist()

    if usar_knn and cols_num:
        try:
            from sklearn.impute import KNNImputer
            imp = KNNImputer(n_neighbors=n_vecinos)
            resultado[cols_num] = imp.fit_transform(resultado[cols_num])
        except ImportError as e:
            raise ImportError("scikit-learn es requerido para KNN") from e
    else:
        for col in cols_num:
            serie = resultado[col]
            if serie.isna().any():
                valor = serie.median() if usar_mediana else serie.mean()
                resultado[col] = serie.fillna(valor)

    for col in cols_cat:
        serie = resultado[col]
        if serie.isna().any():
            moda = serie.mode(dropna=True)
            if not moda.empty:
                resultado[col] = serie.fillna(moda.iloc[0])

    return resultado


def recortar_outliers_iqr(df: pd.DataFrame, factor: float = 1.5) -> pd.DataFrame:
    resultado = df.copy()
    cols = resultado.select_dtypes(include=[np.number]).columns

    for col in cols:
        s = resultado[col]
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr = q3 - q1
        inf = q1 - factor * iqr
        sup = q3 + factor * iqr
        resultado[col] = s.clip(lower=inf, upper=sup)

    return resultado


def remover_outliers_zscore(df: pd.DataFrame, umbral: float = 3.0) -> pd.DataFrame:
    cols = df.select_dtypes(include=[np.number]).columns
    if not len(cols):
        return df.copy()

    datos = df[cols]
    medias = datos.mean()
    desv = datos.std(ddof=0).replace(0, np.nan)
    z = (datos - medias) / desv
    mask = (z.abs() <= umbral) | z.isna()

    return df[mask.all(axis=1)].copy()

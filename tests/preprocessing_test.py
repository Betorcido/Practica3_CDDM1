import numpy as np
import pandas as pd

from ctg_viz.preprocessing import (
    eliminar_columnas_nulos_altos,
    imputar_faltantes,
    recortar_outliers_iqr,
    remover_outliers_zscore,
)


def test_eliminar_columnas_nulos_altos():
    df = pd.DataFrame({"a": [1, 2, np.nan], "b": [np.nan, np.nan, 1]})
    r = eliminar_columnas_nulos_altos(df, 0.5)
    assert "a" in r.columns and "b" not in r.columns


def test_imputar_faltantes():
    df = pd.DataFrame({"num": [1, np.nan, 3], "cat": ["a", None, "a"]})
    r = imputar_faltantes(df)
    assert r.isna().sum().sum() == 0


def test_recortar_outliers_iqr():
    df = pd.DataFrame({"x": [1, 2, 3, 999]})
    r = recortar_outliers_iqr(df)
    assert r["x"].max() < 999


def test_remover_outliers_zscore():
    df = pd.DataFrame({"x": [1, 2, 3, 999]})
    r = remover_outliers_zscore(df)
    assert len(r) < len(df)

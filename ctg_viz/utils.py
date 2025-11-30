import pandas as pd


def es_numerica(serie: pd.Series) -> bool:
    return pd.api.types.is_numeric_dtype(serie)


def completitud(serie: pd.Series) -> float:
    return float(serie.notna().mean())


def clasificar_columna(serie: pd.Series) -> str:
    if not es_numerica(serie):
        return "otra"
    unicos = serie.dropna().nunique()
    if unicos > 10:
        return "continua"
    return "discreta"

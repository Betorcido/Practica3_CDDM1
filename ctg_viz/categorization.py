import numpy as np
import pandas as pd
from .utils import completitud, clasificar_columna


def check_data_completeness_nomnbrecompleto(df: pd.DataFrame) -> pd.DataFrame:
    registros = []

    for col in df.columns:
        s = df[col]
        faltantes = int(s.isna().sum())
        comp = completitud(s)
        tipo = str(s.dtype)
        unicos = int(s.nunique(dropna=True))

        if np.issubdtype(s.dtype, np.number):
            std = float(s.std(ddof=1)) if s.notna().sum() > 1 else np.nan
            var = float(s.var(ddof=1)) if s.notna().sum() > 1 else np.nan
            mn = float(s.min()) if s.notna().any() else np.nan
            mx = float(s.max()) if s.notna().any() else np.nan
        else:
            std = var = mn = mx = np.nan

        categoria = clasificar_columna(s)

        registros.append(
            {
                "columna": col,
                "faltantes": faltantes,
                "completitud %": comp*100,
                "tipo": tipo,
                "std": std,
                "var": var,
                "min": mn,
                "max": mx,
                "unicos": unicos,
                "categoria": categoria,
            }
        )

    return pd.DataFrame(registros)

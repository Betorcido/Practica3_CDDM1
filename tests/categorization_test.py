import numpy as np
import pandas as pd

from ctg_viz.categorization import revisar_completitud


def test_revisar_completitud():
    df = pd.DataFrame(
        {"num": [1, 2, np.nan], "cat": ["a", None, "b"], "disc": [1, 1, 2]}
    )
    r = revisar_completitud(df)
    assert set(r["columna"]) == {"num", "cat", "disc"}
    assert "completitud" in r.columns
    assert "categoria" in r.columns

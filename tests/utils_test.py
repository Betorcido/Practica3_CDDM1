import pandas as pd

from ctg_viz.utils import (
    es_numerica,
    completitud,
    clasificar_columna
)


def test_es_numerica():
    assert es_numerica(pd.Series([1, 2, 3])) is True
    assert es_numerica(pd.Series(["a", "b", "c"])) is False


def test_completitud():
    serie = pd.Series([1, None, 3, None])
    assert completitud(serie) == 0.5


def test_clasificar_columna_otra():
    serie = pd.Series(["a", "b", "c"])
    assert clasificar_columna(serie) == "otra"


def test_clasificar_columna_continua():
    serie = pd.Series([i for i in range(11)])
    assert clasificar_columna(serie) == "continua"


def test_clasificar_columna_discreta():
    serie = pd.Series([1, 1, 2, 3])
    assert clasificar_columna(serie) == "discreta"

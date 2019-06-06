import pandas as pd
import numpy as np


def isTable(x):
    return (type(x) in [pd.DataFrame, pd.Series]) * 1


def missing(x):
    try:
        return (pd.isnull(x)).sum()
    except:
        return (np.isnan(x)).sum()


def isCategory(x, pct, catg):
    unique = x.nunique(dropna=True)
    total = x.count()
    rem = total - unique
    percentage = rem / total * 100
    if percentage > pct or unique < catg:
        return True
    else:
        return False


def isContinous(x, pct, catg):
    unique = x.nunique(dropna=True)
    total = x.count()
    rem = total - unique
    percentage = rem / total * 100
    if percentage < pct or unique > catg:
        return True
    else:
        return False


def table(x):
    return pd.DataFrame(x)


def concat(*args):
    a = args[0]
    if type(a) == pd.Series: a = table(a)
    for b in args[1:]:
        if type(b) != pd.DataFrame:
            b = table(b)
        a = pd.concat([a, b], 1)
    del b
    return a


def wrap(col, val):
    return pd.Series(data=val, index=[col])

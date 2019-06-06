import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from utils import *

def normality_plot(x, col, ax=0):
    ax1 = plt.subplot(ax)
    stats.probplot(x[col], plot=plt)
    plt.show()


def bar_plot(x, col):
    sns.catplot(y=col, kind="count", data=x)


def dist_plot(x, col):
    sns.distplot(x[col])


def box_plot(x, col, ax=0):
    sns.boxplot(x=x[col], ax=ax)


def anomalies_graph(x, col):
    f, axes = plt.subplots(1, 2)
    box_plot(x, col, axes[0])
    normality_plot(x, col, axes[1])


def catg_graph(x, col):
    bar_plot(x, col)


def continous_graph(x, col,pct, catg):
    if (isContinous(x[col],pct, catg)):
        dist_plot(x, col)
    else:
        bar_plot(x, col)

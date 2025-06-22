import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .ttest import ttest
from .correlation import corr_case
from .anova import anova
from .crosstab import crosstab

sns.set_theme(style="whitegrid", palette="muted")


def plot_ttest(group1, group2, paired=False, equal_variances=True, palette="muted"):
    """Visualize distributions for a t-test."""
    _desc, _results = ttest(
        group1,
        group2,
        paired=paired,
        equal_variances=equal_variances,
    )

    data = pd.DataFrame(
        {
            "value": pd.concat([group1, group2]),
            "group": [group1.name] * len(group1) + [group2.name] * len(group2),
        }
    )
    plt.figure()
    ax = sns.boxplot(x="group", y="value", data=data, palette=palette)
    sns.stripplot(x="group", y="value", data=data, color="black", alpha=0.5, ax=ax)
    ax.set_title("T-Test" if not paired else "Paired T-Test")
    return ax


def plot_correlation(dataframe, method="pearson", annot=True, cmap="coolwarm"):
    """Plot correlation matrix heatmap."""
    _info, r_vals, _ = corr_case(dataframe, method=method)
    plt.figure()
    ax = sns.heatmap(r_vals.astype(float), annot=annot, cmap=cmap, vmin=-1, vmax=1)
    ax.set_title(f"{method.capitalize()} Correlation Matrix")
    return ax


def plot_anova(formula, data, palette="muted"):
    """Visualize group means for ANOVA."""
    analysis = anova(formula, data)
    dv = formula.split("~")[0].strip()
    iv = formula.split("~")[1].strip()
    plt.figure()
    ax = sns.boxplot(x=iv, y=dv, data=data, palette=palette)
    ax.set_title("ANOVA")
    return ax


def plot_crosstab(group1, group2, palette="crest"):
    """Plot heatmap for crosstab counts."""
    table = crosstab(group1, group2)
    plt.figure()
    ax = sns.heatmap(table, annot=True, fmt="d", cmap=palette)
    ax.set_title("Crosstabulation")
    return ax

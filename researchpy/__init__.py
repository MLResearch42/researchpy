# -*- coding: utf-8 -*-
"""
ResearchPy: A comprehensive statistical analysis library for researchers.

ResearchPy produces pandas DataFrames that contain relevant statistical testing
information commonly required for academic research. It provides an easy-to-use
interface for conducting various statistical analyses including t-tests,
correlation analysis, ANOVA, regression, and descriptive statistics.

Key Features:
- Comprehensive statistical tests with effect sizes
- Research-friendly output format
- Pandas integration for data manipulation
- Missing data handling
- Publication-ready statistical tables

@author: Corey Bryant
Last updated: 03/05/2024
"""

from .version import __version__, __author__, __email__, __license__

# Core statistical functions
from .ttest import ttest
from .difference_test import difference_test

# Summary statistics
from .summary import summary_cont, summary_cat, codebook, summarize

# Correlation analysis
from .correlation import corr_case, corr_pair

# Crosstabulation and chi-square
from .crosstab import crosstab

# Visualization functions
from .visualization import (
    plot_ttest,
    plot_correlation,
    plot_anova,
    plot_crosstab,
)

# Basic statistical functions
from .basic_stats import (
    count,
    nanvar,
    nanstd,
    nansem,
    value_range,
    kurtosis,
    skew,
    confidence_interval,
    l_ci,
    u_ci,
)

# Utility functions
from .utility import variable_information, base_table

# Advanced statistical modeling
from .model import model
from .anova import anova
from .ols import ols

# Non-parametric tests
from .signrank import signrank

# Model utilities and prediction
from .predict import (
    predict,
    predict_y,
    residuals,
    standardized_residuals,
    studentized_residuals,
    leverage,
)

# Define what gets imported with "from researchpy import *"
__all__ = [
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    # Core statistical tests
    "ttest",
    "difference_test",
    # Summary statistics
    "summary_cont",
    "summary_cat",
    "codebook",
    "summarize",
    # Correlation analysis
    "corr_case",
    "corr_pair",
    # Crosstabulation
    "crosstab",
    # Visualization functions
    "plot_ttest",
    "plot_correlation",
    "plot_anova",
    "plot_crosstab",
    # Basic statistics
    "count",
    "nanvar",
    "nanstd",
    "nansem",
    "value_range",
    "kurtosis",
    "skew",
    "confidence_interval",
    "l_ci",
    "u_ci",
    # Utility functions
    "variable_information",
    "base_table",
    # Advanced modeling
    "model",
    "anova",
    "ols",
    # Non-parametric tests
    "signrank",
    # Model utilities
    "predict",
    "predict_y",
    "residuals",
    "standardized_residuals",
    "studentized_residuals",
    "leverage",
]

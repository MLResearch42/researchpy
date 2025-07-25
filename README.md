# ResearchPy

[![PyPI version](https://badge.fury.io/py/researchpy.svg)](https://badge.fury.io/py/researchpy)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**ResearchPy** is a comprehensive statistical analysis library designed specifically for researchers and data analysts. It produces pandas DataFrames containing relevant statistical testing information commonly required for academic research, making it easy to generate publication-ready results.

## 🚀 Key Features

- **Comprehensive Statistical Tests**: T-tests, correlation analysis, ANOVA, regression, and more
- **Research-Friendly Output**: Publication-ready tables with effect sizes and confidence intervals  
- **Pandas Integration**: Input and output designed around pandas DataFrames and Series
- **Missing Data Handling**: Robust handling of missing values across all functions
- **Effect Size Calculations**: Comprehensive effect size measures (Cohen's d, Hedge's g, etc.)
- **Professional Documentation**: Detailed statistical information for academic use
- **Visualization Utilities**: High-quality plotting functions for t-tests, ANOVA, correlations, and crosstabs

## 📦 Installation

Install ResearchPy using pip:

```bash
pip install researchpy
```

### Dependencies

ResearchPy requires the following packages:
- pandas
- numpy
- scipy
- statsmodels
- patsy

## 🏃‍♂️ Quick Start

```python
import researchpy as rp
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
group1 = pd.Series(np.random.normal(10, 2, 30), name='Control')
group2 = pd.Series(np.random.normal(12, 2, 30), name='Treatment')

# Perform t-test
descriptives, results = rp.ttest(group1, group2)
print(descriptives)
print(results)

# Visualize the distributions
rp.plot_ttest(group1, group2)
rp.plot_correlation(pd.DataFrame({'group1': group1, 'group2': group2}))
```

## 📚 Core Functions

### Statistical Tests

#### T-Tests (`ttest`)
Comprehensive t-test function supporting multiple variants:

```python
import researchpy as rp

# Independent samples t-test
desc, results = rp.ttest(group1, group2)

# Paired samples t-test  
desc, results = rp.ttest(before, after, paired=True)

# Welch's t-test (unequal variances)
desc, results = rp.ttest(group1, group2, equal_variances=False)

# Wilcoxon signed-rank test (non-parametric)
desc, results = rp.ttest(group1, group2, wilcoxon=True)
```

**Supported Tests:**
- Independent samples t-test (equal variances)
- Welch's t-test (unequal variances) 
- Satterthwaite t-test (unequal variances)
- Paired samples t-test
- Wilcoxon signed-rank test

**Effect Sizes:**
- Cohen's d, Hedge's g, Glass's delta
- Point-biserial correlation
- Confidence intervals for all measures

#### Difference Testing (`difference_test`)
Formula-based interface for statistical testing:

```python
# Using R-style formulas
test = rp.difference_test("score ~ group", data=df)
desc, results = test.summary()
```

### Summary Statistics

#### Continuous Data (`summary_cont`)
Descriptive statistics for continuous variables:

```python
# Basic summary
summary = rp.summary_cont(data['score'])

# Grouped summary
summary = rp.summary_cont(data['score'], group_by=data['condition'])

# Multiple variables
summary = rp.summary_cont(data[['score1', 'score2', 'score3']])
```

#### Categorical Data (`summary_cat`)
Descriptive statistics for categorical variables:

```python
# Frequency counts and percentages
summary = rp.summary_cat(data['category'])

# Grouped categorical summary
summary = rp.summary_cat(data['category'], group_by=data['condition'])
```

#### Data Exploration (`codebook`)
Comprehensive data exploration:

```python
# Generate codebook for entire dataset
codebook = rp.codebook(data)

# Codebook for specific variables
codebook = rp.codebook(data[['var1', 'var2', 'var3']])
```

### Correlation Analysis

#### Case-wise Correlation (`corr_case`)
Correlation analysis with listwise deletion:

```python
# Pearson correlations
info, corr_matrix, p_values = rp.corr_case(data)

# Spearman correlations
info, corr_matrix, p_values = rp.corr_case(data, method='spearman')

# Kendall's tau
info, corr_matrix, p_values = rp.corr_case(data, method='kendall')
```

#### Pairwise Correlation (`corr_pair`)
Correlation analysis with pairwise deletion:

```python
# Pairwise correlations with sample sizes
correlations = rp.corr_pair(data)
```

### Crosstabulation and Chi-Square

#### Crosstabulation (`crosstab`)
Comprehensive crosstabulation with statistical tests:

```python
# Basic crosstab
crosstab = rp.crosstab(data['var1'], data['var2'])

# With chi-square test
crosstab, chi2_results = rp.crosstab(data['var1'], data['var2'], 
                                     test='chi-square')

# With different table types
crosstab = rp.crosstab(data['var1'], data['var2'], 
                       table='row_prop')  # row percentages
```

**Supported Tests:**
- Chi-square test of independence
- G-test (log-likelihood ratio)
- Fisher's exact test
- McNemar test (for paired data)

**Table Types:**
- Raw counts (`'count'`)
- Row percentages (`'row_prop'`)
- Column percentages (`'col_prop'`) 
- Cell percentages (`'cell_prop'`)

### Advanced Statistical Modeling

#### ANOVA (`anova`)
Analysis of variance:

```python
# One-way ANOVA
results = rp.anova("dependent ~ factor", data=df)

# Multi-factor ANOVA  
results = rp.anova("dependent ~ factor1 + factor2 + factor1:factor2", data=df)
```

#### Regression Analysis (`ols`)
Ordinary least squares regression:

```python
# Simple linear regression
results = rp.ols("dependent ~ independent", data=df)

# Multiple regression
results = rp.ols("dependent ~ var1 + var2 + var3", data=df)
```

## 🔧 Advanced Usage

### Working with Missing Data

All ResearchPy functions handle missing data appropriately:

```python
# Functions automatically handle NaN values
data_with_missing = pd.Series([1, 2, np.nan, 4, 5])
summary = rp.summary_cont(data_with_missing)  # Excludes NaN values
```

### Customizing Output

Many functions accept parameters to customize output:

```python
# Custom confidence level
desc, results = rp.ttest(group1, group2, alpha=0.01)  # 99% CI

# Different return format
summary = rp.summary_cont(data, return_type='dict')  # Dictionary instead of DataFrame
```

### Effect Size Options

T-test functions provide multiple effect size measures:

```python
# Different effect sizes for paired t-test
desc, results = rp.ttest(before, after, paired=True,
                         effect_size=['cohen_d', 'hedge_g'])
```

### Visualization Utilities

Easily generate professional plots for common statistical tests:

```python
# T-test distribution plot
rp.plot_ttest(group1, group2)

# Correlation heatmap
rp.plot_correlation(data[['var1', 'var2', 'var3']])

# ANOVA group comparison
rp.plot_anova("score ~ group", data=df)

# Crosstab heatmap
rp.plot_crosstab(df['group'], df['outcome'])
```

## 📊 Output Format

ResearchPy functions typically return pandas DataFrames formatted for research use:

### T-Test Output Example

**Descriptive Statistics:**
```
Variable    N      Mean    SD      SE      95% Conf.    Interval
Control    30    10.15   1.98    0.36     9.41        10.89
Treatment  30    12.03   2.12    0.39    11.24        12.82
combined   60    11.09   2.18    0.28    10.53        11.65
```

**Test Results:**
```
Independent samples t-test                    results
Difference (Control - Treatment) =             -1.88
Degrees of freedom =                           58.00
t =                                           -3.52
Two side test p value =                        0.00
Difference < 0 p value =                       0.00
Difference > 0 p value =                       1.00
Cohen's d =                                   -0.91
Hedge's g =                                   -0.90
Glass's delta1 =                              -0.95
Point-Biserial r =                            -0.42
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment: `source .venv/bin/activate` (Unix) or `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install in development mode: `pip install -e .`

## 📖 Documentation

For comprehensive documentation, examples, and tutorials, visit: [https://researchpy.readthedocs.io/](https://researchpy.readthedocs.io/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 📝 Citation

If you use ResearchPy in your research, please cite:

```
Bryant, C. (2018). ResearchPy. https://github.com/researchpy/researchpy
```

## 🆕 Recent Updates

### Version 0.3.6
- Fixed pandas compatibility issues with FutureWarnings
- Improved DataFrame creation for mixed data types
- Enhanced error handling and stability

## 🐛 Issues and Support

If you encounter any issues or have questions:

1. Check the [documentation](https://researchpy.readthedocs.io/)
2. Search [existing issues](https://github.com/researchpy/researchpy/issues)
3. Create a [new issue](https://github.com/researchpy/researchpy/issues/new) if needed

## 🔗 Related Projects

- [pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [scipy](https://scipy.org/) - Scientific computing
- [statsmodels](https://www.statsmodels.org/) - Statistical modeling
- [numpy](https://numpy.org/) - Numerical computing

---

**ResearchPy** - Making statistical analysis accessible for researchers 📊✨
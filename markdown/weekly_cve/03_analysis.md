---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Weekly CVE - Vulnerability Analysis

```python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

```

## Loading Processed Data for Analysis

### Procedure

1. **Reading CSV Data**:
   - The `pd.read_csv` function from the pandas library is used to read the data stored in the CSV file located at `'../../data/weekly_cve/processed/nvd_epss_kev.csv`.
   - This file contains the processed data that integrates NIST NVD data and EPSS scores, which was previously prepared and saved in an earlier step of the workflow.

2. **DataFrame Storage**:
   - The data read from the CSV file is stored in the DataFrame `weekly_cve_df`. This DataFrame will serve as the primary data structure from which all further data manipulations, analyses, and visualizations will be conducted.


```python
weekly_cve_df = pd.read_csv("../../data/weekly_cve/processed/nvd_epss_kev.csv")
weekly_cve_df.head()
```

```python

```

```python
# Create a pivot table showing the count of CVEs for each vendor
heatmap_data = weekly_cve_df.pivot_table(index='Vendor', columns='Product', values='CVE', aggfunc='count')

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".0f", cbar=False)
plt.title('Vendor-Product Vulnerability Heatmap')
plt.show()
```



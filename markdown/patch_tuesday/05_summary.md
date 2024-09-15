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

# Patch Tuesday - Vulnerability Summary

```python
import pandas as pd
from IPython.display import Markdown, display
```

## Read CSV into a Pandas DataFrame


```python
patch_tuesday_df = pd.read_csv("../../data/patch_tuesday/processed/patch_tuesday_prioritized.csv")
```

## Summary of the Latest Patch Tuesday Security Updates

```python
# Function to display Markdown text
def print_md(text):
    display(Markdown(text))


# Data Extraction

# Total CVEs
total_cves = patch_tuesday_df["CVE"].nunique()

# Severity Distribution with percentages
severity_counts = patch_tuesday_df["Severity"].value_counts()
severity_percentages = patch_tuesday_df["Severity"].value_counts(normalize=True).mul(100).round(1)
severity_dict = severity_counts.to_dict()
severity_percentage_dict = severity_percentages.to_dict()

# Affected Products
total_products_affected = patch_tuesday_df["Product"].nunique()

# For percentages, calculate the percentage of total vulnerabilities each product represents
product_counts = patch_tuesday_df["Product"].value_counts()
top_affected_products_counts = product_counts.head(3)
total_vulnerabilities = patch_tuesday_df.shape[0]
top_affected_products_percentages = top_affected_products_counts.div(total_vulnerabilities).mul(100).round(1).to_dict()

# Top 5 Prioritized Vulnerabilities based on CVSS and EPSS
top_5_vulnerabilities = (
    patch_tuesday_df.sort_values(by=["CVSS", "EPSS"], ascending=[False, False])
    .head(5)[["CVE", "CVSS", "EPSS", "Title"]]
    .to_dict(orient="records")
)

# Impact Analysis with percentages
impact_counts = patch_tuesday_df["Impact"].value_counts()
impact_percentages = patch_tuesday_df["Impact"].value_counts(normalize=True).mul(100).round(1)
impact_dict = impact_counts.to_dict()
impact_percentage_dict = impact_percentages.to_dict()

# Display Summary
print_md("**Patch Tuesday Summary: Key Highlights from the Latest Security Updates**\n")

# Overview
print_md("**🔍 Overview**\n")
print_md(
    f"- **Total Vulnerabilities Addressed**: {total_cves} CVEs have been patched.")
print_md("- **Severity Breakdown**:")
for severity in ["Critical", "Important", "Moderate", "Low"]:
    count = severity_dict.get(severity, 0)
    percentage = severity_percentage_dict.get(severity, 0.0)
    if count > 0:
        print_md(f"  - **{severity}**: {count} vulnerabilities ({percentage:.0f}%)")

# Affected Products
print_md("\n**🛠️ Affected Products**\n")
print_md(
    f"- {total_products_affected} products are affected.")
print_md("- **Top Affected Products**:")
for product in top_affected_products_counts.index:
    count = top_affected_products_counts[product]
    percentage = top_affected_products_percentages[product]
    print_md(f"  - **{product}**: {count} vulnerabilities ({percentage:.0f}%)")

# Top 5 Prioritized Vulnerabilities
print_md("\n**🚨 Top Prioritized Vulnerabilities**\n")
for idx, vuln in enumerate(top_5_vulnerabilities, 1):
    cvss_score = vuln['CVSS']
    epss_score = vuln['EPSS']

    # Interpret EPSS score
    if epss_score >= 0.7:
        epss_risk = "Elevated risk of exploitation"
    elif epss_score >= 0.3:
        epss_risk = "Notable risk"
    else:
        epss_risk = "Lower risk"
    # Interpret CVSS score
    if cvss_score >= 9.0:
        cvss_rating = "Critical"
    elif cvss_score >= 7.0:
        cvss_rating = "High"
    elif cvss_score >= 4.0:
        cvss_rating = "Moderate"
    else:
        cvss_rating = "Low"
    print_md(f"{idx}. **{vuln['CVE']}**")
    if pd.notna(vuln['Title']):
        print_md(f"   - *Title*: {vuln["Title"]}")

    print_md(f"   - *CVSS Score*: {cvss_score} ({cvss_rating})")
    if pd.notna(vuln['EPSS']):
        print_md(f"   - *EPSS Score*: {epss_score} ({epss_risk})")

# Impact Analysis
print_md("\n**💥 Impact Analysis**\n")
for impact, count in impact_dict.items():
    percentage = impact_percentage_dict[impact]
    print_md(f"- **{impact}**: {count} vulnerabilities ({percentage:.0f}%)")
```

```python

```

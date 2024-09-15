# vuln-data-science

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

Welcome to the vuln-data-science repository! This project focuses on applying data science techniques to vulnerability
management and analysis. Our goal is to explore, analyze, and share insights on vulnerabilities using data science
methodologies.

## Table of Contents

- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notebooks and Markdown](#notebooks-and-markdown)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Future Work](#future-work)
- [Acknowledgments](#acknowledgments)

## Introduction

In the modern cybersecurity landscape, vulnerability management is crucial. By leveraging data science, we can gain
deeper insights into vulnerabilities, predict trends, and enhance our overall security posture. This repository contains
data, Jupyter notebooks, and analysis scripts aimed at advancing our understanding of vulnerabilities across various
domains, including software and network vulnerabilities. We utilize data from trusted sources such as:

- [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/)
- [NIST National Vulnerability Database (NVD)](https://nvd.nist.gov/)

## Motivation

Effective vulnerability management is essential for maintaining a strong security posture. This project demonstrates how
data science can be used to identify patterns, predict vulnerabilities, and provide actionable insights to security
professionals.

## Features

- **Data Collection**: Automated scripts for collecting vulnerability data from various sources.
- **Data Cleaning**: Techniques to preprocess and clean the data for analysis.
- **Exploratory Data Analysis**: Visualizations and insights into vulnerability trends.
- **Predictive Analysis**: Models to predict future vulnerabilities and their potential impact.
- **Tools & Libraries**: Utilization of tools like Pandas, Polars, Matplotlib, and Scikit-learn for data processing and
  analysis.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.7 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/typeerror/vuln-data-science.git
   ```

2. Navigate to the project directory:

   ```bash
   cd vuln-data-science
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start exploring the data and running the analyses, open the Jupyter notebooks in the `notebooks` directory. Each
notebook focuses on a different aspect of the data pipeline:

- `01_data_collection.ipynb`: Collects and aggregates data from various vulnerability sources.
- `02_data_cleaning.ipynb`: Cleans and preprocesses the raw data for analysis.
- `03_weighted_vulnerability_scoring.ipynb`: Applies weighted scoring to prioritize vulnerabilities based on multiple
  factors.
- `04_analysis.ipynb`: Analyzes the processed data to identify trends and insights.
- `05_summary.ipynb`: Summarizes the findings and prepares the final report.

You can launch Jupyter Notebook with the following command:

```bash
jupyter notebook
```

Navigate to the `notebooks` directory and open any notebook to get started.

To keep the Markdown files in sync with the Jupyter notebooks, you can use the provided conversion script:

```bash
python scripts/nb_to_md.py
```

This script requires the `jupytext` package, which will be installed with the other dependencies.

## Project Structure

```
vuln-data-science/
├── data/
│   ├── raw/
│   ├── processed/
├── notebooks/
│   ├── patch_tuesday/
│   │   ├── 01_data_collection.ipynb
│   │   ├── 02_data_cleaning.ipynb
│   │   ├── 03_weighted_vulnerability_scoring.ipynb
│   │   ├── 04_analysis.ipynb
│   │   ├── 05_summary.ipynb
├── markdown/
├── scripts/
│   ├── nb_to_md.py
├── README.md
├── requirements.txt
└── LICENSE
```

- `data/`: Contains raw and processed data files, organized by project (e.g., `patch_tuesday`, `weekly_cve`).
- `notebooks/`: Jupyter notebooks for data exploration, cleaning, and analysis.
- `markdown/`: Markdown versions of the Jupyter notebooks.
- `scripts/`: Python scripts for data processing and analysis tools.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.
- `LICENSE`: License information.

## Notebooks and Markdown

Jupyter notebooks are located in the `/notebooks` directory. These contain code and analysis for various aspects of
vulnerability management. For convenience, markdown versions are available in the `/markdown` directory.

To keep the Markdown files in sync with the Jupyter notebooks, use the conversion script:

```bash
python scripts/nb_to_md.py
```

The `jupytext` package will be installed with the other dependencies.

### Patch Tuesday

#### Notebooks

- [Data Collection Notebook](notebooks/patch_tuesday/01_data_collection.ipynb)
- [Data Cleaning Notebook](notebooks/patch_tuesday/02_data_cleaning.ipynb)
- [Vulnerability Analysis Notebook](notebooks/patch_tuesday/03_vulnerability_analysis.ipynb)

#### Markdown

- [Data Collection Markdown](markdown/patch_tuesday/01_data_collection.md)
- [Data Cleaning Markdown](markdown/patch_tuesday/02_data_cleaning.md)
- [Vulnerability Analysis Markdown](markdown/patch_tuesday/03_vulnerability_analysis.md)

## Contributing

We welcome contributions! If you have ideas or find issues, please open a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, reach out via GitHub issues, email
at [projects@typeerror.com](mailto:projects@typeerror.com), or connect with Caleb
on [LinkedIn](https://linkedin.com/in/calebk).

## Future Work

We plan to expand the project with the following features:

- **Additional Data Sources**: Integration with more vulnerability databases and threat intelligence feeds.
- **Advanced Analytics**: Machine learning models for predicting vulnerability exploitation likelihood.
- **Visualization Dashboards**: Interactive dashboards for visualizing trends and insights.

## Acknowledgments

We would like to acknowledge the work of researchers and contributors who are advancing the field of vulnerability data
science. Their insights and tools have been instrumental in shaping this project.

- **[Jay Jacobs](https://www.linkedin.com/in/jayjacobs1/)**  
  Co-founder of the Cyentia Institute, focusing on security metrics and data-driven decision-making in vulnerability
  management and risk assessment.

- **[Jerry Gamblin](https://www.linkedin.com/in/jgamblin/)** / [GitHub](https://github.com/jgamblin)  
  Security researcher and advocate, contributing to vulnerability analysis, remediation strategies, and the development
  of security tools.

- **[Patrick Garrity](https://www.linkedin.com/in/patrickmgarrity/)**  
  Acclaimed security researcher with deep expertise in vulnerabilities, exploitation, and threat actor analysis, focused
  on transforming complex vulnerability data into clear, actionable visualizations.

- **[Wade Baker](https://www.linkedin.com/in/drwadebaker/)**  
  Co-founder of the Cyentia Institute and co-creator of the Verizon Data Breach Investigations Report (DBIR),
  specializing in security data analytics and risk management.

We also want to thank the broader cybersecurity and data science communities for their contributions. This project draws
inspiration from collective efforts to improve security practices and promote knowledge sharing.

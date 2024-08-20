# vuln-data-science

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

Welcome to the vuln-data-science repository! This project focuses on applying data science techniques to vulnerability management and analysis. Our goal is to explore, analyze, and share insights on vulnerabilities using data science methodologies.

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
- [Acknowledgments](#acknowledgments)

## Introduction

In the modern cybersecurity landscape, vulnerability management is crucial. By leveraging data science, we can gain deeper insights into vulnerabilities, predict trends, and enhance our overall security posture. This repository contains data, Jupyter notebooks, and analysis scripts aimed at advancing our understanding of vulnerabilities across various domains, including software and network vulnerabilities. We utilize data from trusted sources such as the CISA Known Exploited Vulnerabilities (KEV), the Exploit Prediction Scoring System (EPSS), and the NIST National Vulnerability Database (NVD).

## Motivation

Effective vulnerability management is essential for maintaining a strong security posture. This project aims to demonstrate how data science can be used to identify patterns, predict future vulnerabilities, and provide actionable insights to security professionals. By sharing these analyses, we hope to contribute to the broader security community.

## Features

- **Data Collection**: Automated scripts for collecting vulnerability data from various sources.
- **Data Cleaning**: Techniques to preprocess and clean the data for analysis.
- **Exploratory Data Analysis**: Visualizations and insights into vulnerability trends.
- **Predictive Analysis**: Models to predict future vulnerabilities and their potential impact.
- **Tools & Libraries**: Utilization of tools like Pandas, Polars, Matplotlib, Scikit-learn for data processing and analysis.

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

To start exploring the data and running the analyses, open the Jupyter notebooks in the `notebooks` directory. You can launch Jupyter Notebook with the following command:

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
│   ├── patch_tuesday/
│   │   ├── 01_data_collection.ms
│   │   ├── 02_data_cleaning.md
│   │   ├── 03_weighted_vulnerability_scoring.md
│   │   ├── 04_analysis.md
│   │   ├── 05_summary.md
├── scripts/
│   ├── nb_to_md.py
├── README.md
├── requirements.txt
└── LICENSE
```

- `data/`: Contains raw and processed data files.
- `notebooks/`: Jupyter notebooks for data exploration, cleaning, and analysis.
- `markdown/`: Markdown versions of the Jupyter notebooks for easier viewing and editing.
- `scripts/`: Python scripts for data processing and analysis tools.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.
- `LICENSE`: License information.

## Notebooks and Markdown

The Jupyter notebooks are located in the `/notebooks` directory. These notebooks contain the code and analysis for various aspects of vulnerability management.

For convenience, we also provide the notebooks in Markdown format, located in the `/markdown` directory. These files are useful for viewing and editing without requiring Jupyter Notebook.

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

We welcome contributions to this project! If you have an idea or find an issue, please open a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out via GitHub issues, email at [projects@typeerror.com](mailto:projects@typeerror.com), or connect with Caleb on [LinkedIn](https://linkedin.com/in/calebk).

## Acknowledgments

Special thanks to the cybersecurity and data science communities for their support and contributions. This project is inspired by the continuous efforts to improve security practices and knowledge sharing. We also acknowledge the valuable data and resources provided by:

- [CISA Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/)
- [NIST National Vulnerability Database (NVD)](https://nvd.nist.gov/)

# 📊 Project Overview
This project analyzes the Gross Domestic Product (GDP) of 227 countries using 20 socio-economic factors. The analysis aims to uncover patterns and insights that can inform economic policies and development strategies.

# 🚀 Getting Started
1. Clone the Repository
To download the project files to your local machine, open your terminal or command prompt and run:

```bash
git clone https://github.com/AnkitBohare16/GDP-Data-Analysis.git
cd GDP-Data-Analysis
```
Alternatively, you can download the ZIP file directly from the GitHub repository.

## 2. Set Up the Python Environment
It's recommended to use a virtual environment to manage dependencies. If you have Python 3.11 installed, you can create and activate a virtual environment as follows:

```bash
python -m venv gdp-env

# On Windows
gdp-env\Scripts\activate

# On macOS/Linux
source gdp-env/bin/activate
```

## 3. Install Required Dependencies
With the virtual environment activated, install the necessary Python packages:
```
pip install -r requirements.txt
```
You can manually install the required packages:
```
pip install pandas matplotlib seaborn
```
These packages are essential for data manipulation and visualization.

## 4. Run the Analysis
To execute the analysis script, run:

```bash
python app.py
```
This script processes the dataset and generates visualizations to help interpret the economic data.

# 📁 Project Structure

```graphql
GDP-Data-Analysis/
├── analysis.py           # Main script for data analysis
├── app.py                # Web application (if applicable)
├── world_gdp_dataset.csv # Dataset containing GDP and socio-economic factors
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
```

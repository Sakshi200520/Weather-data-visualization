Project Overview

This project focuses on analyzing weather data using Python. It involves data cleaning, basic statistical analysis, and generating meaningful visualizations to understand temperature and humidity patterns.

The goal is to convert raw data into clear insights that can help in understanding weather trends over time and across different locations.

Objectives

- Load and process raw weather data
- Clean and prepare the dataset for analysis
- Perform basic statistical analysis
- Create visualizations for better understanding
- Generate a structured analysis report

 Technologies Used

Python
Pandas – for data handling and preprocessing
Matplotlib – for data visualization
OS module – for file and folder management


Project Structure
Weather-Data-Analysis/
│
├── visualizations/
│   ├── temp_trend.png
│   ├── location_temp.png
│   ├── temp_distribution.png
│   └── humidity_trend.png
│
├── report/
│   └── report.txt
│
├── weather_data.csv
└── main.py

Workflow Explanation
1. Data Loading

The dataset is loaded using Pandas. The program checks if the file exists and displays the available columns.

2. Data Cleaning
Column names are standardized (lowercase, trimmed spaces)
Numeric values are converted properly
Date columns are formatted correctly
Missing values are removed

This step ensures the dataset is ready for accurate analysis.

3. Data Analysis

Basic statistics are calculated:

Average temperature
Maximum temperature
Minimum temperature

These values give a quick understanding of the dataset.

4. Data Visualization

The project creates multiple charts:

Temperature Trend (Line Chart)

Shows how temperature changes over time.
Helps identify patterns like increase, decrease, or fluctuations.

Temperature by Location (Bar Chart)

Compares average temperature across different locations.
Useful to understand geographical differences.

Temperature Distribution (Pie Chart)

Divides temperature into categories like:

Very Cold
Cold
Moderate
Hot

Gives an overall idea of climate conditions.

Humidity Trend (Line Chart)

Displays how humidity changes over time.
Helps understand moisture and weather conditions.

5. Report Generation

A text report is automatically created which includes:

Key statistics
Explanation of each visualization
Final insights

This makes the project more complete and easy to present.

 How to Run the Project

Install required libraries:
pip install pandas matplotlib
Update the file path in the code:
file_path = "your_file_path/weather_data.csv"
Run the script:
python main.py
 Output

After running the project:

visualizations folder → contains all charts
report folder → contains detailed analysis report

 Key Insights

Temperature varies over time and does not remain constant
Different locations experience different climate conditions
Most temperature values fall into moderate ranges
Humidity levels fluctuate, indicating changing weather patterns


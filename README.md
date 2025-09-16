# python_week_seven_assignmentAnalyzing Data with Pandas and Visualizing Results with Matplotlib
**Assignment Overview**

This project demonstrates data analysis and visualization in Python using the pandas and matplotlib libraries.
The goal is to practice:

- Loading and cleaning datasets

- Performing basic statistical analysis

- Grouping and aggregating data

- Creating visualizations to discover insights

**Objectives**

- Load and Explore Data

- Import dataset in CSV (Iris dataset is used here).

- Inspect first few rows and dataset info.

- Handle missing values by filling or dropping.

- Basic Data Analysis

- Compute descriptive statistics (mean, median, std, etc.).

- Perform grouping by category (species) and calculate averages.

- Identify key patterns/observations.

**Data Visualization**

- Create at least four types of plots using matplotlib:

- Line Chart

- Bar Chart

- Histogram

- Scatter Plot

- Customize with titles, labels, and legends.

**Requirements**

- Make sure you have Python 3.x installed with the following libraries:

pip install pandas matplotlib seaborn

**How to Run**

- Clone or download this repository.

- Navigate to the project folder.

- Run the script:

python main.py

**Example Outputs**

- The script generates:

- Line chart showing petal length across samples

- Bar chart comparing average petal length per species

- Histogram showing sepal length distribution

- Scatter plot of sepal length vs. petal length

**Findings**

- The dataset contained no missing values (but cleaning logic is included).

- Iris-virginica has the longest average petal length.

- Sepal length distribution is roughly normal (5–7 cm common).

- Positive correlation observed between sepal length and petal length.

**Notes**

- You can replace the Iris dataset with any CSV file (e.g., sales or time-series data) by editing the pd.read_csv() line in the script.

- All visualizations open in pop-up windows; close them to proceed to the next plot
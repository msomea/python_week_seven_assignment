"""
Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib
Objective:
- Load and analyze a dataset with pandas
- Visualize the data with matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # only used to load Iris dataset easily

# Task 1: Load and Explore the Dataset


# Load the Iris dataset from seaborn (can be replaced with pd.read_csv("yourfile.csv"))
df = sns.load_dataset("iris")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Inspect data structure
print("Dataset Info:")
print(df.info(), "\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Clean the dataset (if any missing values, fill with column mean)
df = df.fillna(df.mean(numeric_only=True))


# Task 2: Basic Data Analysis

# Basic statistics
print("Basic Statistics:")
print(df.describe(), "\n")

# Grouping: Average petal length by species
grouped = df.groupby("species")["petal_length"].mean()
print("Average petal length by species:")
print(grouped, "\n")

# Observation (printed to console for assignment clarity)
print("Observation: Iris-virginica has the longest average petal length.\n")

# Task 3: Data Visualization

# 1. Line chart – simulate trend by plotting petal length across index
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["petal_length"], label="Petal Length")
plt.title("Line Chart: Petal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart – average petal length per species
plt.figure(figsize=(8, 5))
grouped.plot(kind="bar", color=["skyblue", "orange", "green"])
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram – distribution of sepal length
plt.figure(figsize=(8, 5))
plt.hist(df["sepal_length"], bins=15, color="purple", alpha=0.7)
plt.title("Histogram: Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot – sepal length vs. petal length
plt.figure(figsize=(8, 5))
plt.scatter(df["sepal_length"], df["petal_length"], c="red", alpha=0.6, label="Samples")
plt.title("Scatter Plot: Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()


# Findings/Observations

"""
1. The dataset has no missing values (but cleaning step is included if needed).
2. Iris-virginica species shows the highest petal length on average.
3. Sepal length distribution is roughly normal with most values between 5–7 cm.
4. Scatter plot reveals a positive correlation between sepal length and petal length.
"""

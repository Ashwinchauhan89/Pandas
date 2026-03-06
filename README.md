# 🐼 Pandas Cheat Sheet

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Level](https://img.shields.io/badge/Level-Beginner--Intermediate-green)

A quick reference guide for **Pandas**, the powerful Python library used for **data analysis, data manipulation, and data science workflows**.

---

# 📌 What is Pandas?

Pandas is an open-source Python library used for:

* Data analysis and manipulation
* Handling structured datasets
* Cleaning and transforming data
* Working with CSV, Excel, and databases
* Data preprocessing for machine learning

---

# ⚙️ Installation

Install Pandas using pip:

```bash
pip install pandas
```

Import Pandas:

```python
import pandas as pd
```

Check version:

```python
pd.__version__
```

---

# 📊 Core Data Structures

Pandas provides two main data structures.

### Series (1D data)

```python
import pandas as pd

data = pd.Series([10,20,30,40])
print(data)
```

### DataFrame (2D table)

```python
data = {
    "Name": ["Alice","Bob","Charlie"],
    "Age": [23,25,30]
}

df = pd.DataFrame(data)
print(df)
```

---

# 📥 Loading Data

### Read CSV

```python
df = pd.read_csv("data.csv")
```

### Read Excel

```python
df = pd.read_excel("data.xlsx")
```

### Read JSON

```python
df = pd.read_json("data.json")
```

---

# 📤 Export Data

Save data to CSV:

```python
df.to_csv("output.csv")
```

Save to Excel:

```python
df.to_excel("output.xlsx")
```

---

# 🔎 View Data

First rows

```python
df.head()
```

Last rows

```python
df.tail()
```

Dataset information

```python
df.info()
```

Statistical summary

```python
df.describe()
```

Columns list

```python
df.columns
```

Shape of dataset

```python
df.shape
```

---

# 🔍 Selecting Data

Select column

```python
df["Name"]
```

Multiple columns

```python
df[["Name","Age"]]
```

Select row using index

```python
df.loc[0]
```

Select using position

```python
df.iloc[0]
```

---

# 🎯 Filtering Data

Example:

```python
df[df["Age"] > 25]
```

Multiple conditions

```python
df[(df["Age"] > 20) & (df["Age"] < 30)]
```

---

# ✏️ Data Cleaning

Check missing values

```python
df.isnull()
```

Count missing values

```python
df.isnull().sum()
```

Drop missing values

```python
df.dropna()
```

Fill missing values

```python
df.fillna(0)
```

Remove duplicates

```python
df.drop_duplicates()
```

---

# 🔄 Data Transformation

Add new column

```python
df["Salary"] = [50000,60000,70000]
```

Rename columns

```python
df.rename(columns={"Age":"User_Age"})
```

Sort values

```python
df.sort_values("Age")
```

---

# 📊 GroupBy Operations

Group data

```python
df.groupby("Department").mean()
```

Example:

```python
df.groupby("Department")["Salary"].sum()
```

---

# 🔗 Merge DataFrames

Join datasets

```python
pd.merge(df1, df2, on="id")
```

Concatenate datasets

```python
pd.concat([df1, df2])
```

---

# 📈 Basic Data Analysis

Mean

```python
df["Age"].mean()
```

Maximum

```python
df["Age"].max()
```

Minimum

```python
df["Age"].min()
```

Value counts

```python
df["Department"].value_counts()
```

---

# 📊 Common Pandas Functions

| Function        | Purpose               |
| --------------- | --------------------- |
| `pd.read_csv()` | Load CSV file         |
| `df.head()`     | First rows            |
| `df.tail()`     | Last rows             |
| `df.info()`     | Dataset info          |
| `df.describe()` | Statistical summary   |
| `df.dropna()`   | Remove missing values |
| `df.fillna()`   | Fill missing values   |
| `df.groupby()`  | Group data            |
| `pd.merge()`    | Merge datasets        |

---

# 🚀 Quick Reference

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()
df.info()
df.describe()

df["column"]
df.loc[0]

df.dropna()
df.fillna(0)

df.groupby("column").mean()
```

---

# 📚 Use Cases

Pandas is widely used in:

* Data Science
* Machine Learning
* Data Analysis
* Business Analytics
* Financial Data Processing

Libraries commonly used with Pandas:

* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---



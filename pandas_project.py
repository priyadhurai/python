import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA
df = pd.read_csv("employee_data.csv", parse_dates=["JoinDate"])

print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

# 2. HANDLE MISSING VALUES
print("\n--- Missing Values Before ---")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Bonus"] = df["Bonus"].fillna(0)

print("\n--- Missing Values After ---")
print(df.isnull().sum())

# 3. SUMMARY STATISTICS
print("\n--- Summary Statistics ---")
print(df.describe())

# 4. FILTERING
print("\n--- Employees with Salary > 60000 ---")
print(df[df["Salary"] > 60000])

# 5. SORTING
print("\n--- Sorted by Salary Desc ---")
print(df.sort_values("Salary", ascending=False))

# 6. GROUPBY
print("\n--- Average Salary by Department ---")
print(df.groupby("Department")["Salary"].mean())

# 7. DATE COLUMN OPERATIONS
df["Join_Year"] = df["JoinDate"].dt.year
df["Join_Month"] = df["JoinDate"].dt.month

print("\n--- Added Year & Month Columns ---")
print(df.head())

# 8. SIMPLE VISUALIZATION
plt.figure()
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

plt.figure()
df["Salary"].plot(kind="hist")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.show()

# 9. EXPORT CLEANED DATA
df.to_csv("employee_data_cleaned.csv", index=False)
print("\nCleaned data exported to employee_data_cleaned.csv")

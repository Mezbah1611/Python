import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'C:\Users\Mezbah Uddin\Downloads\Compressed\test.csv')

# List of numerical columns to check for outliers
numerical_columns = ['battery_power', 'ram']

# IQR Outlier Detection
for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Outliers in {column} based on IQR:\n", outliers)

    # Box plot for visualization
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column} (IQR Method)')
    plt.xlabel(column)
    plt.show()

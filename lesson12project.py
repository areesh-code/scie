import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('FuelConsumption (3).csv')

# 1. Check for null values
null_check = df.isnull().sum()
print("Null values in each column:")
print(null_check)

# 2. Check dataset details (feature types)
print("\nData types of each feature:")
print(df.dtypes)

# 3. Create a new DataFrame with mean values grouped by Fuel Type
grouped_df = df.groupby('FUELTYPE')['CO2EMISSIONS'].mean().reset_index()
print("\nMean CO2 Emissions by Fuel Type:")
print(grouped_df)

# 4. Reset index (already done in the grouped DataFrame)

# 5. Create a barplot for Fuel Type and Average CO2 Emissions
plt.figure(figsize=(10, 6))
bars = plt.bar(grouped_df['FUELTYPE'], grouped_df['CO2EMISSIONS'], color='skyblue')

# 6. Annotate the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
             f'{height:.1f}',
             ha='center', va='bottom')

plt.xlabel('Fuel Type')
plt.ylabel('Average CO2 Emissions')
plt.title('Average CO2 Emissions by Fuel Type')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\User\Downloads\scottish_hills.csv"
df = pd.read_csv(file_path)

print(df.head())

print(df.info())
print(df.describe())

sns.set(style='whitegrid')

# Plot 1: Histogram of height
plt.figure(figsize=(10, 6))
sns.histplot(df['Height'], kde=False, bins=30, color='blue')
plt.title('Distribution of Heights')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()

# Plot 2: Frequency polygon of height
plt.figure(figsize=(10, 6))
sns.histplot(df['Height'], kde=True, bins=30, color='blue', stat='density')
plt.title('Frequency Polygon of Heights')
plt.xlabel('Height')
plt.ylabel('Density')
plt.show()

# Plot 3: Histogram of Latitude
plt.figure(figsize=(10, 6))
sns.histplot(df['Latitude'], kde=False, bins=30, color='green')
plt.title('Distribution of Latitude')
plt.xlabel('Latitude')
plt.ylabel('Frequency')
plt.show()

# Plot 4: Frequency polygon of Latitude
plt.figure(figsize=(10, 6))
sns.histplot(df['Latitude'], kde=True, bins=30, color='green', stat='density')
plt.title('Frequency Polygon of Latitude')
plt.xlabel('Latitude')
plt.ylabel('Density')
plt.show()
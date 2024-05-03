import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Dataset\main Dataset.csv")

# Extract the necessary columns
gender_data = data["Indicator Name"]

# Count the occurrences of each gender
gender_counts = gender_data.value_counts()

# Create a bar chart to visualize the distribution
plt.figure(figsize=(10, 6))
gender_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Create a bar chart to visualize the distribution of countries
data['Country Name'].value_counts().plot(kind='pie')
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Distribution of Countries')
plt.show()
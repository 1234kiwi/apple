'''Finding Relationships Among Variables:  
3.a. Use a dataset with multiple variables 
and perform correlation analysis to 
determine the strength and direction of relationships between 
pairs of variables. '''

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv("advertising_sales Pract3.csv")


# Step 3: Display Dataset
print("Display Dataset : head")
print(df.head())


# Step 4: Check Dataset Information
print("Check Dataset Information")
print(df.info())


# Step 5: Calculate Correlation Matrix
correlation = df[['TV_Advertising',
                  'Radio_Advertising',
                  'Newspaper_Advertising',
                  'Sales_Revenue']].corr()

print(correlation.to_string())


# Step 6: Display Correlation Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(correlation,
            annot=True,
            cmap="coolwarm",
            linewidths=0.5)

plt.title("Correlation Matrix")

plt.show()

# Step 7: Scatter Plot (TV Advertising vs Sales Revenue)
plt.figure(figsize=(7,5))

sns.scatterplot(data=df,
                x="TV_Advertising",
                y="Sales_Revenue")

plt.title("TV Advertising vs Sales Revenue")

plt.show()


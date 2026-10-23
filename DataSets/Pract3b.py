'''3.b Apply regression analysis to identify the relationship between an independent 
variable (e.g., advertising expenditure) and a dependent variable (e.g., sales 
revenue). '''

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Step 2: Load Dataset
df = pd.read_csv("advertising_sales Pract3.csv")


# Step 3: Display Dataset
print("Display Dataset : head")
print(df.head())


# Step 4: Check Dataset Information
print("Check Dataset Information")
print(df.info())

# Step 2: Define Independent and Dependent Variables
X = df[['TV_Advertising']]

y = df['Sales_Revenue']

# Step 3: Train the Regression Model
model = LinearRegression()

model.fit(X, y)

# Step 4: Display Regression Equation
print("Intercept :", model.intercept_)

print("Slope :", model.coef_[0])
'''Interpretation
•	Intercept: Estimated sales revenue when TV advertising expenditure is zero. 
•	Slope: Increase in sales revenue for every additional ₹1 spent on TV advertising. '''


# Step 5: Predict Sales Revenue
predicted_sales = model.predict(X)

print(predicted_sales)

# Step 6: Calculate R² Score
r2 = model.score(X, y)

print("R² Score :", r2)
'''Interpretation
R² close to 1 indicates that TV advertising explains most of the variation in sales revenue. 
R² close to 0 indicates a weak predictive model. '''


# Step 7: Plot Regression Line
plt.figure(figsize=(8,5))

plt.scatter(X, y, color='blue')

plt.plot(X,
         predicted_sales,
         color='red',
         linewidth=2)

plt.xlabel("TV Advertising (₹)")

plt.ylabel("Sales Revenue (₹)")

plt.title("Linear Regression: TV Advertising vs Sales Revenue")

plt.show()

# Step 8: Predict Future Sales
# Predict sales if the company spends ₹50,000 on TV advertising.
future = [[50000]]

prediction = model.predict(future)

print("Predicted Sales Revenue =", prediction)

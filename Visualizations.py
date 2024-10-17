import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Other', 'Female', 'Male', 'Female', 'Male', 'Other'],
    'Age': [25, 34, 28, 40, 22, 33, 27, 45, 23, 38],
    'PurchaseAmount': [200, 150, 300, 400, 100, 350, 250, 450, 200, 500],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing']
}
df = pd.DataFrame(data)

sns.set(style="whitegrid")

plt.figure(figsize=(8,6))
sns.countplot(x='ProductCategory', data=df, hue='ProductCategory', palette='Set2', legend=False)
plt.title('Number of Purchases by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Count of Purchases')
plt.show()

gender_distribution = df['Gender'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', colors=sns.color_palette('Set3'))
plt.title('Customer Gender Distribution')
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x='Age', y='PurchaseAmount', data=df, hue='Gender', palette='Set1', s=100)
plt.title('Customer Spending Across Different Age Groups')
plt.xlabel('Age')
plt.ylabel('Purchase Amount')
plt.show()


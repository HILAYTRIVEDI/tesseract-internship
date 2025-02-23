import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset with categorical columns
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'HR', 'IT', 'Sales', 
                   'HR', 'IT', 'Sales', 'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.countplot(x=df['Department'], palette='coolwarm')
plt.title("Department Distribution")

plt.subplot(1, 2, 2)
sns.countplot(x=df['Gender'], palette='coolwarm')
plt.title("Gender Distribution")

# Show the plots
plt.tight_layout()
plt.show()

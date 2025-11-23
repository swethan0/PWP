import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize data
data = {
    'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
    'Age': [30, 21, 29, 28]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create boxplot for Age
sns.boxplot(x=df['Age'])

# Show the plot
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()

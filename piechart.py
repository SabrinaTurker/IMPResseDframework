import pandas as pd
import matplotlib.pyplot as plt

# Load your DataFrame (replace 'your_file.csv' with the actual file path)
df = pd.read_csv('datasets/Production/Production_trunc23.csv')

# Assuming 'Part_Desc_' is a column in your DataFrame
plt.pie(df['Part_Desc_'].value_counts(), labels=df['Part_Desc_'].unique(), autopct='%1.1f%%')
plt.title('Pie Chart of Part Descriptions')
plt.show()

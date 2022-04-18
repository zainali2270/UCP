import pandas as pd
import numpy as np
df = pd.read_csv('jsrt_metadata.csv')
# Task 1
plt.pyplot.hist(df['diagnosis'].value_counts())

# Task 2
plt.pyplot.pie(df['state'].value_counts())

#Task3
plt.pyplot.pie(df['gender'].value_counts())

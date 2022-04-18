import pandas as pd
import numpy as np
df = pd.read_csv('jsrt_metadata.csv')
# Task 1
plt.pyplot.hist(df['state'])

#Task3

plt.pyplot.pie(dff['gender'].value_counts())

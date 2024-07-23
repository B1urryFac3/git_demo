# This is a sample pyhton script for Git demo

import umpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("file.csv")
df.head(5)

plt.plot(df['col1'], df['col2'])

print("Plot successful!")


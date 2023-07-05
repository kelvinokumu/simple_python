import numpy as np

dataset = [70, 75, 80, 85, 90]
q1 = np.percentile(dataset, 25)
q3 = np.percentile(dataset, 75)
iqr = q3 - q1
print("Interquartile Range:", iqr)

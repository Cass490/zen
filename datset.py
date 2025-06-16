import numpy as np
import pandas as pd

filename = "santafe_laser.npy"
output_csv_file = 'laser_train.csv'
data= np.load(filename)
if data.ndim >1:
  print(f"Warning: Input data has {data.ndim} dimensions. Flattening to a single time series.")
  data=data.flatten()
df= pd.DataFrame(data, columns=["values"])
df.to_csv(output_csv_file, index=False, header=False)
print(f"Successfully created '{output_csv_file}' with {len(data)} rows.")


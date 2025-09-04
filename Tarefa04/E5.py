import pandas as pd
import numpy as np

CSV_URL = "https://raw.githubusercontent.com/emmendorfer/idwr/main/demo/datasets/amazon.csv"

def pd_to_np(CSV_URL):
    df = pd.read_csv(CSV_URL)
    numpy_array = df.to_numpy()
    return numpy_array

data = pd_to_np(CSV_URL)

print(data)
from pandas import read_parquet
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os
import numpy as np
from PIL import Image
from io import BytesIO

data = read_parquet('./train-00001-of-00013.parquet')
keys = data.keys()
print(keys)
print(len(data['image']))
print(data.head())
img = Image.open(BytesIO(data['image'][2]['bytes']))
img.show()
print(data['conversations'][2])


# data = pd.read_parquet('./train-00000-of-00013.parquet')
# keys = data.keys()
# print(keys)


# data = pq.read_table('./train-00000-of-00013.parquet')
# print(data)
# print(data.to_pandas())
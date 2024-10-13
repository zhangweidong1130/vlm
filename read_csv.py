from pandas import read_parquet
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os
import numpy as np
from PIL import Image
from io import BytesIO

import requests


# data = pd.read_csv(r'E:\\zwd_code\\vlm_data\\wukong_release\\wukong_test.csv')
# test_imgs_path = "E:\\zwd_code\\vlm_data\\wukong_release\\wukong_test"
# keys = data.keys()
# print(keys)
# img_name_lst = data['dir']
# img_path_lst = data['url']
# caption_lst = data['text']
# for img_name, img_path, caption in zip(img_name_lst, img_path_lst, caption_lst):
#     try:
#         response = requests.get(img_path)
#         pil_image = Image.open(BytesIO(response.content)).convert('RGB')
#         #pil_image.show()
#         #print(os.path.join(test_imgs_path,img_name))
#         pil_image.save(os.path.join(test_imgs_path,img_name))
#         #break
#     except:
#         print(img_name, '   ', img_path)

path = 'E:\\zwd_code\\vlm_data\\wukong_release\\wukong_release\\'
lst = os.listdir(path)
count = 0
for i in lst:
    data = pd.read_csv(path + i)
    img_path_lst = data['url']
    caption_lst = data['caption']
    print('img num: ', len(img_path_lst), len(caption_lst))
    count += len(img_path_lst)

print('Wukong img num: ', count)
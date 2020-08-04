import os
import numpy as np
import pandas as pd
from PIL import Image

train = pd.read_csv('CheXpert-v1.0-small/train.csv')
val = pd.read_csv('CheXpert-v1.0-small/valid.csv')

for img_path in train['Path']:
    print(img_path)
    img = Image.open(img_path)
    img = img.resize((224, 224))
    save_path = 'CheXpert-resized_1channel/' + (img_path.partition("/")[2]).rpartition("/")[0]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img.save('CheXpert-resized_1channel/' + img_path.partition("/")[2], format='jpeg')
    
for img_path in val['Path']:
    print(img_path)
    img = Image.open(img_path)
    img = img.resize((224, 224))
    save_path = 'CheXpert-resized_1channel/' + (img_path.partition("/")[2]).rpartition("/")[0]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img.save('CheXpert-resized_1channel/' + img_path.partition("/")[2], format='jpeg')
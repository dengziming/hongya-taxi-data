# coding: utf-8

# - Taxi data analyze




# In[1]:


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# ## Data exploration

# In[2]:

from os import listdir

data = list()
count = 0
for line in open("/Users/dengziming/Downloads/green_tripdata_2016-01.csv"):

    split = line.split(",")
    if len(split) >= 5 and count > 0:
        data.append(int(split[4]))
    count += 1

num_bins = 3

# 得到对象
fig, ax = plt.subplots()

# 柱状图
n, bins, patches = ax.hist(data)


# 横坐标
ax.set_xlabel('vendor_id')
# 纵坐标
ax.set_ylabel('amount')
# 标题
ax.set_title(r'Histogram of rate_code')

# 调整间距
fig.tight_layout()
# 展示
plt.show()

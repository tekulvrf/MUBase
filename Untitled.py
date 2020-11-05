#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df = pd.read_csv("Miami_Pitching_Heatmap_Data.csv")
hm_data = df.pivot("Pitcher","Zone","BAA")
hm_data.dtypes


# In[9]:


fig, ax = plt.subplots(figsize=(9, 6))

sns.heatmap(hm_data,annot=True,fmt="d",cmap='BuPu',ax=ax,linewidths=2.5)
ax.set_title("Heatmap of Slash Lines By Zone")


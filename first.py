#!/usr/bin/env python
# coding: utf-8

# ## Seaborn이란?
# * Python에서 통계 그래픽을 만들기 위한 라이브러리.
# 

# In[1]:


# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)


# In[2]:


dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)


# In[ ]:





# In[ ]:





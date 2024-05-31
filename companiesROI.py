#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# ###### Load the dataset from an Excel file
# 
# 

# In[16]:


df = pd.read_csv("companies.csv")
df


# ###### Calculate the ROI for each campaign
# 
# 
# 

# In[18]:


df['ROI'] = ((df['Revenue'] - df['Spent']) / df['Spent']) * 100
df['ROI']


# ###### Calculate the average ROI for all campaigns
# 
# 

# In[20]:


average_roi = df['ROI'].mean()

average_roi


# ###### Identify the campaign with the highest ROI
# 
# 

# In[22]:


highest_roi_campaign = df.loc[df['ROI'].idxmax()]

highest_roi_campaign


# ###### Visualize the ROI distribution (Optional)
# 
# 

# In[23]:


import matplotlib.pyplot as plt


# In[24]:




plt.figure(figsize=(10,6))
plt.hist(df['ROI'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('ROI Distribution')
plt.xlabel('ROI (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# ###### Print results
# 
# 

# In[25]:


print("Average ROI for all campaigns:", average_roi)
print("Campaign with the highest ROI:")
print(highest_roi_campaign)


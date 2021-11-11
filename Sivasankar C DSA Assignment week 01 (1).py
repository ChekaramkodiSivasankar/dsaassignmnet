#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


data=pd.read_excel(r'C:\Users\sivae\OneDrive\Desktop\iris (1).xls')
data


# In[6]:


data=pd.DataFrame(data)
data


# In[7]:


mean=np.mean(data['SL'])


# In[8]:


mean


# In[9]:


mean1=np.mean(data['SW'])
mean1


# In[10]:


mean2=np.mean(data['PL'])
mean2


# In[11]:


mean3=np.mean(data['PW'])
mean3


# In[16]:


data1 = data.isna()
data1


# In[19]:


data=pd.readdata=pd.read_excel(r'C:\Users\sivae\OneDrive\Desktop\iris (1).xls')
data


# In[20]:


fig, axes = plt.subplots(figsize=(16,9))
sns.boxplot(y='SL', x= 'Classification',data=data)
plt.show()


# In[21]:


fig, axes = plt.subplots(figsize=(16,9))
sns.boxplot(y='SW', x= 'Classification',data=data)
plt.show()


# In[22]:


fig, axes = plt.subplots(figsize=(16,9))
sns.boxplot(y='PL', x= 'Classification',data=data)
plt.show()


# In[23]:


fig, axes = plt.subplots(figsize=(16,9))
sns.boxplot(y='PW', x= 'Classification',data=data)
plt.show()


# In[37]:


plt.figure(figsize=(16,9))
sns.scatterplot(data['PL'],data['PW'],hue=data['Classification'],data=data)
plt.title('PL and PW',fontsize=16)
plt.show()
print('* Iris-setosa have less PL and PW, Where Iris-virgina have high PW and PL')


# In[36]:


plt.figure(figsize=(10,11))
sns.heatmap(data.corr(),annot=True)
plt.xticks(rotation=90,fontsize=16)
plt.yticks(fontsize=16)
plt.show()

print ('*SL and SW are sligtly correaleted')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Analysis on Google PlayStore Apps

Analyzing the Apps found on Google Playstore to gain an insight into the present Android Market. Pandas, NumPy are the libraries used here.


# In[3]:


# Imports
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


# Loading the dataset as a pandas data frame.

# In[4]:


googlestore_df =  pd.read_csv('googleplaystore.csv')


# In[5]:


rows = googlestore_df.shape[0]
column = googlestore_df.shape[1]


# In[6]:


print('There are {} Rows and {} Columns in the dataset'.format(rows, column))


# For the structure and the manner in which the data is organized.

# In[7]:


googlestore_df.head(10)


# In[8]:


googlestore_df.info()


# To know if there is any missing value or Nan value in the dataset, we can use the isnull() function.

# In[9]:


googlestore_df.isnull().sum()


# For information about the different attributes of the dataset, also there is one more valid point in defining a function which it will be reusable.

# In[10]:


def printinfo():
    temp = pd.DataFrame(index=googlestore_df.columns)
    temp['data_type'] = googlestore_df.dtypes
    temp['null_count'] = googlestore_df.isnull().sum()
    temp['unique_count'] = googlestore_df.nunique()
    return temp


# To see the missing number of values of any attribute, its unique count, and its respective data types. So called the function. 

# In[12]:


printinfo()


# For data cleaning. Displaying column Type 

# In[13]:


googlestore_df[googlestore_df.Type.isnull()]


# Since there is only one missing value in this column, So filled the missing value with free .

# In[14]:


googlestore_df['Type'].fillna("Free", inplace = True)


# For checking if that has been correctly placed.

# In[38]:


googlestore_df[googlestore_df['Content Rating'].isnull()]


# For Content Rating column

# Row 10472 has missing data for the Category column and all the prevailing column values are being replaced with its previous column. 

# In[39]:


googlestore_df.loc[10468:10477, :]


# In[40]:


googlestore_df.dropna(subset = ['Content Rating'], inplace=True)


# There are some of the unwanted columns which will be of not much use in the analysis process. So drop those columns.

# In[41]:


googlestore_df.drop(['Current Ver','Last Updated', 'Android Ver'], axis=1, inplace=True)


# In[42]:


googlestore_df


# The Rating column contains a total of 1474 of missing values.So replacing the missing values with the Mode value of that entire column.

# In[45]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# For defining our x and y axis and plotting graph.

# In[46]:


y = googlestore_df['Category'].value_counts().index
x = googlestore_df['Category'].value_counts()
xsis = []
ysis = []
for i in range(len(x)):
    xsis.append(x[i])
    ysis.append(y[i])


# In[47]:


plt.figure(figsize=(18,13))
plt.xlabel("Count")
plt.ylabel("Category")

graph = sns.barplot(x = xsis, y = ysis, palette= "husl")
graph.set_title("Top categories on Google Playstore", fontsize = 25);


# there are all total of 33 categories in the dataset from the above output we can come to the conclusion that in the play store most of the apps are under Family & Game category and least are of Beauty & Comics Category.

# In[48]:


plt.figure(figsize=(10,10))
labels = googlestore_df['Type'].value_counts(sort = True).index
sizes = googlestore_df['Type'].value_counts(sort = True)
colors = ["blue","lightgreen"]
explode = (0.2,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.title('Percent of Free Vs Paid Apps in store',size = 20)
plt.show()


# From the above graph,  92%(Approx.) of apps in the google play store are free and 8%(Approx.) are paid.

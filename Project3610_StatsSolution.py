#!/usr/bin/env python
# coding: utf-8

# # Importing the dataset

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('car_prices.csv')


# # Learning the dataset

# In[3]:


df.head(3)


# In[4]:


df.info()


# In[5]:


#df['year'].value_counts()
df['make'].value_counts()


# In[6]:


df['body'].value_counts()


# In[7]:


df['state'].value_counts()


# In[8]:


df['transmission'].value_counts()


# In[9]:


df['sellingprice'].value_counts()


# In[10]:


df['mmr'].value_counts()


# #### Here we can see that there are values in the "transmission" column which do not make sense; a sedan is a the body of the vehicle and can be either manual or automatic. Considering that the dataset is so large we can afford to drop those rows with an incorrect value for the "transmission" column. There are still rows with empty cells so part of the preprocessing would be to populate those cells with null values and then remove later. 
# 
# #### Here we see that some values in the "state" column are out of place, we can remove those rows. 

# # Data Preprocessing 

# #### Firstly, we remove all the column which we are not using in the dataset. These include: model,trim , vin, condition, odometer, color , interior and saledate .

# In[11]:


#code
df.drop('model', axis=1, inplace=True)
df.drop('trim', axis=1,inplace=True)
df.drop('vin', axis=1,inplace=True)
df.drop('condition', axis=1,inplace=True)
df.drop('odometer', axis=1,inplace=True)
df.drop('color', axis=1,inplace=True)
df.drop('interior', axis=1,inplace=True)


# In[12]:


df.info()


# #### Secondly , we clean the 'Transmission' column by removing the values 'sedan' and 'Sedan', then we will remove all the rows with null values in the column.

# In[17]:


#code
df.drop(df.loc[df['transmission']=="sedan"].index, inplace=True)
df.drop(df.loc[df['transmission']=="Sedan"].index, inplace=True)


# #### Thirdly, we clean the 'body', 'sellingprice',  'mmr' and 'transmission' column by removing all the null values

# In[33]:


#code
df.dropna()


# #### Then we clean the 'state' column by removing the rows which have nonsensical values.

# In[34]:


#code 
df['state'].unique()


# usa: ALABAMA -AL
# ALASKA 	-AK
# ARIZONA -AZ
# CALIFORNIA -CA
# COLORADO -CO
# FLORIDA -FL
# GEORGIA -GA
# HAWAII- HI
# ILLINOIS -IL
# INDIANA -IN
# LOUISIANA -LA
# MARYLAND -MD
# MASSACHUSETTS -MA
# MICHIGAN -MI
# MINNESOTA -MN
# MISSISSIPPI -MS
# MISSOURI -MO
# NEVADA -NV
# NEW JERSEY -NJ
# NEW MEXICO -NM
# NEW YORK -NY
# NORTH CAROLINA -NC
# OHIO -OH
# OKLAHOMA -OK
# OREGON -OR
# PENNSYLVANIA -PA
# PUERTO RICO-PR 
# SOUTH CAROLINA -SC
# TENNESSEE -TN
# TEXAS -TX
# UTAH- UT
# VIRGINIA -VA
# WASHINGTON -WA
# WISCONSIN -WI
# 
# canada: QUEBEC-QC, ALBERTA-AB, ONTARIO-ON

# In[44]:


df.loc[df['state'] == "on"]


# In[47]:


#df.loc[df['state'] == "ab", 'state'] = "mn"
#df.drop(df['state'] == "ne", inplace=True)


# In[42]:


df['state'].value_counts()


# In[ ]:





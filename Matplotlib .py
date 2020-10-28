#!/usr/bin/env python
# coding: utf-8

# ## Observations and Insights 

# In[ ]:





# 

# In[4]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset

# Display the data table for preview



# In[31]:


import matplotlib. pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x = list(range)0,10
y = list(range)- 10, 0

plt.plot(x,y)


# In[ ]:





# In[ ]:





# In[16]:


import pandas as pd
dataframe ={'key1':[1,2,5,1,2,7,2,2],'key2':[2,2,1,2,2,5,2,3],'data':[5,4,2,5,1,6,2,7]}


# In[15]:


import pandas as pd
df = pd.DataFrame({'Name' : ['don','jim','adam','yusuf','joeph','jamal','Gary'], 'Age' : [25,32,37,43,45,56,37],  'Zone' : ['East','West','North','South','East','West','North']})


# In[22]:


Diabete.Head()


# ## Summary Statistics

# In[7]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.


# In[8]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Using the aggregation method, produce the same summary statistics in a single line


# ## Bar and Pie Charts

# In[25]:


# Generate a bar plot showing the total number of unique mice tested on each drug regimen using pandas.
Dataframe=pd.read_cvsindex_col=1


# In[33]:


company=[`gobal`,AMZN,`MSFT,`FB`
revenue= [95,100,200,]


# In[34]:


# Generate a pie plot showing the distribution of female versus male mice using pandas


# In[12]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot


# ## Quartiles, Outliers and Boxplots

# In[13]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

# Start by getting the last (greatest) timepoint for each mouse


# Merge this group df with the original dataframe to get the tumor volume at the last timepoint


# In[14]:


# Put treatments into a list for for loop (and later for plot labels)


# Create empty list to fill with tumor vol data (for plotting)


# Calculate the IQR and quantitatively determine if there are any potential outliers. 

    
    # Locate the rows which contain mice on each drug and get the tumor volumes
    
    
    # add subset 
    
    
    # Determine outliers using upper and lower bounds
    


# In[15]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin


# In[17]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO
import numpy as np
temp_sequences = []
for record in SeqIO.parse("/home/samridhi/boatgang/sequences.fa", "fasta"):
    temp_sequences.append(str(record.seq))


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("/home/samridhi/boatgang/labels.txt", sep="\t")


# In[4]:


print temp_sequences[0]
print type(temp_sequences[0])


# In[5]:


temp_target = df['task1']


# In[6]:


print temp_sequences[0]


# In[7]:


dict_i = {"A" : 0, "C": 1, "G": 2, "T" : 3}


# In[8]:


def one_hot_encode(s):
    i=0
    ohe = np.zeros((len(s), 4))
    for k in s:
        ohe[i,dict_i[k]] = 1
        i+=1
    return ohe


# In[9]:


ohe_sequences = np.array([one_hot_encode(s) for s in temp_sequences])
ohe_sequences.shape


# In[10]:


from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(ohe_sequences, temp_target, test_size = 0.25, random_state = 42, shuffle=True)


# In[11]:


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv1D
from keras.layers import MaxPooling1D
from keras.layers import Dropout,Flatten
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


# In[12]:


model = Sequential()
model.add(Conv1D(filters=40, kernel_size=12, activation='relu', input_shape=(200,4)))
model.summary()


# In[13]:


model.add(MaxPooling1D(pool_size=189, strides=1))


# In[14]:


model.add(Dense(200,  activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())


# In[15]:


model.add(Dense(1, activation = "sigmoid"))


# In[16]:


model.summary()


# In[17]:


model.compile(loss='binary_crossentropy', optimizer='Adam',metrics=['accuracy'])


# In[ ]:


model.fit(train_x, train_y, epochs=10, verbose=1)


# In[ ]:


scores = model.evaluate(test_x, test_y)
print ("Test loss ", scores[0])
print ("Test acc ", scores[1])


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[51]:


import speech_recognition as sr
import warnings;warnings.simplefilter("ignore")



filename = (r"C:\Users\sruja\Desktop\dummy\task_data\wavs\speakers\2BqVo8kVB2Skwgyb\1da8c750-447a-11e9-a9a5-5dbec3b8816a.wav")
r=sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data=r.record(source)
    t=r.recognize_google(audio_data)
    print(t)

import pandas as pd
df=pd.read_csv(r"C:\Users\sruja\Desktop\dummy\task_data\data.csv")

df.head()

import pandas as pd
df1=pd.read_csv(r"C:\Users\sruja\Desktop\dummy\task_data\test.csv")
df1.head()










# In[ ]:





# In[49]:





# In[43]:





# In[44]:





# In[ ]:





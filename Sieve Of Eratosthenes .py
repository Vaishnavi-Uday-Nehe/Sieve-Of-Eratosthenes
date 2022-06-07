#!/usr/bin/env python
# coding: utf-8

# In[87]:


val1 = int(input("enter your first value:"))
val2 = int(input("enter your second value:"))
#take user input

for i in range(val1,val2): # put those values in range 
    if i > 1: #check the values greater than 1
        for j in range(2,i): #start nother range from 2 upto the high limit i.e val2
            if i % j == 0: #regular formula for prime number
                break
        else:
            print(i)
            
#CodeByVaishnaviUdayNehe


# In[ ]:





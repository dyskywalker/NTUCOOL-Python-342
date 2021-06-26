#!/usr/bin/env python
# coding: utf-8

# In[1]:


file = open('stores_old.csv', 'r', encoding='big5')
file2 = open('stores_new.csv', 'w', encoding='big5') 
for line in file.readlines():
    d = line.split(',')
    print(f"{d[0]},{d[3]},{d[5]},{d[6]}")
    file2.write(f"{d[0]},{d[3]},{d[5]},{d[6]}\n")

file.close()
file2.close()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input("enter the size of pattern"))

for i in range(n):
    print("*"* i,""*(n-i))
for i in range(n,0,-1):
    print("*"* i,""*(n-i))


# In[4]:


a=input("enter any word' ")
print(a[::-1])


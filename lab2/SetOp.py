#!/usr/bin/env python
# coding: utf-8

# In[1]:


#a)
def add(x,y):
    x.add(y)
    return x


# In[2]:


#b)
def remove(x,y):
    x.discard(y)
    return x


# In[3]:


#c)
def union(x,y):
    return x.union(y)


# In[4]:


def intersection(x,y):
    return x.intersection(y)


# In[5]:


#d)
def diff(s1,s2):
    return s1.difference(s2)


# In[1]:


#e)
def subset_check(s1,s2):
    return s1.issubset(s2)


# In[2]:


#f)
def length(s1):
    temp=0
    for i in s1:
        temp+=1
    return temp


# In[3]:


#g)
def sym_diff(s1,s2):
    return s1.symmetric_difference(s2)


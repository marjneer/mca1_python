#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a)
def merging_Dict(*args):
    merged={}
    for i in args:
        merged.update(i)
    return merged


# In[2]:


def common(*args):
    common_keys=[args[0].keys()]
    for i in args[1:]:
        common_keys=common_keys& i.keys()
    return common_keys


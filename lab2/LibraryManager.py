#!/usr/bin/env python
# coding: utf-8

# In[1]:


library={}
def add(isbn,title,author,publisher,volume,year,topic):
    library[isbn] = {'title': title,'author': author,'publisher': publisher,'volume': volume,'year': year,'topic': topic}
    


# In[2]:


def remove(isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Book not found")


# In[3]:


def retrieve(isbn):
    return library.get(isbn)


# In[4]:


def search(word):
    x=[]
    for isbn, details in library.items():
        if word.lower() in details['title'].lower() or word.lower() in details['author'].lower():
            x.append((isbn, details))
    return x


# In[5]:


def all():
    return library


# In[6]:


def check(isbn):
    return library[isbn]


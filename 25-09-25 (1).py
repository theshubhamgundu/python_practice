#!/usr/bin/env python
# coding: utf-8

# In[5]:


r = float(input("Enter radius: "))
a = 3.14 * r * r
print("Area:", a)


# In[13]:


s = input()
v = "aeiouAEIOU"
c = 0
for char in s:
    if char in v:
        c+= 1
print(c)


# In[16]:


s = input()
v = "aeiouAEIOU"
c = 0
con=0
for char in s:
    if char in v:
        c+= 1
    else:
        con+=1
        
print(c)
print(con)


# In[18]:


n = [30,42,56,70,45,35]
for i in range(len(n)):
    if n[i] % 5 == 0:
        n[i] -= 5
print(n)


# In[20]:


n = list(map(int, input().split()))
for i in range(len(n)):
    if n[i] % 5 == 0:
        n[i] -= 5
print(n)


# In[6]:


n = list(map(int, input().split()))
e = []
o = []
for i, num in enumerate(n):
    if i % 2 == 0:
        e.append(num)
    else:
        o.append(num)
print(e)
print(o)


# In[11]:


n = list(map(int, input().split()))
se = 0  
so = 0  
for i, num in enumerate(n):
    if i % 2 == 0:
        se += num
    else:
        so += num

print(se)
print(so)


# In[14]:


n = list(map(int, input().split()))

e = 0
o = 0

for i, num in enumerate(n):
    if num % 2 == 0:   # check value parity
        e += i
    else:
        o += i

print("even =", e)
print("odd =", o)


# In[16]:


n = list(map(int, input().split()))

e = 0
o = 0

for i in range(len(n)):     
    if n[i] % 2 == 0:       
        e += i
    else:
        o += i

print("even =", e)
print("odd =", o)


# In[20]:


li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar","Danish"]
a=[]
for i in li:
    if i[0]=="D" or i[0]=="d":
        a.append(i)
print(a)


# In[8]:


a = {'Mumbai': 50, 'Hyd': 40, 'delhi': 30, 'Dubai': 20, 'Jaipur': 100, 'Kolkata': 250, 'Dadar': 200, 'chenn': 280}
b = []

for city, value in a.items():
    if value < 100:
        b.append(city)

print(b)


# In[ ]:





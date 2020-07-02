#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math

# return all primes less than n
#faster but more space
def func1(n):
    #results[i]=1 ->i is prime
    results = [1]*(n+1)
    for i in range(2, round(math.sqrt(n))):
        # find all not primes, not neccessarily loop through all numbers
        """
        # if it is not prime, skip to the next i
        # if not, more operations, ie.i=2, set results[8]=0 but i=4, also operate it
        if results[i] == 0:
            continue
        #multiple->more time
        for j in range(2, n):
            cur_num = i*j
            if cur_num >n:
                break
            if result[cur_num] == 1:
                #cur_num hasn't been visited
                result[cur_num] == 0 #not prime
        """
        # if it is not prime, skip to the next i
        # if not, more operations, ie.i=2, set results[8]=0 but i=4, also operate it
        if results[i] == 0:
            continue
        #replace multiple with add
        cur_num = i #2*i
        while cur_num < n:
            results[cur_num] = 0
            cur_num += i
        
    return results

#slower
def func2(n):
    #list of primes
    list_primes = [2]
    for i in range(3, n):
        #check each number i
        for j in range(2,i):#factor should >=2, so i>=3
            #if i%j == 0-> not prime, skip to the next i
            if i%j == 0:
                break
            #have checked all possible factors
            #i->prime, skip to the next i
            if j*j > i:
                list_primes.append(i)
                break
    return list_primes[::]
        
func2(1000)


# In[ ]:





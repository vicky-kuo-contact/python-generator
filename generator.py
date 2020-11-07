#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
split the array by the assgined length
"""
def split(arr, size):
    arrs = []
    while len(arr) > size:
        piece = arr[:size]
        arrs.append(piece)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

arr = [0,1,2,3,4,5,6,7,8,9]
size = 7
split(arr,size)

def split2(arr, size):
     l = [arr[size*(row-1):size*row] for row in range(1,len(arr)//size+1)]
     print(l)
     if len(arr)%size != 0:
            l.append(arr[len(arr)//size*size:])
            print(l)

split2(arr,size)


# In[9]:


"""
filter dictionary 
"""
stock = {
    "Apple":655.95, "IBM": 202.13, "HP":45.51, "Facebook": 12.11, 
    "Intel": 40.51, "Atmel": 10.23, "Amazon": 305.35, "Google":535.81
}

d = dict((k, v) for k, v in stock.items() if v >= 100)
d


# In[1]:


"""
check if the sentence is spelled the same forward and backward
"""
def palin(s):
    l, h = 0, len(s) - 1 #l:left, h:right
    
    # Lowercase string 
    s = s.lower() 
    
    # Compares character until they are equal 
    while (l <= h): 
    
        # If there is another symbol in left of sentence 
        if (not(s[l] >= 'a' and s[l] <= 'z')): 
            l += 1
            
    
        # If there is another symbol in right of sentence 
        elif (not(s[h] >= 'a' and s[h] <= 'z')): 
            h -= 1
           
    
        # If characters are equal 
        elif (s[l] == s[h]): 
            l += 1
            h -= 1
          
        # If characters are not equal then 
        # sentence is not palindrome 
        else: 
            return False
    # Returns true if sentence is palindrome 
    return True

palin("Race car")    


# In[2]:


""" Generate an infinite sequence of prime numbers.
"""

def gen_primes():
  
   
   D = {}
   
   q = 2
   
   while True:
       if q not in D: #prime number
           yield q
           D[q * q] = [q]
       else: #composite number
           for p in D[q]:
               D.setdefault(p + q, []).append(p)
           del D[q]
       
       q += 1

for item in gen_primes():
   print(item)


# In[5]:


"""
hamming distance with generator and map
"""
w=['ground', 'joint']
c=['gnoufd', 'johnt']

def hamming_distance(s1, s2):
    if len(s1)==len(s2):
        return sum(x1 != x2 for x1, x2 in zip(s1, s2))
    
diff = map(hamming_distance, w, c)
print (sum(diff))


# In[52]:


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
r = infinite_sequence()
next(r)
next(r)


# 


# coding: utf-8

# In[2]:


#Algo used: Randomly select Alpha from group of 100 prisoners.
#Assign the net count to 0.
#Initial State of the Bulb is assumed to be OFF - 0
#When Alpha enters the room and finds bulb to be OFF - Do nothing, if Bulb is ON -> Turn the bulb OFF 
#and increase counter by 1
#If counter = total prisoner count N, then declare.
#When a non-alpha enters the room, If bulb is OFF and the non-alpha has never turned the Bulb ON before, turn the Bulb ON.
#If the Bulb is ON, then do nothing
#randint - 1 to 100


# In[ ]:


'''
import random

N=100
visited = dict.fromkeys(range(1, N+1))
switch=0
counter=0
alpha = random.randint(1,N)
days_passed=0
    
while counter!=N:
    selection=random.randint(1,N)
    days_passed=days_passed+1
    if (selection==alpha):
        if(switch == 1):
            switch=0
            counter = counter+1
            if(counter==N):
                break
    else:
        if(switch==0 and visited[selection]!=1):
            visited[selection]=1
            switch=1

print(days_passed)
'''


# In[2]:


import random

print("Hello")

simulation=0
while simulation<=1000:
    N=100
    visited = dict.fromkeys(range(1, N+1))
    switch=0
    counter=0
    alpha = random.randint(1,N)
    days_passed=0
    looper=0

    while looper<=100000:
        selection=random.randint(1,N)
        if (selection==alpha):
            if(switch == 1):
                switch=0
                counter = counter+1
                if(counter==N-1):
                    break
            else:
                days_passed=days_passed+1
        else:
            if(switch==0 and visited[selection]!=1):
                visited[selection]=1
                switch=1
            else:
                days_passed=days_passed+1
        looper=looper+1

    print(days_passed)
    simulation=simulation+1


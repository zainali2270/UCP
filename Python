x = int(input("Enter Value: "))
flag = False
for i in range(2,x,1):
    if x%i==0:
        flag = True
if flag == True:
    print(x,"Not a Prime Number")
else:
    print(x, "is a Prime Number")


# In[28]:


x = int(input("Enter Value: "))
flag = False
for i in range(2,x,1):
    if x%i==0:
        flag = True
        print("Divisible Numbers are: ", i)
if flag == True:
    print(x,"Not a Prime Number")
else:
    print(x, "is a Prime Number")


# In[62]:


x = int(input("Enter Value: "))
z=x
y=x
while(x>=10):
    x = x // 10
while z!=0:
    z = z % 10
if z%2==0:
    print("The First Digit of",y,"is",z,"and is even")
else:
     print("The First Digit of",y,"is",z,"and is odd")
if x%2==0:
    print("The Last Digit of",y,"is",x,"and is even")
else:
     print("The Last Digit of",y,"is",x,"and is Odd")


# In[60]:


x = int(input("Enter Value: "))
even =0 
odd = 0
rem = 0
while x!=0:
    rem=x%10 
    x = x // 10
    if rem%2==0:
        even += 1
    else:
        odd +=1
print("Even Numbers are: ", even)
print("Odd Numbers are: ", odd)


# In[74]:


isOdd = False
rem=x=0
for i in range(111,999):
    x = i
    while x!=0:
        rem=x%10 
        x = x // 10
        if rem%2!=0:
            isOdd = True
        else:
            isOdd = False
            break
    if isOdd == True:
        print(i)

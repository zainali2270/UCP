# import pandas as pd

data = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]

totalDataLength = len(data)

c1 = 16
c2 = 22

c1Data = []
c2Data = []
group1Data = []
group2Data = []

print("X Data: ",end=" ")

for i in data:
    print(i,end=" ")
print("\n")
while True:
    abs = 0
    group1Average = 0
    group2Average = 0
    print("\nC1 Data with "+str(c1)+": ",end=" ")
    for i in range(totalDataLength):
        abs = round(data[i] - c1,2)
        if abs < 0:
            abs = -(abs)
        c1Data.append(abs)
        print(abs,end=" ")
    abs = 0
    print("\nC2 Data with "+str(c2)+": ",end=" ")
    for i in range(totalDataLength):
        abs = round(data[i] - c2,2)
        if abs < 0:
            abs = -(abs)
        c2Data.append(abs)
        print(abs,end=" ")
    for i in range(totalDataLength):
        if c1Data[i] < c2Data[i]:
            group1Average+= data[i]
            group1Data.append(c1Data[i])
        elif c1Data[i] >= c2Data[i]:
            group2Average+= data[i]
            group2Data.append(c2Data[i])
    print("\nGroup 1 Data: ",end=" ")
    for i in group1Data:
        print(i,end=" ")
    print("\nGroup 2 Data: ",end=" ")
    for i in group2Data:
        print(i,end=" ")

    group1Average = round(group1Average / len(group1Data),2)
    group2Average = round(group2Average / len(group2Data),2)

    if c1 == group1Average or c2 == group2Average:
        break
    else:
        c1 = group1Average
        c2 = group2Average
    c1Data.clear()
    c2Data.clear()
    group1Data.clear()
    group2Data.clear()

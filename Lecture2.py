ucpHistory = "On 15 August 1996, The Punjab Group of Colleges petitioned Government of Punjab for the establishment of a university in the province. \Punjab Institute of Computer Science (PICS), Punjab College of Commerce (PCC), Punjab Law College (PLC) and Punjab College of Information Technology (PCIT) formed the core of the university at the time of establishment.Following a restructuring in 2004, the PCBA and PICS operate under the Faculty of Management Studies and Faculty of Information Technology of the University of Central Punjab respectively. The Punjab Colleges of Commerce and the Punjab Law College respectively function under the Faculties of Commerce and of Law of the University of Central Punjab. The Faculty of Engineering (FOE) was introduced in 2002."
len(ucpString)
print(ucpHistory)


# # Count Words
count=0
for i in ucpHistory:
    if i == ' ':
        count +=1
print("Total Words: ",count)


# Remove 'of'
check=False
found=False
spaceFound = False
count=0
for i in ucpHistory:
    if check == True:
        if i == 'f':
            check = True
            found = True
        else:
            if found !=True:
                print('o',end="")
            found = False
            check = False
    if found==False:
        if i == 'o':
            check=True
        else:
            check = False
            found = False
    if check !=True:
            print(i,end="")

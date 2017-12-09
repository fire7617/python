s= "aab"
maxLen = 0
temp = ''
start = 0
for index,x in enumerate(s):            
    if x not in temp:
        temp = temp + x  
    else:
        temp = temp[temp.index(x) + 1:index+1] + x
        start = start + 1

    print(temp)
    if len(temp) > maxLen:
        maxLen = len(temp)

print(maxLen)

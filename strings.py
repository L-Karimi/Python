from unittest import result


school ="AkiraChix"
print("The resulting string is:" +str(school))
x=len(school)//2
result=""
for i in range(len(school)):
    if i>=x:
        result+=school[i].upper()
    else:
        result +=school[i]
        
print("The resulting string is:" +str(result))
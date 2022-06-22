from unittest import result


school =" AkiraChix"
print(str(school))
x=len(school)//2
output=""
for i in range(len(school)):
    if i>=x:
        output+=school[i].upper()
    else:
        output +=school[i]
        
print(str(output))


colors=["Red","Green","Yellow","Marron","Violet","Blue"]
for color in range(len(colors)):
    print( color,colors[color])
    new_list=enumerate(colors)
    print(new_list)
    


my_homeplace="I come from Laikipia county"
print(my_homeplace.replace("Laikipia","Nyeri"))
print(my_homeplace.swapcase())
print("from" in my_homeplace)
print(my_homeplace.find("come"))

for word in my_homeplace:
    print(word.isdigit())
    break

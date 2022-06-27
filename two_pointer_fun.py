# write a program that reverses a list


import string
# use two pointer function to reverse a given

sentence=" I am AkiraChix"

def reverse_string(sentence):
    new_sentence= sentence.split()
    start=0
    end=len(new_sentence)-1
    while start<=end:
        new_sentence[start],new_sentence[end]= new_sentence[end],new_sentence[start]
        start +=1
        end-=1
        new_string=" ".join(new_sentence)
        print(new_string)
reverse_string("I am AkiraChix")





name="Hannah"

def check_if_palindrome(name):
    new_name=name.split()
    start=0
    end=len(new_name)-1
    while start<end:
        new_name[start],new_name[end] = new_name[end],new_name[start]
        new_name+=1
        new_name-+1
        n_name="".join(new_name)
        print(n_name)
check_if_palindrome("Hannah")


new_word="mum"

def palindrome(new_word):
    if new_word==new_word[::-1]:
        print("This is a plaindrome")
    else:
        print("This is not a plaindrome")
palindrome("mum")




    

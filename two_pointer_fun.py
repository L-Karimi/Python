# write a program that reverses a list


import string


sentence="I am AkiraChix"

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

def int_palin():
    num=int(input("Enter a number:"))
    x=num
    s=0
    while(num>0):
        result=num%10
        s=s*10+result
        num=num//10
    if(x==s):
        print("The number is palindrome")
    else:
        print("Not a palindrome!")
int_palin()

s=string(input("Please ender word:"))
def palindrome(s):
    start=0
    end=len(s)-1
    while start<=end:
        s[start],s[end]=s[end],s[start]
        if s==s:
            print("This is a plaindrome")
        else:
            print("This is not a plaindrome")
palindrome("Enter a word:")


    

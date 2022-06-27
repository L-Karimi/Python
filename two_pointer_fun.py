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
# check if a number is a palindrome or not
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
        print("Not a palindrome")
int_palin()


# check is a string is a palindrome or not
x=input("Enter a word:")

def palindrome(x):
    result=x.split()
    start=0
    end=len(result)-1
    while start<end:
        result[start],result[end]=result[end],result[start]
        start +=1
        end-=1
        s="".join(result)
        print(s)
        if s not in x:
            print("This is  not a palindrome")
        else:
            print("This is not a palindrome")
        # break
palindrome("Enter a word:")
      




    

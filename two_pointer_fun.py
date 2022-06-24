# write a program that reverses a list


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


# s="I am AkiraChix"
# def reverseString( ) :
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i = 0
#         j = len(s) - 1
#         while i <= j:
#             s[i] , s[j] = s[j] , s[i]
#             i += 1
#             j -= 1
# reverseString()
    

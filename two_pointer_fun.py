# write a program that reverses a list

def reverse_string():
    sentense="I am AkiraChix"
    new_sentence= sentense.split()
    print(new_sentence)
    start=0
    end=len(new_sentence)-1
    while start<end:
        new_sentence[start],end= new_sentence[end],start
        
        start +=1
        end-=1
        new_string=""
        print(new_sentence)
        new=new_sentence.append(new_string)
        print(new)
        print(new_string)
        print(new_sentence)
reverse_string()
    

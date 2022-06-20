# Write a function that takes one urgument as a list a=[2,3,4,8]
# and remove the second last item from that list
# and returns the whole list without the removed item.

a=[2,3,4,8]
def nums(a):
    print(a.remove([-2]))
nums()
    


# Write a python program that has a list 
# day =["Monday","Tuesday","Friday","Monday" 
# and counts the number occurrences of Monday

days= ["Monday","Tuesday","Friday","Monday"]
def days():
    print(days.count("Monday"))
days()


# Write a python function named smallest that accepts a list of unsorted integers
# and returns the smalest numbers in the list.Example:
#     smallest([3,6,8,2,4,1,5,7])


smallest=[3,6,8,2,4,1,5,7]
def smallest(smallest):
    sorted_nums=smallest.sort()
    print(sorted_nums[0]) 
smallest()
    


# Write a function named divisible_by_seven that;using the range
# function and a for loop returns a list containing all the numbers between 100 and 200
# that are divisible by 7.




def divisble_by_7():
    y=[]
    for num in range(100,200):
        if num%7==0:
             return y.append(num)
divisble_by_7()
    
# Write a python program that takes two inputs(as integers) from a user and adds the 
# 2 numbers,checks if the sum is greater than 10,less than 10 or equal 10 
# and prints a staement after each check.

def conditions():
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    sum= x+y
if sum>10:
    print("Sum is greater than 10")
elif sum>10:
    print("Sum is less than 10")
elif sum==10:
    print("Sum is equal to 10")
else:
    print(sum)

    



# Write a function that takes one urgument which is a list ,a=[1,2,3,4,5]
# and returns True if 4 is present in the 
# list and False is 4 is not in the list.

a=[1,2,3,4,5]
def present_num(a):
    for num in a:
        if 4 in a:
            print("4 is present")
        else:
            print("4 is not available in the list")
    
present_num()



# Write a function that takes one urgument which is a list 
# fruits=["apples","pineapples","grapes"] and removes the last fruit from
# from the list returns the list without the removed fruit.

fruits=["apples","pineapples","grapes"]
def fruits():
    return fruits.pop()
fruits()
    


# Write a pyton program that takes in a list of cars,
# cars=["Ford","BMW","Volvo"] and returns a sorted list

cars=["Ford","BMW","Volvo"]
def cars():
    return cars.sort()
cars()
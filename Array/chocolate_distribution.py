# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.
import random
arr=[7, 3, 2, 4, 9, 12, 56,8,11,13,44,66,99,33,32,45,34]
arr_2=[]
random.shuffle(arr)
count=0
no_of_student=int(input("enter the no of student you want to distribute chocolate:"))
for i in arr:
    if i not in arr_2:
        arr_2.append(i)
        count+=1
    if count==no_of_student:
        break
min_no=min(arr_2)
max_no=max(arr_2)
print(arr_2)
print(max_no-min_no)





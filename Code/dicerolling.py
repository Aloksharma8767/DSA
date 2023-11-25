# importing module for random number generation
import random

# range of the values of a dice
min_val = 1
max_val = 6

# to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?") 
# import random
# def toss():
#     print("\n----toss time--------")
#     user_call=input("choose even or odd:\n")
#     username=int(input("enter a number (1,6):"))
#     computerzug=random.randint(1,6)
#     print(computerzug)
#     total=username+computerzug
#     print(total)
#     if total%2==0:
#         values="even"
#         if user_call==values:
#             print("user won the toss")
#             userselect=int(input("[0]for bat or [1]for bowl")) 
#             if userselect=='0':
#                 firstinning()
#             elif userselect=='1':
#                 secondinning()
#             else:
#                 print("invalid values try again")
#                 toss()
#         else:
#             print("computer won toss")
#             computerselect=random.randint(0,1)
#             if computerselect=='0':
#                 firstinning()
#             elif computerselect=='1':
#                 secondinning()
#             else:
#                 print("invalid values try again")
#                 toss()
#     else:
#         values="odd"
#         if user_call==values:
#             print("user won the toss")
#             userselect=int(input("[0]for bat or [1]for bowl")) 
#             if userselect=='0':
#                 firstinning()
#             elif userselect=='1':
#                 secondinning()
#             else:
#                 print("invalid values try again")
#                 toss()
#         else:
#             print("computer won the toss")
#             computerselect=random.randint(0,1)
#             if computerselect=='0':
                
#                 firstinning()
#             elif computerselect=='1':
#                 secondinning()
#             else:
#                 print("invalid values try again")
#                 toss()
# toss()
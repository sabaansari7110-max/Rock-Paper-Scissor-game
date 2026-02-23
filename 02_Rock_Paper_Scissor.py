# Sanke, Water, Gun game

import random

"""
1 for rock
-1 for paper
0 for scissor

"""

computer= random.choice([-1, 1, 0])
yourstr= input("enter your choice: ")
yourdict= {"r": 1, "p": -1, "s":0} 
reverseDict= {1: "Rock", -1: "Paper", 0: "Scissor"}

you= yourdict[yourstr]

# By now we have 2 numbers (variables), you and computer
print(f"you chosse {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")


else:
     if(computer == -1 and you == 1): #( computer - you )-2
           print("You Lose!")

     elif(computer == -1 and you == 0): #( computer - you ) -1
           print("You Win!")

     elif(computer == 1 and you == 0): #( computer - you ) 1
           print("You Lose!")

     elif(computer == 1 and you == -1): #( computer - you ) 2
           print("You Win!")

     elif(computer == 0 and you == 1): #( computer - you ) 1
           print("You Win!")

     elif(computer == 0 and you == -1): #( computer - you ) -1
           print("You Lose!")


     else:
          print("Something went wrong")

"""

The below logic is written on the basis of the values of the computer - you


if ((computer - you )== -1 or (computer - you ) == 2):
      print("You Lose!")
else:
      print("You Win!")

          
"""
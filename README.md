## 🎮 Rock Paper Scissors – Terminal Game (Python)
<br>
A simple Rock Paper Scissors game built using Python.
<br>
This game runs completely in the terminal/command prompt and allows a user to play against the computer.
<br>
<br>

# 📌 Features
<br>
1. Runs in terminal (no GUI required)
<br>
2. User vs Computer gameplay
<br>
3. Random computer choice
<br>
4.Input validation
<br>
5. Simple and beginner-friendly logic
<br>
6. Easy to modify and improve
<br>
<br>

# Technologies Used
<br>
Python 3
<br>
random module
<br>
<br>

# 🚀 How to Run
<br>
1. Make sure Python is installed on your system.
<br>
2. Clone this repository or download the file.
<br>
       https://github.com/sabaansari7110-max/Rock-Paper-Scissor-game.git
 <br>
3. Open terminal in the project folder.
<br>
4. Run the game:<br>
Bash
<br>

```bash
          02_Rock_Paper_Scissor.py
```

<br>                             
Copy code
<br>

```python 
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
```
         
<br>
<br>
Make sure python is installed.
<br>

# 🎯 How to Play
<br>
Type:
<br>
(r)ock
<br>
(p)aper
<br>
(s)cissors
<br>
The computer will randomly choose one option.
<br>
The winner will be displayed in the terminal.
<br>
<br>

# Game Logic
<br>
1. Rock beats Scissors
<br>
2. Scissors beats Paper
<br>
3. Paper beats Rock
<br>
Same choices result in a Draw
<br>
<br>

# Future Improvements
<br>
1. Add score tracking
<br>
2. Add multiple rounds
<br>
3. Add play again option
<br>
4. Convert to GUI (Tkinter / Flask)
<br>
5. Deploy online version
<br>
<br> 

# Author
<br>
Created as part of Python learning journey to strengthen programming fundamentals and logical thinking.
<br>
<br>

# 📜 License
<br>
This project is licensed under the MIT License.
<br>
You are free to use, modify, and distribute this project with proper attribution.
<br>
<br>

# Contribution
<br>
This is a beginner project.
<br>
Feel free to fork, improve, and experiment with new features.


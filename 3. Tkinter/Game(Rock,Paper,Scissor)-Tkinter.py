import tkinter as tk
import random

# Create a GUI window
root = tk.Tk()
root.title("Stone Paper Scissor")

# Setting Geometry of Tk window
root.geometry("455x400")

# Create a game Lable
game_lable = tk.Label(root, text = 'Game')
game_lable.place(relx = 0.3,rely = 0.1)

# player mode
player= tk.Label(root, text = 'Player Response: ')
player.place(relx = 0.0,rely = 0.3)

player_response = tk.Label(root,text = "None")
player_response.place(relx = 0.3, rely = 0.3)

# computer mode
computer = tk.Label(root, text = 'Computer Response: ')
computer.place(relx = 0.0,rely = 0.4)

computer_response = tk.Label(root,text = "None")
computer_response.place(relx = 0.3,rely = 0.4)

# Create a player-Score  Lable
player_score_lable = tk.Label(root, text = 'Player Score')
player_score_lable.place(relx = 0.0,rely = 0.5)

player_score = tk.Label(root,text = 0)
player_score.place(relx = 0.3,rely = 0.5) 

# Create a computer-Score Lable
computer_score_lable = tk.Label(root, text = 'Computer score')
computer_score_lable.place(relx = 0.5,rely = 0.5)

computer_score = tk.Label(root,text = 0)
computer_score.place(relx = 0.8,rely = 0.5) 

# Create message
msg = tk.Label(root, font=50 ,bg ="white" , fg = "black")
msg.place(relx = 0.3,rely = 0.8)

#update computer score
def updateCompScore():
    score = int(computer_score['text'])
    score +=1
    computer_score['text'] = str(score)

#update player score
def updateUserScore():
    score = int(player_score['text'])
    score +=1
    player_score['text'] = str(score)

#checking winner function
def checking(player_choice,computer_choice):
    if player_choice == computer_choice:
        msg['text'] = "Its a tie!!"
    elif player_choice == "Stone":
        if computer_choice == "Paper":
            msg['text'] = "you loose"
            updateCompScore()
        else:
            msg['text'] = "you win"
            updateUserScore()
    elif player_choice == "Paper":
        if computer_choice == "Scissor":
            msg['text'] = "you loose"
            updateCompScore()
        else:
            msg['text'] = "you win"
            updateUserScore()
    elif player_choice == "Scissor":
        if computer_choice == "Stone":
            msg['text'] = "you loose"
            updateCompScore()
        else:
            msg['text'] = "you win"
            updateUserScore()
    else:
        pass

#choice function
def choice_fn(x):
    # player choice
    if x == "Stone":
        player_response['text'] = "Stone"
    elif x == "Paper":
        player_response['text'] = "Paper"
    else:
        player_response['text'] = "Scissor"

    # computer choice
    computer_choice = random.choice( ['Stone', 'Scissor', 'Paper'] )
    computer_response['text'] = computer_choice

    checking(x,computer_choice)

#reset function
def reset_fn():
    player_score['text'] = 0
    computer_score['text'] = 0

# Create a stone button 
stone_button = tk.Button( root, text = 'Stone', bg = "#FF3E4D", fg ="white", command = lambda:choice_fn("Stone"))
stone_button.place(relx = 0.1,rely = 0.2)

# Create a paper button 
paper_button = tk.Button( root, text = 'Paper', bg = "#FAD02E", fg ="white", command = lambda:choice_fn("Paper"))
paper_button.place(relx = 0.25,rely = 0.2)

# Create a scissor button 
scissor_button = tk.Button( root, text = 'Scissor', bg = "#0ABDE3", fg ="white", command = lambda:choice_fn("Scissor"))
scissor_button.place(relx = 0.4,rely = 0.2)

# Create a Reset button 
reset_button = tk.Button( root, text = 'Reset', command = lambda:reset_fn())
reset_button.place(relx = 0.15,rely = 0.7)

# Create a Exit button 
exit_button = tk.Button( root, text = 'Exit', command = root.destroy)
exit_button.place(relx = 0.3,rely = 0.7)

# Start the GUI
root.mainloop()
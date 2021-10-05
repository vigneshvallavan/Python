import random

while True:

    player_1 = input("\n\nStone, Scissor, Paper? : ")
    computer = random.choice( ['Stone', 'Scissor', 'Paper','stone', 'scissor', 'paper'] )

    print ("\n------------------------ RESULT ------------------------")

    if player_1.lower() == computer.lower():
        print("player_1 --> ",player_1)
        print("computer --> ",computer)
        print("Result   -->  Tie!")

    elif player_1 == 'Stone' or player_1 == 'stone':
        print("player_1 --> ",player_1)
        print("computer --> ",computer)

        if computer == 'Paper' or computer == 'paper':
            print("Result   -->  You Lose! ",computer,' Covers ',player_1)
        else:
            print("Result   -->  You Win! ",player_1,' Smashes ',computer)

    elif player_1 == 'Scissor' or player_1 == 'scissor':
        print("player_1 --> ",player_1)
        print("computer --> ",computer)

        if computer == 'Stone' or computer == 'stone':
            print("Result   -->  You Lose! ",computer,' Smashes ',player_1)
        else:
            print("Result   -->  You Win! ",player_1,' Cut ',computer)

    elif player_1 == 'Paper' or player_1 == 'paper':
        print("player_1 --> ",player_1)
        print("computer --> ",computer)

        if computer == 'Scissor' or computer == 'scissor':
            print("Result   -->  You Lose! ",computer,' cut ',player_1)
        else:
            print("Result   -->  You Win! ",player_1,' Covers ',computer)

    else:
        print('invalid word !!')
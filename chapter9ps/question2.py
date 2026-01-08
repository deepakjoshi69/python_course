'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''
import random

def game():
    print("You are in the game...")
    score = random.randint(1,100)

    with open("hiscore.txt") as file:
        highscore = file.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"Your High Score Is : {score}")

    with open("hiscore.txt","w") as file:
        if score > highscore:
            file.write(str(score))
        else:
            file.write(str(highscore))
    
    return score

game()
        
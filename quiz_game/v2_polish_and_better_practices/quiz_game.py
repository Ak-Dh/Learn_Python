# quiz_game.py

"""
Quiz Game Project
-----------------
A simple interactive quiz game with multiple question types and scoring system.
"""
import time
import os

def clear_screen(i):
    time.sleep(i)
    os.system('clear')

def welcome():
    # Print the welcome message with some ASCII art for decoration
    clear_screen(0)
    print("****************************************************")
    print("*                                                  *")
    print("*           WELCOME TO THE QUIZ GAME!              *")
    print("*                                                  *")
    print("****************************************************")
    print("\n")    
    print("Test your knowledge and win!")
    print("Here's how to play:")
    print("- You will be presented with multiple-choice questions")
    print("- Choose your answer by entering the corresponding number")
    print("- The game will keep track of your score")
    print("- You can play as many rounds as you want")
    player_name=input("What is your name? ")
    print(f"Hi {player_name}, let's get ready to begin!")
    print("Press Enter to play....")
    input()
    clear_screen(0.5)


def ask_question(q,i):
    print(f"{i}.) {q}")
    return input("answer: ")

def check_answer(user_ans,q):
    if(user_ans == q["answer"]):
        print("Correct")
        return q["point"]
    else:
        print("Wrong")
        return 0

def game_status(s):
    if(s=='no'):
        return False
    elif(s=='yes'):
        return True

def main():
    questions = [
        {"q_num":1,"question":"What is 2+2?","answer":"4", "point":1},
        {"q_num":2,"question":"What is 1+1?","answer":"2", "point":1},
        {"q_num":3,"question":"What is 20+20?","answer":"40", "point":1}
    ]
    play_game = True

    while(play_game):
        score = 0
        welcome()
        for q in questions:
            answer=ask_question(q["question"],q["q_num"])
            score+=check_answer(answer,q)
            clear_screen(1)
        print(f"Total points: {score}")
        status=input("Would you like to play again? (yes/no): ....")
        play_game=game_status(status.lower())
    clear_screen(0)

if __name__ == "__main__":
    main()
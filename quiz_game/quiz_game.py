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
    clear_screen(1)


def ask_question(q):
    print(q)
    return input("answer: ")

def check_answer(user_ans,q):
    if(user_ans == q["answer"]):
        print("Correct")
        return q["point"]
    else:
        print("Wrong")
        return 0

def main():
    questions = [
        {"question":"What is 2+2?","answer":"4", "point":1},
        {"question":"What is 1+1?","answer":"2", "point":3},
        {"question":"What is 20+20?","answer":"40", "point":2}
    ]
    score = 0
    welcome()
    for q in questions:
        answer=ask_question(q["question"])
        score+=check_answer(answer,q)
        clear_screen(1)
    print(f"Total points: {score}")
    input("press Enter to exit ....")
    clear_screen(0)

if __name__ == "__main__":
    main()
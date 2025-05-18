# quiz_game.py

"""
Quiz Game Project
-----------------
A simple interactive quiz game with multiple question types and scoring system.
"""
import time
import os
import random
import json

QA = "qa"
MCQ = "mcq"

def clear_screen(delay=0.5):
    time.sleep(delay)
    os.system('clear')

def welcome():
    # Print the welcome message with some ASCII art for decoration
    clear_screen()
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
    clear_screen()


def ask_question(q):
    if(q["type"]==QA):
        print(f"{q['q_num']}.) {q['question']}")
        ans = input("answer: ").strip()
        return ans
    elif(q["type"]==MCQ):
        print(f"{q['q_num']}.) {q['question']}")
        for i,o in enumerate(q["options"], start=1):
            print(f"{i}.) {o}")
        while True:
            ans = input("answer: ").strip()
            if (ans.isdigit() and 1<=int(ans)<=len(q["options"])):
                return q["options"][int(ans)-1]
            else:
                print("Please enter a valid option number: ")
                
        
def check_answer(user_ans,q):
    if(user_ans == q["answer"]):
        print("✅ Correct! Well done!")
        time.sleep(0.5)
        return q["point"]
    else:
        print(f"❌ Oops! The correct answer is: {q['answer']}")
        time.sleep(0.5)
        return 0

def game_status():
    while True:
        s = input("Would you like to play again? (yes/no): ....").lower()
        if(s in ["no","n"]):
            return False
        elif(s in ["yes","y"]):
            return True
        else:
            print("Invalid input. Please type 'yes' or 'no': ")

def load_questions():
    file_name = "questions.json"
    try:
        with open(file_name,"r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"❌ Error: File '{file_name}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"❌ Error: File '{file_name}' is not valid JSON.")
        return []


def main():
    play_game = True
    questions=load_questions()
    if not questions:
        return
    while(play_game):
        random.shuffle(questions)
        score = 0
        welcome()
        for q in questions:
            answer=ask_question(q)
            score+=check_answer(answer,q)
            clear_screen()
        print(f"Total points: {score}")
        play_game=game_status()
    clear_screen()

if __name__ == "__main__":
    main()
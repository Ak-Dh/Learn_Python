# quiz_game.py

"""
Quiz Game Project
-----------------
A simple interactive quiz game with multiple question types and scoring system.
"""
import time
import os
import random

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

def main():
    questions = [
        {"q_num":1,"question":"What is 2+2?","answer":"4","point":1,"type":QA},
        {"q_num":2,"question":"What is 1+1?","answer":"2","point":1,"type":QA},
        {"q_num":3,"question":"What is 20+20?","answer":"40","point":1,"type":QA},
        {"q_num":4,"question":"What is the capital of the USA","options":["Washington DC","Phoneix","Las Vegas"],"answer":"Washington DC","point":1,"type":MCQ},
        {"q_num":5,"question":"What is the capital of India?","options":["Kerala","Goa","Delhi"],"answer":"Delhi","point":1,"type":MCQ},
        {"q_num":6,"question":"What is the capital of Germany?","options":["Munich","Berlin","Frankfurt"],"answer":"Berlin","point":1,"type":MCQ}
    ]
    play_game = True
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
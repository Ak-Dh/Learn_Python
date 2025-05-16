## 🧭 Version 1 Milestone: "Core Quiz Engine"

### You’ve achieved:

* [x] User sees a welcome message
* [x] Score is tracked
* [x] Game can be played multiple times
* [x] Uses functions and loops well

---

## 🛠️ Improvements for Version 2: “Polish & Better Practices”

Here are enhancements you can focus on now, **before adding new features**:

### 1. ✅ Better Question Display

Make sure multiple-choice or open-ended questions are formatted clearly (you can prepare your structure for this):

```python
{"q_num":1, "question":"What is 2+2?", "options": ["3", "4", "5"], "answer":"2", "point":1}
```

Then display like:

```python
def ask_question(q, i):
    print(f"{i}. {q['question']}")
    for idx, option in enumerate(q.get("options", []), 1):
        print(f"{idx}. {option}")
    return input("Your answer: ")
```

Even if not all questions have options, this prepares your code for the next update.

---

### 2. ✅ Add Input Validation

Right now, the user can type anything and it won’t throw an error — but might break logic. Let’s add basic validation:

```python
def get_valid_input(prompt):
    while True:
        answer = input(prompt)
        if answer.strip() == "":
            print("Answer cannot be empty. Try again.")
        else:
            return answer
```

Use this in `ask_question()` or `input()` calls.

---

### 3. ✅ Improve `game_status()` (optional)

This function is simple, but could be written like this:

```python
def game_status():
    while True:
        status = input("Would you like to play again? (yes/no): ").lower()
        if status in ['yes', 'y']:
            return True
        elif status in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")
```

Now it's foolproof!

---

### 4. ✅ Clean Up Terminal Logic

Instead of sending `clear_screen(0)` or `(1)` everywhere, set default:

```python
def clear_screen(delay=0.5):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
```

Now you can just call `clear_screen()` normally.
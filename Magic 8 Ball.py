import random
import time


def rgb_escape_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def is_valid_input(uinput):
    state = False
    for char in uinput:
        if not (char.isalnum() or char.isspace()):
            return False
        if char.isalpha():
            state = True
    return state


# Colors for text
WINNER_COLOR = rgb_escape_code(171, 157, 255)  # lilac for winner
RED_COLOR = rgb_escape_code(255, 139, 104)  # red
FIRST_COLOR = rgb_escape_code(157, 255, 179)  # green
SECOND_COLOR = rgb_escape_code(157, 226, 255)  # teal
YELLOW = rgb_escape_code(255, 222, 106)  # yellow

RESET = "\033[0m"  # Reset color

print(f"\n🔮{WINNER_COLOR}Hi, this is the ✨MAGIC✨ 8 ball!🔮{RESET}\n")
print(f"{SECOND_COLOR}Ask your YES/NO question or type 'exit' at any time to stop:\n")
command = input(f"Your question is: \n{RESET}").strip().lower()

while not is_valid_input(command):
    print(f"{RED_COLOR}Invalid input! Please use only letters, numbers, and spaces, and ensure it contains at least "
          f"one letter. Try again!{RESET}")
    command = input(f"{SECOND_COLOR}Your question is: \n{RESET}").strip().lower()

while command != "exit":
    rand = random.randint(1, 3)
    print(f"{YELLOW}The ✨MAGIC✨ 8 ball shakes!{RESET}")
    time.sleep(1)
    print(f"{YELLOW}The ✨MAGIC✨ 8 ball shakes!!{RESET}")
    time.sleep(1)
    print(f"{YELLOW}The ✨MAGIC✨ 8 ball shakes!!!{RESET}")
    time.sleep(1)
    print(f"{SECOND_COLOR}The answer to your question is: ")
    time.sleep(1)
    if rand == 1:
        print(f"{YELLOW}YES!{RESET}")
    elif rand == 2:
        print(f"{YELLOW}NO{RESET}")
    else:
        print(f"{YELLOW}I'M NOT SURE{RESET}")
    command = input(f"{SECOND_COLOR}Ask your YES/NO question or type 'exit' at any time to stop:\n{RESET}")
    while not is_valid_input(command):
        print(
            f"{RED_COLOR}Invalid input! Please use only letters, numbers, and spaces, and ensure it contains at least "
            f"one letter. Try again!{RESET}")
        command = input(f"{SECOND_COLOR}Your question is: \n{RESET}").strip().lower()

print(f"{WINNER_COLOR}Come back anytime! Bye!{RESET}💜")

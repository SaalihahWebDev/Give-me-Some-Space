import random
import time
dice_faces = {

1: (

"┌───────┐",
"│       │",
"│ ●     │",
"│       │",
"└───────┘"
),
2: (
"┌───┐",
"│ ● │",
"│   │",
"│ ● │",
"└───┘"
),
3: (
"┌───┐",
"│ ● │",
"│ ● │",
"│ ● │",
"└───┘"
),
4: (
"┌─────┐",
"│ ● ● │"
"│     │",
"│ ● ● │",
"└─────┘"
),
5: (
"┌─────┐",
"│ ● ● │",
"│ ●   │ ",
"│ ● ● │",
"└─────┘"
),
6: (
"┌─────┐",
"│ ● ● │",
"│ ● ● │",
"│ ● ● │",
"└─────┘"
)
}
print("Welcome to the dice game🎲🎲🎲")
print("If you want to play please press enter otherwise exit if you want")
print("_"*40)
roll_count=0
while True:
    user_input=input("Please Enter to roll the dice: ")
    if user_input.lower()=="exit":
        break
    print("Rolling the dice")
    time.sleep(1)
    roll=random.randint(1,6)
    roll_count+=1
    for line in dice_faces[roll]:
        print(line)
    print(f"You rolled a {roll}!\n")
    again=input("Enter y to continue or n to exit: ").lower()
    if again !="y":
         break
print("\n Thanks for playing the dice roller game")
print(f"You rolled the dice {roll_count} times.Goodbye")
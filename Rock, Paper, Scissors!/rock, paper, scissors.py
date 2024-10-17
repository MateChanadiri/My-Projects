import random
choices = ["rock", "paper", "scissors"]
bot = random.choice(choices)
human = input("enter, rock paper or scissors: ")
if human == bot:
    print("you and the bot tie")
elif human == "paper" and bot == "rock" or human == "scissors" and bot == "paper" or human == "rock" and bot == "scissors":
    print("nice job you win!!!")
else:
    print(f"sorry you lost!!! you chose {human} but the bot chose {bot}")

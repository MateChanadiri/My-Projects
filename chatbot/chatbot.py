def chatbot():
    print("Hello, im a simple chatbot! can you enter your name for me please? i only ask 5 questions!")
    user_name = input("you: ")
    print(f"Well hello there {user_name}, how are you?")

    user_hru = input("you: ")
    if user_hru == "good":

        print("thats nice to hear")
    elif user_hru == "bad":

        print("oh im sorry to hear that.")

    else:
        print("oh alright then")

    print("how old are you?")
    user_age = int(input("you: "))

    if user_age < 5:
        print("oh i dont think you can type yet...")

    elif user_age <= 25:
        print("thats great to hear!")

    else:
        print("oh thats great to hear but are you sure youre that old?")
    
    print("do you have any pets?")
    user_pets = input("you: ")

    if user_pets == "yes":
        print("thats so cool! whats its name?")
        input("you: ")
        print("that is a nice name")

    elif user_pets == "no":
        print("oh okay! do you wish to have any pets?")
        user_wish = input("you: ")
    
        if user_wish == "yes":
            print("thats cool!")
        elif user_wish == "no":
            print("oh okay!")
        

chatbot()
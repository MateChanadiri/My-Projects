# კოდის გაუმჯობესება, debugging - მათე ჩანადირი
# კითხვების და არჩევნების მართვა, ზოგადი ტექსტი - ალექს ჭიტანავა
# ინპუტი - დემე აზმაიფარაშვილი
# ქულების მართვა - გიორგი რუსიშვილი
# თამაშის flow (სწორად მიდის კოდი თუ არა) - დავით მეპარიშვილი
# კოდის გაუმჯობესება, გრამატიკული შეცდომების გამოსწორება, იდეები - გრიშა გოგიჩაშვილი 

print("") # new line for readibility
print("Hello welcome to Trivia quiz game") # მე გამოვიყენე "print" ფუნქცია და მის დახმარებით დავპრინტე ზოგადი მისალმება.
print("Your goal is to choose the correct answer!") # "print" პუნქციის დახმარებით ავხსენი თამაშის წესი.
print("if you answer correctly you get +1 point otherwise -1 points") # "print" - ის გამოყენებით ავხსენი თუ როგორ მუშაობს ქულები.
print("Enter the guess (only in letters A B C or D): ") # "print" - ის გამოყენებით ავხსენი თუ როგორ უნდა გამოიყენოს მომხმარებელმა ინპუტი.

questions = ["Leonardo da Vinci's “Mona Lisa” hangs in what museum?: ",
            "Roughly how many miles per hour does the earth spin?: ",
            "What is the distance from earth to the sun?: ",
            "What was the first animal to ever be cloned?: ",
            "How many elements are currently on the periodic table?: ",
            "How many moons does Neptune have?: ",
            "What is the largest bone in the human body?: ",
            "What is the fear of flowers called?: "] # მოვძებნე კითხვები და ჩავსვი ლისტში სახელად "questions".
            
options = ["""A. Vatican museums
B. The Louvre Museum in Paris
C. The british museum
D. Museo Nacional del Prado""",
"""A. 1000 mhp
B. 2000 mhp
C. 1500 mhp
D. 2500 mhp""",
"""A. 50 millionkm
B. 200 million km
C. 150 million km
D. 100 million km""",
"""A. Cow
B. Sheep
C. Dog
D. Horse""",
"""A. 100
B. 219
C. 119
D. 118""",
"""A. 9
B. 15
C. 14
D. 21""", 
"""A. Femur
B. Backbone
C. Skull
D. Lower leg bones""",
"""A. Hemophobia
B. Anthophobia
C. mysophobia
D. Ornithophobia"""] # მოვძებნე კითხვების შესაბამისი ვარიანტები და ჩავსვი ლისტში სახელად "options". # იდეა - გრიშა, for readibility 3 """ დავუწერე და ჩამოვამწკვრივე.

answers = ["B", "A", "C", "B", "D", "C", "A", "B"] # შევქმენი ცვლადი "answers" სადაც დავწერე ყველა კითხვის სწორი პასუხი.

score = 0 # მე შევქმენი ცვლადი "score" და მივეცი მნიშვნელობა 0.

# first question

print("") # new line for readibility.
print("The questions will get harder and harder! first question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[0]) 
print("") # new line for readibility.
print(options[0])
print("") # new line for readibility.

user_guess = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess == answers[0]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა ჩამოაკლდა.

print("------------------------------------------------------------------------------------------------------")
# second question

print("") # new line for readibility.
print("This question is more difficult then the previus one right? second question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[1]) 
print("") # new line for readibility.
print(options[1])
print("") # new line for readibility.

user_guess1 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess1 == answers[1]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა ჩამოაკლდა.

print("------------------------------------------------------------------------------------------------------")
# third question

print("") # new line for readibility.
print("This question is more difficult then previus one right? third question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[2]) 
print("") # new line for readibility.
print(options[2])
print("") # new line for readibility.

user_guess2 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess2 == answers[2]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")
# fourth question

print("") # new line for readibility.
print("This question is more difficult then previus one right? fourth question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[3]) 
print("") # new line for readibility.
print(options[3])
print("") # new line for readibility.

user_guess3 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess3 == answers[3]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")
# fifth question

print("") # new line for readibility.
print("Admit it this is more difficult! fifth question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[4]) 
print("") # new line for readibility.
print(options[4])
print("") # new line for readibility.

user_guess4 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess4 == answers[4]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")
# sixth question

print("") # new line for readibility.
print("Admit it this is more difficult! sixth question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[5]) 
print("") # new line for readibility.
print(options[5])
print("") # new line for readibility.

user_guess5 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess5 == answers[5]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")
# seventh question

print("") # new line for readibility.
print("difficult! seventh question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[6]) 
print("") # new line for readibility.
print(options[6])
print("") # new line for readibility.

user_guess6 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess6 == answers[6]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")
# eighth question

print("") # new line for readibility.
print("difficult! eighth question: ") # დავწერე ზოგადი ტექსტი "print" ფუნქციის გამოყენებით.
print("") # new line for readibility. 
print(questions[7]) 
print("") # new line for readibility.
print(options[7])
print("") # new line for readibility.

user_guess7 = input("Enter the guess. (only in letters A B C or D): ").upper() # შევქმენი ინპუტი გადავეცი 4 სავარაუდო პასუხი მივანიჭე upper. 

if user_guess7 == answers[7]: # ვადარებთ თუ ინფუთი ტოლია პასუხის მნიშვნელობას.
        score = score + 1 # აქ მე მომხმარებელს მივეცი + 1 ქულა.
        print("") # new line for readibility.
        print(f"correct! your score is {score}.") # დავწერე ტექსტი სადაც terminal-ი ეუბნება მომხმარებელს რომ ქულა მოემატა.

else:                              
    score = score - 1 # თუ არასწორია ვაკლებთ 1 ქულას.
    print("") # new line for readibility.
    print(f"incorrect! your score is {score}.")

print("------------------------------------------------------------------------------------------------------")

# if the user got 5+ points = pass else sorry you didnt pass

if score >= 5:
    print("")
    print("Nice you passed!")
else:
    print("")
    print("Sorry you didnt pass.")

# final score...

print(f"your final score is... ")
print(score)
print("If your score is low, good job anyway You did great!")
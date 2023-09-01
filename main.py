# Python quiz game

questions = ("1. How many elements are in periodic table?: ",
            "2. Which animal lays the largest eggs?: ",
            "3. What is the most abundant gas in Earths atmosphere?: ",
            "4. How many bones are in the human body?: ",
            "5. Which planet in the solar system is the hottest?: ",
            "6. What Icelandic geothermal location shares the same name as a 1980 film?: ",
            "7. What popular tourist destination was once called “The Island of Swine”?: ",
            "8. Which African country is the worlds smallest by land area?: ",
            "9. Which ocean has more coastline on it the Pacific or the Atlantic?: ",
            "10. What is the full form of AFSPA?: ",
            "11. Which of the following bacteria forms an endosymbiotic nitrogen fixing association with roots of legumes that helps in Nitrogen Fixation?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrgen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Pacific", "B.  The Blue Lagoon", "C. Asia", "D. Indian"),
           ("A. Spain", "B. Kashmir", "C. Cuba", "D. America"),
           ("A. Seychelles", "B. Imdomesia", "C. South Africa", "D. Lamba"),
           ("A. Indian Ocean", "B. Atlantic Ocean", "C. Dead Sea", "D. Pacific Ocean"),
           ("A. Assian Future Space Planing Association", "B. Army For Special Problem Act", "C. Armed Forces Special Power Acts", "D. African Forces Special Para Association"),
           ("A. Clostridium", "B. Rhizobium", "C. Salmonella", "D. Staphylococcus"))

answers = ("C", "D", "A", "A", "B", "B", "C", "A", "D", "C", "B")
guesses = []
score = 0
question_num = 0 

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1
       print("CORRECT!")
    else:
       print("INCORRECT!")
       print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("--------------------------")
print("         RESULT           ")
print("--------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
    print()

    score =  int(score / len(questions) * 100)
print(f"Your score is: {score}%")

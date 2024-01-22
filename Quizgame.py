#Quiz game using python
#By Abhijit Mahadik


questions = ("Q.1 Who invented atomic bomb?: ",
             "Q.2 What country has the highest world population? :",
             "Q.3 Which of the following gas is considered as inert gas? : ",
             "Q.4 In which year India got independent from britishers? :",
             "Q.5 When the information is between 0 and 1 in a quantum computer, what do we call this? :")

options = (("A. Nikola Tesla", "B. Albert Einstein", "C. Robert J. Oppenheimer", "D. Werner Heisenberg"),
           ("A. China", "B. India", "C. Bangladesh", "D.Japan"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Monoxide", "D. Helium"),
           ("1947", "1932", "1954", "1912"),
           ("A. Superposition", "B. Middle position", "C. Ordinary position", "D. Same position"))

answers = ("C", "B", "D", "A", "A") #Correct answers
guesses = []
score = 0
question_num = 0


for question in questions:
    print("--------------------")
    print (question)
    for option in options[question_num] :
         print(option)

    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
         score += 1
         print("CORRECT!")
    else:
         print("INCORRECT!")
         print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----RESULTS-----")

print("answers: ", end="")
for answer in answers:
     print(answer, end=" ")
print()



print("guesses: ", end="")
for guess in guesses:
     print(guess, end=" ")
print()


score = int(score/ len(questions) * 100)     #Used int function with mathematical formula of percentage which returns a numeric value in form of percentage.
print (f"Your score is : {score}%")         

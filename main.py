# Te Reo Quiz - Vincent Beet
score = 0
question = input("Welcome the Te Reo Quiz, Are you ready to begin? ").lower()

if question == "yes":
  print("Question one!")

print("\n")
question_1 = input("1. What does Pero mean in english? A. Dog? B. Sparrow? C. Lizard? ").lower()


if question_1 == "a" or question_1 == "dog":
  score += 1
  print("Correct.")
  print("Score:", score)

elif question_1 == "b" or question_1 == "sparrow":
  print("Incorrect.") 
  print("Score:", score)

elif question_1 == "c" or question_1 == "lizard":
  print("Incorrect.") D
  print("Score:", score)

else: 
  print("Please choose one of the options")
  print(question_1)

print("\n")
question_2 = input("2. What does Moana mean in english? A. Beauty? B. Ocean? C. Water?").lower()

if question_2 == "b" or question_2 == "ocean":
  score += 1
  print("You are correct.")
  print("Score:", score)

elif question_2 == "a" or question_2 == "beauty":
  print("Incorrect.") 
  print("Score:", score)

elif question_2 == "c" or question_2 == "water":
  print("Incorrect.") 
  print("Score:", score)

else: 
  print("Please choose one of the options")
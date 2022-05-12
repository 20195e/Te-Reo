# Te Reo Quiz - Vincent Beet
score = 0
question = input("Welcome the Te Reo Quiz, Are you ready to begin? ").lower()

if question == "yes":
  print("Question one!")

question1 = input("1. What does Pero mean in english? A. Dog? B. Sparrow? C. Lizard? ").lower()

if question1 == "A" or "Dog":
  score += 1
  print("Correct.")
  print("Score:", score)
 
else:
  print("Incorrect.")
  print("Score:", score)


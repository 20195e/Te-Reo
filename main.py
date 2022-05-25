def question1():
  global score
  print("This is question One")
  ans1 = input("Pero means Sparrow in english! True or False?").lower()

  if ans1 == "false":
    print("Correct")
    score += 1
    print("Score:",score)
    question2()


  elif ans1 == "true":
    print("Incorrect")

  else:
    print("Please choose True or False")
    question1()


def question2():
  global score
  print("This is question Two")
  ans2 = input("Moana means Beauty in English! True or False?").lower()

  if ans2 == "false":
    print("Correct")
    score += 1
    print("Score:",score)

  elif ans2 == "true":
    print("Incorrect")




score = 0
question1()

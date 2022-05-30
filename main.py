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
    question2()

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
    question3()

  elif ans2 == "true":
    print("Incorrect")
    question3()

  else:
    print("Please choose True or False")
    question2()


def question3():
  global score
  print("This is question Three")
  ans3 = input("Mane means Monday in English! True or False?").lower()

  if ans3 == "true":
    print("Correct")
    score += 1
    print("Score:",score)
    question4()

  elif ans3 == "false":
    print("Incorrect")
    question4()

  else:
    print("Please choose True or False")
    question3()


def question4():
  global score
  print("This is question Four")
  ans4 = input("heihei means a group of two kids in English! True or False?").lower()

  if ans4 == "false":
    print("Correct")
    score += 1
    print("Score:",score)
    question5()

  elif ans4 == "true":
    print("Incorrect")
    question5()

  else:
    print("Please choose True or False")
    question4()


def question5():
  global score
  print("This is question Five")
  ans5 = input("Iwa means 6 in English! True or False?").lower()

  if ans5 == "false":
    print("Correct")
    score += 1
    print("Score:",score)
    print("The quiz is over you have scored",score)
    print("points, Congratulations!")

  elif ans5 == "true":
    print("Incorrect")

  else:
    print("Please choose True or False")
    question5()

score = 0
print("This is a quiz meant to test your basic knowledge of Te Reo")
print("\n")
question1()

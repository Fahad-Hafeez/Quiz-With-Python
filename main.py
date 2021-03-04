import random

def get_tof_statements():

  statements = []
  statements.append(["Tigers have stripes", "T"])
  statements.append(["The captal of France is Madrid", "F"])
  statements.append(["The Queen owns one sixth of the land on the Earth", "T"])

  return statements

def play_tof_quiz():

  # Get true or false statements
  tof_statements = get_tof_statements()

  # Randomise tof statements
  random.shuffle(tof_statements)

  # Set PLayer score to 0
  score = 0
  # Show tof statements using a loop
  for s in tof_statements:
    # present statement
    print("True or False:" + s[0])
    # user enter guess
    guess = input("Enter T or F: ")
    # check if guess is correct
    if guess == s[1]:
      print("Correct!")
      # update score
      score = score + 1
    else:
      print("Incorrect! :(")
  # Show final score
  print("Your Final Score Is: " + str(score))


def main_menu():

  print("+------------------------------+")
  print("| Welcome to QUIZ MASTER 3000! |")
  print("+------------------------------+")
  print("Please Select an Option:       |")
  print("|                              |")
  print("| 1. Play True or False quiz   |")
  print("| 2. Play General Knowledge Quiz |")
  print("| 0. Quit                       |")
  print("+------------------------------+")
  choice = input("Enter 1, 2 or 0: ")
  if choice == "1":
    play_tof_quiz()
  elif choice == 0:
    print("Thanks for Playing")
    quit()

main_menu()
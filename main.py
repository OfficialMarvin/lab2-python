# Author: Marvin Jakobs mkj5388@psu.edu
# Collaborator: Brian Chettle bjc5969@psu.edu
# Collaborator: Fletcher Henneman fdh5031@psu.edu
# Collaborator: Andrew Ou ajo5499@psu.edu
# Collaborator: Michael Sullivan mls6888@psu.edu
# Section: 1
# Breakout: 8

def getLetterGrade(num):
  if(num >= 93):
    return "A"
  elif(num >= 90):
    return "A-"
  elif(num >= 87):
    return "B+"
  elif(num >= 83):
    return "B"
  elif(num >= 80):
    return "B-"
  elif(num >= 77):
    return "C+"
  elif(num >= 70):
    return "C"
  elif(num >= 60):
    return "D"
  else:
    return "F"

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print("Your letter grade for CMPSC 131 is " +(getLetterGrade(grade)) + ".")

if __name__ == "__main__":
  run()
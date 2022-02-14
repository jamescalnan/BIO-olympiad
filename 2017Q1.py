#https://www.olympiad.org.uk/papers/2017/bio/bio17-exam.pdf

def printLine(input, spacing):
  print("." * spacing + "".join(letter + " " for letter in input))

def addColours(colour1, colour2):
  if (colour1 == "R" and colour2 == "G") or (colour1 == "G" and colour2 == "R"):
    return "B"
  elif (colour1 == "R" and colour2 == "B") or (colour1 == "B" and colour2 == "R"):
    return "G"
  elif (colour1 == "B" and colour2 == "G") or (colour1 == "G" and colour2 == "B"):
    return "R"
  else:
    return colour1


userInput = input("Input: ")

currentLine = []

for letter in userInput:
  currentLine.append(letter)

printLine(currentLine, len(userInput) - len(currentLine))

while len(currentLine) > 1:
  nextLine = []
  for i in range(len(currentLine) - 1):
    valueUnder = addColours(currentLine[i], currentLine[i + 1])
    nextLine.append(valueUnder)
  currentLine = nextLine
  printLine(currentLine, len(userInput) - len(currentLine))
  

print(currentLine[0])

#functions:
# pass a variable into the funtion
# the function returns a variable

#R G
#condition: if "R" and "G" -> "B"
#->



#def addColours(listOFTHING):
#   return listOFTHING[0] if listOFTHING.count(listOFTHING[0]) == 2 else list({"R", "G", "B"} - set(listOFTHING))[0]
#nigger
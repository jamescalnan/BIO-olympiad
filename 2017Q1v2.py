def addColours(listOFTHING):
  return listOFTHING[0] if listOFTHING.count(listOFTHING[0]) == 2 else list(set(["R","B","G"]) - set(listOFTHING))[0]

user = input()
line = [letter for letter in user]
nextLine = []

while len(line) > 1:
  nextLine = []
  for i in range(len(line)-1):
    nextLine.append(addColours([line[i], line[i+1]]))
  line = nextLine

print(nextLine[0])
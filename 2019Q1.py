def isPalindrome(inputStr):
  return True if inputStr == inputStr[::-1] else False

def addNumber(listVer, pos2):
  nextValue = str(int(listVer[pos2]) + 1)
  if nextValue == "10":
    nextValue = "0"
    addNumber(listVer, pos2-1)

  listVer[pos2] = nextValue

def just9(inputStr):
  for letter in inputStr:
    if letter != "9":
      return False
  return True

def nextHighestPalindrome(inputStr):
  listVer = [letter for letter in inputStr]

  if inputStr == "9":
    return "11"
  elif len(inputStr) == 1:
    return str(int(inputStr) + 1)
  elif just9(inputStr):
    new = ["0"] * (len(inputStr) + 1)
    new[0] = "1"
    new[len(inputStr)] = "1"
    return "".join(new)

  pos1, pos2 = 0, len(listVer) - 1

  while "".join(listVer) == inputStr or not isPalindrome(listVer):
    if "".join(listVer) == inputStr:
      addNumber(listVer, pos2)
    elif listVer[pos1] == listVer[pos2]:
      pos1 += 1
      pos2 -= 1
    else:
      addNumber(listVer, pos2)

  return "".join(listVer)

print(nextHighestPalindrome("789"))
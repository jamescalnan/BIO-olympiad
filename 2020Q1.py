import time
conversions = {
  "I"   : 1,
  "IV"  : 4,
  "V"   : 5,
  "IX"  : 9,
  "X"   : 10,
  "XL"  : 40,
  "L"   : 50,
  "XC"  : 90,
  "C"   : 100,
  "CD"  : 400,
  "D"   : 500,
  "CM"  : 900,
  "M"   : 1000
}


def convert(number):
  romanNumeral = ""
  for k, v in reversed(conversions.items()):
    if number >= v:
      amount = number - number % v
      romanNumeral += k * int(amount / v)
      number -= amount
  return romanNumeral

def lookandsay(userInput):
  result = ""
  listVer = userInput
  count = 0
  prev = listVer[0]

  for letter in listVer:
    if letter != prev:
      result += f"{convert(count)}{prev}"
      prev = letter
      count = 1
    else:
      count += 1

  result += f"{convert(count)}{prev}"
  
  return result

def iterations(userInput):
  result = userInput.split(" ")[0]
  for i in range(int(userInput.split(" ")[1])):
    result = lookandsay(result)
  return f"{str(result.count('I'))} {str(result.count('V'))}"

while True:
  userInput = input("input: ")
  start = time.time()
  print(iterations(userInput))
  print(f"Time taken: {time.time() - start}")
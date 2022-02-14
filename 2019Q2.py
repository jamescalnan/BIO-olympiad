"""
doesn't work on all tests
fails on two tests due to recursion depth being reached, retried again on a higher recursion depth but repl crashes around 33000, probably shouldnt use recursion at this point
fails on 2 other tests for unknown reasons 
"""

while True:
  user = input("")
  trailLife = int(user.split(" ")[0])
  moves = [letter for letter in user.split(" ")[1]]
  moveCount = int(user.split(" ")[2])

  (x,y) = (0,0)
  direction = "N"
  directions = {"N": (0,1), "E" : (1,0), "S" : (0,-1), "W" : (-1,0)}
  ad = ["N", "E", "S", "W"]
  previousLocations = [(0,0)]

  def getNewDir(direction, move, ad):
    return ad[(ad.index(direction) + 3) % len(ad)] if move == "L" else ad[(ad.index(direction) + 1) % len(ad)]

  def tryMove(direction, move, pL, x, y, directions, ad):
    if move != "F":
      direction = getNewDir(direction, move, ad)
    tX, tY = (x + directions[direction][0], y + directions[direction][1])
    if move == "F":
      if (tX, tY) in pL:
        return tryMove(getNewDir(direction, "R", ad), "F", pL, x, y, directions, ad)
      else:
        return tX, tY, direction
    elif move == "L":
      if (tX, tY) in pL:
        return tryMove(getNewDir(direction, "R", ad), "F", pL, x, y, directions, ad)
      else:
        return tX, tY, direction
    elif move == "R":
      if (tX, tY) in pL:
        return tryMove(getNewDir(direction, "R", ad), "F", pL, x, y, directions, ad)
      else:
        return tX, tY, direction
    return None

  i = 0
  while i < moveCount:
    for move in moves:
      i += 1
      x,y,direction = tryMove(direction, move, previousLocations, x, y, directions, ad)
      
      previousLocations.append((x,y))
      if i > trailLife-2:
        previousLocations.pop(0)
      if i > moveCount-1:
        i += moveCount + 1
        break
        
  print(f"({x}, {y})")
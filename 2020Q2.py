"""
not full mark solution, takes slightly more than 1 second to execute on longest input, still works though
"""

import time
def subtractLists(completePlan, plan):
  return list(sorted(list(set(completePlan) - set(plan))))

def getRoomNotInPlan(completePlan, plan, previouslyChosen):
  roomsNotInPlanSorted = subtractLists(completePlan, plan)
  availableRooms = subtractLists(roomsNotInPlanSorted,previouslyChosen)
  firstRoom = availableRooms.pop(0)
  plan.pop(0)
  previouslyChosen.append(firstRoom)
  return firstRoom

def makeConnections(completePlan, plan):
  connections = []
  while len(plan) > 0:
    connections.append((plan[0], getRoomNotInPlan(completePlan, plan, previouslyChosen)))
  
  finalTwoRooms = subtractLists(completePlan, previouslyChosen)
  connections.append((finalTwoRooms[0], finalTwoRooms[1]))  
  return connections

def returnConnections(connections, completePlan):
  connectionsReturn = []
  for room in completePlan:
    printStr = ""
    for room2 in connections:
      if room2[0] == room or room2[1] == room:
        printStr += room2[0] if room2[0] != room else room2[1]
    connectionsReturn.append(sorted(printStr))
  return connectionsReturn

def printConnections(dictconnections):
  for v in dictconnections.values():
    if len(v) == 0:
      continue
    print("".join(v))

def getRoomExits(dictConnections):
  temp = {}
  for key, value in dictConnections.items():
    tempDict = {}
    for val in value:
      tempDict[val] = 0
    temp[key] = tempDict
  return temp

def makeDictionaryConnections(completePlan, connections):
  newDict = {}
  for i, eachConnection in enumerate(returnConnections(connections, completePlan)):
    if len(eachConnection) == 0:
      continue
    newDict[completePlan[i]] = eachConnection
    i += 1
  return newDict

def getSpyLocation(connections, p, q, leaveCounts):
  valueAtP = 0
  valueAtQ = 0
  currentRoom = "A"

  roomCounts = {}
  
  for key, value in dictConnections.items():
      roomCounts[key] = 0
  
  roomCounts["A"] = 1
  count = 0
  while count < int(q):
    visitCount = roomCounts[currentRoom]

    leaveThrough = None

    if visitCount % 2 == 1:
      leaveThrough = connections[currentRoom][0]
    else:
      exits = connections[currentRoom]
      for i, exit in enumerate(exits):
        if leaveCounts[currentRoom][exit] % 2 == 1:
          if i == len(exits) - 1:
            leaveThrough = exit
            break
          else:
            leaveThrough = exits[i + 1]
            break
    
    leaveCounts[currentRoom][leaveThrough] += 1
    
    roomCounts[leaveThrough] += 1
    currentRoom = leaveThrough
    count += 1
    if int(p) == count:
      valueAtP = currentRoom
    if int(q) == count:
      valueAtQ = currentRoom
  return valueAtP, valueAtQ

def getpqLocations(dictConnections, p,q, roomExit):
  p,q = getSpyLocation(dictConnections, p, q, roomExit)
  return f"{str(p)}{str(q)}"

previouslyChosen = []

userInput = input("Input: ")
plan = [letter for letter in userInput.split(" ")[0]]
p = userInput.split(" ")[1]
q = userInput.split(" ")[2]
r = len(plan) + 2
completePlan = [chr(c + ord("A")) for c in range(r)]

connections = makeConnections(completePlan, plan)

dictConnections = makeDictionaryConnections(completePlan, connections)

roomExits = getRoomExits(dictConnections)
start = time.time()
printConnections(dictConnections)
print("\n"+getpqLocations(dictConnections, p, q, roomExits))
print(f"\ntime taken: {(time.time() - start)}")
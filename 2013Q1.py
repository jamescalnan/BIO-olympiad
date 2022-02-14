import datetime

def sameTime(clock1, clock2):
  return clock1.hour == clock2.hour and clock1.minute == clock2.minute

userInput = input("").split(" ")

processed = [int(i) for i in userInput]

clock1 = datetime.datetime(1,1,1,0,0,0)
clock2 = datetime.datetime(1,1,1,0,0,0)
clock1 += datetime.timedelta(hours=1, minutes=processed[0])
clock2 += datetime.timedelta(hours=1, minutes=processed[1])

while not sameTime(clock1, clock2):
  clock1 += datetime.timedelta(hours=1, minutes=processed[0])
  clock2 += datetime.timedelta(hours=1, minutes=processed[1])

hour = "0" if str(clock1.hour) == "0" else ""
hourPadding = "0" if len(str(clock1.hour)) == 1 and not str(clock1.hour) == "0" else ""
minute = "0" if str(clock1.minute) == "0" else ""
minutePadding = "0" if len(str(clock1.minute)) == 1 and not str(clock1.minute) == "0" else ""

print(f"{hourPadding}{str(clock1.hour)}{hour}:{minutePadding}{clock1.minute}{minute}\n\n")
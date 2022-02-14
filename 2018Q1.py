import math

debt = 10000
total_repaid = 0
interest, repay = (int(x) for x in input().split(" "))

while debt > 0:
    interest_month = math.ceil((interest / 100) * debt)

    debt += interest_month
    repaid = math.ceil((repay / 100) * debt)

    repaid = min(max(5000, repaid), debt)

    total_repaid += repaid
    debt -= repaid

print(total_repaid / 100)
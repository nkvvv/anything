import random
import time

colors = ['🟥','🟧','🟨','🟩','🟦','🟪','🟫']

while True:
    check_list = []
    for i in range(3):
        check_list.append(random.choice(colors))
    for x in check_list:
        print(x, end=' ')
    if all(x == check_list[0] for x in check_list):
        print(" - win\n")
        break
    else:
        print(" - looser\n")
    time.sleep(0.1)
import numpy as np
import random as rand

blank_card = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]

def generate_card(blank_card):
    column_one = rand.sample(range(1,16), 5)
    column_two = rand.sample(range(16, 31), 5)
    column_three = rand.sample(range(31, 46), 5)
    column_four = rand.sample(range(46, 61), 5)
    column_five = rand.sample(range(61, 76), 5)

    for x in range(0,5) :
        if column_one[x] < 10 :
            blank_card[x][0] = "{:02d}".format(column_one[x])
        else:
            blank_card[x][0] = column_one[x]
    for x in range(0,5) :
        blank_card[x][1] = column_two[x]
    for x in range(0,5) :
        blank_card[x][2] = column_three[x]
    for x in range(0,5) :
        blank_card[x][3] = column_four[x]
    for x in range(0,5) :
        blank_card[x][4] = column_five[x]

    blank_card[2][2] = "GO" # setting wild-spot
    return blank_card

while True:
    print("    B    I    N    G    O   ")
    print("  " + "-"*24)
    pop_card = generate_card(blank_card)
    print(str(np.matrix(pop_card))
          .replace("[", " ")
          .replace("]", " ")
          .replace("\'", "|"))
    input()

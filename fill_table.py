import random
l = [[], [], []]  # 1st square
g = [[], [], []]  # 2nd square
d = [[], [], []]  # 3d square
lg = [l, g, d]  # kinda 1st level

for sq in range(len(lg)):

    values = [i for i in range(1, 10)]  # available numbers for one square

    for line in range(len(lg[sq])):
        avail = []  # available especially for one list (line)
        for i in values:  # considering the remained numbers in "values"
            if line < len(lg[sq]) - 1:  # we add the possible numbers
                if i in lg[sq-1][line+1] and i not in lg[sq-1][line]:  # if the value is forbidden for the next line
                    avail.append(i)

        while len(avail) < 3:  # filling the rest of the space
            for i in values:
                if i not in lg[sq - 1][line]:  # if value was not already used on the same line (in the same list)
                    avail.append(i)

        for el in range(3):  # choosing from available
            lg[sq][line].append(random.choice(avail))
            avail.remove(lg[sq][line][el])
            values.remove(lg[sq][line][el])

for sq in range(3):
    print(l[sq], g[sq], d[sq], sep=" ")

columns = [
         [[l[0][0], l[1][0], l[2][0]],  # 0
          [l[0][1], l[1][1], l[2][1]],  # 1
          [l[0][2], l[1][2], l[2][2]],  # 2
          [g[0][0], g[1][0], g[2][0]]],  # 3

         [[g[0][0], g[1][0], g[2][0]],  # 3
          [g[0][1], g[1][1], g[2][1]],  # 4
          [g[0][2], g[1][2], g[2][2]],  # 5
          [d[0][0], d[1][0], d[2][0]]]  # 6
]  # for easier work with columns

q = [[], [], []]
w = [[], [], []]
qw = [q, w]

for sq in range(len(qw)):
    values = [i for i in range(1, 10)]

    for line in range(len(qw[sq])):

        for el in range(3):  # every column (element) will be checked for one line
            avails = []

            for a in values:

                if line < len(qw[sq])-1:  # if not the last line

                    if a in columns[sq][el + 1] and a not in columns[sq][el] and a in qw[sq - 1][line + 1] and a not in qw[sq - 1][line]:
                        avails.append(a)  # if a on next line and next column - the best variant

                    elif a in qw[sq][line+1] and a not in qw[sq-1][line]:
                        avails.append(a)  # if only on next line (if can't find desired a)

                    elif a in columns[sq][el + 1] and a not in columns[sq][el] and a not in qw[sq - 1][line]:
                        avails.append(a)  # if only on next column

                elif el < len(columns)-1 and line >= len(qw[sq])-1:  # if it's not the last element in square and it's
                    # the last line
                    if a in columns[sq][el + 1] and a not in columns[sq][el] and a not in qw[sq - 1][line]:
                        avails.append(a)  # for last line only column check is needed

            if len(avails) == 0:
                for a in values:
                    if a not in columns[sq][el] and a not in qw[sq - 1][line]:
                        avails.append(a)

            qw[sq][line].append(random.choice(avails))
            columns[sq][el].append(qw[sq][line][el])
            values.remove(qw[sq][line][el])  # -1 option for next elements

            print(sq, line, el, avails, qw[sq][line][el], sep=" : ")

for i in range(3):
    print(q[i], w[i], sep=" ")

#values = [i for i in range(1, 10)]
#for sp in l:
 #   for i in range(3):
  #      sp.append(str(random.choice(values)))
   #     values.remove(int(sp[i]))

#for sp in l:
 #   print(" ".join(sp))


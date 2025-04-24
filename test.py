# Brain Teaser: What will this print?
x = 5
y = 10

for i in range(1, x):               # Loop 1: Iterates from 1 to 4
    for j in range(y, x, -2):       # Loop 2: Iterates from 10 down to x (5) by steps of -2
        if i % 2 == 0:              
            print(i, j, "Even!")    # Prints if i is even
        else:
            print(i, j, "Odd!")     # Prints if i is odd
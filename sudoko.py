def print_sudoko(sudoko):
    print("+" + "---+"*9)
    for i, row in enumerate(sudoko):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        print("+" + "---+"*9)

def is_full(sudoko):
    for i in range(9):
        for j in range(9):
            if sudoko[i][j] == 0:
                return False
    return True

def inbox(sudoko,row,col,k):
    n = row // 3 * 3
    m = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoko[i + n][j + m] == k:
                return True
    return False

def incol(sudoko,col,k):
    for i in range(9):
        if sudoko[i][col] == k:
            return True
    return False

def inrow(sudoko,row,k):
    if k in sudoko[row]:
        return True
    return False

def is_safe(sudoko,row,col,k):
    if inrow(sudoko,row,k) or incol(sudoko,col,k) or inbox(sudoko,row,col,k):
        return False
    return True

def solve_sudoko(sudoko):

    if is_full(sudoko):
        return True
    for i in range(9):
        for j in range(9):
            if sudoko[i][j] == 0:
                for k in range(1,10):
                    if is_safe(sudoko,i,j,k):
                        sudoko[i][j] = k
                        if solve_sudoko(sudoko):
                            return True
                        sudoko[i][j] = 0
                return False

sudoko = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 1, 0, 0, 0, 3, 4, 8, 0],
    [0, 3, 9, 8, 0, 0, 2, 0, 0],
    [0, 6, 0, 3, 0, 4, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 6, 0, 7, 0, 4, 0],
    [0, 0, 8, 0, 0, 2, 1, 7, 0],
    [0, 2, 6, 7, 0, 0, 0, 9, 8],
    [0, 9, 0, 0, 0, 0, 0, 0, 0]
]

print("\n")
print("this is the sudoko you want to solve :")
print("\n")
print_sudoko(sudoko)
new = solve_sudoko(sudoko)
if new:
    print("\n")
    print("**********************************************************")
    print("\n")
    print("good job it worked !")
    print("\n")
    print_sudoko(sudoko)

else:
    print("\n")
    print("the sudoko you entered was invalid")
    print("\n")

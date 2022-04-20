# Utils to help in the main App

def againprompt():
    if int(input("Enter any key to continue, 0 to exit >> ")) == 0:
        return False
    else:
        return True


# get matrix input
def get_2Matrix():
    rows = int(input("Enter number of rows >> "))
    cols = int(input("Enter number of cols >> "))
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            mat[i][j] = int(input("Enter value " + str(j+1) + " for row "+ str(i+1) + ">> "))

    return mat


# get row total list from a matrix
def get_row_total(mat):
    row_list = []
    for i in range(0, len(mat)):
        total = 0
        for j in range(0, len(mat[i])):
            total += mat[i][j]
        row_list.append(total)

    return row_list


# get col total list from a matrix
def get_col_total(mat):
    col_list = []
    for i in range(0, len(mat[0])):
        total = 0
        for j in range(0, len(mat)):
            total += mat[j][i]
        col_list.append(total)

    return col_list

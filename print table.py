table1 = [["1.1", "1.2", "1.3", "1.4"], ["2.1", "2.2", "2.3", "2.4"], ["3.1", "3.2", "3.3", "3.4"], ["vjeijwos", "csk", "jcaoijc", "cjiq0cjzl1"]]
replace_list = ['[', ']', '"', "'"]


def print_table(table):
    col_width = len(table[0][0])
    for i in range(len(table)):
        for k in range(len(table[i])):
            current_width = len(table[k][i])
            if col_width < current_width:
                col_width = current_width
    for i in range(len(table)):
        for k in range(len(table[i])):
            if k == len(table[i])-1:
                print(table[k][i].rjust(col_width + 3))
            else:
                print(table[k][i].rjust(col_width + 3), end=" ")
    print("\nStroke width:" + str(col_width + 3))


print_table(table1)


def user_table():
    print("Enter value. \"Exit\" to end, \"change\" to change list level")
    current_table = []
    while True:
        current_value = input()
        if current_value == "Exit":
            break
        if current_value == "change":

        current_table.append(current_value)
        print(current_table)
        print("Enter value. \"Exit\" to end, \"change\" to change list level")
    return current_table


user_table()


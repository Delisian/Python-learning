theBoard = {"topL": " ", "topM": " ", "topR": " ",
            "midL": " ", "midM": " ", "midR": " ",
            "botL": " ", "botM": " ", "botR": " "}


def print_b(board):
    print(board["topL"] + "|" + board["topM"] + "|" + board["topR"])
    print("--+--+--")
    print(board["midL"] + "|" + board["midM"] + "|" + board["midR"])
    print("--+--+--")
    print(board["botL"] + "|" + board["botM"] + "|" + board["botR"])


def check(x):
    while True:
        try:
            theBoard[x]
        except KeyError:
            print("Enter space name.\n"
                  "\nFull list of names:"
                  "\ntop left: topL; "
                  "\ntop middle: topM;"
                  "\ntop right: topR;"
                  "\nmiddle left: midL;"
                  "\ncentral: midM;"
                  "\nmiddle right midR;"
                  "\nbottom left: botL;"
                  "\nbottom middle: botM;"
                  "\nbottom right: botR.")
            x = input()
            continue
        global move
        move = x
        break


turn = "X"


for i in range(9):
    print_b(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    while True:
        move = input()
        check(move)
        if theBoard[move] == "X" or theBoard[move] == "O":
            print("This place is already taken. Try another")
        else:
            break
    theBoard[move] = turn
    if (theBoard["topL"] == turn
            and theBoard["topM"] == turn        # first case
            and theBoard["topR"] == turn)\
            or (theBoard["midL"] == turn        # second case
                and theBoard["midM"] == turn
                and theBoard["midR"] == turn)\
            or (theBoard["botL"] == turn        # third case
                and theBoard["botM"] == turn
                and theBoard["botR"] == turn) \
            or (theBoard["topL"] == turn        # fourth case
                and theBoard["midL"] == turn
                and theBoard["botL"] == turn)\
            or (theBoard["topM"] == turn        # fifth case
                and theBoard["midM"] == turn
                and theBoard["botM"] == turn)\
            or (theBoard["topR"] == turn        # sixth case
                and theBoard["midR"] == turn
                and theBoard["botR"] == turn)\
            or (theBoard["topL"] == turn        # seventh case
                and theBoard["midM"] == turn
                and theBoard["botR"] == turn)\
            or (theBoard["topR"] == turn        # eighth case
                and theBoard["midM"] == turn
                and theBoard["botL"] == turn):
        print("The " + turn + " won. Congratulations!")
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    if i == 9:
        print("Draw!")

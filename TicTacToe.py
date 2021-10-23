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
    if theBoard["topL"]:
        print("The" + turn + "won. Congratulations!")
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    if i == 9:
        print("Draw!")



def DayTwoP2(w,y):
    opCode = [1,w,y,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
    length = len(opCode) + 1
    x = 0

    while x <= length:
        if opCode[x] == 1:
            opCode[opCode[(x + 3)]] = opCode[opCode[(x + 1)]] + opCode[opCode[(x + 2)]]
            x += 4
        elif opCode[x] == 2:
            opCode[opCode[(x + 3)]] = opCode[opCode[(x + 1)]] * opCode[opCode[(x + 2)]]
            x += 4
        elif opCode[x] == 99:
            print(opCode)
            print("99 encountered, ending")
            return opCode[0]
        else:
            print("coding error, probably")
w = 78
y = 70
while True:
    check = DayTwoP2(w,y)
    if check == 19690720:
        print(w,y)
        break
    else:
        w += 0
        y += 1

def main():
    msg = str(raw_input("Enter msg : "))
    msg = list(msg)

    while len(msg) <= 9:
        msg.append('a')

    arr = [[0 for x in range(3)] for x in range(3)]

    c = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = msg[c]
            c+=1

    new = []
    new1 = [0 for x in range(9)]
    c = 0
    new = [arr[i] for i in range(2,-1,-1)]
    for i in range(3):
        for j in range(3):
            new1[c] = new[i][j]
            c+=1
    print ("encrypted text is : ")
    print (str(new1).replace(",",'')[1:-1])

    c = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = new1[c]
            c+=1

    c = 0
    new = [arr[i] for i in range(2,-1,-1)]
    for i in range(3):
        for j in range(3):
            new1[c] = new[i][j]
            c+=1
    print ("decrypted text is : ")
    print (str(new1).replace(",",'')[1:-1])


if __name__ == '__main__':
    main()

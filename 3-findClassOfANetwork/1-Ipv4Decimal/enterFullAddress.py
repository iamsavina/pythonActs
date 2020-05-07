usrIn = input("Enter your ip address in decimal format: ")

rec = usrIn.split(".")

firstOct = int(rec[0])
if firstOct<0 or firstOct>255:
    print("Wrong input - Enter valid number")
else:
    if firstOct<128:
        print("Class A IP address")
    elif firstOct<192:
        print("Class B IP adrrres")
    elif firstOct<224:
        print("Class C Ip address")
    elif firstOct<240:
        print("Class D Ip address")
    else:
        print("Class E IP address")
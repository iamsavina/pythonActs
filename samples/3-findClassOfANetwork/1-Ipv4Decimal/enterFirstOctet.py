usrIn = int(input("Enter first octet of the IP address in Deciaml Format : "))

if usrIn<0 or usrIn>255:
    print("Wrong input - Enter valid number")
else:
    if usrIn<128:
        print("Class A IP address")
    elif usrIn<192:
        print("Class B IP adrrres")
    elif usrIn<224:
        print("Class C Ip address")
    elif usrIn<240:
        print("Class D Ip address")
    else:
        print("Class E IP address")
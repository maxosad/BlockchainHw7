import hashlib
import sys


f = open(sys.argv[1],"r")
numbilets =     int (sys.argv[2]) 
parameter = sys.argv[3] 



for line in f:
    spl = line.split()
    firstName = spl[0]
    secondName = spl[1]

    fio = firstName.join([secondName,parameter])
    fioByte = bytes(fio, 'utf-8')
    hash_object = hashlib.sha3_512(fioByte)
    hex_dig = hash_object.hexdigest()
    h = int(hex_dig,16)
    ticket = h%numbilets + 1
    print(f"{firstName} {secondName} {ticket}")


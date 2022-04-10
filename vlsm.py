ip = input()
mtmp = ip.partition("/")
prefix = int(mtmp[2])
adresy = 2**(32 - prefix)
hosti = adresy - 2
stmp = mtmp[0].split(".")
tmp = 0
count = 4
bytes = [128, 64, 32, 16, 8, 4, 2, 1]
moct = 0
#while count != 0:
#    print(format(int(stmp[tmp]), "08b"))
#    print(format(int(prefix), "08b"))
#    count = count -1
#    tmp = tmp + 1

for x in range(0, 4):
    for y in range(0 ,int(prefix/8)):
        if int(prefix%8) > 0:
            moct = 0
            for count in range(0,int(prefix%8)):
                moct = moct + bytes[count]
                print(moct)
        elif int(prefix%8) == 0 and int(prefix/8) != 3:
            print(0)

#print("Síť: ", sit)
print("Počet Adres:", adresy)
print("Počet Hostů:", hosti)
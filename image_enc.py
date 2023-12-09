with open('img.jpg', 'rb',) as file:
    imgbytefile = file.read()

declist1 = list(imgbytefile)

f3 = ''

for i in declist1:
    j = bin(i)
    number = int(j[2:])
    k = "%08d" % (number,)
    f3 += k

# encode
encstr = ''

# print(f3)

c1 = 0
c0 = 0

for i2 in f3:
    
    if i2 == '0':
        c0 += 1

    elif i2 == '1' and i2 != f3[-1]:
        encstr += str(c0)
        c0 = 0
    if i2 == f3[-1]:
        encstr += str(c0)
        c0 = 0

print(len(encstr))
print(encstr)


# decode convertion process
declist2 = []


def binarytodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal

# print(binarytodecimal(int(f3)))


for m in range(1, int(len(f3)), 8):
    m1, m2 = m - 1, m + 7
    bin1 = f3[m1:m2]
    declist2.append(binarytodecimal(int(bin1)))

imgbyte2 = bytes(declist2)

with open('close1.jpg', 'wb') as f4:
    f4.write(imgbyte2)

# import pyperclip

# Open image as Read-Binary type
with open('testpdf.pdf','rb',) as file:
    imgbytefile=file.read()

declist1=list(imgbytefile)

# print(declist1)

binary_value=''

for i in declist1:
    j=bin(i)
    number=int(j[2:])
    k="%08d" % (number,)
    binary_value+=k

# pyperclip.copy(binary_value)

# print(binary_value)
print(len(binary_value))

#encode
encstr=''

def zerocal():
    global encstr
    # if binary_value[0]=='0':
    #     encstr+="1"

current_value=None
current_count=0

for i in binary_value:
    if current_value == i:
        current_count+=1
        print(current_value,current_count)
    
    # elif current_value==None:
    else:
        current_value=i
        current_count=0
        current_count+=1    

# zerocal()
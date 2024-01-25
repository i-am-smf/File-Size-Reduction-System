from tkinter import *

main=Tk()
main.title("File Compression System")
main.geometry("500x600")
main.resizable(False,False)

# File size redusion system using Binary Conversion


main.mainloop()


def filetobin():
    with open('image.png', 'rb',) as file:
        img_byte_file = file.read()
    file.close()

    img_dec_list_open = list(img_byte_file)

    img_bin_string = ''

    for i in img_dec_list_open:
        j = bin(i)
        number = int(j[2:])
        k = "%08d" % (number,)
        img_bin_string += k
    return img_bin_string

def binarytodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n//10
        decimal += rem*power
        power = power*2
    
    return decimal

def bintofile():
    img_dec_list_save = []
    data=filetobin()
    for m in range(1, int(len(data)), 8):
        m1, m2 = m - 1, m + 7
        bin1 = data[m1:m2]
        img_dec_list_save.append(binarytodecimal(int(bin1)))
    imgbyte2 = bytes(img_dec_list_save)

    with open('close.jpg', 'wb') as f4:
        f4.write(imgbyte2)

bintofile()
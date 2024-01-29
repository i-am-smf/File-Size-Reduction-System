from tkinter import *
from tkinter import filedialog,simpledialog
from PIL import Image
import sys

main=Tk()
main.title("File Size Reduction System")
main.geometry("500x600")
main.resizable(False,False)

iconImage = PhotoImage(file="image.gif",format="gif")

Label(main,text="Welcome to \nFile Size Reduction System",font=("Arial Bold",20),justify=CENTER,image=iconImage).place(relx=0.14,rely=0.1)


def reduce_size():
    file=filedialog.askopenfile()
    print(file)

def increase_size():
    file=filedialog.asksaveasfile(confirmoverwrite=True)


reduce_size_button=Button(main,text="Reduce Size",command=lambda:reduce_size(),width=10,height=2,activebackground="#C6E2FF").place(relx=0.2,rely=0.4)
increace_size_button=Button(main,text="Increase Size",command=lambda:increase_size(),width=10,height=2,activebackground="#C6E2FF").place(relx=0.6,rely=0.4)

# main.mainloop()

class FileProcess:

    def filetobin(self):
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

    def binarytodecimal(self,n):
        decimal = 0
        power = 1
        while n > 0:
            rem = n % 10
            n = n//10
            decimal += rem*power
            power = power*2
        
        return decimal

    def bintofile(self):
        img_dec_list_save = []
        data=self.filetobin()
        for m in range(1, int(len(data)), 8):
            m1, m2 = m - 1, m + 7
            bin1 = data[m1:m2]
            img_dec_list_save.append(self.binarytodecimal(int(bin1)))
        imgbyte2 = bytes(img_dec_list_save)

        with open('close.jpg', 'wb') as f4:
            f4.write(imgbyte2)

fp=FileProcess()
data=fp.filetobin()

print(len(data))
sys.set_int_max_str_digits(965208)

data=int(data)/99

print(len(data))
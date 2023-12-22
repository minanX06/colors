from tkinter import *

root = Tk()
root.title("색깔 추천 프로그램")
root.configure(background="#E4E4E4")
root.geometry("720x540+275+50")
root.resizable(False, False)

hex_loc = 0
similar = [-15, -7, 7, 15]

def angle(R, G, B):
    global hex_loc
    Origin = [R, G, B]
    Convert = [R, G, B]
    lst = [R, G, B]
    lst.sort()

    min = Origin.index(lst[0])
    mid = Origin.index(lst[1])
    max = Origin.index(lst[2])

    if Origin[min] + Origin[max] <= 255:
        Convert[mid] = int(255*Origin[mid]/(Origin[max]+Origin[min]))
    else:
        Convert[mid] = int((Origin[min]+Origin[max]-255)*Origin[mid]/255)
    Convert[min] = 0
    Convert[max] = 255

    if Convert.index(255) == 0:
        a_set = set([1, 6])
    elif Convert.index(255) == 1:
        a_set = set([2, 3])
    else:
        a_set = set([4, 5])
    
    if Convert.index(0) == 0:
        b_set = set([3, 4])
    elif Convert.index(0) == 1:
        b_set = set([5, 6])
    else:
        b_set = set([1, 2])

    hex_loc = list(a_set & b_set)[0] - 1
    return int((hex_loc + hex_loc%2)*60 + ((-1)**hex_loc)*Convert[mid]/255*60)%360

def distance(R, G, B):
    lst = [R, G, B]
    lst.sort()
    M = lst[2]
    m = lst[0]
    return 510-M-m

def chroma(R, G, B):
    lst = [R, G, B]
    lst.sort()
    M = lst[2]
    m = lst[0]
    return (M-m)/(255-abs(M+m-255))*100

def convert(a, d, c):
    global hex_loc
    lst = []
    for i in range(1, 4):
        lst.append((((((a//60)//3)*7 + ((-1)*((a//60)//3)*2+1)*(3-((a//60)%3)))//2**i)%2)*255 + ((-2)*((a//60)%2)+1)*((pow(2, int(4-(a//60)%3))//4)%2)*int((a%60)*17/4))
    lst.sort()
    M = int((c/100*(255-abs(d-255)) + (510-d))/2)
    m = 510-d-M
    A = lst[1]
    if hex_loc == 0:
        code = hex_reverse[M//16] + hex_reverse[M%16] + hex_reverse[A//16] + hex_reverse[A%16] + hex_reverse[m//16] + hex_reverse[m%16]
    elif hex_loc == 1:
        code = hex_reverse[A//16] + hex_reverse[A%16] + hex_reverse[M//16] + hex_reverse[M%16] + hex_reverse[m//16] + hex_reverse[m%16]
    elif hex_loc == 2:
        code = hex_reverse[m//16] + hex_reverse[m%16] + hex_reverse[M//16] + hex_reverse[M%16] + hex_reverse[A//16] + hex_reverse[A%16]
    elif hex_loc == 3:
        code = hex_reverse[m//16] + hex_reverse[m%16] + hex_reverse[A//16] + hex_reverse[A%16] + hex_reverse[M//16] + hex_reverse[M%16]
    elif hex_loc == 4:
        code = hex_reverse[A//16] + hex_reverse[A%16] + hex_reverse[m//16] + hex_reverse[m%16] + hex_reverse[M//16] + hex_reverse[M%16]
    elif hex_loc == 5:
        code = hex_reverse[M//16] + hex_reverse[M%16] + hex_reverse[m//16] + hex_reverse[m%16] + hex_reverse[A//16] + hex_reverse[A%16]

    return '#' + str(code)

def change():
    RGB = color_entry.get()
    RGB = RGB[-6:]

    R = RGB[0:2]
    R = 16*hexadecimal[str(R[0])] + hexadecimal[str(R[1])]

    G = RGB[2:4]
    G = 16*hexadecimal[str(G[0])] + hexadecimal[str(G[1])]

    B = RGB[4:6]
    B = 16*hexadecimal[str(B[0])] + hexadecimal[str(B[1])]
    
    label_1.config(text=convert(angle(R, G, B) + similar[0], distance(R, G, B), chroma(R, G ,B)))
    label_1.config(bg=convert(angle(R, G, B) + similar[0], distance(R, G, B), chroma(R, G ,B)))
    label_2.config(text=convert(angle(R, G, B) + similar[1], distance(R, G, B), chroma(R, G ,B)))
    label_2.config(bg=convert(angle(R, G, B) + similar[1], distance(R, G, B), chroma(R, G ,B)))
    label_3.config(text=convert(angle(R, G, B) + similar[2], distance(R, G, B), chroma(R, G ,B)))
    label_3.config(bg=convert(angle(R, G, B) + similar[2], distance(R, G, B), chroma(R, G ,B)))
    label_4.config(text=convert(angle(R, G, B) + similar[3], distance(R, G, B), chroma(R, G ,B)))
    label_4.config(bg=convert(angle(R, G, B) + similar[3], distance(R, G, B), chroma(R, G ,B)))

    label_5.config(bg="#" + RGB)

hexadecimal = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
hex_reverse = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

color_label = Label(root, text='enter the color', font=("G마켓 산스 Bold", 10), bg='#E4E4E4')
color_entry = Entry(root, width=15, relief='flat', bg="#D0CECE", font=("G마켓 산스 Bold", 10))
check_btn = Button(root, bg="#E4E4E4", bd=0, relief="flat", overrelief="flat", activebackground="#E4E4E4", text='Convert!', font=("G마켓 산스 Bold", 10), command=change)
label_1 = Label(root, width=13, height=10, bg="#D4D4D4", font=("G마켓 산스 Bold", 10))
label_2 = Label(root, width=13, height=10, bg="#D4D4D4", font=("G마켓 산스 Bold", 10))
label_3 = Label(root, width=13, height=10, bg="#D4D4D4", font=("G마켓 산스 Bold", 10))
label_4 = Label(root, width=13, height=10, bg="#D4D4D4", font=("G마켓 산스 Bold", 10))
label_5 = Label(root, width=19, height=10, bg="#D4D4D4")

color_label.place(x=302, y=180)
color_entry.place(x=290, y=200)
check_btn.place(x=440, y=200)
label_1.place(x=20, y=300)
label_2.place(x=200, y=300)
label_3.place(x=380, y=300)
label_4.place(x=560, y=300)
label_5.place(x=80, y=80)

root.mainloop()
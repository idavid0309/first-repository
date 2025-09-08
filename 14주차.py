##ex.1
##import matplotlib.pyplot as plt
##Y=[13.5, 17.2, 15.9, 21.6, 23.4, 29.1, 32.3]
##plt.plot(Y)
##plt.show()


##ex.2
##import matplotlib.pyplot as plt
##X = [ "Jan", "Feb", "Mar", "April", "May", "Jun", "July" ]
##Y= [13.5, 17.2, 15.9, 21.6, 23.4, 29.1, 32.3]
##
##plt.plot(X,Y)
##plt.xlabel ("Month")
##plt.ylabel ("PM25")
##plt.show()


##ex.3
##import matplotlib.pyplot as plt
##X = [ "Jan", "Feb", "Mar", "April", "May", "Jun", "July" ]
##Y1= [13.5, 17.2, 15.9, 21.6, 23.4, 29.1, 32.3]
##Y2 = [9.4, 32.4, 18.9, 20.7, 19.8, 34.7, 26.7]
##plt.plot(X, Y1, label="Gumi")
##plt.plot(X, Y2, label=" Daejon")
##plt.xlabel("Month")
##plt.ylabel("Pm25")
##plt.legend(loc="lower right")
##plt.title("PM2.5 Dust")
##plt.show()


##ex.4
##import matplotlib.pyplot as plt
##x, y, z = [], [], []
##for i in range(100):
##    x.append(i/50.0)
##for i in x:
##    y.append(i**2)
##for i in x:
##    z.append(i**3)
##    
##plt.plot(x, x, label="linear")
##plt.plot(x, y, label="quadratic")
##plt.plot(x, z, label="cubic")
##
##plt.xlabel("input")
##plt.ylabel("output")
##plt.legend(loc="upper left")
##plt.title(" Function")
##plt.show()


##ex.5
##from PIL import Image,ImageTk # PIL 모듈에서 클래스 불러오기
##import tkinter as tk # tkinter 모듈 포함
##
###윈도우 생성하고 윈도우 안에 캔버스 생성
##window =tk.Tk()
##canvas =tk.Canvas (window, width=500, height=500)
##canvas.pack()
##
###윈도우를 생성하고 윈도우 안에 캔버스를 생성한다 .
##img= Image.open ("lenna.png")
##
###tk 형식으로 영상을 변환한다 .
##tk_img= ImageTk.PhotoImage(img)
##
###tkinter 의 캔버스에 영상을 표시한다 .
##canvas.create_image(250, 250,image=tk_img)
##
##window.mainloop()


##ex.6
import tkinter as tk

def open():
    pass

def quit():
    window.quit()
    
window =tk.Tk()
m =tk.Menu (window)
fm= tk.Menu (m)

m.add_cascade(label="파일 ",menu=fm ) # 탭 메뉴 생성

fm.add_command(label=" 열기 ", command=open) # 하위 메뉴 생성
fm.add_command(label="종료 ", command=quit)

window.config(menu=m)
window.mainloop()

from PIL import Image,ImageTk ,ImageFilter
import tkinter as tk
from tkinter import filedialog as fd

im= None
tk_img= None

#파일 메뉴에서 열기”를 선택하였을 때 호출되는 함수
def open():
    global im , tk_img
    fname= fd.askopenfilename()
    im= Image.open(fname)
    tk_img= ImageTk.PhotoImage(im)
    canvas.create_image(250, 250,image=tk_img)
    window.update()
    
#파일 메뉴에서 종료”를 선택하였을 때 호출되는 함수
def quit():
    window.quit()

#영상처리 메뉴에서 회전”을 선택하였을 때 호출되는 함수
def image_rotate():
    global im , tk_img
    out =im.rotate (45)
    tk_img= ImageTk.PhotoImage(out)
    canvas.create_image(250, 250,image=tk_img)
    window.update()

#영상처리 메뉴에서 흐리게”를 선택하였을 때 호출되는 함수
def image_blur():
    global im , tk_img
    out =im.filter(ImageFilter.BLUR)
    tk_img= ImageTk.PhotoImage (out)
    canvas.create_image(250, 250,image=tk_img)
    window.update()

#윈도우를 생성한다
window =tk.Tk()
canvas =tk.Canvas (window, width=500, height=500)
canvas.pack()

#메뉴를 생성한다 .
m =tk.Menu (window) # root 메뉴 생성
filemenu= tk.Menu(m) # 파일 메뉴 생성
ipmenu= tk.Menu(m) # 영상처리 메뉴생성
m.add_cascade(label="파일",menu=filemenu)
m.add_cascade(label="영상처리",menu=ipmenu)

filemenu.add_command( label="열기 ", command=open)
filemenu.add_command( label="종료 ", command=quit)
ipmenu.add_command( label="영상회전 ", command=image_rotate)
ipmenu.add_command( label="영상흐리게 ", command=image_blur)
                    
window.config(menu=menubar)
window.mainloop()

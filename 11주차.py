##Ex.1
##infile= open("phones.txt", "r")
##lines =infile.read ()
##print(lines)

##infile= open("phones.txt", "r")
##lines =infile.readlines ()
##print(lines)

##infile= open("phones.txt", "r")
##lines =infile.readlines ()
##print(lines[0]) 

##infile= open("phones.txt", "r")
##
##for line in infile:
##             data =line.rstrip () # 개행문자 제거
##             print(data)
##infile.close()

##text = '1111Water boils at 100 degrees 11'
##print(text.lstrip ('1'))
##print(text.rstrip ('1'))
##print(text.strip ('1'))

##ex.2
##outfile= open("phones1.txt", "w")
##outfile.write("홍길동 010 1234 5678\n")
##outfile.write("김철수 010 1234 5679\n")
##outfile.write("김영희 010 1234 5680\n")
##outfile.close()

##outfile= open("phones1.txt", "a")
##outfile.write("강감찬 010 1234 5681 \n")
##outfile.write("김유신 010 1234 5682 \n")
##outfile.write("정약용 010 1234 5683 \n")
##outfile.close()


##ex.3
##infile= open("proverbs.txt", "r")
##for line in infile:
##             sentence = line.rstrip () # 한
##             word_list= sentence.split()
##             for word in word_list :
##                    print(word)
##infile.close()


##ex.4
##import csv
##
##f = open('weather.csv')
##data =csv.reader(f)
##header = next(data)
##for row in data:
##    print(row)
##f.close
##input()

##import csv #좋은 문제
##f = open('weather.csv')
##data =csv.reader(f)
##header = next(data)
##temp = 1000
##for row in data:
##    if temp > float(row[3]):
##        temp = float(row[3])
##print(temp)
##f.close
##input()


##ex.5
##import random
##
##guesses = ''
##turns = 10
##
##infile= open("words.txt", "r")
##lines =infile.readlines ()
##word =random.choice (lines)
##             
##print("정답:",word)
##while turns > 0:
##    failed = 0
##    for char in word:
##        if char in guesses:
##            print(char, end="")
##        else:
##            print("_", end="")
##            failed += 1
##        print("failed:", failed)
##       if failed == 0:
##           print("사용자승리")
##           break


##ex.6
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
window = Tk()
text = Text(window, height=30, width=80)
text.pack()
def save():
    print()
def open():
    file = filedialog.askopenfile(parent=window, mode='r')
    if file != None:
        lines = file.read()
        text.insert('1.0', lines)
        file.close()
def saveas():
    print()
def edit():
    print()
def copy():
    print()
def paste():
    print()
def delete():
    print()

    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None:
        lines = text.get('1.0', END+'-1c')
        file.write(lines)
        file.close()
        
def exit():
    if messagebox.askokcancel("Quit", "종료하시겠습니까?"):
        window.destroy()
        
def about():
    label = messagebox.showinfo("About", "메모장 프로그램")
    
m = Menu(window)
window.config(menu=m)

filemenu = Menu(m)
m.add_cascade(label="파일", menu=filemenu)

m.add_command(label="새로운 이름으로 저장", command=saveas)
m.add_command(label="편집", command=edit)
m.add_command(label="복사", command=copy)
m.add_command(label="추가", command=paste)
m.add_command(label="삭제", command=delete)

m.add_command(label="열기", command=open)
m.add_command(label="저장하기", command=save)
filemenu.add_command(label="종료", command=exit)

helpmenu = Menu(m)
m.add_cascade(label="도움말", menu=helpmenu)

helpmenu.add_command(label="프로그램 정보",
command=about)

window.mainloop()

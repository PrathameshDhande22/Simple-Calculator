""" 
# Made by Prathamesh Dhande
# Version 1.2
# Since 1/03/2022 """

from tkinter import *
import os

class Calculator(Tk):
    global history
    def __init__(self):
        super().__init__()
        self.title("Calculator by Prathamesh")
        self.resizable(0, 0)
        self.geometry("285x420")
        self.configure(bg='black')
        self.wm_iconbitmap("calci.ico")

    # makes the button and entry widget to enter
    def makingGui(self):
        # making the userentry field
        self.textfield = StringVar()
        self.userfield = Entry(
            self, textvariable=self.textfield, font='lucida 28', relief='solid', bd=2,state='disabled',bg='black',fg='white')

        # making the radiobutton
        self.rad = Radiobutton(self, text="OFF", font='calibri 10 bold', command=self.off,
                               value=0, padx=3)
        self.rad.select()               
        self.rad.place(x=5, y=3)
        self.rad = Radiobutton(self, text="ON", font='calibri 10 bold', command=self.on,
                               value=1, padx=3).place(x=64, y=3)
                   
        # making the div1 button
        self.div1 = Frame(self, bg='black')
        self.backspace=Button(self.div1,text="DEL",font='calibri 16',padx=6,pady=6,state='disabled',bg='orange')
        self.clear=Button(self.div1,text="AC",font='calibri 16',padx=11,pady=6,state='disabled',bg='orange')
        self.doublezero=Button(self.div1,text="%",font='calibri 16 bold',padx=16,pady=6,state='disabled',bg='black',fg='orange')
        self.multiply=Button(self.div1,text="*",font='calibri 16',padx=16,pady=6,state='disabled',bg='black',fg='orange')

        # making the div2 button
        self.div2 = Frame(self, bg='black')
        self.sevenbtn=Button(self.div2,text="7",font='calibri 16',padx=16,pady=6,state='disabled',bg='black',fg='white')
        self.eightbtn=Button(self.div2,text="8",font='calibri 16',padx=17,pady=6,state='disabled',bg='black',fg='white')
        self.ninebtn=Button(self.div2,text="9",font='calibri 16',padx=18,pady=6,state='disabled',bg='black',fg='white')
        self.plus=Button(self.div2,text="+",font='calibri 16 bold',padx=16,pady=6,state='disabled',bg='black',fg='orange')

        # making the div3 button
        self.div3 = Frame(self, bg='black')
        self.fourbtn=Button(self.div3,text="4",font='calibri 16',padx=16,pady=6,state='disabled',bg='black',fg='white')
        self.fivebtn=Button(self.div3,text="5",font='calibri 16',padx=17,pady=6,state='disabled',bg='black',fg='white')
        self.sixbtn=Button(self.div3,text="6",font='calibri 16',padx=18,pady=6,state='disabled',bg='black',fg='white')
        self.minus=Button(self.div3,text="-",font='calibri 16 bold',padx=18,pady=6,state='disabled',bg='black',fg='orange')

        # making the div4 button
        self.div4 = Frame(self, bg='black')
        self.onebtn=Button(self.div4,text="1",font='calibri 16',padx=16,pady=6,state='disabled',bg='black',fg='white')
        self.twobtn=Button(self.div4,text="2",font='calibri 16',padx=17,pady=6,state='disabled',bg='black',fg='white')
        self.threebtn=Button(self.div4,text="3",font='calibri 16',padx=18,pady=6,state='disabled',bg='black',fg='white')
        self.divide=Button(self.div4,text="/",font='calibri 16 bold',padx=17,pady=6,state='disabled',bg='black',fg='orange')

        # making the div5 button
        self.div5 = Frame(self, bg='black')
        self.dotbtn=Button(self.div5,text=".",font='calibri 16 bold',padx=19,pady=6,state='disabled',bg='orange')
        self.zerobtn=Button(self.div5,text="0",font='calibri 16 bold',padx=17,pady=6,state='disabled',bg='black',fg='white')
        self.equal=Button(self.div5,text="=",font='calibri 16 bold',padx=52,pady=6,state='disabled',bg='red')
        Label(text="Developed By Prathamesh Dhande",font="calibri 9 bold",bg='black',fg='white').place(x=2,y=402)
        
        # binding all the button
        self.backspace.bind("<Button-1>",self.click)
        self.clear.bind("<Button-1>",self.click)
        self.doublezero.bind("<Button-1>",self.click)
        self.multiply.bind("<Button-1>",self.click)
        self.sevenbtn.bind("<Button-1>",self.click)
        self.eightbtn.bind("<Button-1>",self.click)
        self.ninebtn.bind("<Button-1>",self.click)
        self.plus.bind("<Button-1>",self.click)
        self.fourbtn.bind("<Button-1>",self.click)
        self.fivebtn.bind("<Button-1>",self.click)
        self.sixbtn.bind("<Button-1>",self.click)
        self.minus.bind("<Button-1>",self.click)
        self.onebtn.bind("<Button-1>",self.click)
        self.twobtn.bind("<Button-1>",self.click)
        self.threebtn.bind("<Button-1>",self.click)
        self.divide.bind("<Button-1>",self.click)
        self.dotbtn.bind("<Button-1>",self.click)
        self.zerobtn.bind("<Button-1>",self.click)
        self.equal.bind("<Button-1>",self.click)
    
        # packing all the button,text
        self.userfield.pack(fill='both', padx=6, pady=32)
        self.div1.place(x=3,y=85)
        self.backspace.pack(side=LEFT,padx=5,pady=5)
        self.clear.pack(side=LEFT,padx=5,pady=5)
        self.doublezero.pack(side=LEFT,padx=5,pady=5)
        self.multiply.pack(side=LEFT,padx=5,pady=5)

        self.div2.place(x=3,y=148)
        self.sevenbtn.pack(side=LEFT,padx=5,pady=5)
        self.eightbtn.pack(side=LEFT,padx=5,pady=5)
        self.ninebtn.pack(side=LEFT,padx=5,pady=5)
        self.plus.pack(side=LEFT,padx=5,pady=5)

        self.div3.place(x=3,y=211)
        self.fourbtn.pack(side=LEFT,padx=5,pady=5)
        self.fivebtn.pack(side=LEFT,padx=5,pady=5)
        self.sixbtn.pack(side=LEFT,padx=5,pady=5)
        self.minus.pack(side=LEFT,padx=5,pady=5)

        self.div4.place(x=3,y=275)
        self.onebtn.pack(side=LEFT,padx=5,pady=5)
        self.twobtn.pack(side=LEFT,padx=5,pady=5)
        self.threebtn.pack(side=LEFT,padx=5,pady=5)
        self.divide.pack(side=LEFT,padx=5,pady=5)

        self.div5.place(x=3,y=340)
        self.dotbtn.pack(side=LEFT,padx=5,pady=5)
        self.zerobtn.pack(side=LEFT,padx=5,pady=5)
        self.equal.pack(side=LEFT,padx=5,pady=5)

    # this function disabled all the button
    def off(self):
        self.userfield['state']=DISABLED
        self.backspace['state']=DISABLED
        self.clear['state']=DISABLED
        self.doublezero['state']=DISABLED
        self.multiply['state']=DISABLED
        self.sevenbtn['state']=DISABLED
        self.eightbtn['state']=DISABLED
        self.ninebtn['state']=DISABLED
        self.plus['state']=DISABLED
        self.fourbtn['state']=DISABLED
        self.fivebtn['state']=DISABLED
        self.sixbtn['state']=DISABLED
        self.minus['state']=DISABLED
        self.onebtn['state']=DISABLED
        self.twobtn['state']=DISABLED
        self.threebtn['state']=DISABLED
        self.divide['state']=DISABLED
        self.dotbtn['state']=DISABLED
        self.zerobtn['state']=DISABLED
        self.equal['state']=DISABLED
        self.textfield.set('')

    # this fuction active all the button when the self.rad button is clicked
    def on(self):
        self.userfield['state']=NORMAL
        self.clear['state']=NORMAL
        self.backspace['state']=NORMAL
        self.doublezero['state']=NORMAL
        self.multiply['state']=NORMAL
        self.sevenbtn['state']=NORMAL
        self.eightbtn['state']=NORMAL
        self.ninebtn['state']=NORMAL
        self.plus['state']=NORMAL
        self.fourbtn['state']=NORMAL
        self.fivebtn['state']=NORMAL
        self.sixbtn['state']=NORMAL
        self.minus['state']=NORMAL
        self.onebtn['state']=NORMAL
        self.twobtn['state']=NORMAL
        self.threebtn['state']=NORMAL
        self.divide['state']=NORMAL
        self.dotbtn['state']=NORMAL
        self.zerobtn['state']=NORMAL
        self.equal['state']=NORMAL
        self.textfield.set("")

    # perform when a button is clicked
    def click(self,event):
        text=event.widget.cget("text")
        if text=="=":
            gettext=self.textfield.get()
            try:
                if '%' in gettext:
                    j=gettext.replace("%","/100")
                    self.finalno=eval(j)
                    self.textfield.set(self.finalno)
                else:
                    self.finalno=eval(self.textfield.get())
                    self.textfield.set(self.finalno)
            except:
                self.textfield.set("Error")
        elif text=="AC":
            self.textfield.set("")
        elif text=="DEL":
            self.no=self.textfield.get()
            self.no=self.no[0:len(self.no)-1]
            self.textfield.set(self.no)
        else:
            self.textfield.set(self.textfield.get()+text)


if __name__ == "__main__":
    gui = Calculator()
    gui.makingGui()
    gui.mainloop()
    


from tkinter import * ##  biblioteca para utilização de GUI
class imcCaculator:
    def __init__(self,master):
        self.widgetA=Frame(master)
        self.widgetB=Frame(master)
        self.widgetC=Frame(master)
        self.widgetD=Frame(master)
        self.widgetA.pack()
        self.widgetB.pack()
        self.widgetC.pack()
        self.widgetD.pack()
        self.title=Label(self.widgetA, text='Bem vindo ao IMC Calculator',font=('Verdana','16','bold'),height=3,fg='darkblue')
        self.title.pack()
        self.font1=('Verdana','14','bold')
        self.font2=('Verdana','13')
        self.msgA=Label(self.widgetB,text='Altura: ',font=self.font1,width=8)
        self.msgA.pack(side=LEFT)
        self.height=Entry(self.widgetB,width=10,font=self.font2)
        self.height.focus_force()
        self.height.pack(side=LEFT)
        self.msgB = Label(self.widgetC, text='Peso: ', font=self.font1, width=8)
        self.msgB.pack(side=LEFT)
        self.weight = Entry(self.widgetC, width=10, font=self.font2)
        self.weight.pack(side=LEFT)
        self.calculator=Button(self.widgetD,font=self.font1,text='Calcular',bg='sienna1',command=self.imc)
        self.calculator.pack()
    def imc(self):
        self.window = Toplevel()
        self.display = Label(self.window, text='Resultado',font=self.font1)
        self.display.pack()
        self.getHeight=float(self.height.get())
        self.getWeight=float(self.weight.get())
        if self.getHeight > 100:
            self.getHeight=self.getHeight/100
            self.result=self.getWeight/(self.getHeight*self.getHeight)
        else:
            self.result=self.getWeight/(self.getHeight*self.getHeight)
        if self.result <= 18.5:
            self.display2 = Label(self.window,
                text='O seu IMC é {:.2f} você está abaixo do peso ideal, por favor procure um médico.'.format(self.result)
                ,font=self.font2,bg='red',heigh=3,width=100)
            self.display2.pack()
        elif self.result >= 18.6 and self.result <= 24.9:
            self.display2 = Label(self.window,
            text='O seu IMC é {:.2f} você está no peso ideal, PARABÉNS.'.format(
            self.result), font=self.font2, bg='green', heigh=3, width=100)
            self.display2.pack()
        elif self.result >=25.0 and self.result <= 29.9:
            self.display2 = Label(self.window,
            text='O seu IMC é {:.2f} você está levemente acima do peso, procure fazer exercícios.'.format(
             self.result), font=self.font2, bg='yellow', heigh=3, width=100)
            self.display2.pack()
        else:
            self.display2 = Label(self.window,
            text='O seu IMC é {:.2f} você está acima do peso, procure fazer exercícios e um médico.'.format(
             self.result), font=self.font2, bg='red', heigh=3, width=100)
            self.display2.pack()

root=Tk()
imcCaculator(root)
root.mainloop()
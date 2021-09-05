from tkinter import *
from tkinter import ttk
import numpy as np
import sys
import os
import Problem
 
 
class NumberSense:
 
    def __init__(self, root):
        root.title("Number Sense")
 
        self.content = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.frame1 = ttk.Frame(self.content, borderwidth=5,
                                relief="ridge", width=600, height=800)
        self.frame2 = ttk.Frame(self.content, borderwidth=5,
                                relief="ridge", width=600, height=800)
 
        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frame1.grid(column=0, row=0, columnspan=1,
                         rowspan=2, sticky=(N, S, E, W))
        self.frame2.grid(column=1, row=0, columnspan=1,
                         rowspan=2, sticky=(N, S, E, W))
 
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=3, minsize=600)
        self.content.columnconfigure(1, weight=3, minsize=600)
        self.content.rowconfigure(1, weight=3, minsize=800)
 
        self.frame1.columnconfigure(0, weight=3, minsize=300)
        self.frame1.columnconfigure(1, weight=3, minsize=300)
 
        self.p = Problem.Problem()
        self.problems = [self.p.p1, self.p.p2,
                         self.p.p3, self.p.p4, self.p.p5, self.p.p6]
        # Add new problems here by calling method in Problem instance
 
        self.q1()
 
    def q1(self):
        self.porc = ""
        self.press = False
 
        def Porc(x):
            self.porc = x
            for i in self.frame1.winfo_children():
                i.destroy()
            self.q2()
 
        q1 = ttk.Label(
            self.frame1, text="Would you like a printed test or to take on this application?")
        Print_entry = ttk.Button(
            self.frame1, text="Print", command=lambda: Porc("false"))
        Console_entry = ttk.Button(
            self.frame1, text="Application", command=lambda: Porc("true"))
 
        q1.grid(column=0, row=0, columnspan=2, rowspan=1,
                sticky=(N, S, E, W), padx=200, pady=15)
        Print_entry.grid(column=0, row=1, columnspan=1, rowspan=1,
                         sticky=(N, S, E, W), padx=15, pady=15)
        Console_entry.grid(column=1, row=1, columnspan=1, rowspan=1,
                           sticky=(N, S, E, W), padx=15, pady=15)
 
    def q2(self):
 
        q1 = ttk.Label(
            self.frame1, text="How many questions would you like? Pick a number from 1 to {0}".format(str(len(self.problems))))
        # How many questions would you like? Pick a number from 1 to "+str(len(problems))
 
        self.ans = StringVar()
        ans_entry = ttk.Entry(self.frame1, width=10, textvariable=self.ans)
 
        def next():
            self.num = int(self.ans.get())
            if(self.num != None and self.num < (len(self.problems)+1) and self.num > 0):
                for i in self.frame1.winfo_children():
                    i.destroy()
                self.q3()
 
        ok = ttk.Button(
            self.frame1, text="Okay", command=next)
 
        q1.grid(column=0, row=0, columnspan=2, rowspan=1,
                sticky=(N, S, E, W), padx=180, pady=15)
        ans_entry.grid(column=0, row=1, columnspan=2, rowspan=1,
                       sticky=(N, S, E, W), padx=325, pady=15)
        ok.grid(column=0, row=2, columnspan=2, rowspan=1,
                sticky=(N, S, E, W), padx=180, pady=15)
        ans_entry.focus()
 
    def q3(self):
        for i in range(len(self.problems)):
            # This is a random int from 0 to the last index
            rand = np.random.randint((len(self.problems)-1))
            ind1 = self.problems[i]  # Saving the ith index value
            ind2 = self.problems[rand]  # Saving the random index value
            # Replacing the ith index value with the random one
            self.problems[i] = ind2
            # Replacing the radom index value with the ith one
            self.problems[rand] = ind1
 
        if(self.porc == "true"):
            def show():
                self.q4()
            q1 = ttk.Label(
                self.frame1, text="Problems")
            show_answers = ttk.Button(
                self.frame1, text="Show Answers", command=show)
 
            q1.grid(column=0, row=0, columnspan=2, rowspan=1,
                    sticky=(N, S, E, W), padx=350, pady=15)
            show_answers.grid(column=0, row=self.num+2, columnspan=2, rowspan=1,
                              sticky=(N, S, E, W), padx=325, pady=15)
 
            for i in range(self.num):
                prob = "{0}. {1}".format(i+1, self.problems[i]())
                ttk.Label(
                    self.frame1, text=prob).grid(column=0, row=i+1, columnspan=2, rowspan=1,
                                                 sticky=(N, S, E, W), padx=100, pady=15)
        else:
            q1 = ttk.Label(
                self.frame1, text="Check folder for question and answer files")
 
            q1.grid(column=0, row=0, columnspan=2, rowspan=1,
                    sticky=(N, S, E, W), padx=180, pady=15)
            file = open(os.path.join(
                sys.path[0], "PrintedTest.txt"), "w")
            for i in range(self.num):
                prob = "{0}. {1}".format(i+1, self.problems[i]())
                file.write(prob+"\n")
            file.close()
 
            f = open(os.path.join(sys.path[0], "Answers.txt"), "w")
            for i in range(self.num):
                # dequeue stack here for answers
                f.write(str(i+1) + ". "+str(self.p.answers.dequeue()) + "\n")
            f.close()
 
        def show():
            for i in self.frame1.winfo_children():
                i.destroy()
            for i in self.frame2.winfo_children():
                i.destroy()
            self.__init__(root)
 
            # restarting mechanism
 
        restart = ttk.Button(
            self.frame1, text="Take test again?", command=show)
        restart.grid(column=0, row=self.num+3, columnspan=2, rowspan=1,
                     sticky=(N, S, E, W), padx=180, pady=15)
 
    def q4(self):
        q1 = ttk.Label(
            self.frame2, text="Answers")
        q1.grid(column=0, row=0, columnspan=2, rowspan=1,
                sticky=(N, S, E, W), padx=350, pady=15)
        for i in range(self.num):
            # change for queue;counter for answer number
            prob = "{0}. {1}".format(i+1, self.p.answers.dequeue())
            lab = ttk.Label(
                self.frame2, text=prob).grid(column=0, row=i+1, columnspan=2, rowspan=1,
                                             sticky=(N, S, E, W), padx=100, pady=15)
 
 
root = Tk()
NumberSense(root)
root.mainloop()



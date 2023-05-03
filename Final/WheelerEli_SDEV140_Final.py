import tkinter as tk                
from tkinter import font as tkfont  





global route
route = []



class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, American, Italian, Greek, smallServing,
                  largeServing, LessThanTen, MoreThanTen, MoreThanThirty,
                  LessThanThirty):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    

# START PAGE

class StartPage(tk.Frame):
    route = []
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def AmericanRt():
            controller.show_frame("American")
            route.append("American")
            print(route[:])
        
        def ItalianRt():
            controller.show_frame("Italian")
            route.append("Italian")
            print(route[:])
        
        def GreekRt():
            controller.show_frame("Greek")
            route.append("Greek")
            print(route[:])

        
        label = tk.Label(self, text="What's For Dinner?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        americanBtn = tk.Button(self, text="American",
                            command=AmericanRt)
        italianBtn = tk.Button(self, text="Italian",
                            command=ItalianRt)
        greekBtn = tk.Button(self, text="Greek",
                            command=GreekRt)
        americanBtn.pack()
        italianBtn.pack()
        greekBtn.pack()

# PAGE ONE CLUSTER - AMERICAN, ITALIAN, GREEK ----------------------------
class American(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def largeRt():
            controller.show_frame("largeServing")
            route.append("Large")
            print(route[:])
        
        def smallRt():
            controller.show_frame("smallServing")
            route.append("Small")
            print(route[:])
        
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        label = tk.Label(self, text="American", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        moreBtn = tk.Button(self, text="More than 4", command=largeRt)
        moreBtn.pack()

        lessBtn = tk.Button(self, text="Less than 4", command=smallRt)
        lessBtn.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()



class Greek(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def largeRt():
            controller.show_frame("largeServing")
            route.append("Large")
            print(route[:])
        
        def smallRt():
            controller.show_frame("smallServing")
            route.append("Small")
            print(route[:])
        
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        label = tk.Label(self, text="Greek", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        moreBtn = tk.Button(self, text="More than 4",
                            command=largeRt)
        moreBtn.pack()

        lessBtn = tk.Button(self, text="Less than 4",
                            command=smallRt)
        lessBtn.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()


class Italian(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def largeRt():
            controller.show_frame("largeServing")
            route.append("Large")
            print(route[:])
        
        def smallRt():
            controller.show_frame("smallServing")
            route.append("Small")
            print(route[:])
        
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        label = tk.Label(self, text="Italian", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        moreBtn = tk.Button(self, text="More than 4",
                            command=largeRt)
        moreBtn.pack()

        lessBtn = tk.Button(self, text="Less than 4",
                            command=smallRt)
        lessBtn.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()

# PAGE TWO CLUSTER - SMALL SERVING, LARGE SERVING ----------------------------
class smallServing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def moreRt():
            controller.show_frame("MoreThanTen")
            route.append("More")
            print(route[:])
        
        def lessRt():
            controller.show_frame("LessThanTen")
            route.append("Less")
            print(route[:])

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        label = tk.Label(self, text="Small Serving", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="Would you like to spend more or less than 10 dollars?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="MORE",
                            command=moreRt)           
        button1.pack()

        button2 = tk.Button(self, text="LESS",
                            command=lessRt)           
        button2.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()

class largeServing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def moreRt():
            controller.show_frame("MoreThanTen")
            route.append("More")
            print(route[:])
        
        def lessRt():
            controller.show_frame("LessThanTen")
            route.append("Less")
            print(route[:])

        def startOver():
            controller.show_frame("StartPage")
            route.clear()


        label = tk.Label(self, text="Large Serving", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="Would you like to spend more or less than 10 dollars?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="MORE", command=moreRt)           
        button1.pack()

        button2 = tk.Button(self, text="LESS", command=lessRt)           
        button2.pack()


        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()



# PAGE THREE CLUSTER - LESS THAN 10 DOLLARS, MORE THAN TEN DOLLARS ----------------------------
class LessThanTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def moreThan():
            controller.show_frame("MoreThanThirty")
            route.append("More than 30")
            
        
        def lessThan():
            controller.show_frame("LessThanThirty")
            route.append("Less than 30")
            

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        label = tk.Label(self, text="Less than 10 dollars", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="How long would you like total cook time to be?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="More than 30 minutes", command=moreThan)           
        button1.pack()

        button2 = tk.Button(self, text="Less than 30 minutes", command=lessThan)           
        button2.pack()


        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()

class MoreThanTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def moreThan():
            controller.show_frame("MoreThanThirty")
            route.append("More than 30")
            
        
        def lessThan():
            controller.show_frame("LessThanThirty")
            route.append("Less than 30")
            for i in route[:]:
                text = tk.Text(self)
                text.insert(tk.END, "Dish Type: " + route[0] + "\n" +
                    "Serving Size: " + route[1] + "\n" +
                    "More or less than 10 dollars: " + route[2] + "\n" +
                    "More or less than 30 minute prep time: " + route[3])
                text.pack()
            print(route[:])
            

        def startOver():
            controller.show_frame("StartPage")
            route.clear()
            
        label = tk.Label(self, text="More than 10 dollars", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="How long would you like total cook time to be?",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="More than 30 minutes", command=moreThan)           
        button1.pack()

        button2 = tk.Button(self, text="Less than 30 minutes", command=lessThan)           
        button2.pack()

        

        button = tk.Button(self, text="Go to the start page",
                           command=startOver)
        button.pack()

###
###
# PAGE FOUR CLUSTER - MORE THAN THIRTY MINUTES, LESS THAN THIRTY MINUTES ----------------------------
###

class MoreThanThirty(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def startOver():
            controller.show_frame("StartPage")
            route.clear()
        

            
        label = tk.Label(self, text="These are your choices!", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="",
                           font=("Helvetica", 14))
        label2.pack(side="top", fill="x", pady=10)

        # button1 = tk.Button(self, text="Generate Recipe", command=moreThanThirty)           
        # button1.pack()

        
        button = tk.Button(self, text="Start over",
                           command=startOver)
        button.pack()

class LessThanThirty(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        

        label = tk.Label(self, text="These are your choices!", font=controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        # text = tk.Text(self)
        # text.insert("Dish Type:", route[0],
        #             "\nServing Size:", route[1],
        #             "\nMore or less than 10 dollars:", route[2],
        #             "\nMore or less than 30 minute prep time:", route[3])
        
        
        # text.pack(side="top", fill="x", pady=10)
        # def totals():
            # for i in route[:]:
            #     text.insert(tk.END, "Dish Type: " + route[0] + "\n" +
            #         "Serving Size: " + route[1] + "\n" +
            #         "More or less than 10 dollars: " + route[2] + "\n" +
            #         "More or less than 30 minute prep time: " + route[3] + "\n\n")
        # totals()

        # label2 = tk.Label(self, text="", 
        #                    font=("Helvetica", 14),
        #                    command=totals)
        # label2.pack(side="top", fill="x", pady=10)

        # button1 = tk.Button(self, text="Generate Recipe!", command=moreThanThirty)           
        # button1.pack()



        # route print check
        print(route[:])

        button = tk.Button(self, text="Start over",
                           command=startOver)
        button.pack()



if __name__ == "__main__":
    app = App()
    app.mainloop()

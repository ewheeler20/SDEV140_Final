import tkinter as tk                
from tkinter import font as tkfont  
from tkinter.ttk import *

from tkinter import *
from PIL import Image, ImageTk

 

      

route = []

class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the title font
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic" )

        # Set the window size
        self.geometry("400x250")
        
        
        # Set the button font
        self.button_font =tkfont.Font(font = ('calibri', 12, 'bold', 'underline'),
                foreground = 'red')

        # Create a container for all the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        

        
        # Create a dictionary to hold all the frames
        self.frames = {}

        # Add all the frames to the dictionary
        for F in (StartPage, American, Italian, Greek, smallServing,
                  largeServing, LessThanTen, MoreThanTen, MoreThanThirty,
                  LessThanThirty, ASLM, GSLM, ISLM):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page first
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    

# START PAGE

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        # American button function
        def AmericanRt():
            controller.show_frame("American")
            route.append("American")
            print(route[:])
        
        # Italian button function
        def ItalianRt():
            controller.show_frame("Italian")
            route.append("Italian")
            print(route[:])
        
        # Greek button function
        def GreekRt():
            controller.show_frame("Greek")
            route.append("Greek")
            print(route[:])

                
        # Display
        label = tk.Label(self, text="What's For Dinner?", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady=5)
        #American button
        americanBtn = tk.Button(self, text="American",
                                font= controller.button_font,
                                background='#F5E3D6',   
                                command=AmericanRt)
        #Italian buttons
        italianBtn = tk.Button(self, text="Italian",
                               font= controller.button_font,
                                background='#F5E3D6',
                            command=ItalianRt)
        #Greek button
        greekBtn = tk.Button(self, text="Greek",
                             font= controller.button_font,
                            background='#F5E3D6',
                            command=GreekRt)
        # Buttons
        americanBtn.pack(side="left", padx= 30, fill="x")
        italianBtn.pack(side="left", padx= 30, fill="x")
        greekBtn.pack(side="left", padx= 30, fill="x")
###
#
#
#
# PAGE ONE CLUSTER - AMERICAN, ITALIAN, GREEK ----------------------------
class American(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Set the background color of the frame
        self.configure(bg='#B76E69')
        

        # Define a function that will be called when the "More than 4" button is clicked
        def largeRt():
            controller.show_frame("largeServing")
            route.append("Large")
            print(route[:])
        
        # Define a function that will be called when the "Less than 4" button is clicked
        def smallRt():
            controller.show_frame("smallServing")
            route.append("Small")
            # route.remove("Large")
            print(route[:])

        # Define a function that will be called when the "Start over" button is clicked
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        # Create a label widget with text "American"
        label = tk.Label(self, text="American", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady=10)
        
        # Create another label widget with text "How many people are you cooking for?"
        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        # Create a button widget with text "More than 4"
        moreBtn = tk.Button(self, text="More than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=largeRt)
        moreBtn.pack(side="left", padx= 20, fill="x")

        # Create another button widget with text "Less than 4"
        lessBtn = tk.Button(self, text="Less than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=smallRt)
        lessBtn.pack(side="left", padx= 20, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 20, fill="x")



class Greek(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        

        #Functions for the button pushes
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

        #Display labels
        label = tk.Label(self, text="Greek", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        # Create a button widget with text "More than 4"
        moreBtn = tk.Button(self, text="More than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=largeRt)
        moreBtn.pack(side="left", padx= 20, fill="x")

        # Create another button widget with text "Less than 4"
        lessBtn = tk.Button(self, text="Less than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=smallRt)
        lessBtn.pack(side="left", padx= 20, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 20, fill="x")


class Italian(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        #Functions for the button pushes
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

        #display labels
        label = tk.Label(self, text="Italian", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="How many people are you cooking for?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        #button for more than 4
        moreBtn = tk.Button(self, text="More than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=largeRt)
        moreBtn.pack(side="left", padx= 20, fill="x")

        #Button for less than 4
        lessBtn = tk.Button(self, text="Less than 4",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=smallRt)
        lessBtn.pack(side="left", padx= 20, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 20, fill="x")

# PAGE TWO CLUSTER - SMALL SERVING, LARGE SERVING ----------------------------
class smallServing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        #Functions for the button pushes
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

        #display labels
        label = tk.Label(self, text="Small Serving", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="Would you like to spend more\n or less than 10 dollars?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=5)

        #button with text more
        button1 = tk.Button(self, text="MORE",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=moreRt)           
        button1.pack(side="left", padx= 30, fill="x")

        #Button with text less
        button2 = tk.Button(self, text="LESS",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=lessRt)           
        button2.pack(side="left", padx= 30, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 30, fill="x")

class largeServing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        #Functions for the button pushes
        def moreRt():
            controller.show_frame("MoreThanTen")
            route.append("More")
            # route.remove("Less")
            print(route[:])
        
        def lessRt():
            controller.show_frame("LessThanTen")
            route.append("Less")
            # route.remove("More")
            print(route[:])

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        #Display labels
        label = tk.Label(self, text="Large Serving", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="Would you like to spend more\n or less than 10 dollars?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        #Button for more
        button1 = tk.Button(self, text="MORE",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=moreRt)           
        button1.pack(side="left", padx= 30, fill="x")
        
        #Button for less
        button2 = tk.Button(self, text="LESS",
                             font= controller.button_font,
                                background='#F5E3D6',
                            command=lessRt)           
        button2.pack(side="left", padx= 30, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 30, fill="x")



# PAGE THREE CLUSTER - LESS THAN 10 DOLLARS, MORE THAN TEN DOLLARS ----------------------------
class LessThanTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        

        #Functions for the button pushes
        def moreThan():
            controller.show_frame("MoreThanThirty")
            route.append("More than 30")
            print(route[:])
        
        def lessThan():
            controller.show_frame("LessThanThirty")
            route.append("Less than 30")
            print(route[:])

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        #Display labels
        label = tk.Label(self, text="Less than 10 dollars", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="How long would you like\n total cook time to be?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        #Button for more than 30
        button1 = tk.Button(self, text="More than 30 minutes",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=moreThan)           
        
        #Button for less than 30
        button2 = tk.Button(self, text="Less than 30 minutes",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=lessThan)           
        

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                             font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button1.pack(side="bottom", fill="x")


class MoreThanTen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        
        #Functions for the button pushes
        def moreThan():
            route.append("More than 30")
            controller.show_frame("MoreThanThirty")
            if len(route[:]) == 4:
                if all(elem in route for elem in ["American","Small", "Less", "More than 30"]):
                    label2 = tk.Label(self, text=route[0]+ "\n"+
                                            route[1] + "\n"+
                                            route[2] + "\n"+
                                            route[3] + "\n",
                                            font=("Helvetica", 14, 'bold'),
                                            bg='#B76E69')
                    label2.pack()
                    print("Go for gold")
                print(route[:]) 
            else:
                print("The route does not contain all of the elements.")
            
            
        def lessThan():
            route.append("Less than 30")
            controller.show_frame("LessThanThirty")
            if len(route[:]) == 4:
                if all(elem in route for elem in ["American","Small", "Less", "Less than 30"]):
                    label2 = tk.Label(self, text=route[0]+ "\n"+
                                            route[1] + "\n"+
                                            route[2] + "\n"+
                                            route[3] + "\n",
                                            font=("Helvetica", 14, 'bold'),
                                            bg='#B76E69')
                    label2.pack()
                    print("Go for gold")
                print(route[:])
            else:
                print("The route does not contain all of the elements.")
                print(route[:])

        def startOver():
            controller.show_frame("StartPage")
            route.clear()
            
        #Display labels
        label = tk.Label(self, text="More than 10 dollars", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 10)

        label2 = tk.Label(self, text="How long would you like\n total cook time to be?",
                           font=("Helvetica", 14, 'bold'), bg='#B76E69')
        label2.pack(side="top", fill="x", pady=10)

        #More than 30 button
        button1 = tk.Button(self, text="More than 30 minutes",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=moreThan)           
        
        #Less than 30 button
        button2 = tk.Button(self, text="Less than 30 minutes",
                             font= controller.button_font,
                                background='#F5E3D6',
                             command=lessThan)           
        
        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                            font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="bottom", fill="x")
        button2.pack(side="bottom", fill="x")
        button1.pack(side="bottom", fill="x")
        
###
###
# PAGE FOUR CLUSTER - MORE THAN THIRTY MINUTES, LESS THAN THIRTY MINUTES ----------------------------
###

class MoreThanThirty(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        #Functions for the button pushes
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        #display labels
        label = tk.Label(self, text="These are your choices!", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 10)
        
        # Create button widget with text "Generate Recipe"
        button2 = tk.Button(self, text="Generate Recipe",
                            font= controller.button_font,
                                background='#F5E3D6',
                                command=lambda: controller.show_frame("ASLM")
                           )
        button2.pack(side="left", padx= 20, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                            font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 20, fill="x")

class LessThanThirty(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        
        #Functions for the button pushes
        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        
        label = tk.Label(self, text="These are your choices!", font=controller.title_font, background='#ADD8E6')
        label.pack(side="top", fill="x", pady = 5)

        
        # Create button widget with text "Generate Recipe"
        button2 = tk.Button(self, text="Generate Recipe",
                            font= controller.button_font,
                                background='#F5E3D6',
                                command=lambda: controller.show_frame("ASLM")
                           )
        button2.pack(side="left", padx= 20, fill="x")

        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                            font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.pack(side="left", padx= 20, fill="x")
        

############################################################
##
##
## Final Recipe Pages #######################################
##
#############################################################
##

class ASLM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        

        # Create the left container
        left_container = tk.Frame(self)
        left_container.grid(row=0, column=0)

        # Add a recipe label to the left container
        recipe_title = tk.Label(left_container, text="One-Pot American Goulash", font=controller.title_font, background='#ADD8E6')
        recipe_title.pack(side="top")

        # Add a picture to the right container
        max_width = 200
        pixels_x = 200
        pixels_y = 200

        img = Image.open("OnePotGoulash.gif")
        pixels_x, pixels_y = tuple([int(max_width/img.size[0] * x) for x in img.size])
        resized_image = img.resize((pixels_x, pixels_y))

        img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(left_container, image=img, background='#B76E69')
        label.image = img
        label.pack(side="top")

        recipe_label = tk.Label(left_container, text="1 pound ground beef \n1 onion, chopped\n 1 green bell pepper, chopped\n 2 cloves garlic, minced\n 1 (14.5 ounce) can diced tomatoes\n 1 (8 ounce) can tomato sauce\n 1 tablespoon Worcestershire sauce\n 1 teaspoon dried basil\n 1 teaspoon dried oregano\n 1/2 teaspoon salt\n 1/4 teaspoon black pepper\n 2 cups water\n 1 cup elbow macaroni\n"
                                "Instructions:\n\n"
                                "In a large pot or Dutch oven over medium-high heat, cook the ground beef until browned.\n"
                                "Add the onion, green bell pepper, and garlic and cook until the vegetables are tender.\n"
                                "Add the diced tomatoes (with their juice), tomato sauce, Worcestershire sauce, basil, oregano, salt, black pepper, and water to the pot.\n"
                                "Bring the mixture to a boil.\n"
                                "Add the elbow macaroni and stir well.\n"
                                "Reduce the heat to low and cover the pot.\n"
                                "Simmer for about 20 minutes, stirring occasionally until the macaroni is tender.", 
                                background='#B76E69',
                                font= ('bold'))
        recipe_label.pack(side="left")

        # Create the right container
        right_container = tk.Frame(self)
        right_container.grid(row=0, column=1)

        button2 = tk.Button(self, text="Greek Recipe",
                            font= controller.button_font,
                                background='#F5E3D6',
                                command=lambda: controller.show_frame("GSLM")
                           )
        button2.grid()
        

        
        # Place the Recipe class on the window
        # self.grid(row=1, column=0)

class GSLM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')
        

        # Create the left container
        left_container = tk.Frame(self)
        left_container.grid(row=0, column=0)

        # Add a picture to the right container
        max_width = 200
        pixels_x = 200
        pixels_y = 200

        img = Image.open("greekChickenSalad.gif")
        pixels_x, pixels_y = tuple([int(max_width/img.size[0] * x) for x in img.size])
        resized_image = img.resize((pixels_x, pixels_y))

        # Add a recipe label to the left container
        recipe_title = tk.Label(left_container, text="Greek Chicken Bowl", font=controller.title_font, background='#ADD8E6')
        recipe_title.pack(side="top")

        img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(left_container, image=img, background='#B76E69')
        label.image = img
        label.pack(side="top")


        
        recipe_label = tk.Label(left_container, text="1 pound boneless skinless chicken breasts\n"
                                                        "1/4 cup olive oil\n"
                                                        "2 cloves garlic, minced\n"
                                                        "1/4 cup lemon juice\n"
                                                        "1 tablespoon red wine vinegar\n"
                                                        "1 teaspoon dried oregano\n"
                                                        "1/2 teaspoon salt\n"
                                                        "1/4 teaspoon black pepper\n"
                                                        "1/2 cup Greek yogurt\n"
                                                        "2 cups cooked brown rice\n"
                                                        "2 cups chopped romaine lettuce\n"
                                                        "1 cup cherry tomatoes, halved\n"
                                                        "1/2 cup sliced cucumber\n"
                                                        "1/4 cup sliced red onion\n"
                                                        "Instructions:\n\n"
                                                        "In a large plastic zip bag, combine olive oil, garlic, lemon juice, red wine vinegar, oregano, Greek yogurt, salt and pepper.\n"
                                                        "Add chicken into the bag. Massage to make sure chicken is fully covered and marinate for at least 20 minutes, up to 12 hours.\n"
                                                        "Preheat oven to 375°F.\n"
                                                        "Remove chicken from marinade and discard remaining marinade.\n"
                                                        "Place chicken on a baking sheet lined with parchment paper\n"
                                                        "Bake for about 20 minutes, or until the internal temperature of the chicken reaches 165°F\n"
                                                        "Divide cooked brown rice among four bowls.\n"
                                                        "Top each bowl with chopped romaine lettuce, cherry tomatoes, sliced cucumber, sliced red onion and baked chicken.\n",
                                                        background='#B76E69',
                                                        font= ('bold'))
        recipe_label.pack(side='left')

        # Create the right container
        right_container = tk.Frame(self)
        right_container.grid(row=0, column=1)

        button2 = tk.Button(self, text="Italian Recipe",
                            font= controller.button_font,
                                background='#F5E3D6',
                                command=lambda: controller.show_frame("ISLM")
                           )
        button2.grid()

        # # Place the Recipe class on the window
        # self.grid(row=1, column=0)

class ISLM(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#B76E69')

        def startOver():
            controller.show_frame("StartPage")
            route.clear()

        # Create the left container
        left_container = tk.Frame(self)
        left_container.grid(row=0, column=0)

        # Add a picture to the right container
        max_width = 200
        pixels_x = 200
        pixels_y = 200

        img = Image.open("SausageAndPeppers.gif")
        pixels_x, pixels_y = tuple([int(max_width/img.size[0] * x) for x in img.size])
        resized_image = img.resize((pixels_x, pixels_y))

        # Add a recipe label to the left container
        recipe_title = tk.Label(left_container, text="Italian Sausage and Peppers", font=controller.title_font, background='#ADD8E6')
        recipe_title.pack(side="top")

        img = ImageTk.PhotoImage(resized_image)
        label = tk.Label(left_container, image=img, background='#B76E69')
        label.image = img
        label.pack(side="top")


        
        recipe_label = tk.Label(left_container, text="1 pound Italian sausage\n"
                                                        "1 red bell pepper, sliced\n"
                                                        "1 green bell pepper, sliced\n"
                                                        "1 onion, sliced\n"
                                                        "1/2 teaspoon salt\n"
                                                        "1/4 teaspoon black pepper\n"
                                                        "1/2 teaspoon dried basil\n"
                                                        "1/2 teaspoon dried oregano\n"
                                                        "1/4 teaspoon garlic powder\n"
                                                        "Instructions:\n\n"
                                                        "Preheat oven to 375°F.\n"
                                                        "In a large skillet over medium heat, cook sausage until browned on all sides.\n"
                                                        "Add sliced peppers and onions to the skillet.\n"
                                                        "Season with salt, black pepper, dried basil, dried oregano and garlic powder.\n"
                                                        "Cook for about 10 minutes, or until vegetables are tender.\n"
                                                        "Transfer the skillet to the oven and bake for about 10 minutes, or until sausage is cooked through.\n",
                                                        background='#B76E69',
                                                        font= ('bold'))
        recipe_label.pack()

        # Create the right container
        right_container = tk.Frame(self)
        right_container.grid(row=0, column=1)


        # Create button widget with text "Start over"
        button = tk.Button(self, text="Start over",
                            font= controller.button_font,
                                background='#F5E3D6',
                           command=startOver)
        button.grid()

        # # Place the Recipe class on the window
        # self.grid(row=1, column=0)
 
# class ALLM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')

# class GLLM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')

# class ILLM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')

# class ALSM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')

# class GLSM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')

# class ILSM(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.configure(bg='#B76E69')




if __name__ == "__main__":
    app = App()
    app.mainloop()

import time
import math
import datetime
import colorama
import art
import PySimpleGUI

def step_print(string): # creating a function for printing the menu in a more stylish way
    print(string)   
    # OPTIONAL: you could add sound effects with the vlc library here
    time.sleep(0.1) # time sleep function to pause the program for a splitsecond so the menu experience is better

main_loop = True # main loop for main menu

while main_loop == True:
    step_print("####################")
    step_print("#                  #")
    step_print("#                  #")
    step_print("#  W E L C O M E   #")
    step_print("#    i n  t h e    #")
    step_print("#    b r a v e     #")
    step_print("# n e w  W o r l d #")
    step_print("#                  #")
    step_print("#                  #")
    step_print("####################")
    step_print("(1) Dig in It (2) Dig Deeper (3) Dig more into the Depth (4) Get Out")
    choice = input("Choose: ")
    if   choice == "1":
        step_print("You chose 1")
        step_print("You begin Digging in it")
        #now menu1 somehow...
    elif choice == "2":
        step_print("You chose 2")
        step_print("Now You get Deeper in it")
        #now menu2 somehow...
    elif choice == "2":
        step_print("You chose 2")
        step_print("Now You get Deeper in it")
        #now menu2 somehow...
    elif choice == "3":
        step_print("You chose 3")
        step_print("Now You are to Deep in It! It's to Dark here, you can't see anything!")
        #now menu2 somehow...
    elif choice == "4":
        step_print("You chose 4")
        step_print("You Get Out")
        main_loop = False
    else:
        step_print("Invalid Input! unidentified Command!  Choose between 1-4!")

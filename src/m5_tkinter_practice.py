"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Timothy Li.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
from tkinter import Label
import math


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    root = tkinter.Tk()

    #Making the background yellow
    root.configure(bg='#feffbe', highlightcolor='#feffbe')
    root.geometry("500x500+500+100")

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # ------------------------------------------------------------------
    # DONE 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    button_1 = ttk.Button(frame1, text='Button 1')

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

    def print_hello():
        print("Hello")

    button_1['command'] = (lambda:print_hello())
    button_1.grid()

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    entry_1 = ttk.Entry(frame1)
    entry_1.grid()

    def get_entry(entry):
        text = entry.get()
        if text == 'ok':
            print('Hello')
        else:
            print('Goodbye')

    button_2 = ttk.Button(frame1, text='Print entry 1')
    button_2['command'] = (lambda:get_entry(entry_1))
    button_2.grid()

    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    entry_2 = ttk.Entry(frame1)
    entry_2.grid()

    def print_n(e_1,e_2):
        text = e_1.get()
        for i in range(int(e_2.get())):
            print(text)

    button_3 = ttk.Button(frame1, text='Print entry 2')
    button_3['command'] = (lambda: print_n(entry_1,entry_2))
    button_3.grid()

    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.title("CSSE 120")

    #text_1 = Label(frame1,text = 'Hello')

    def fun_1():
        print('Fun button 1 pressed')
        #text_1.configure(text='Clicked!')

    fun_button_1 = ttk.Button(frame1,text='Fun Button 1')
    fun_button_1['command'] = (lambda:fun_1())
    fun_button_1.grid()

    root.mainloop()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

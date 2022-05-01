from doctest import master
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import String_To_Morse
import Morse_To_Blink
import RPi.GPIO as GPIO

DEBUG = True




class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.close)
        self.master.title('SIT210-Task5.3D-RPiGUI')
        self.pack()
        self.stringToMorse = tk.StringVar()

        self.create_widgets()


    def close(self):
        print("Closing safely")
        GPIO.cleanup()
        self.master.destroy()

    def textToMorseConvert(self):
        stringLike = self.stringToMorse.get()
        if len(stringLike) > 12:
            print("String too long. Please enter a string under 12 characters.")
            return
        morseCode = String_To_Morse.ConvertToMorse(stringLike)
        if DEBUG: print(morseCode)
        Morse_To_Blink.ConvertToBlink(morseCode, 0.125)
        

    def create_widgets(self):
        std_font = tkinter.font.Font(family= 'Helvetica', size = 12)
        head_font = tkinter.font.Font(family= 'Helvetica', size = 16, weight="bold")
        ## Widgets
        
        # images make everything better
        '''tk.Label(self.master,
                    image=self.img).pack(side='top', fill='x', pady=15)'''

        tk.Label(self.master,
                text='Task 5.3D - Blink Morse code using GUI',
                font=head_font).pack(padx=15, pady=15)

        tk.Label(self.master,
                text="Enter message to convert to Morse Code Here:").pack(padx=15, pady=15)

        self.text_box = tk.Entry(self.master, textvariable=self.stringToMorse).pack(padx=15, pady=15)

        bottom_buttons = tk.Frame(self.master).pack(side='bottom', fill='both', expand=True)

        tk.Button(bottom_buttons,
         text='Enter',
          font=std_font,
           command= self.textToMorseConvert,
            height=1,
            width=8).pack(in_=bottom_buttons, side='left', pady=15, expand=True)

        tk.Button(bottom_buttons,
         text='Exit',
          font=std_font,
           command= self.close,
            height=1,
            width=8).pack(in_=bottom_buttons, side='right', pady=15, expand=True)





# temporary debugging


root = tk.Tk()
root.resizable(False,False)
app = Application(master=root)
app.mainloop()
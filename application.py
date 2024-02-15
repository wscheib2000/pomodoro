import tkinter as tk
from timer import Timer


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


class Main(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Pomodoro')
        self.config(padx=100, pady=50, bg=YELLOW)

        frame = Application(self, bg=YELLOW)
        frame.grid()
        self.mainloop()


class Application(tk.Frame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.canvas = tk.Canvas(self, width=200, height=224, bg=YELLOW, highlightthickness=0)
        master.tomato_img = tomato_img = tk.PhotoImage(file='./tomato.png')
        self.canvas.create_image(100, 112, image=tomato_img)
        self.timer = Timer()
        self.countdown_cycle = 0
        self.timer_text = self.canvas.create_text(100, 134, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
        self.canvas.grid(row=1, column=1)

        self.title_lbl = tk.Label(self, text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, width=5)
        self.title_lbl.grid(row=0, column=1)

        self.start_button = tk.Button(self, text='Start', command=lambda: self.start_timer(master), highlightthickness=0)
        self.start_button.grid(row=2, column=0)
            
        self.start_button = tk.Button(self, text='Reset', command=lambda: self.reset_timer(master), highlightthickness=0)
        self.start_button.grid(row=2, column=2)

        self.check_marks = tk.Label(self, fg=GREEN, bg=YELLOW)
        self.check_marks.grid(row=3, column=1)

    def update_labels(self):
        self.canvas.itemconfig(self.timer_text, text=f'{self.timer.printable_time()}')
        self.check_marks.config(text='✔'*((self.timer.reps-1)//2))
        match self.timer.mode:
            case 'Work':
                self.title_lbl.config(text='Work', fg=GREEN)
            case 'Long Break':
                self.title_lbl.config(text='Break', fg=RED)
            case 'Short Break':
                self.title_lbl.config(text='Break', fg=PINK)
            case _:
                self.title_lbl.config(text='Timer', fg=GREEN)

    def reset_timer(self, master):
        master.after_cancel(self.countdown_cycle)
        self.timer.reset_timer()
        self.update_labels()

    def start_timer(self, master):
        self.timer.start_timer()
        self.update_labels()
        self.countdown(master)

    def countdown(self, master):
        self.timer.decrement()
        self.update_labels()        
        if self.timer.time >= 0:
            self.countdown_cycle = master.after(250, self.countdown, master)
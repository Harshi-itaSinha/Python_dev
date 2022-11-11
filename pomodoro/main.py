from tkinter import *
#import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_label.config(text="Timer", fg=RED)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_label.config(text="BREAK", fg = PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_label.config(text="BREAK", fg=YELLOW)
    else:
        Timer_label.config(text="WORK",fg= RED)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = count//60
    sec = count % 60
    if(sec<10):
        sec = f"0{sec}"
    if(min<10):
        min = f"0{min}"

    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if(count>0):
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range (work_sessions):
            marks += "✓ "
        check_marks.config(text = marks)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50,bg=GREEN)


# def som(thing):
#     print(thing)
# window.after(1000,som,"Hello")

canvas = Canvas(width=200,height=224 ,bg=GREEN, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=tomato_img)
timer_text= canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

start_button=Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

#start_button.pack(side=right)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

Timer_label=Label(text="Timer",fg=RED,font=(FONT_NAME,50),bg=GREEN)
Timer_label.grid(column=1,row=0)

check_marks =Label(text=" ",fg=RED,bg=GREEN)
check_marks.grid(column=1,row=3)


canvas.grid(column=1,row=1)
#count_down(5)
window.mainloop()

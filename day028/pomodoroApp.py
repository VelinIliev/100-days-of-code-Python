import tkinter 
import time 

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_marks = 0 
timer = None

# reset mehanism
def reset_button_clicked():
    window.after_cancel(timer)
    global reps
    global count_marks
    reps = 0
    count_marks = 0
    check_marks.config(text="")
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    
# timer mehanism
def start_button_cliked():
    global reps
    reps += 1
    print(reps)
    if reps%8 == 0:
        minutes = LONG_BREAK_MIN
        timer_label["text"] = "Break"
        timer_label["fg"] = RED
    elif reps%2 == 0:
        minutes = SHORT_BREAK_MIN
        timer_label.config(text = "Break", fg = PINK)
    elif reps%2 != 0:
        minutes = WORK_MIN
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
    seconds = minutes*60
    countdown(seconds)
    

# countdown mehanism
def countdown(count):
    global count_marks

    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f'{minutes:02}:{seconds:02}')
    if count > 0:
       global timer
       timer = window.after(1000, countdown, count-1)
    else:
        start_button_cliked()
        if reps%2 == 0:
            count_marks += 1
            marks = "✔"*count_marks
            check_marks.config(text = marks)

# init window
window = tkinter.Tk()
window.title("Pomodoro App")
window.minsize(width=550,height=450)
window.config(padx = 100, pady = 50, bg=YELLOW)

# Timer title
timer_label = tkinter.Label(text="Timer", font= (FONT_NAME, 45),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1, row=0)

# image of pomodoro
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image = tomato_image)

# timer in pomodoro
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start button
start_button = tkinter.Button(text = "Start", highlightbackground=YELLOW, command=start_button_cliked)
start_button.grid(column=0, row=2)

# reset button
reset_button = tkinter.Button(text = "Reset", highlightbackground=YELLOW, command=reset_button_clicked)
reset_button.grid(column=2, row=2)

# check marks ✔
check_marks = tkinter.Label(text="", font= (FONT_NAME, 20),bg=YELLOW,fg=GREEN)
check_marks.grid(column=1, row=3)


window.mainloop()

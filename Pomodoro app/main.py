from datetime import datetime
from tkinter import *
import datetime


# ---------------------------- CONSTANTS ------------------------------- #
## Color constants for pop-up window
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = '✔'

#Predetermined times for app
WORK_MIN = datetime.timedelta(minutes=25)
SHORT_BREAK_MIN = datetime.timedelta(minutes=5)
LONG_BREAK_MIN = datetime.timedelta(minutes=20)

#Counter for long Brake
LONG_BREAK = 0

#Place holder string for checkmark display
REPS = ''

#Conditional gates
TAKE_SHORT_BREAK = True # Signals the program to take a short brake after the work session has ended
BACK_TO_WORK = False # Signals the program to resume the work session
timer = None # Place holder for the tkinter.window.after object that allows the program to 'RESET'

#Test times
TEST = datetime.timedelta(seconds=5)
TEST_1= datetime.timedelta(seconds=3)
TEST_2= datetime.timedelta(seconds=6)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    '''
        Resets opp to orginal settings
    '''
    global timer
    #Stops timer
    window.after_cancel(timer)
    #Restting label,timer and clearing checks
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(canvas_timer_text, text='00:00',font=(FONT_NAME,35,'bold'),fill = 'white')
    check_label.config(text='', fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    '''
            Employs recursion with tkinter.window.after object to countdown a predetermined
            amount of time represented by a delta.timedelta object.
        Args:
            count (datetime.timedelta): time to countdown from
    '''
    #Time deducted for countdown
    sec = datetime.timedelta(seconds=1)
    #Zero in a datetime.timedelta object
    zero = datetime.timedelta(seconds=0)

    #Constants modified throughout the program
    global TAKE_SHORT_BREAK
    global LONG_BREAK
    global BACK_TO_WORK
    global CHECK_MARK
    global REPS
    global timer

    #Configuring the timer display on the canvas
    canvas.itemconfig(canvas_timer_text, text=f'{count}')
    #Counting down
    count -= sec

    #if count is greater the zero display time and keep counting down
    if count >= zero:
        timer = window.after(1000,count_down,count)

    #Taking a short break condition. Basically take a short break after every session
    # for the purpose of testing after 4 work/short break sessions take long brake
    # Thus Long break < 3
    elif count <= zero and TAKE_SHORT_BREAK and LONG_BREAK < 3: #Short Break

        BACK_TO_WORK = True #Back to work
        TAKE_SHORT_BREAK = False# Short break finished
        LONG_BREAK += 1# Long break counter

        #Check mark for every work/Short break session
        REPS += CHECK_MARK
        #display checkmark
        check_label.config(text=REPS, fg=GREEN)

        #Indicating its break time by substituting 'Timer' with 'Break'
        timer_label.config(text = 'Break',fg = PINK)
        window.after(1000, count_down, TEST_1)

    # In this conditional statement when the work session has ended and the
    #number of short breaks has reached 4 then 'Stop' and take a Long break
    elif count <= zero and TAKE_SHORT_BREAK and LONG_BREAK == 3: #Long break
        #Resetting the values
        LONG_BREAK = 0
        TAKE_SHORT_BREAK = False
        BACK_TO_WORK = True
        #Displaying the number of checks which represents the number of work sessions
        REPS += CHECK_MARK
        check_label.config(text=REPS, fg=GREEN)
        #Resetting the number of checks
        REPS = ''

        #Displaying 'Stop'
        timer_label.config(text='Stop', fg=RED)
        window.after(1000,count_down,TEST_2)

    #When the breaks are finished return to the work session
    elif count <= zero and BACK_TO_WORK and LONG_BREAK <= 3: # Back to work
        #Setting the short brake condition to True
        TAKE_SHORT_BREAK = True

        #After a long brake clear the number of checks
        if REPS == '':
            check_label.config(text=REPS, fg=YELLOW)

        #Substituting 'Break' label with 'Work'
        timer_label.config(text='Work', fg=GREEN)
        window.after(1000,count_down,TEST)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def manage_time(time = TEST):
    '''
        Provides the initial count down time and allows for recustion to take place
    Args:
        time (datetime.timedelta object)
    '''
    count_down(time)


# ---------------------------- UI SETUP ------------------------------- #
#Instatiating window object
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW) # Window dimenssions

#This is a label at position (0,0) for reference in the grid
blank_label_1 = Label(bg=YELLOW)
blank_label_1.grid(column = 0,row =0)

#Label for the timer
timer_label = Label(text = 'Timer',
                    font=(FONT_NAME,40,'bold'),
                    bg=YELLOW,
                    highlightthickness=0,
                    fg = GREEN
                    )
timer_label.grid(column = 1,row =0)


#label for the check marks
check_label = Label(bg=YELLOW,text = ' ' ,fg = GREEN,font=(FONT_NAME,12,'bold'))
check_label.grid(column = 1,row = 2)

#image setup
tomato_img = PhotoImage(file = 'tomato.png')

#Canvas setup
canvas = Canvas(width=200,height=240,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,120,image = tomato_img)# Tomato image set up

#Timer image set up
canvas_timer_text = canvas.create_text(101,140,text = '00:00',font=(FONT_NAME,35,'bold'),fill = 'white')


#Grid set up
canvas.grid(column = 1,row =1)

# Buttons set up
start_button = Button(text = 'Start',command= manage_time)
start_button.grid(column = 0,row =2)

reset_button = Button(text='Reset',command=reset_timer)
reset_button.grid(column = 2,row =2)




#window mainloop
window.mainloop()
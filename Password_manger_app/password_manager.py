
from tkinter import *
from tkinter import messagebox
import random
import pyperclip




#________________________________________________Saving Info_________________________________________________#
def save_info():
    '''
        Saves field information to a text field
    Args: None
    Vars:
        website(str) : receives info from Entry() instance
        user_name(str) : receives info from Entry() instance
        password(str) : receives info from Entry() instance

    Returns: Nove
        Saves information to txt file
    '''
    website = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()

    #This conditional block gives out warnings if the fields are empty
    if len(website) ==0:
        messagebox.showwarning(title='Empty field',
                               message='The website field is empty')
    elif len(user_name) ==0:
        messagebox.showwarning(title='Empty field',
                               message='The user name field is empty')
    elif len(password) ==0:
        messagebox.showwarning(title='Empty field',
                               message='The password field is empty')

    else:

        info_answer = messagebox.askokcancel(title = website,
                                 message=f'User name: {user_name}\n Password: {password}\n Is the info ok?')
        #if the info is ok save
        if info_answer:
            with open('password_info.txt','a') as file:
                file.write(f'Website: {website}    |    User: {user_name}    |    Password: {password}\n')
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#___________________________Password Generator_______________________________________________#
def generate_password():

    #lists of characters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Listst of lists
    choice_list = [letters,numbers,symbols]
    password = ''
    while len(password) < 9 :

        choice = random.choice(choice_list)#random chosen list
        k = random.randint(1,3)#length of random sample
        sample = random.sample(choice,k)
        p = ''.join(sample)
        password += p#password string
        choice_list.remove(choice)#After a character from a list is chosen the list is removed from the pool
        #After the list is empty replenish the list
        if not choice_list:
            choice_list = [letters, numbers, symbols]

        #Shuffuling password characters
        password = list(password)
        n = len(password)
        password = random.sample(password,n)
        password = ''.join(password)

    # Displaying password
    password_entry.insert(0,password)
    #copying the password to the clipboard
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
# Window instance
window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)
#_____________________Labels______________________________________#

website_label = Label(text = 'Website:')
website_label.grid(column=0,row=1)

usr_name_label = Label(text = 'Email/User name:')
usr_name_label.grid(column=0,row=2)

password_label = Label(text = 'password:')
password_label.grid(column=0,row=3)

#__________________Entry box____________________________________#
website_entry = Entry(width= 55)
website_entry.grid(column = 1,row=1,columnspan=2)
website_entry.focus()

user_name_entry = Entry(width= 55)
user_name_entry.grid(column = 1,row=2,columnspan=2)
user_name_entry.insert(0,'your-email@---.com')
password_entry = Entry(width= 37)
password_entry .grid(column = 1,row=3,)

#_________________________________Button_________________________#
generate_button = Button(text = 'Generate Password',command=generate_password)
generate_button.grid(column = 2,row=3)

add_button = Button(width = 47,text = 'add',command=save_info)
add_button.grid(column = 1,row=4,columnspan=2)
#___________________image setup_________________________________#
lock_img = PhotoImage(file = 'logo.png')

#_________________Canvas setup_______________________________________#
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image = lock_img)# Lock image set up
#Grid set up
canvas.grid(column = 1,row =0)

#___________main loop________________________________________________#
window.mainloop()



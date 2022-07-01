from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letter=[random.choice(letters) for char in range(nr_letters)]


    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbol=[random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_number=[random.choice(numbers) for char in range(nr_numbers)]

    password_list=password_letter+password_symbol+password_number
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password="".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=Email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title= "OOPs", message="Please make sure u entered details")
    else:

        is_ok=messagebox.askokcancel(title=website, message=f"These are the details are entered:\nEmail:{email}"
                                                      f"\n password:{password}")
        if is_ok:
            with open("text.txt1","a")as text_document:
                text_document.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200 , height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

Email_label=Label(text="Email/Username:")
Email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

Email_entry=Entry(width=35)
Email_entry.grid(row=2,column=1,columnspan=2)
Email_entry.insert(0,"ashok@gmail.com")
Email_entry.get()

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


generate_password_button=Button(text="Generate Password",command=password_generator)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()

# def add(x,y):
#     print(x+y)
# def sub(x,y):
#     print(x-y)
# def mul(x,y):
#     print(x*y)
# def div(x,y):
#     float(x,y)
#     print(x/y)

# while(True):
#     x=int(input("Enter the number1: "))
#     y=int(input("Enter the number2: "))
#     z=input("Enter the operation to be performed (Addition, Subtraction, Multiplication, Division): ").lower()

#     if z.startswith('a'):
#         add(x,y)
#     elif z.startswith('s'):
#         sub(x,y)
#     elif z.startswith('m'):
#         mul(x,y)
#     elif z.startswith('d'):
#         div(x,y)
#     else:
#         print('Arghh! Something went wrong... Try again!')





# print('Welcome to Password Generator')
# from random import randint
# a=''
# for i in range(int(input('Enter the password length: '))):
#     a+=chr(randint(33,124))
# print(a)




# print('Welcome to the game of Rock-Paper-Scissors')
# from random import choice

# print('Whoever gets three points first, Wins!!')
# Win_point = 3
# p1_points = 0
# p2_points = 0
# p1_name = input("Enter Player's name: ")
# p2_name = 'Computer'

# while True:
#     print(f"{p1_name} points: {p1_points}")
#     print(f"Computer's points: {p2_points}")
    
#     p1 = input('Enter your response (rock, paper, or scissors): ').lower()
#     p2 = choice(['rock', 'paper', 'scissors'])
#     print('Computer:', p2)

#     if p1 not in ['rock', 'paper', 'scissors']:
#         print('Invalid response! Please enter rock, paper, or scissors.')
#         continue

#     if p1 == p2:
#         print('It\'s a tie! Both get a point.')
#         p1_points += 1
#         p2_points += 1
#     elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
#         print(f'{p1_name} wins this round!')
#         p1_points += 1
#     else:
#         print('Computer wins this round!')
#         p2_points += 1

#     if p1_points == Win_point or p2_points == Win_point:
#         if p1_points == p2_points:
#             print(f'Both {p1_name} and {p2_name} won.')
#         elif p1_points == Win_point:
#             print(f'{p1_name} wins the game!')
#         else:
#             print(f'{p2_name} wins the game!')
#         break





# class Contact:
#     def __init__(self, name, number, email, address):
#         self.name = name
#         self.number = number
#         self.email = email
#         self.address = address

#     def view(self):
#         print(f'''
#         Name: {self.name}
#         Number: {self.number}
#         Email: {self.email}
#         Address: {self.address}
#         ''')

# class ContactBook:
#     def __init__(self):
#         self.contacts = []

#     def add(self):
#         name = input("Enter the person's name: ")
#         number = int(input("Enter the person's number: "))
#         email = input("Enter the person's email: ")
#         address = input("Enter the person's address: ")
#         self.contacts.append(Contact(name, number, email, address))

#     def delete(self, name):
#         self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]

#     def search(self, hint):
#         found = False
#         for contact in self.contacts:
#             if hint.lower() in contact.name.lower() or hint in str(contact.number) or hint.lower() in contact.email.lower() or hint.lower() in contact.address.lower():
#                 contact.view()
#                 found = True
#         if not found:
#             print('Not Found')

#     def update(self, name):
#         found = False
#         for contact in self.contacts:
#             if contact.name.lower() == name.lower():
#                 found = True
#                 change = input('Enter what field to update (name, number, email, address): ').lower()
#                 if hasattr(contact, change):
#                     new_value = input(f'Enter new value for {change}: ')
#                     if change == "number":
#                         setattr(contact, change, int(new_value))
#                     else:
#                         setattr(contact, change, new_value)
#                 else:
#                     print("Invalid field.")
#         if not found:
#             print('Contact not found.')

#     def view_all(self):
#         for contact in self.contacts:
#             contact.view()

# print("Welcome to Gantavya's Contact book")
# contact_book = ContactBook()

# while True:
#     task = int(input('''
#     1: Add a contact
#     2: Search for a contact
#     3: Update a contact
#     4: Delete a contact
#     5: View all contacts
#     0: Exit
#     '''))

#     if task == 0:
#         break
#     elif task == 1:
#         contact_book.add()
#         print("Add a contact function called.")
#     elif task == 2:
#         contact_book.search(input('Enter the info here: '))
#         print("Search a contact function called.")
#     elif task == 3:
#         contact_book.update(input('Enter the contact name for the update: '))
#         print("Update a contact function called.")
#     elif task == 4:
#         contact_book.delete(input('Enter the contact name to be deleted: '))
#         print("Delete a contact function called.")
#     elif task == 5:
#         contact_book.view_all()
#         print("View all contacts function called.")
# print("Program exited.")




# import tkinter as tk
# from tkinter import messagebox
# from random import choice

# def play_round(player_choice):
#     global p1_points, p2_points, Win_point
    
#     p2 = choice(['rock', 'paper', 'scissors'])
#     computer_choice_label.config(text=f"Computer chose: {p2}")

#     if player_choice == p2:
#         result_label.config(text='It\'s a tie! Both get a point.')
#         p1_points += 1
#         p2_points += 1
#     elif (player_choice == 'rock' and p2 == 'scissors') or (player_choice == 'paper' and p2 == 'rock') or (player_choice == 'scissors' and p2 == 'paper'):
#         result_label.config(text=f'{p1_name} wins this round!')
#         p1_points += 1
#     else:
#         result_label.config(text='Computer wins this round!')
#         p2_points += 1

#     p1_points_label.config(text=f"{p1_name} points: {p1_points}")
#     p2_points_label.config(text=f"Computer's points: {p2_points}")

#     if p1_points == Win_point or p2_points == Win_point:
#         if p1_points == p2_points:
#             messagebox.showinfo("Result", f'Both {p1_name} and Computer won.')
#         elif p1_points == Win_point:
#             messagebox.showinfo("Result", f'{p1_name} wins the game!')
#         else:
#             messagebox.showinfo("Result", f'Computer wins the game!')
#         root.quit()

# root = tk.Tk()
# root.title("Rock-Paper-Scissors Game")
# Win_point = 3
# p1_points = 0
# p2_points = 0
# p1_name = input("Enter Player's name: ")

# p1_points_label = tk.Label(root, text=f"{p1_name} points: {p1_points}")
# p1_points_label.pack()
# p2_points_label = tk.Label(root, text=f"Computer's points: {p2_points}")
# p2_points_label.pack()
# result_label = tk.Label(root, text="Make your move!")
# result_label.pack()
# computer_choice_label = tk.Label(root, text="Computer chose: ")
# computer_choice_label.pack()
# buttons_frame = tk.Frame(root)
# buttons_frame.pack()
# rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play_round('rock'))
# rock_button.pack(side=tk.LEFT)
# paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play_round('paper'))
# paper_button.pack(side=tk.LEFT)
# scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play_round('scissors'))
# scissors_button.pack(side=tk.LEFT)
# root.mainloop()













import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Initialize variables
a = None
listdo = []
filename = ''

# Function to open an existing file
def open_file():
    global listdo, filename
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        try:
            with open(filename, 'r') as f:
                listdo = f.read().splitlines()
                a = 1
                messagebox.showinfo("Success", f"{filename} opened successfully")
                show_list()
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

# Function to create a new file
def create_file():
    global filename
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'w') as f:
            pass
        a = 1
        messagebox.showinfo("Success", f"{filename} created successfully")

# Function to add a task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        listdo.append(task)
        messagebox.showinfo("Success", f"Task '{task}' added successfully")
        show_list()

# Function to remove a task
def remove_task():
    task = simpledialog.askstring("Remove Task", "Enter the task to remove:")
    if task in listdo:
        listdo.remove(task)
        messagebox.showinfo("Success", f"Task '{task}' removed successfully")
        show_list()
    else:
        messagebox.showerror("Error", "Task not found in the list")

# Function to show the list
def show_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(listdo):
        listbox.insert(tk.END, f"{i + 1}. {task}")

# Function to save the list
def save_list():
    if filename:
        with open(filename, 'w') as f:
            for item in listdo:
                f.write("%s\n" % item)
        messagebox.showinfo("Success", f"{filename} saved successfully")
    else:
        messagebox.showerror("Error", "No file opened or created")

# Function to exit the program
def exit_program():
    if messagebox.askyesno("Exit", "Do you want to save changes before exiting?"):
        save_list()
    root.quit()

# Setting up the main window
root = tk.Tk()
root.title("TODO List Application")

# Menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Create New", command=create_file)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Buttons for task operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save List", command=save_list)
save_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=exit_program)
exit_button.pack(side=tk.LEFT, padx=5)

# Run the GUI event loop
root.mainloop()

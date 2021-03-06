"""
A program that stores the following book information:
Title, Author
Year, ISBN
"""

from tkinter import *
from backend import Database

database = Database("books.db")

# Button command functions
def view_command():
    """
    Function to read the database rows and
    return the data for the list box
    """
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    """
    Function to search the database rows
    using user input text and return the data
    for the list box
    """
    list1.delete(0, END)
    for row in database.search(
            title_text.get(),
            author_text.get(),
            year_text.get(),
            isbn_text.get()):
        list1.insert(END, row)


def add_command():
    """
    Function to add in a new book to the database
    and display the item in the list box.
    """
    list1.delete(0, END)
    database.insert(
            title_text.get(),
            author_text.get(),
            year_text.get(),
            isbn_text.get())
    list1.insert(
            END,
            (
                title_text.get(),
                author_text.get(),
                year_text.get(),
                isbn_text.get()
            ))


def get_selected_row(event):
    """
    Function to get the specific row data when it is
    clicked on in the listbox
    """

    try:
        # Global variable needed for delete and update functions
        global selected_tuple

        # Returns the list index from the row data tuple
        index = list1.curselection()[0]

        # Returns the row data tuple with the specified index
        selected_tuple = list1.get(index)

        # Populate the entry fields with the selected row data
        entry1.delete(0, END)
        entry1.insert(0, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(0, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(0, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(0, selected_tuple[4])
    except IndexError:
        pass

def update_command():
    """
    Function to update the selected row data
    """
    database.update(
        selected_tuple[0],
        title_text.get(),
        author_text.get(),
        year_text.get(),
        isbn_text.get())


def delete_command():
    """
    Function to delete the selected row data
    """
    database.delete(selected_tuple[0])

# Build the GUI Window
window = Tk()
window.geometry("390x210")

# Window Title
window.title("Book Store")



# create the data field labels
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

# Create the data fields
title_text = StringVar()  # Create a spatial object for the user input field
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()  # Create a spatial object for the user input field
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()  # Create a spatial object for the user input field
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()  # Create a spatial object for the user input field
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# Create the list box window
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create the scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

"""
Bind a function to a widget event.
When a listbox row is clicked, add the data to the entry fields.
"""
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create the buttons
button1 = Button(
    window,
    text="View All",
    width=12,
    command=view_command)
button1.grid(row=2, column=3)

button2 = Button(
    window,
    text="Search Entry",
    width=12,
    command=search_command)
button2.grid(row=3, column=3)

button3 = Button(
    window,
    text="Add Entry",
    width=12,
    command=add_command)
button3.grid(row=4, column=3)

button4 = Button(
    window,
    text="Update Selected",
    width=12,
    command=update_command)
button4.grid(row=5, column=3)

button5 = Button(
    window,
    text="Delete Selected",
    width=12,
    command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(
    window,
    text="Close",
    width=12,
    command=window.destroy)
button6.grid(row=7, column=3)

window.mainloop()
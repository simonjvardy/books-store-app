"""
A program that stores the following book information:
Title, Author
Year, ISBN
"""

from tkinter import *

window = Tk()

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

# Create buttons
button1 = Button(window, text="View All", width=12)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search Entry", width=12)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add Entry", width=12)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Selected", width=12)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete Selected", width=12)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12)
button6.grid(row=7, column=3)

window.mainloop()
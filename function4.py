import tkinter as t
from tkinter import *
from tkinter import messagebox

object = t.Tk()


# create def for button command actions to change view configurations
def view():
    display.config(text=option.get())


# option datatype
option = StringVar()
# set default menu option
option.set("Relevant View")
# menu choices
choices = ["Relevant View", "Irrelevant View"]
# create drop-down menu with view options
view_menu = OptionMenu(object, option, *choices)
drop.pack()

# create sliding scale for relevance criteria or ask user for static input
# ask user for static relevance/containment value
user_i = input("How many children would you like your entities to contain in order for them to be viewed as ‘relevant’?")

# for each Entity ID in the Entities Table, select the entity ID and...
for Entity_ID in range(0, len(Entities)):
    # if the user selects the “Relevant_View” option from the GUI drop-down menu
    if user_selection = ('Relevant View'):

        # test to see whether each entity in range above are relevant
        def test_range_for_relevant_view_frame(n):

        # if the object is permanent and the ‘Contains’ column is greater than or equal to user     input
            if Permanent = 'Yes' and Contains >= user_i:
            # then the object is considered relevant. Configure to display entity
            config1 = {'display': true}
            # else, if each entity in the range above is not permanent, they are not         considered relevant. Configure to NOT display entity.
            else:
            # configure to not display the Entity_ID
            config1 = {'display': none}
            # User display option two (I.e., “Irrelevant_View”) allows user to display all objects, i    ncluding those that are irrelevant
            else:
            config2 = {'display': true}


view_button = Button(object, text=”View”, command = show).pack()

object.mainloop()
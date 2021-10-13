import tkinter
import json
from matrix_operations import Matrix

# window = tkinter.Tk()
# window.title(string="Workout Builder")
# window.config(padx=20, pady=20)
# Labels

# Buttons

# Entries

matrix = Matrix()
going = True
while going:
    exercise = input("Add an exercise: ")
    matrix.add_new(exercise)
    cont = input("Continue? y/save/n: ")
    if cont == "y":
        going = True
    elif cont == "save":
        matrix.save()
        going = False
    else:
        going = False


# keep this at the end
# window.mainloop()

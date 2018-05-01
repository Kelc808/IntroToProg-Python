#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   <KChun>, 4-30-18, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "C:/_PythonClass/Todo.txt"
strData = ""
dicRow = {"Task": "Clean House", "Priority": "low"}
lstTable = [dicRow]
with open(objFileName, mode="r+") as todo:
    todo.write(str(dicRow))

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

# Step 2 - Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - \n"))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        with open(objFileName, mode="r") as todo:
            todo.seek(0)
            print(todo.readline())
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        add_task = input("What is the task?\n")
        add_priority = input("What is the priority?\n")
        new_dic_row = {"Task": add_task, "Priority": add_priority}
        lstTable.append(new_dic_row)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        try:
            print(list(lstTable))
            n = int(input("Input list number to remove starting at 0\n"))
            del lstTable[n]
        except:
            pass
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        with open(objFileName, mode="w+") as todo:
            todo.write(str(lstTable))
        continue
    elif (strChoice == '5'):
        break #and Exit the program


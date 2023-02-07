#Documentation, Task, Personal tought
#
#Importing my personal utility
#The class bookInfo is not really used, insert as possible future update
#_____________________________________________________________________________

#=========Import=========
import sqlite3
#Import my personal utility code
#Class that contains terminal text extra and color
from P_Utility import Class_TextMod
#Function to align all the string content
from P_Utility import method_textAlignmentCorrector

#========Class Declaration========
#Class to create object book and have all the info about it
class Class_bookInfo():
    def __init__(self, local_id : int, local_title : str, local_author : str, local_quantity : int) -> None:
        self.local_id = local_id
        self.local_title = local_title
        self.local_author = local_author
        self.local_quantity = local_quantity


    #Getter method for all the important info about this object
    def method_get_id(self):
        return self.local_id

    def method_get_title(self):
        return self.local_title

    def method_get_author(self):
        return self.local_author

    def method_get_quantity(self):
        return self.local_quantity



    def __str__(self) -> str:
        print(f"""Info about this book{Class_TextMod.cyan}
        ID: {self.local_id}
        Title: {self.local_title}
        Author: {self.local_author}
        Quantity: {self.local_quantity}
        {Class_TextMod.reset}""")

#========END Class Declaration========

#==========Variable declaration==========

#==========END Variable==========

#==========Function declaration==========

    #=====Program function=====
        #====DEBUG====

#Print the whole database to show each step
def func_showData(local_cursor_student : sqlite3):
    print("id : title : author : quantity")
    local_cursor_student.execute('''SELECT id, title, author, quantity FROM table_bookDB''')
    for records in local_cursor_student:
        #records [0] ID, [1] Title, [2] Author, [3] Quantity
        print(f'{records[0]} : {records[1]} : {records[2]} : {records[3]}')

    print()


#Add all the specified book if their id is not used already
def func_populate(local_sql_bookDB : sqlite3):

    #Get a cursor object
    local_cursor_bookDB = local_sql_bookDB.cursor() 

    #Create student table
    local_cursor_bookDB.execute('''
        CREATE TABLE if NOT EXISTS table_bookDB(id INTEGER PRIMARY KEY, title TEXT,
                        author TEXT, quantity INTEGER)
    ''')

    local_sql_bookDB.commit()

    list_container_multy = []
    list_id_database = []

    list_container_multy = [[3001, "A Tale of Two Cities", "Charles Dickens", 30],
    [3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 30],
    [3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25],
    [3004, "The Lord of the Rings", "J.R.R Tolkien", 37],
    [3005, "Alice in Wonderland","Lewis Carroll", 12]]

    #Prevent from adding same value again as task give a fixed id that will not be unique each time program work
    local_cursor_bookDB.execute('''SELECT id FROM table_bookDB''')
    for records in local_cursor_bookDB:
        list_id_database.append(records[0])

    for new_entry in list_container_multy[:]:
        if new_entry[0] in list_id_database:
            list_container_multy.remove(new_entry)



    #Insert all book
    local_cursor_bookDB.executemany('''INSERT INTO table_bookDB(id, title, author, quantity)
                    VALUES(?,?,?,?)''', list_container_multy)
    

    local_sql_bookDB.commit()

        #====END DEBUG====

#Add a book and all the info about to database
def func_addBook(local_cursor_bookDB : sqlite3):
    #New book info
    local_list_bookInfo = ["", "", 0]
    local_index = 0
    local_string_input = ""

    print(f"{Class_TextMod.green}Perfect! You will need now to add some information about.")
    print("Keep in mind, you can exit by insert 'e' on details confirmation")
    #Loop to insert all the new info, there is an index to prevent have to insert everything
    #again if conversion fail
    while True:
        if local_index == 0:
            local_list_bookInfo[0] = input(f"{Class_TextMod.pink}Title: ").strip()
            local_index += 1
        elif local_index == 1:
            local_list_bookInfo[1] = input(f"{Class_TextMod.pink}Author: ").strip()
            local_index += 1
        elif local_index == 2:
            try:
                local_list_bookInfo[2] = int(input(f"{Class_TextMod.pink}Quantity: ").strip())
                local_index += 1
            except:
                #Error message
                print(f"{Class_TextMod.lightred}You have to insert a valid number")
                print()
        else:
            print()
            print(f"{Class_TextMod.blue}Resume\nTitle: {local_list_bookInfo[0]}\nAuthor: {local_list_bookInfo[1]}\nQuantity: {local_list_bookInfo[2]}")
            
            #Ask if details are correct or eventually if want to exit without change
            local_string_input = input(f"{Class_TextMod.pink}Are those details correct? y/n/e: ").lower().strip()
            if local_string_input == "y":
                break
            elif local_string_input == "e":
                return
            else:
                #Error message
                local_index = 0
                print(f"{Class_TextMod.lightred}Please insert them again")

    #Insert a new book
    local_cursor_bookDB.execute('''INSERT INTO table_bookDB(title, author, quantity)
                    VALUES(?,?,?)''', (local_list_bookInfo[0], local_list_bookInfo[1], local_list_bookInfo[2]))

def func_updateBook(local_cursor_bookDB : sqlite3):

    local_list_bookInfo = [0 ,"", "", 0]
    local_int_input = 0
    local_list_string_menu = ["|1. Title",
    "|2. Author",
    "|3. Quantity",
    "|0. Exit"]

    #Loop to ask for an book id to change info about
    while True:
        try:
            local_int_input = int(input(f"{Class_TextMod.pink}Insert the id of the book you want to change info about: "))
            break
        except:
            #Error message
            print(f"{Class_TextMod.lightred}You have to insert a valid number")
            print()            

    #Get info about the selected book
    try:
        local_cursor_bookDB.execute('''SELECT * FROM table_bookDB WHERE id = ? ''', (local_int_input,))

        #Get and set up all the original records to change only the needed one
        records = local_cursor_bookDB.fetchone()

        print("What you want to change?")
        local_list_bookInfo[0] = records[0]
        local_list_bookInfo[1] = records[1]
        local_list_bookInfo[2] = records[2]
        local_list_bookInfo[3] = records[3]
    except:
        #Error message
        print()
        print(f"{Class_TextMod.lightred}Something went wrong, probabily id doesn't exist")
        print()
        #If id not exist exit from this function
        return



    #Align to nice printing and add enclosure
    local_list_string_menu = method_textAlignmentCorrector(local_list_string_menu, 3, " ", True, "|")

    #Create a top/bottom enclosure by adding - to an empty string to reach same lenght of string_menu[0]
    local_string_container = method_textAlignmentCorrector(["", local_list_string_menu[0]],0,"-")[0]

    #Loop until a valid option is inserted
    while True:
        while True:
            #Printing option menu
            print(f"{Class_TextMod.yellow}{local_string_container}")
            print(f"{Class_TextMod.green}{local_list_string_menu[0]}")
            print(f"{local_list_string_menu[1]}")
            print(f"{local_list_string_menu[2]}")
            print(f"{local_list_string_menu[3]}")
            print(f"{Class_TextMod.yellow}{local_string_container}")
            print()

            try:
                local_int_input = int(input(f"{Class_TextMod.green}Select what you want to update: ").strip())
                break
            except:
                #Error message
                print(f"{Class_TextMod.lightred}Please insert a valid option")
                print()
                continue

        if local_int_input == 0: #Exit
            return
        elif local_int_input == 1: #Title
            local_list_bookInfo[1] = input(f"{Class_TextMod.pink}Insert the new title: ")
            break
        elif local_int_input == 2: #Author
            local_list_bookInfo[2] = input(f"{Class_TextMod.pink}Insert the new author: ")
            break
        elif local_int_input == 3: #Quantity
            while True:
                try:
                    local_list_bookInfo[3] = int(input(f"{Class_TextMod.pink}Insert the new title: "))
                    break
                except:
                    #Error message
                    print(f"{Class_TextMod.lightred}Please insert an integer number")
                    print()
                    continue
            break
        else:
            #Error message
            print(f"{Class_TextMod.lightred}No valid option have been entered")
            print()
            continue

    #Update new info
    local_cursor_bookDB.execute('''UPDATE table_bookDB SET title = ?, author = ?, quantity = ? WHERE id = ? ''', 
    (local_list_bookInfo[1], local_list_bookInfo[2],local_list_bookInfo[3], local_list_bookInfo[0]))


#Delete a book by ID from database
def func_deleteBook(local_cursor_bookDB : sqlite3):

    #Loop asking for the ID of the book that want to be removed from database
    while True:
        try:
            local_int_input = int(input(f"{Class_TextMod.pink}Insert the book ID you want to remove: "))
            break
        except:
            #Error message
            print(f"{Class_TextMod.lightred}You have to insert a valid number")
            print()


    local_cursor_bookDB.execute('''DELETE FROM table_bookDB WHERE id = ? ''', (local_int_input,))


#Search a book by ID from database
def func_searchBook(local_cursor_bookDB : sqlite3):
    #Loop asking for the ID of the book that want to be removed from database
    while True:
        try:
            local_int_input = int(input(f"{Class_TextMod.pink}Insert the book ID you want to see: "))
            break
        except:
            #Error message
            print(f"{Class_TextMod.lightred}You have to insert a valid number")
            print()

    #Get info about the selected book
    try:
        local_cursor_bookDB.execute('''SELECT * FROM table_bookDB WHERE id = ? ''', (local_int_input,))

        records = local_cursor_bookDB.fetchone()

        print(f'{Class_TextMod.blue}ID: {records[0]}\nTitle: {records[1]}\nAuthor: {records[2]}\nQuantity: {records[3]}')
    except:
        #Error message
        print()
        print(f"{Class_TextMod.lightred}Something went wrong, probabily id doesn't exist")
        print()


#Function to print the menu
def func_menu():
    local_list_string_menu = ["|1. Enter book",
    "|2. Update book",
    "|3. Delete book",
    "|4. Search books",
    "|0. Exit",]

    #Align to nice printing and add enclosure
    local_list_string_menu = method_textAlignmentCorrector(local_list_string_menu, 3, " ", True, "|")

    #Create a top/bottom enclosure by adding - to an empty string to reach same lenght of string_menu[0]
    local_string_container = method_textAlignmentCorrector(["", local_list_string_menu[0]],0,"-")[0]

    print(f"{Class_TextMod.yellow}{local_string_container}")
    print(f"{Class_TextMod.green}{local_list_string_menu[0]}")
    print(f"{local_list_string_menu[1]}")
    print(f"{local_list_string_menu[2]}")
    print(f"{local_list_string_menu[3]}")
    print(f"{local_list_string_menu[4]}")
    print(f"{Class_TextMod.yellow}{local_string_container}")
    #=====Program function END=====

    #=====Utility function=====


    #=====Utility function END=====
#==========END Function==========

#START CODE


def func_main():

    #SET UP ALL THE NEEDED INFO FOR START
    sql_bookDB = sqlite3.connect("sql_bookDB")
    #Get a cursor object
    cursor_bookDB = sql_bookDB.cursor() 

    #Create student table
    cursor_bookDB.execute('''
        CREATE TABLE if NOT EXISTS table_bookDB(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT,
                        author TEXT, quantity INTEGER)
    ''')

    sql_bookDB.commit()
    
    string_option = ""
    while True:
        func_menu()

        #Select option
        string_option = input(f"{Class_TextMod.pink}Select option: ").lower().strip()
        print()
        if string_option == "0": #Exit
            break
        elif string_option == "1": #Enter book
            func_addBook(cursor_bookDB)
            sql_bookDB.commit()
        elif string_option == "2": #Update book
            func_updateBook(cursor_bookDB)
            sql_bookDB.commit()
        elif string_option == "3": #Delete book
            func_deleteBook(cursor_bookDB)
            sql_bookDB.commit()
        elif string_option == "4": #Search books
            func_searchBook(cursor_bookDB)
        elif string_option == "show": #Debug
            func_showData(cursor_bookDB)
        elif string_option == "populate": #Debug
            func_populate(sql_bookDB)
        else:
            #Error message
            print()
            print(f"{Class_TextMod.lightred}No valid option selected")
            print()
        

    sql_bookDB.close()

#=========START CODE===========
func_main()
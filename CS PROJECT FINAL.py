#REQUIRED MODULES
from tkinter import *
window=Tk()
#WINDOW SIZE
window.geometry('1000x1000')
#WINDOW TITLE
window.title('AK AND NK HOTELS')
window.configure(background='white')
Label(window, text = 'AK AND NK HOTELS', font =( 
    'Algerian', 15)).pack(side = TOP, pady = 10)
photo = PhotoImage(file = r"ak and nk.gif")
Button(window, image = photo).pack(side = TOP)
bg = PhotoImage(file = r"hotel1.gif")
label1 = Label( window, image = bg) 
label1.place(x = 730, y = 0)
bg1 = PhotoImage(file = r"hotel2.gif")
label2 = Label( window, image = bg1) 
label2.place(x = 0, y = 0)
l = Label(window, text ='''The phenomenal AK AND NK is spread over 50 acres.Truly spectacular
design leaves an impossible impression, and swimming pools are no different.
we offer unique experiences that include private beachside dining, traditional
boat rides, private cooking sessions and fun activities for children. The
indoor and alfresco restaurants have man made water falls and hill views,
and we serve fine international and Indian cuisine.No matter the climate,it’s
hard to say whether it’s more awe-inspiring to be submerged beside
a sand-trimmed sea or surrounded by snowy peaks.
The property is surrounded by mature palm, fruit and eucalyptus trees, which
shade the emerald-green pool. Beyond the palatial Suites, spa and gardens,
guests will discover welcoming villages, majestic forts and ruins, and
the jungle of Sariska National Park, where tigers still roam free.The
white-marble-and-mosaic HOTEL AK and NK beckons to travelers.
Today, guests are treated like royalty by an entourage of palace butlers who
ensure that everybody is provided royal comfort.
The resort has 1000 exquisitely appointed rooms and suites,complemented by
our warm,personalized hospitality.



Guestrooms are rich in color.We were voted 1st best restaurant in the world by
Elite Traveler in 2019, where six-course dinners are served.''')
l.config(font =("Courier", 14))
l.pack()
btn = Button(window, text = 'TO DO DATABASE WORKS(CLICK ME) !', bd = '5', 
                          command = window.destroy)
btn.pack(side = 'top')



from datetime import datetime

import mysql.connector

from sys import exit

from tabulate import tabulate




#ABOUT OUR HOTEL

print('''             /\                                |\    |
            /  \                      ___      | \   |
           /____\          /\   |\  ||   )     |  \  |
          /      \        /__\  | \ ||   |     |   \ |
         /        \      /    \ |  \||___)     |    \|



         ''')


#REQUIRED TABLES IN DATABASE

ROOMS_TABLE_NAME = "rooms"
CUSTOMER_TABLE_NAME = "customers"
WORKER_TABLE_NAME='workers'


#CODE TO CONNECT TO DATABASE


            
      

def get_database():
    database = mysql.connector.connect(host='localhost',user='root',password='',database='hotel')
    cursor = database.cursor()
    return database, cursor

def table1(database,cursor):
    cursor.execute('show tables')
    a=cursor.fetchall()
    if (ROOMS_TABLE_NAME,) not in a:
        q='create table {0}(room_id integer,floor varchar(10),beds integer)'.format(ROOMS_TABLE_NAME)
        cursor.execute(q)
        database.commit()

def table2(database,cursor):
    cursor.execute('show tables')
    a=cursor.fetchall()
    if (CUSTOMER_TABLE_NAME,) not in a:
        q='''create table {0}(name varchar(25),customer_id integer,address varchar(15),phone_number integer,
room_id integer primary key,checkin_date date,checkout_date date)'''.format(CUSTOMER_TABLE_NAME)
        cursor.execute(q)
        database.commit()

def table3(database,cursor):
    cursor.execute('show tables')
    a=cursor.fetchall()
    if(WORKER_TABLE_NAME,) not in a:
        q='''create table {0}(name varchar(20),worker_id integer,department varchar(25),phone_number integer,
salary integer)'''.format(WORKER_TABLE_NAME)
        cursor.execute(q)
        database.commit()

#CODE TO PRINT DATA FROM ROOMS TABLE

def print_table(cursor,database):
    query= 'select * from rooms'
    cursor.execute(query)
    records=cursor.fetchall()
    print(tabulate(records,headers=['ROOM_ID','FLOOR','BEDS']))
        
#CODE TO TAKE INPUT FROM USER FOR TABLE ROOMS

def create_room():
    room_id = int(input("Enter the room no: "))
    floor = input("Enter the floor (Ex. ground, first etc.): ")
    beds = int(input("Enter number of beds: "))
    return (room_id, floor, beds)

#USER DEFINED FUNCTION TO ADD ROOMS IN ROOMS TABLE

def add_room(database, cursor):
    room = create_room()
    query = "insert into {0}(room_id,floor,beds) values({1},'{2}',{3})".\
            format(ROOMS_TABLE_NAME, room[0],room[1],room[2])
    cursor.execute(query)
    database.commit()
    print_table(cursor,database)
    print("Operation Successful")

#USER DEFINED FUNCTION TO SHOW RECORDS IN TABLE

def show_room_record(cursor, query):
    cursor.execute(query)
    records = cursor.fetchall()
    if cursor.rowcount == 0:
        print("No Matching Records")
        return
    else:
        print(tabulate(records,headers=['ROOM_ID','FLOOR','BEDS']))
    return records

def exist(database,cursor,room_ids):
    query='select * from {0} where room_id={1}'.format(ROOMS_TABLE_NAME,room_ids)
    cursor.execute(query)
    records = cursor.fetchall()
    if cursor.rowcount==0:
        return False
    else:
        return True
        
#USER DEFINED FUNCTION TO EDIT ROOMS TABLE BY ROOM ID

def edit_room_by_room_no(database, cursor):
    query = "update {0} set".format(ROOMS_TABLE_NAME)
    room_ids =int(input('Room_ID to be changed:'))
    s=exist(database,cursor,room_ids)
    if s==True:
        print('1:CHANGE ROOM ID')
        print('2:CHANGE FLOOR')
        print('3:CHANGE NUMBER OF BEDS')
        choice=int(input('ENTER YOUR CHOICE:'))
        if choice==1:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_room_id=int(input("Enter new room no: "))
                query += " room_id={0},".format(new_room_id)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                cursor.execute('select * from rooms')
                records = cursor.fetchall()
                print(tabulate(records,headers=['RECORD_ID','FLOOR','BEDS']))
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==2:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_floor =input('NEW Floor:')
                query += " floor='{0}',".format(new_floor)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                cursor.execute('select * from rooms')
                records = cursor.fetchall()
                print(tabulate(records,headers=['RECORD_ID','FLOOR','BEDS']))
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==3:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_beds = input("Enter number of beds: ")
                query += " beds='{0}',".format(new_beds)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                cursor.execute('select * from rooms')
                records = cursor.fetchall()
                print(tabulate(records,headers=['RECORD_ID','FLOOR','BEDS']))
                print("Operation Successful")
            else:
                print("Operation Cancelled")
    else:
        print('NO MATCH FOUND')

#USER DEFINED FUNCTION TO DELETE ROOM BY ROOM ID

def delete_room_by_room_no(database, cursor):
    room_ids=int(input('ENTER ROOM NUMBER TO DELETE:'))
    s=exist(database,cursor,room_ids)
    if s==True:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where room_id={1}".format(ROOMS_TABLE_NAME,room_ids)
            cursor.execute(query)
            database.commit()
            print_table(cursor,database)
            print("Operation Successful")
        else:
            print("Operation Cancelled")
    else:
        print('NO MATCH FOUND')
        
#USER DEFINED FUNCTION TO DO ABOVE OPERATIONS IN ROOMS TABLE

def room_menu(database, cursor):
    while True:
        print()
        print("============================")
        print("==========Room Menu=========")
        print("============================")
        print()
        print("1. Add new room")
        print("2. Get room details by room no")
        print("3. Edit Room details")
        print("4. Delete room")
        print("5. View all rooms")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_room(database, cursor)
        elif choice == 2:
            room_no = int(input("Enter the room no: "))
            query = "select * from {0} where room_id={1}".format(ROOMS_TABLE_NAME, room_no)
            show_room_record(cursor, query)
        elif choice == 3:
            edit_room_by_room_no(database, cursor)
        elif choice == 4:
            delete_room_by_room_no(database, cursor)
        elif choice == 5:
            print_table(cursor,database)
        elif choice == 6:
            break
        else:
            print("Invalid choice (Press 6 to go back)")



#USER DEFINED FUNCTION TO PRINT DATA IN CUSTOMERS TABLE

def print_table_customers(cursor,database):
    query= 'select * from customers'
    cursor.execute(query)
    records=cursor.fetchall()
    print(tabulate(records,headers=['NAME','CUSTOMER_ID','ADDRESS','PHONE NUMBER','ROOM_ID','CHECKIN DATE',\
    'CHECKOUT DATE']))

#USER DEFINED FUNCTION TO TAKE INPUT FROM USER TO ENTER DATA IN CUSTOMERS TABLE

def create_customer():
    name=input('Enter customer name:')
    customer_id=int(input('Enter customer id:'))
    address=input('Enter address:')
    phone_number=int(input('Enter phone number:'))
    room_id=int(input('Enter room_id:'))
    checkin_date=datetime.now()
    return(name,customer_id,address,phone_number,room_id,checkin_date)

#USER DEFINED FUNCTION TO ADD CUSTOMER DETAILS    

def add_customer(database, cursor):
    customer = create_customer()
    confirm = input("Complete the operation? (Y/N) ").lower()
    if confirm == 'y':
        query = "insert into {0}(name,customer_id,address,phone_number,room_id,checkin_date)\
        values('{1}',{2},'{3}',{4},{5},'{6}')".format(CUSTOMER_TABLE_NAME,customer[0],customer[1],customer[2],customer[3],customer[4],customer[5])
        cursor.execute(query)
        database.commit()
        print_table_customers(cursor,database)
        print("Operation Successful")
    else:
        print("Operation Canceled")

def show_customer_records(cursor,query):
    cursor.execute(query)
    records = cursor.fetchall()
    if cursor.rowcount == 0:
        print("No Matching Records")
        return
    else:
        print(tabulate(records,headers=['NAME','CUSTOMER_ID','ADDRESS','PHONE NUMBER','ROOM_ID','CHECKIN DATE','CHECKOUT DATE']))

def exist_c(database,cursor,room_ids):
    query='select * from {0} where room_id={1}'.format(CUSTOMER_TABLE_NAME,room_ids)
    cursor.execute(query)
    records = cursor.fetchall()
    if cursor.rowcount==0:
        return False
    else:
        return True
        

def edit_customer_by_room_no(database, cursor):
    query = "update {0} set".format(CUSTOMER_TABLE_NAME)
    room_ids =int(input('Room_ID to be changed:'))
    w=exist_c(database,cursor,room_ids)
    if w==True:
        print('1:CHANGE ROOM ID')
        print('2:CHANGE ADDRESS')
        print('3:CHANGE PHONE NUMBER')
        print('4:EDIT CHECHOUT DATE')
        choice=int(input('ENTER YOUR CHOICE:'))
        if choice==1:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_room_id=int(input("Enter new room no: "))
                query += " room_id={0},".format(new_room_id)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                print_table_customers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==2:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_address =input('NEW ADDRESS:')
                query += " address='{0}',".format(new_address)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                print_table_customers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==3:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_phoneno = input("Enter new phone number: ")
                query += " phone_number='{0}',".format(new_phoneno)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                print_table_customers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==4:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                checkout_date = datetime.now()
                query += " checkout_date='{0}',".format(checkout_date)
                query = query[0:-1] + " where room_id={0} ".format(room_ids)
                cursor.execute(query)
                database.commit()
                print_table_customers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
    else:
        print('NO MATCH FOUND') 
  
def delete_customer_by_room_no(database, cursor):
    room_ids=int(input('ENTER ROOM ID TO DELETE:'))
    w=exist_c(database,cursor,room_ids)
    if w==True:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where room_id={1}".format(CUSTOMER_TABLE_NAME,room_ids)
            cursor.execute(query)
            database.commit()
            print_table_customers(cursor,database)
            print("Operation Successful")
        else:
            print("Operation Cancelled")
    else:
        print('NO MATCH FOUND')
            
#USER DEFINED FUNCTION TO DO ABOVE GIVEN OPERATIONS IN CUSTOMERS TABLE

def customer_menu(database, cursor):
    while True:
        print()
        print("==============================")
        print("==========Customer Menu=========")
        print("==============================")
        print()
        print("1. New Customer")
        print("2. Show Customer Details by name")
        print("3. Show customer details by customer_id")
        print("4. Show customer details by phone number")
        print("5. Show customer details by room no")
        print("6. Show current list of customers")
        print("7. Edit customer Details")
        print("8. Delete Customer record")
        print('9. Show all customers details')
        print("10. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_customer(database, cursor)
        elif choice == 2:
            name = input("Enter the name: ").lower()
            query = "select * from {0} where name like '%{1}%'".format(CUSTOMER_TABLE_NAME, name)
            show_customer_records(cursor, query)
        elif choice == 3:
            customer_id = input("Enter the customer id: ")
            query = "select * from {0} where customer_id = {1}".format(CUSTOMER_TABLE_NAME, customer_id)
            show_customer_records(cursor, query)
        elif choice == 4:
            phone = input("Enter the phone number: ")
            query = "select * from {0} where phone_number like '%{1}%'".format(CUSTOMER_TABLE_NAME, phone)
            show_customer_records(cursor, query)
        elif choice == 5:
            room_no = input("Enter the room_id: ")
            query = "select * from {0} where room_id = {1}".format(CUSTOMER_TABLE_NAME, room_no)
            show_customer_records(cursor, query)
        elif choice == 6:
            query = "select * from {0} where checkout_date is NULL ".format(CUSTOMER_TABLE_NAME)
            show_customer_records(cursor, query)
        elif choice == 7:
            edit_customer_by_room_no(database, cursor)
        elif choice == 8:
            delete_customer_by_room_no(database, cursor)
        elif choice==9:
            query = "select * from {0} ".format(CUSTOMER_TABLE_NAME)
            show_customer_records(cursor, query)
        elif choice == 10:
            break
        else:
            print("Invalid choice (Press 9 to go back)")

def print_table_workers(cursor,database):
    query= 'select * from workers'
    cursor.execute(query)
    records=cursor.fetchall()
    print(tabulate(records,headers=['NAME','WORKER_ID','DEPARTMENT','PHONE_NO','SALARY']))

def create_workers():
    name=input('Enter worker name:')
    worker_id=int(input('Enter worker id:'))
    dept=input('Enter department:')
    phone_number=int(input('Enter phone number:'))
    salary=float(input('Enter salary:'))
    return(name,worker_id,dept,phone_number,salary)

def add_workers(database, cursor):
    worker = create_workers()
    confirm = input("Complete the operation? (Y/N) ").lower()
    if confirm == 'y':
        query = "insert into {0}(name,worker_id,department,phone_number,salary)\
        values('{1}',{2},'{3}',{4},{5})". \
        format(WORKER_TABLE_NAME,worker[0],worker[1],worker[2],worker[3],worker[4])
        cursor.execute(query)
        database.commit()
        print_table_workers(cursor,database)
        print("Operation Successful")
    else:
        print("Operation Canceled")

def exist_w(database,cursor,worker_id):
    query='select * from {0} where worker_id={1}'.format(WORKER_TABLE_NAME,worker_id)
    cursor.execute(query)
    records = cursor.fetchall()
    if cursor.rowcount==0:
        return False
    else:
        return True

def edit_worker_by_worker_id(database, cursor):
    query = "update {0} set".format(WORKER_TABLE_NAME)
    worker_id=int(input('Worker_id to be changed:'))
    w=exist_w(database,cursor,worker_id)
    if w==True:
        print('1:CHANGE WORKER ID')
        print('2:CHANGE SALARY')
        print('3:CHANGE PHONE NUMBER')
        print('4:CHANGE DEPARTMENT')
        choice=int(input('ENTER YOUR CHOICE:'))
        if choice==1:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_worker_id=input("Enter new worker id: ")
                query += " worker_id={0},".format(new_worker_id)
                query = query[0:-1] + " where worker_id={0} ".format(worker_id)
                cursor.execute(query)
                database.commit()
                print_table_workers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==2:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_salary =input('NEW SALARY:')
                query += " salary='{0}',".format(new_salary)
                query = query[0:-1] + " where worker_id={0} ".format(worker_id)
                cursor.execute(query)
                database.commit()
                print_table_workers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==3:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_phoneno = int(input("Enter new phone number: "))
                query += " phone_number='{0}',".format(new_phoneno)
                query = query[0:-1] + " where worker_id={0} ".format(worker_id)
                cursor.execute(query)
                database.commit()
                print_table_workers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
        if choice==4:
            confirm = input("Confirm Update (Y/N): ").lower()
            if confirm == 'y':
                new_dept = input("Enter new department: ")
                query += " department='{0}',".format(new_dept)
                query = query[0:-1] + " where worker_id={0} ".format(worker_id)
                cursor.execute(query)
                database.commit()
                print_table_workers(cursor,database)
                print("Operation Successful")
            else:
                print("Operation Cancelled")
    else:
        print('NO MATCH FOUND')

def delete_worker_by_room_no(database, cursor):
    worker_id=int(input('ENTER worker ID TO DELETE:'))
    w=exist_w(database,cursor,worker_id)
    if w==True:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where worker_id={1}".format(WORKER_TABLE_NAME,worker_id )
            cursor.execute(query)
            database.commit()
            print_table_workers(cursor,database)
            print("Operation Successful")
        else:
            print("Operation Cancelled")
    else:
        print('NO MATCH FOUND')

def annual_salary(database,cursor):
    query='select name,salary*12 from {0}'.format(WORKER_TABLE_NAME)
    print('1.Want to print all workers salary')
    print('2.Print salary of particular worker')
    choice=int(input('Enter your choice ='))
    if choice==1:
        cursor.execute(query)
        records=cursor.fetchall()
        print(tabulate(records,headers=['NAME','ANNUAL SALARY']))
    elif choice==2:
        worker_id=int(input('Enter worker id : '))
        w=exist_w(database,cursor,worker_id)
        if w==True:
            query='select name,salary*12 from {0} where worker_id={1}'.format(WORKER_TABLE_NAME,worker_id)
            cursor.execute(query)
            record=cursor.fetchall()
            print(tabulate(record,headers=['NAME','ANNUAL SALARY']))
        else:
            print('NO MATCH FOUND')
    else:
        print('invalid input')
        
def worker_menu(database, cursor):
    while True:
        print()
        print("==============================")
        print("==========WORKER MENU=========")
        print("==============================")
        print()
        print("1. New Worker")
        print("2. Edit Worker Details")
        print("3. Delete Worker record")
        print("4. Annual Salary")
        print('5. Show Worker Details')
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_workers(database, cursor)
        elif choice == 2:
            edit_worker_by_worker_id(database, cursor)
        elif choice == 3:
            delete_worker_by_room_no(database, cursor)
        elif choice==4:
            annual_salary(database,cursor)
        elif choice==5:
            print_table_workers(cursor,database)
        elif choice == 6:
            break
        else:
            print("Invalid choice (Press 9 to go back)")

#MAIN PART OF THE SYSTEM

database, cursor = get_database()
if database is None:
    print("The Database does not exist or not accessible.")
    exit(1)
table1(database,cursor)
table2(database,cursor)
table3(database,cursor)
psd=input('ENTER PASSWORD TO ACCESS DATABASE : ').lower()
if psd=='aknk':
    while True:
        print()
        print("==============================")
        print("=====A AND N=====")
        print("==============================")
        print("1. Manage Rooms")
        print("2. Manage Customers")
        print('3. Worker details')
        print("0. Exit")
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            room_menu(database, cursor)
        elif choice == 2:
            customer_menu(database, cursor)
        elif choice==3:
            worker_menu(database, cursor)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")

else:

    print('invalid password')
    exit()


    

import psycopg2 # would help in interacting with postgres
from psycopg2.extras import execute_batch
import datetime # tasks would have dates
'''
features:
- add task
- view tasks
- update tasks
- delete task
- save to the db
- read from the db

a task should have a description, a due date and done or yet to be done status
using postgres for persistence (CRUD)
'''

def display_menu():
    print("\nTodo App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return int(choice)

class task:
    def __init__(self, title :str, description : str, due_date : datetime.date, due_time: datetime.time, status=0):
        self.description = description
        self.due_date = due_date
        self.due_time = due_time 
        self.status = status
        self.title = title

def validate_due_date():
    while True:
        due_date = input("due date in yy-mm-dd: ").strip()
        
        try:
            year, month, day = map(int, due_date.split("-"))
            if not (year >= int(datetime.date.today().year)):
                raise ValueError("Year can not be in the past")
                continue
            elif year > datetime.date.today().year  and (month < datetime.date.today().month or day < datetime.date.today().day):
                raise ValueError("Month or Day can't be in the past")
                continue
            elif year > 9999 or month not in range(1,13) or day not in range(1,32):
                raise ValueError("Values out of range")
                continue
            return(datetime.date(year, month, day))
            break
            
        except Exception as err:
            print("supply the date in the correct format", err)
            continue

def validate_creation_date():
        
    while True:    
        creation_date = input("creation date in yy-mm-dd: ").strip()
        try:

            year, month, day = map(int, creation_date.split("-"))
            if not (year in range(1900, int(datetime.date.today().year) + 1)):
                raise ValueError("Year created can not be in the future")
                continue
            elif (year == datetime.date.today().year  and month > datetime.date.today().month) or (year == datetime.date.today().year and month == datetime.date.today().month and day > datetime.date.today().day):
                raise ValueError("Month or Day can't be in the past")
                continue
            elif year > 9999 or month not in range(1,12) or day not in range(1,31):
                raise ValueError("Values out of range")
                continue
            return(datetime.date(year, month, day))
            break
            
        except Exception as err:
            print("supply the date in the correct format", err)
            


def add_task():

    due_date = validate_due_date()
    status = False
    date_created = datetime.date.today()
    
    while True: # title is compulsory
        title = input("Task title: ")
        match title:
            case "":
                print("supply a valid title")
                continue
            case _:
                break
    
    description = input("Task description: ") #optional
    
   
        
    
    while True:
        due_time = input("Due time in HH:MIN:SS ").strip()
        try:
            hour, min, sec = map(int, due_time.split(":"))
            if not (hour in range(0,23) and min in range(0, 59) and sec in range(0,59)):
                raise ValueError("Invalid time values")
            time = datetime.time(hour, min, sec)

            break   
        except Exception  as err:
            print("supply the time in the correct format", err)
    

    return (title, description, date_created ,due_date, time, status) # return a tuple with the details

def save_to_db(conn, cur, tasks_arr: list):
    sql_insert_statement= '''
                    INSERT INTO tasks (title, description, Date_created, Due_date, due_time, status)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    '''
    try:
        execute_batch(cur, sql_insert_statement, tasks_arr) #faster than running cur.execute in a loop which is similar to executemany()
    except (psycopg2.errors, Exception) as e:
        print(f"error saving to the DB: {e} ")
    else:
        print("successfully saved to DB")
    conn.commit()
 
    #for task in tasks_arr:
    #    cur.execute('''
    #                INSERT INTO tasks (title, description, status, Due_date, due_time)
    #                VALUES (%s, %s, %s, %s, %s)
    #                ''', (task.title, task.description, task.status, task.due_date, task.due_time ))

def view_tasks(cur):
    date_created = validate_creation_date()
    cur.execute('''
        SELECT * FROM tasks WHERE Date_created = %s
''', (date_created,)) #NOTE:The second argument to execute must be a tuple, even if only one variable is passed.
    retrieved_Tasks = cur.fetchall()
    for task in retrieved_Tasks:
        print(f"\n{task}")
    
    
    
    

#connect to database 
def main():
    #print(datetime.date.today().year)
    DBNAME = "todolist"
    USER = "postgres"
    PASSWORD = "9191s"
    HOST = "localhost"
    PORT = 5432

    try:
        conn = psycopg2.connect(database=DBNAME, user=USER, host=HOST, password=PASSWORD, port=PORT)
        cur = conn.cursor()
    except (psycopg2.Error, Exception) as e:
        print(f"an error occured: {e}")
        raise # reraise the error to interrupt the program

    else:
        print("connection sucessful")
        cur.execute("CREATE TABLE IF NOT EXISTS tasks(\
                    id serial Primary Key, \
                    title varchar(100) Not Null,\
                    description text,\
                    Date_created date Not Null,\
                    Due_date date Not Null,\
                    due_time time,\
                    status boolean Not Null);")
        
        
        tasks = []
        action = display_menu()
        if action == 1:
            while True:
                tasks.append(add_task())
                x = input("do you want to add another task? ")
                if x not in ['y','Y', "yes", "YES", "Yes"]:
                    break
                else:
                    continue
            save_choice = input("Do you want to save current tasks? ")
            if save_choice in ['y','Y', "yes", "YES", "Yes"]:
                save_to_db(conn, cur,tasks)
            # if not, then you want to update a certain task, but I won't implement that yet
        
        if action == 2:
            view_tasks(cur)


    
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
    
 


import Expense
import Budget
import mysql.connector as db
from Expense import Expense as Expense_Obj
from datetime import datetime

#Budget Creation
#Get Year   (str)
#Get Month  (str)
#Dict key = Month+Year (str)
#Dict values are lists of Expense_Objs

#a = Expense_Obj(1,2,2023, 20, "gas", "shell")
#b = Expense_Obj(3,1,2020, 10, "food", "bk")

mydb = db.connect(
        host="192.168.1.111",
        user="hayden",
        password="032600",
        database = "PiEx"
    )
    #buffered = true is important
cursor = mydb.cursor(buffered=True)

def format_month(month):
        if type(month) is int or float:
            if month in Expense.month_dict.keys():
                return Expense.month_dict[month].upper()
            else:
                month = input("ERROR: Invalid Month\nEnter a valid number for month: ")
                return format_month(month)
        elif type(month) is str:
            if month.lower() in Expense.month_dict.values():
                return month.upper()
            elif month.lower() in  Expense.month_dict_str:
                return Expense.month_dict_str[month.lower()].upper()
            else:
                month = input("Enter the month of this expense as a word: ")
                return format_month(month)
        else:
                month = input("Enter the month of this expense as a word: ")
                return format_month(month)

def main_menu() -> None:
    while(True):
        while(True):
            print("Budget Tracking Program v0.1")
            print("______________________________________________________")
            print("1. View Budget For Current Month")
            print("2. View Budget For Another Month")
            print("3. Create a Budget For This Month")
            print("4. Read file")
            print("0. Exit")
            try:
                menu_selection = int(input("Your Selection: "))
                if menu_selection < 0 or menu_selection > 4:
                    raise ValueError("ERROR: Invalid Number Selected.")
                else:
                    break
            except ValueError as err:
                print(err)
                print("Continue cycle")
                continue
            
        match menu_selection:
            case 1:
                #Get Curent Month
                #View for current month
                get_month_budget(datetime.today().month, datetime.today().year)
                print(1)
            case 2:
                #Get Month
                #View for that month
                month = Expense.Expense.format_month(month)
                year = Expense.get_year()
                get_month_budget(month, year)
                print(2)
            case 3:
                #Create Budget for this month
                #View Budget after creation
                budget_categories = Budget.create_budget(datetime.today().month, datetime.today().year)
                insert_budget(format_month(datetime.today().month), datetime.today().year, budget_categories)
                #print(3)
            case 4:
                #Read?
                print(4)
            case 0:
                return None
    
def drop_tables():
    cursor.execute("DROP TABLE Expense;"
                    "DROP TABLE Budget;"
                    "DROP TABLE Categories;"
                    )
def db_replace_tables():
    
    TABLES = {}
    TABLES['Categories'] = (
        "CREATE OR REPLACE TABLE Categories ("
        "cat varchar(20) NOT NULL,"
        "PRIMARY KEY (cat)"
        ")")

    TABLES['Budget'] = (
        "CREATE OR REPLACE TABLE Budget ("
        "month varchar(15) NOT NULL,"
        "year int NOT NULL,"
        "amount int(10) NOT NULL,"
        "cat varchar(20) NOT NULL,"
        "PRIMARY KEY (month,year,cat),"
        "CONSTRAINT bud_cat_fk FOREIGN KEY (cat)"
        "REFERENCES Categories(cat) ON DELETE CASCADE"
        ")")
    
    TABLES['Expense'] = (
        "CREATE OR REPLACE TABLE Expense ("+
        "month varchar(15) NOT NULL,"
        "day int(3) NOT NULL,"
        "year int NOT NULL,"
        "amount decimal(10,2) NOT NULL,"
        "cat varchar(20) NOT NULL,"
        "thing varchar(50) NOT NULL,"
        "PRIMARY KEY (month,day,thing),"
        "CONSTRAINT exp_month_fk FOREIGN KEY (month, year)"
        "REFERENCES Budget(month, year) ON DELETE CASCADE,"
        "CONSTRAINT exp_cat_fk FOREIGN KEY (cat)"
        "REFERENCES Categories(cat) ON DELETE CASCADE"
        ")")
   # for item in TABLES.keys():
      #  cursor.execute("DROP TABLE IF EXISTS " + item)
    for item in TABLES.values():
        cursor.execute(item)

    return

def insert_budget(month, year, bud_list):
    for item in bud_list:
        sql = "INSERT INTO Categories (cat) VALUES (%s)"
        val = (item[0],)
        cursor.execute(sql, val)
        sql = "INSERT INTO Budget (month, year, amount, cat) VALUE (%s, %s, %s, %s)"
        val = (month, year, item[1], item[0])
        cursor.execute(sql,val)
    mydb.commit()
    return
def get_month_budget(month, year):
    cursor.execute("SELECT * FROM Budget WHERE month = '"+
                   month+
                   "' AND year = '"+
                   str(year)+
                   ";")
    result = cursor.fetchall()
    for row in result:
        print(row)
    return

def main() -> int:
    db_replace_tables()
    drop_tables()
    #main_menu()
    return 0


if __name__ == '__main__':
    main()
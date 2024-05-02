from datetime import datetime

month_dict = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec"
}

month_dict_str= {
    "january": month_dict[1],
    "february": month_dict[2],
    "march": month_dict[3],
    "april": month_dict[4],
    "may": month_dict[5],
    "june": month_dict[6],
    "july": month_dict[7],
    "august": month_dict[8],
    "september": month_dict[9],
    "october": month_dict[10],
    "november": month_dict[11],
    "december": month_dict[12]
}


class Expense:
    def __init__ (self, month, day:int, year:int, amount:float, cat:str, thing:str):
        self.month = self.format_month(month)
        self.day = day
        self.year = year
        self.cat = cat.upper()  #Dependent on budget categories set outside this class
        self.amount = amount
        self.thing = thing

    #LESS THAN COMPARES DAY FOR EASY LIST.SORT() OF MONTH BUDGET
    def __lt__(self, other) -> bool:
        if self.day < other.day:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return str(self.month) + " " + str(self.day) + ", " + str(self.year) +": $" + str(self.amount) + " on " + str(self.cat) +" at " + str(self.thing)


    def format_month(self, month):
        if type(month) is int or float:
            if month in month_dict.keys():
                return month_dict[month].upper()
            else:
                month = input("ERROR: Invalid Month\nEnter a valid number for month: ")
                return self.format_month(month)
        elif type(month) is str:
            if month.lower() in month_dict.values():
                return month.upper()
            elif month.lower() in  month_dict_str:
                return month_dict_str[month.lower()].upper()
            else:
                month = input("Enter the month of this expense as a word: ")
                return self.format_month(month)
        else:
                month = input("Enter the month of this expense as a word: ")
                return self.format_month(month)
        
    def set_cat(self,cat:str):
        self.cat = cat.upper()

def get_day() -> int:
    while True:
        try:
            day = int(input("Enter the day: "))
            if day <=0 or day >31:
                raise ValueError("ERROR: Day must be between 1 and 31.\n")
            else:
                break
        except TypeError as err:
            print("ERROR: Enter an integer.\n")
            continue
        except ValueError as err:
            print(err)
            continue

    return day

def get_year() -> int:
    while True:
        try:
            year = int(input("Enter the year: "))
            if year < 2023 or year > datetime.now().year:
                raise ValueError("ERROR: Year must be between between 2023 and " + str(datetime.now().year) + ".\n")
            else:
                break
        except TypeError:
            print("ERROR: Enter an integer.\n")
            continue
        except ValueError as err:
            print(err)
            continue

    return year

def get_amount() -> float:
    while True:
        try:
            amount = float(input("Dollar amount for expense: "))
            if amount <=0 :
                raise ValueError("ERROR: Amount must be greater than 0.\n")
            else:
                break
        except TypeError as err:
            print("ERROR: Enter a decimal value.\n")
            continue
        except ValueError as err:
            print(err)
            continue

    return amount

def new_expense() -> Expense:
    print("Creating new expense...\n")
    print("Enter Date\n=======================================")
    month = input("Enter the month: ")

    day = get_day()
    year = get_year()

    print("\nExpense Information\n=======================================")
    #Find a way to enforce categories later
    cat: str = input("Category for this expense: ")
    amount: float = get_amount()
    thing: str = input("Where/What was this for: ")
    
    return Expense(month, day, year, amount, cat, thing)
    
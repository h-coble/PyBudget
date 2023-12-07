import Expense
import Budget
from Expense import Expense as Expense_Obj
from datetime import datetime

#Budget Creation
#Get Year   (str)
#Get Month  (str)
#Dict key = Month+Year (str)
#Dict values are lists of Expense_Objs

"""a = Expense_Obj(1,2,2023, 20, "gas", "shell")
b = Expense_Obj(3,1,2020, 10, "food", "bk")"""

def main_menu() -> None:
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
            
            print(1)
        case 2:
            #Get Month
            #View for that month
            print(2)
        case 3:
            #Create Budget for this month
            #View Budget after creation
            Budget.create_budget(datetime.today().month, datetime.today().year)
            print(3)
        case 4:
            #Read?
            print(4)
        case 0:
            return None
    
def main() -> int:
    main_menu()
    print("Out of Menu")
    return 0


if __name__ == '__main__':
    main()
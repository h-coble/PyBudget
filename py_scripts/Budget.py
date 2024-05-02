Budgets = {

}

def create_budget(month, year):
    key = str(month) + "_"+ str(year)
    print("Budget for " + key)
    print("=========================================")

    #Get Income
    while True:
        try:
            income = float(input("Enter your total income for this month: "))
            if income < 0:
                raise ValueError("ERROR: Negative Income")
            else:
                match input("You earned/will earn $" + str(income) + " this month.\nIs this correct (Y/N)?")[0].upper():
                    case "Y":
                        print("Income confirmed, moving on...\n")
                        break
                    case "N":
                        print("Income not confirmed, restarting...")
                        continue
                    case _:
                        raise ValueError("ERROR: Enter Y or N")
        except ValueError as err:
            print(err)
            continue

    #Get Categories
    category_count = 1
    cat_list = []
    print("MESSAGE TO USER: Enter \"Done\" when you have entered all categories.\n")
    
    while True:
        try:
            cat = input("Enter the Name of Category #" + str(category_count) +": ").upper()
            if cat == "DONE":
                print("Your categories are: ")
                for each in cat_list:
                    print("\t-"+each)
                break
            elif cat not in cat_list:
                cat_list.append(cat)
                category_count += 1
            elif cat in cat_list:
                raise ValueError("ERROR: Category already entered")
            
        except ValueError as err:
            print(err)
        continue
    
    #Planned Amounts
    amount_list = []
    amount = float(0)
    income_dec = income
    for each in cat_list:
        while True:
            try:
                print("You have $"+str(income_dec) + " remaining for this month.")
                amount =  float(input("Enter the dollar amount you will spend on " + each+": "))
                if amount < 0:
                    raise ValueError("ERROR: Negative Expenses")
                elif amount > income_dec:
                    raise ValueError("ERROR: Expenses > Remaing Income")
                else:
                    match input("You spent/will spend " + str(amount) + " this month on " + each+". Is this correct (Y/N)?")[0].upper():
                        case "Y":
                            print("Confirmed, next...\n")
                            income_dec -= amount
                            break
                        case "N":
                            raise ValueError("Amount not confirmed, going back...")
                        case _:
                            raise ValueError("ERROR: Enter Y or N")            
            except ValueError or IndexError as err:
                amount = 0
                print(err)
                continue

        amount_list.append(amount)

    if income_dec > 0:
        cat_list.append("SAVINGS")
        amount_list.append(income_dec)

    final_list = [("TOTAL", income)]
    for each in cat_list:
        final_list.append((each, amount_list[cat_list.index(each)]))
    
    Budgets[key] = final_list
    #Print Budget to It's own file
    return final_list


        
def main():
    return None

if __name__ == '__main__':
    main()


"""
IDEAS TO CONTINUE:
-Budget class
    >Plan (create_budget -> list of tuples)
    >Expenses (list of Expense obj)
        =Get Month Day Year Format Uniform
"""
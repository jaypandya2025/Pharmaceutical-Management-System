import mysql.connector

# database: yep
# Table: medmgmt
# columns: Medicine_ID, Medicine, Manufacturer, Date_of_Manufacture, Date_of_Expiry, Quantity, Price

conn = mysql.connector.connect(host="localhost", password="batman", username="root")
mycur = conn.cursor()

# (after the table is created)
print("WELCOME TO PHARMACEUTICAL MANAGEMENT.")


def access():
    print()
    while True:
        pwd = input("Enter password: ")
        if pwd == "PharmaRox123":
            print("\nWelcome retailer. Choose from the following possible options.")
            mainmenu()
            break
        else:
            print("Try again. Hint: It's a horrible password.")


# FUNCTIONS
def group_medicine():
    print("Grouping by medicine name and displaying their count")
    sql = "select count(*),Medicine from medmgmt group by Medicine"
    mycur.execute(sql)
    for i in mycur:
        print(i)
    print("Records successfully grouped by medicine names")
    print()


def group_price():
    print("Grouping by price and displaying its count")
    sql = "select count(*),Price from medmgmt group by Price"
    mycur.execute(sql)
    for i in mycur:
        print(i)
    print("Prices successfully grouped.")
    print()


def addrec():
    print()
    print("Adding record of medicine")
    medid = int(input("Enter medicine ID: "))
    medicine = input("Enter name of medicine: ")
    manuf = input("Enter name of manufacturer: ")
    dom = input("Enter date of manufacture (YYYY-MM-DD): ")
    doe = input("Enter date of expiry (YYYY-MM-DD): ")
    quantity = int(input("Enter quantity of medicine: "))
    price = int(input("Enter price of 1 unit: "))
    sql = "insert into medmgmt values(%s,%s,%s,%s,%s,%s,%s);"
    val = (medid, medicine, manuf, dom, doe, quantity, price,)
    mycur.execute(sql, val)
    print("Record added successfully.")
    print()


def viewall():
    print()
    mycur.execute("select * from medmgmt;")
    records = mycur.fetchall()
    for x in records:
        print(x, sep="\t")
    print()
    print("\nRecords printed successfully")
    print()


def removerec():
    print()
    medid = int(input("Enter ID of the medicine that you want to remove: "))
    l = [medid]
    sql = "delete from medmgmt where Medicine_ID = %s;"
    mycur.execute(sql, l)
    print("\nRecord deleted successfully.")
    print()


def updaterec():
    print()
    while True:
        medid_ = int(input("Enter ID of the medicine whose information is to be updated: "))
        mycur.execute("select * from medmgmt where Medicine_ID = " + (str(medid_)))
        for i in mycur:
            print(i, end="\t")
        x = input("\nIs this the record that needs to be updated? (y/n) ").strip().lower()
        if x == "y":
            print()
            mycur.execute("delete from medmgmt where Medicine_ID =" + (str(medid_)))
            print("Enter the updated values of the medication")
            medid = int(input("Medicine ID: "))
            med = input("Medicine Name: ")
            manuf = input("Manufacturer: ")
            dom = input("Date of Manufacture (YYYYMMDD): ")
            doe = input("Date of Expiry (YYYYMMDD): ")
            quantity = int(input("Quantity: "))
            price = int(input("Price: "))
            sql = "insert into medmgmt values(%s,%s,%s,%s,%s,%s,%s);"
            val = (medid, med, manuf, dom, doe, quantity, price,)
            mycur.execute(sql, val)
            # first removed the selected info, and then added newer, updated info
            print("\nRecord updated successfully")
            print()
            break
        else:
            print()


def sortrecs():
    print()
    while True:
        print("COLUMNS: Medicine_ID, Medicine, Manufacturer, Date_of_Manufacture, Date_of_Expiry, Quantity, Price")
        choice = input("Enter column name on the basis of which table should be sorted: ")
        ascdesc = input("Ascending or descending? (asc/desc): ").strip().lower()
        if choice in ("Medicine_ID", "Medicine", "Manufacturer", "Date of Manufacture", "Date of Expiry", "Quantity", "Price"):
            if ascdesc == "asc":
                mycur.execute("select * from medmgmt order by " + choice + " asc;")
                for i in mycur:
                    print(i)
                print("\nAll records printed.\n")
                break
            elif ascdesc == "desc":
                mycur.execute("select * from medmgmt order by " + choice + " desc;")
                for i in mycur:
                    print(i)
                print("\nAll records printed.\n")
                break
            else:
                print("Kindly respond with asc or desc.\n")
        else:
            print("Please enter column name in the correct case and ensure there are no mistakes. Thank you!\n")


def search():
    print("Search for medicine based on name, manufacturer, or expiry date")
    choice = input("Enter 'name', 'manufacturer', or 'expiry date' to search by: ").strip().lower()
    if choice == 'name':
        name = input("Enter medicine name: ").strip().lower()
        val = (name,)
        sql = "SELECT * FROM medmgmt WHERE Medicine = %s"
        mycur.execute(sql, val)
    elif choice == 'manufacturer':
        manufacturer = input("Enter manufacturer name: ").strip().lower()
        val = (manufacturer,)
        sql = "SELECT * FROM medmgmt WHERE Manufacturer = %s"
        mycur.execute(sql, val)
    elif choice == 'expiry date':
        expiry_date = input("Enter expiry date (YYYYMMDD): ").strip().lower()
        val = (expiry_date,)
        sql = "SELECT * FROM medmgmt WHERE Date_of_Expiry = %s"
        mycur.execute(sql, val)
    else:
        print("Invalid choice. Please enter 'name', 'manufacturer', or 'expiry date'.")
        return
    results = mycur.fetchall()
    for record in results:
        print(record)
    if not results:
        print("No records found.")
    print()


def exit_program():
    print("Exiting the program. Goodbye!")
    conn.close()


def mainmenu():
    print()
    print('=' * 30)
    print("\tMAIN MENU")
    print('=' * 30)
    print("1. Add new medication")
    print("2. Remove medication record")
    print("3. Update information")
    print("4. Group medicines by prices")
    print("5. Group by medicine stocks")
    print("6. Search for medicine on the basis of name, manufacturer, expiry date")
    print("7. View all records")
    print("8. Sorting records in ascending or descending order")
    print("9. Exit")
    print('=' * 30)
    while True:
        user_choice = int(input("\nEnter choice number from 1 to 9: "))
        if user_choice == 1:
            addrec()
        elif user_choice == 2:
            removerec()
        elif user_choice == 3:
            updaterec()
        elif user_choice == 4:
            group_price()
        elif user_choice == 5:
            group_medicine()
        elif user_choice == 6:
            search()
        elif user_choice == 7:
            viewall()
        elif user_choice == 8:
            sortrecs()
        elif user_choice == 9:
            exit_program()
        else:
            print("Kindly enter a valid choice from 1 to 9 numbers.\n")

        conn.commit()
        x = input("Would you like to execute any of the given operations again? (y/n): ").strip().lower()
        if x == "n":
            print("Thank you :)")
            conn.close()
            break


access()


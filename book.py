import add_Contacts
import view_add_Contacts
from remove_Contacts import remove_Contacts


all_Contacts =[]

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1.Add Contacts:")
    print("2. View Contacts")
    print("3. remove Contracts")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Contact Book Management System!")
        break
    elif menu == "1":
        add_Contacts = add_Contacts.add_Contacts(all_Contacts)
        
    elif menu == "2":
        view_add_Contacts.view_add_Contacts(all_Contacts)

    elif menu == "3":
        add_Contacts = remove_Contacts(all_Contacts)
    else:
        print("Choose a valid number.")

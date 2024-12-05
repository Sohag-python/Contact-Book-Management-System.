def view_add_Contacts(add_Contacts):
    if add_Contacts != []:
        for Contacts in add_Contacts:
            print(f"Title: {Contacts['title']} | Name: {Contacts['Name']} | Phone: {Contacts['Phone']} | Email: {Contacts['Email']} | Address: {Contacts['Address']}")
    else:
        print("No Book found in program")
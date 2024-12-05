class Contracts:
    pass


def remove_Contacts(add_Contacts):
    if not add_Contacts:
        print("No Contracts available to remove.")
        return add_Contacts

    phone = int(input("Enter phobe of the book to remove: "))
    for i, Contacts in enumerate(add_Contacts):
        if Contracts['phone'] == phone:
            print(f"Contacts '{Contacts['title']}' removed successfully!")
            del add_Contacts[i]
            return add_Contacts
    print("Book with the given ISBN not found.")
    return add_Contacts
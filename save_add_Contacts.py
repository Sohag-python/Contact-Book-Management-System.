def save_add_Contacts(add_Contacts):
    with open("add_Contacts.csv", "w") as fp:
        for Contacts in add_Contacts:
            line = f"{Contacts['title']}, {Contacts['name']}, {Contacts['phone']}, {Contacts['email']}, {Contacts['address']}\n"
            fp.write(line)
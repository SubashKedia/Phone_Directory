contact = {}

def display_contact():
    print("Name\t\tContact")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))

while True:
    choice = int(input("1. Add contact \n2. Search contact \n3. Display contact \n4. Edit contact \n5. Delete contact \n6. Exit \nEnter your choice: "))
    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "phone number is", contact[search_name])
        else:
            print("The name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("The contact book is empty")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the name for editing: ")
        if edit_contact in contact:
            phone = input("Enter the phone number: ")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("The contact is not found in the contact book")
    elif choice == 5:
        del_contact = input("Enter the name to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n: ")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("The contact is not found in the contact book")
    else:
        break

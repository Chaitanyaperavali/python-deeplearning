
# class to create contact objects
class Contact(object):

    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email

    def setName(self,name):
        self.name = name

    def setNum(self,num):
        self.number = num

    def setEmail(self,email):
        self.email = email

# class that holds list of classes
class ContactList(object):

    contacts = []

    # Edits contact by name. Takes name and contact as input.
    def edit_contact_by_name(self,name,contact):
        found = -1
        # iterate over each item in a contacts list and updates values from the argument contact object
        # if contact is found updates the data else return error message
        for list_item in self.contacts:
            if list_item.name == name:
                found = 1
                list_item.setName(contact.name)
                list_item.setNum(contact.number)
                list_item.setEmail(contact.email)
                break
        if found == -1:
            print("Contact not found")

    # Displays contact by name
    def display_contact_by_name(self, name):
        # Iterates over all the contacts in a list and compares based on name
        # if Contact not found returns error message
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                # self.display_contact(contact)
                return contact
        print("Contact for "+name+" not found")

    # Display contact by Number
    def display_contact_by_number(self, number):
        # Iterates over all the contacts in a list and compares based on number
        # if Contact not found returns error message
        for contact in self.contacts:
            if contact.number.lower() == number.lower():
                return contact
        print(number + " not found")

    # Adds new contact, name number and email are arguments
    def add_contact(self, name, num, email):
        contact = Contact(name, num, email)
        self.contacts.append(contact)

    # Displays contact
    def display_contact(self,contact):
        print(str(contact.name)+" "+str(contact.number)+" "+str(contact.email))

    # Function to display full contact list
    def display_contact_list(self):
        for contact in self.contacts:
            self.display_contact(contact)

    # System execution start from here
    def do_operations(self):

        print("Select from options\n"
              "0: Display contact by name\n"
              "1: Display contact by number\n"
              "2: Edit contact\n"
              "3: Add contact\n"
              "\nq/Q to quit")

        operation = str(input("Option: "))

        # if true respective operations are performed
        while operation != "q" and operation != "Q":

            # display contact by name
            if operation == "0":
                val = self.display_contact_by_name(str(input("Enter name to display\n")))
                if type(val) == Contact:
                    self.display_contact(val)

            # display contact by number
            elif operation == "1":
                val = self.display_contact_by_number(str(input("Enter number to display\n")))
                if type(val) == Contact:
                    self.display_contact(val)

            # edit contact
            elif operation == "2":
                print("Editing contact...")
                name = str(input("Enter name: \n"))
                con = self.display_contact_by_name(name)
                if Contact == type(con):
                    new_name = name
                    number = con.number
                    email = con.email
                    if str(input("Do u want to change name? y/n:\n")) == "y":
                        print("Enter new name: ")
                        new_name = str(input())
                    if str(input("New number? y/n:")) == "y":
                        print("Enter Phone: ")
                        number = str(input())
                    if str(input("New email? y/n:")) == "y":
                        print("Enter email: ")
                        email = str(input())
                    contact = Contact(new_name, number, email)
                    self.edit_contact_by_name(name, contact)
                    self.display_contact_list()

            # add contact
            elif operation == "3":
                print("Adding new contact..")
                name = str(input("Name : "))
                number = str(input("Number : "))
                email = str(input("Email : "))
                if name != "" and (number != "" or email != ""):
                    self.add_contact(name, number, email)
                self.display_contact_list()
            else:
                print("Please select from the given set of operations")

            operation = str(input("Option: "))


# Creates empty contact list and adds contact one by one
c = ContactList()
c.do_operations()
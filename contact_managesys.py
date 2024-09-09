#contact management system

class ContactManager:
    def __init__(self):  #constructor
        self.contacts={}

    def add_contact(self): #in this function details were added.
        name=input("Enter name: ")
        phone_number=input("enter phone number: ")
        email=input("Enter email: ")
        self.contacts[name]={"phone_number":phone_number,"email":email}
        print("Contact added successfully.")


    def view_contacts(self): #in this we will view the contact details
        for name,details in self.contacts.items():
            print(f"Name:{name}")
            print(f"Phone Number:{details['phone_number']}")
            print(f"Email:{details['email']}")
            print("-------------------")

    def edit_contact(self): #we will update the contacts detail
        name=input("Enter name of contact to edit: ")

        if name in self.contacts:
            phone_number=input("Enter new phone number(press enter to skip):")
            email=input("Enter new email(press enter to skip):")
    
            if phone_number:
                self.contacts[name]["phone_number"]=phone_number
            if email:
                self.contacts[name]["email"]=email
                print("Contact updated successfully.")
            else:
                print("Contact not found!")
        
    def delete_contact(self): #we will delete the contact details
        name=input("Enter name of contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found!")


        
def main():
     contact_manager=ContactManager()
     while True:
        print("1. ADD Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        Choice=int(input("Enter your choice: "))
        if Choice==1:
            contact_manager.add_contact()
        elif Choice==2:
            contact_manager.view_contacts()
        elif Choice==3:
            contact_manager.edit_contact()
        elif Choice==4:
            contact_manager.delete_contact()
        elif Choice==5:
            break
        else:
            print("Invalid choice! Please try again.")

if __name__=="__main__":
    main()

    
# ob=ContactManager()
# ob.add_contact()



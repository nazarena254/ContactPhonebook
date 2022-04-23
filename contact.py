from os import device_encoding
import pyperclip

class Contact:
    contact_list=[]
    def __init__(self,first_name,last_name, phone_number, email):
          self.first_name=first_name
          self.last_name=last_name
          self.phone_number = phone_number
          self.email=email
    def save_contact(self):
          Contact.contact_list.append(self)
    def delete_contact(self):
        Contact.contact_list.remove(self) 
    @classmethod
    def find_by_number(cls,number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    @classmethod
    def contact_exist(cls,number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True
        return False 
    @classmethod
    def display_contacts(cls): #  method that returns the contact list
        return cls.contact_list 
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)                                    
    def viewcontact(self):
          print(self.first_name)
          print(self.last_name)
          print(self.phone_number)
          print(self.email) 
        #   print("list of contacts: ",self.contact_list)
   
def main():
    new_contact = Contact ("James","Muriuki","0712345678","james@gmail.com") 
    print(new_contact.viewcontact())
 
if __name__=="__main__":
    main()

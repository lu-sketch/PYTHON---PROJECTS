
# An Email simulation:

class Email:
    inbox = []

    def __init__(self, from_address, email_contents, has_been_read, is_spam):
        """ Constructor method for class Email:"""
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    has_been_read = False
    is_spam = False


# Marked email in inbox as read
def mark_as_read(self):
    return self.has_been_read == True


# Marked email in inbox as spam
def mark_as_spam(self):
    return self.is_spam == True


# adding an email to inbox
def add_mail(address = None,contents = None):
    """ This function is supposed to add email to be sent to inbox"""
    if address and contents == None:
        return address,contents
    else:
        email = address, contents
        return Email.inbox.append(email)


# Create objects for Email()
email1 = ("nick@standardbank.co.za", "Hi Nick can we have the budget meeting tomorrow, Chris", False, False)
Email.inbox.append(email1)
email2 = ("jacques@cssr.co.za", "Hi Thabo send me the project list for Gauteng, Thanks", True, False)
Email.inbox.append(email2)


def get_count(self):
    """Here user get count of how many emails are in the inbox"""
    email_count = len(self.inbox)
    return 'The number of emails in your inbox is:', email_count


# Menu with menu options for user to choose what he would like to do
menu = input('What would you like to do,\n'
             ' - Read email ENTER: r\n'
             ' - Mark spam ENTER: s\n'
             '- Send email ENTER: n\n'
             '- Quit program ENTER: q\n')

while menu:
    if menu.lower( ) == 'r':
        print(Email.inbox)
    elif menu.lower( ) == 's':
        print()
    elif menu.lower( ) == 'n':
        address = input("Add email address\n")
        contents = input("Enter email message\n")
        print(add_mail())
    elif menu.lower( ) == 'q':
        print("Goodbye, Thank you for using Email Server")
        print("Have a nice day")
    break
else:
    print("Incorrect input")



print("Objects for Instance variables......")
# Objects of constructor method
email3 = Email("joe@hotmail.com", "Hi how are you,", True, False)
email4 = Email("Sale@sales.com", "Enter now and win!", False, False)

# Print instance variables
print("Instance variables for Class Email examples.........")
print(email3.from_address)
print(email3.email_contents)
print(email3.has_been_read)
print(email4.from_address)
print(email4.email_contents)
print(email4.is_spam)

# Use add_mail method to add to inbox
print("Adding Email4 to inbox[].......")
Email.inbox.append(email4)
print(Email.inbox)


#######################################################################################################################

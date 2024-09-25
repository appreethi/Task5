''' write a python function to validate the regular expression for the following:
a) email address
b) mobile numbers of bangladesh
c)telephone numbers of USA
d) 16 character alpha numeric password composed of alphabets of upper case,lower case,special characters , Numbers'''

import re

class Myregex:
    
    def __init__(self, email_address,mobile_number,telephone_number,password):
        self.email_address = email_address
        self.mobile_number = mobile_number
        self.telephone_number = telephone_number
        self.password = password
    
    def validate_email(self): #appreethi123@gmail.com
        #defining regular expression to validate the email_address
        pattern = r"^[a-z0-9._]+@[a-z]+\.[a-z]{3}$"

        if re.match(pattern,self.email_address):
            print("Pattern Matched")
        else:
            print("Pattern Mismatched")
    
    def validate_mobilenumber_bangladesh(self):
        #defining regular expresiion to validate the mobile number of bangladesh
        pattern = r"^01[0-9]{9}$" #01567932427

        if re.match(pattern,self.mobile_number):
            print("Pattern matched")
        else:
            print("Pattern mismatched")

    def validate_telephone_number_usa(self):
        #defining the regular expresiion to validate the telephone number of USA
        pattern= r"^[2-9]{1}+[0-9]{2}+[2-9]{1}+[0-9]{2}+[0-9]{4}$"  #(the standard US telephone number is an 10 digit number - ex: 555 555 1234)

        if re.match(pattern,self.telephone_number):
            print("Pattern matched")
        else:
            print("pattern mismatched")
    
    def validate_password(self):
        pattern = r"^[A-Za-z0-9!@#$%^&*()]{16}$"

        if re.match(pattern,self.password):
            print("pattern matched")
        else:
            print("pattern mismatched")

    
reobject = Myregex("appreethi123@gmail.com","01567932427","5555551234","AqsA128J@#iu&#HD")
# reobject.validate_email() 
'''call when required'''
# reobject.validate_mobilenumber_bangladesh() 
'''call when required''' 
# reobject.validate_telephone_number_usa()
reobject.validate_password()  


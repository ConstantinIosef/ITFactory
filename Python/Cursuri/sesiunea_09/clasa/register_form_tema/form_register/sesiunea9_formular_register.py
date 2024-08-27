"""
fa un formular de register dupa https://budgetandstuff.com/register/
"""

class RegisterForm:
    def __init__(self, username, first_name, last_name, email, password, confirm_password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validation(self):

        if not all([self.username, self.first_name, self.last_name, self.email, self.password, self.confirm_password]):
            return False, "All fields must be filled!"
        else:
            return True, "You successfully registered!"
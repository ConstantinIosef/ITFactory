from sesiunea9_formular_register import RegisterForm

def register():
    username = input("Type your username: \n")
    first_name = input("Type your first name: \n")
    last_name = input("Type your last name: \n")
    email = input("Type your email: \n")
    password = input("Type your password: \n")
    confirm_password = input("Type your password so we can confirm it: \n")
    formRegister = RegisterForm(username, first_name, last_name, email, password, confirm_password)


    register_form_valid = formRegister.validation()
    if register_form_valid:
        print("Your account has been registered.")
    else:
        print("Error: ", )


register()
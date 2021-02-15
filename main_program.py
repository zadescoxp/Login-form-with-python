# first sign up your account and then use all these
with open('email_and_password.txt') as f:
    contents = f.read()

def login(e_mail,password):
    if e_mail in contents and password in contents:
        print("You are logged in...")
    elif e_mail in contents and password not in contents:
        print("You put the E-mial / Password wrong")
    else:
        print("You are not logged in !")


def signUp(e_mail,password,name):
    if e_mail in contents:
        print("This is e-mai already exist")
    else:
       with open('email_and_password.txt','a') as f:
           f.write(f"Name: {name} Email: {e_mail} PassWord: {password}\n\n") 

ask_for_login_or_signup = input("(a) Login\n(b) Sign Up\n: ")
if ask_for_login_or_signup == 'a':
    e_mail = input("Enter your e-mail : ")
    password = input("Enter your password : ")
    login(e_mail,password)

elif ask_for_login_or_signup == 'b':
    name = input("Enter your username: ")
    e_mail = input("Enter your e-mail : ")
    password = input("Enter your password : ")

    signUp(e_mail,password,name)
else:
    print("You entered something wrong")


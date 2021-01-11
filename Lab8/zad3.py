import webbrowser
users = {
    'admin':'admin',
    'bbb':'bbb',
    'ccc':'ccc',
    'ddd':'ddd',
    'eee':'eee',
    'fff':'fff',
}
login = input('podaj login: ')
passw = input('podaj password: ')
if login in users.keys() and passw == users[login]:
    if login == "admin" and passw == "admin":
        print("Witaj adminie")
    else:
        print("Witaj userze")
else:
    print("Niepoprawne dane logowania")
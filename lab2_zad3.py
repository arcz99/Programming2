class UserNotFoundError(Exception):
    pass
class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users
    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(f"Uzytkownik '{username}' nie istnieje.")
        if self.users[username] != password:
            raise WrongPasswordError(f"Złe hasło")

        print(f"Zalogowano pomyślnie jako: {username}")



auth = UserAuth({"admin":"1234", "user": "abcd"})

for username, password in [("admin", "1234"), ("user", "wrongpass"), ("Unknown", "pass")]:
    try:
        auth.login(username, password)
    except (UserNotFoundError, WrongPasswordError) as e:
        print(f"Błąd: {e}")

#try:
#    auth.login("admin", "1234")
#    auth.login("unknown", "pass")
#    auth.login("user", "wrongpass")
#except UserNotFoundError as e:
#    print(f"Błąd: {e}")

#except (UserNotFoundError, WrongPasswordError)  as e:
#    print(f"Błąd: {e}")


#try:
#    auth.login("user", "wrongpass")
##except UserNotFoundError as e:
#    print(f"Błąd: {e}")
#except WrongPasswordError as e:
#    print(f"Błąd: {e}")

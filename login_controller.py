from db import User

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class LoginController(metaclass=Singleton):

    def __init__(self, on_login, on_logout):
        self.logged_in_user = None
        self.on_login = on_login
        self.on_logout = on_logout

    def do_login(self, username, password):
        # if username == 'Stratos' and password == '1234':
        user = User.query.eq_username(username).one()
        if user is None:
            return False
        
        if username == user.username and password == user.password:
            # print('Succesfull', username)
            self.logged_in_user = username
            self.on_login()
            return True
        else:
            return False
        
    def do_logout(self):
        self.logged_in_user = None
        self.on_logout()

    def get_logged_in_user(self):
        return self.logged_in_user



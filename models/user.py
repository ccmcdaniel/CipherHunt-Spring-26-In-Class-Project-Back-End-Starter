
class UserModel:
    def __init__(self):
        self.__id = 1
        self.__username = "johndoe1111"
        self.__email = "johndoe1111@gmail.com"
        self.__rank = None

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
    
    def set(self, username = None, email = None):
        if(username != None):
            self.__username = username
        if(email != None):
            self.__email = email

        return True
    

if __name__ == "__main__":
    test_user = UserModel()

    print(test_user.username, ", ", test_user.email)

    test_user.set(username="janedoe11")
    test_user.set(email="janedoe11@gmail.com")
    
    print(test_user.username, ", ", test_user.email)
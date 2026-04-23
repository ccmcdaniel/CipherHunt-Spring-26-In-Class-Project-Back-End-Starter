
class RankModel:
    def __init__(self, current_points):
        self.__current_points = current_points
        self.__ranks = {
            'Bystander': 0,
            'Inqusitor': 100,
            'Cryptic': 300,
            'Cipher-Smith': 500,
            'Oracle': 700
        }

    @property
    def current_points(self):
        return self.__current_points

    @property
    def current_rank(self):
        rank = list(self.__ranks.keys())[0]

        for next_rank, points_needed in self.__ranks.items():
            if self.__current_points < points_needed:
                return rank
            else:
                rank = next_rank

        return rank
    
    @property
    def next_rank_points(self):
        for next_rank, points_needed in self.__ranks.items():
            if self.__current_points < points_needed:
                return points_needed

        return points_needed



class UserModel:
    def __init__(self):
        self.__id = 1
        self.__username = "johndoe1111"
        self.__email = "johndoe1111@gmail.com"
        self.__rank = RankModel(654)

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
    
    @property
    def rank(self):
        return self.__rank
    
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
    print(test_user.username, 
          ": Rank - ", 
          test_user.rank.current_rank,
        "(", 
        test_user.rank.current_points, 
        "/", 
        test_user.rank.next_rank_points,
        ")")

# class Profile:
#     pass

# user1 = Profile()
# user1.first_name = "Davit"
# user1.last_name = "Torgomyan"
# user1.profile_picture = "Davit.jpeg"
# user1.cover_picture = "Davit_cover.jpeg"

# user2 = Profile()
# user2.first_name = "Arman"
# user2.last_name = "Avetisyan"
# user2.profile_picture = "Arman.jpeg"
# user2.cover_picture = "Arman_cover.jpeg"



class Profile:
    def __init__(self,first_name,last_name,profile_picture,cover_picture):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture
    
    def getFullName(self) :
        return f"{self.first_name} {self.last_name}"


class Page(Profile):
    @staticmethod
    def getUSer(name):
        return name

    def __init__(self,name,profile_picture,cover_picture):
        self.name = name
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture
    
    def getFullName(self) :
        return f"{self.first_name} {self.last_name}"
    
    @property
    def getFullNameProperty(self) :
        return f"{self.name} {self.profile_picture}"

user1 = Profile("Davit","Torgomyan","Davit.jpeg","Davit_cover.jpeg")
flowersPage = Page("DALI-FLOWER","DALI.jpeg","FLOWER.jpeg")
fullNaem = user1.getFullName()
# print(fullNaem)

# userName = Page.getUSer("Davo")
# print(userName)

userName = flowersPage.getFullNameProperty
print(userName)


# print("{} {}".format(user2.first_name,user2.last_name))
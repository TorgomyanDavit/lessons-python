class Registration:
    @staticmethod
    def register_user(email,password,firstName,lastName):
        if ("@" in email) and (len(password) > 6):
            return Profile(firstName,lastName)

class FBModel:
    def __init__(self, profilePicture, coverPicture):
        self.profilePicture = profilePicture
        self.coverPicture = coverPicture

class Profile(FBModel):
    def __init__(self, firstName, lastName, coverPicture=None, profilePicture=None):
        super().__init__(profilePicture, coverPicture)
        self.firstName = firstName
        self.lastName = lastName
    
    @property
    def getFullName(self):
        return self.firstName + " " + self.lastName
    
    def __str__(self):
        return self.firstName + " " + self.firstName
    
    def __add__(self,other):
        return self.firstName + "-" + other.firstName

class Page(FBModel):
    def __init__(self, name, profilePicture, coverPicture, followers=0):
        super().__init__(profilePicture, coverPicture)
        self.name = name
        self.followers = followers
        
    def getPage(self):
        return {
            "name": self.name,
            "followers" : str(self.followers)
        } 

    def __str__(self):
        return self.name + " " + self.followers



DaylyFlow = Page("DayLy", "dayly.jpeg", "cover.jpeg", 8)
user1 = Profile("Davit", "Torgomyan", "Davit.jpeg", "cover.jpeg")
user2 = Profile("Gevor", "VardaNYAN", "GEVOR.jpeg", "cover.jpeg")

# print(user1.profilePicture)
# print(user2 + user1)

myProfile = Registration.register_user("arman@mail.ru", "Password123!", "Arman", "Avetisyan")

print(myProfile.getFullName)
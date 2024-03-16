class FBModel:
    def __init__(self, profilePicture, coverPicture):
        self.profilePicture = profilePicture
        self.coverPicture = coverPicture
        
    def getProfilePictureAndCoverPicture(self):
        return self.profilePicture + " " + self.coverPicture
        

class Profile(FBModel):
    def __init__(self, firstName, lastName, coverPicture, profilePicture):
        super().__init__(profilePicture, coverPicture)
        self.firstName = firstName
        self.lastName = lastName
    
    def getFullName(self):
        return self.firstName + " " + self.lastName
    
def __str__(self):
    return {
        "firstName": self.firstName,
        "lastName": self.lastName
    }


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
    



# DaylyFlow = Page("DayLy", "dayly.jpeg", "cover.jpeg", 8)
# print(DaylyFlow.getPage())

user1Profile = Profile("Davit", "Torgomyan", "Davit.jpeg", "cover.jpeg")
print(user1Profile)

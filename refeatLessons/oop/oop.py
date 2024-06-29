
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

class FbModel:
    def __init__(self,profile_picture,cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture

    def getProfilePictures(self):
        return {
            "cover_pictures":self.cover_picture,
            "profile_pictures":self.profile_picture
        }



class Profile(FbModel):
    def __init__(self,first_name,last_name,profile_picture,cover_picture):
        super().__init__(profile_picture,cover_picture)
        self.first_name = first_name
        self.last_name = last_name

    def getFullName(self):
        return f"{self.first_name} {self.last_name}"
        
    


class Page(FbModel):
    def __init__(self,name,profile_picture,cover_picture,followers=0):
        super().__init__(profile_picture,cover_picture)
        self.name = name
        self.followers = followers

    def getInfo(self):
        return {
            "name":self.name,
            "followers":self.followers
        }
    



user = Profile("Davit","Torgomyan","Davit.jpeg","Davit_cover.jpeg")
page = Page("D&L FLower","Arman.jpeg","Arman_cover.jpeg")



print(user.getFullName())
print(user.getProfilePictures())
print(page.getProfilePictures())

# print(user.profile_picture)
# print(page.profile_picture)
# infoPage = page.getInfo()
# print(list(infoPage.keys())[0])
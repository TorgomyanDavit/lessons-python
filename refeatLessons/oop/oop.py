
# # class Profile:
# #     pass

# # user1 = Profile()
# # user1.first_name = "Davit"
# # user1.last_name = "Torgomyan"
# # user1.profile_picture = "Davit.jpeg"
# # user1.cover_picture = "Davit_cover.jpeg"

# # user2 = Profile()
# # user2.first_name = "Arman"
# # user2.last_name = "Avetisyan"
# # user2.profile_picture = "Arman.jpeg"
# # user2.cover_picture = "Arman_cover.jpeg"




# class Registration:
#     def register_user(self,email,password,first_name,last_name,):
#         if("@" in email and len(password) > 6) :
#             return Profile(first_name,last_name)
 
# class FbModel:
#     def __init__(self,profile_picture,cover_picture):
#         self.profile_picture = profile_picture
#         self.cover_picture = cover_picture
    
#     def getFullName(self) :
#         return f"{self.first_name} {self.last_name}"

#     def getProfilePictures(self):
#         return {
#             "cover_pictures":self.cover_picture,
#             "profile_pictures":self.profile_picture
#         }

# class Page(Profile):
#     @staticmethod
#     def getUSer(name):
#         return name

#     def __init__(self,name,profile_picture,cover_picture):
#         self.name = name
#         self.profile_picture = profile_picture
#         self.cover_picture = cover_picture
    
#     def getFullName(self) :
#         return f"{self.first_name} {self.last_name}"
    
#     @property
#     def getFullNameProperty(self) :
#         return f"{self.name} {self.profile_picture}"

# user1 = Profile("Davit","Torgomyan","Davit.jpeg","Davit_cover.jpeg")
# flowersPage = Page("DALI-FLOWER","DALI.jpeg","FLOWER.jpeg")
# fullNaem = user1.getFullName()
# # print(fullNaem)

# # userName = Page.getUSer("Davo")
# # print(userName)

# userName = flowersPage.getFullNameProperty
# print(userName)


# # print("{} {}".format(user2.first_name,user2.last_name))


# class Profile(FbModel):
#     def __init__(self,first_name,last_name,profile_picture=None,cover_picture=None):
#         super().__init__(profile_picture,cover_picture)
#         self.first_name = first_name
#         self.last_name = last_name

#     def getFullName(self):
#         return f"{self.first_name} {self.last_name}"
    

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
        
    


# class Page(FbModel):
#     def __init__(self,name,profile_picture,cover_picture,followers=0):
#         super().__init__(profile_picture,cover_picture)
#         self.name = name
#         self.followers = followers

#     def getInfo(self):
#         return {
#             "name" : self.name,
#             "followers" : self.followers
#         }
    
#     def __add__(self,other):
#         return f"{self.name} {other.name} total Folowers {self.followers + other.followers}"
    
        
#     def __sub__(self,other):
#         return f"{self.name} {other.name} total Folowers {self.followers - other.followers}"
    


# regUser = Registration()
# myProfile = regUser.register_user("Davit@gmail.com","password111","DavitProfile","Torgomyan")

# print(myProfile.getFullName())

# user = Profile("Davit","Torgomyan","Davit.jpeg","Davit_cover.jpeg")
# user2 = Profile("Arman","gabrielyan","Arman.jpeg","Arman_cover.jpeg")

# page = Page("D&LL FLower","Arman.jpeg","Arman_cover.jpeg",10)
# page2 = Page("ERO FLower","ERO.jpeg","ERO_cover.jpeg",50)

# # Method Overloading
# # print(page2  -  page) # __add__ 
# # print(page2  -  page) # __sub__

# # print(user.getFullName())
# # print(user.getProfilePictures())
# # print(page.getProfilePictures())
# # print(user)


# # print(user.profile_picture)
# # print(page.profile_picture)
# # infoPage = page.getInfo()
# # print(list(infoPage.keys())[0])

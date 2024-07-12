
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




class Registration:
    def register_user(self,email,password,first_name,last_name,):
        if("@" in email and len(password) > 6) :
            return Profile(first_name,last_name)
 
class FbModel:
    def __init__(self,profile_picture,cover_picture):
        self.profile_picture = profile_picture
        self.cover_picture = cover_picture


user1 = Profile("Davit","Torgomyan","Davit.jpeg","Davit_cover.jpeg")
user2 = Profile("Arman","Avetisyan","Arman.jpeg","Arman_cover.jpeg")

print(f"{user1.first_name} {user1.last_name}")
print("{} {}".format(user2.first_name,user2.last_name))
import instaloader

ig = instaloader.Instaloader()
user_name = input("Enter Insta username : ")

dp = ig.download_profile(user_name, profile_pic_only=True)

print("downloaded")

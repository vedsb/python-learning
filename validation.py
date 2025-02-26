username = input("enter the username")

if len(username) > 12:
    print("shall nort contain more than 12 char")
elif username.find(" ") == 1:
    print ("shall not contain  ")
elif username.isdigit():
    print("sall not contain dights")
else:
    print(f"welcome {username}")
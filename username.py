username = input("Enter username: ")

if  len(username) >= 5 and " " not in username:
    print("Valid username")
else:
    print("Invalid username")

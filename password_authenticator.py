# create a dictionary to store usernames and passwords
users = {"user1": "gaurav", "user2": "gaurav", "user3": "password3"}

# prompt user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# check if the username exists in the dictionary and if the password matches
if username in users and users[username] == password:
    print("Authentication successful!")
    print("Authentication failed.")
else:
# append a user to the end of the file, creates file if it does not exist
def add_user(user):
    f = open('users.txt', 'a')
    f.write(f"{user}\n")
    f.close()

# places all names into a list, changes the list to update users, overwrites file with new set of names
def update_user(old, new):
    with open('users.txt', 'r') as f:
        users = f.readlines()
        for i in range(len(users)):
            if users[i] == f"{old}\n":
                users[i] = f"{new}\n"
                
    with open('users.txt', 'w') as f:
        f.writelines(users)
    
# places all names into a list, removes specified name from list, overwrites file with new set of names
def remove_user(user):
    with open('users.txt', 'r') as f:
        users = f.readlines()
        for i in range(len(users)):
            if users[i] == f"{user}\n":
                users[i] = ''
                
    with open('users.txt', 'w') as f:
        f.writelines(users)

# testing
add_user("bob")
add_user("joe")
add_user("ann")
add_user("mike")
update_user("joe", "jo")
remove_user("ann")
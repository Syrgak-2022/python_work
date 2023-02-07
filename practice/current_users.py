current_users = ['syrgak', 'eldo', 'tima', 'jiku', 'asel']
new_users = ['sancho', 'sezima', 'botya', 'arushka', 'abdy', 'gulmira', 'syrgak']
for new_users in new_users:
    if new_users in current_users:
        print(f"Sorry, {new_users.title()}, choice another name")
    else:
        print(f"{new_users.title()}, you can use this name")

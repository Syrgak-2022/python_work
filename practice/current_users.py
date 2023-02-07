current_users = ['syrgak', 'eldo', 'tima', 'jiku', 'asel']
new_users = ['sancho', 'sezima', 'botya', 'arushka', 'abdy', 'gulmira', 'syrgak']
for new_users in new_users:
    if new_users in current_users:
        print(f"Sorry, {new_users.title()}, choice another name")
    else:
        print(f"{new_users.title()}, you can use this name")


old_cars = ['bmw_x1', 'bmw_x2', 'bmw_x3', 'bmw_x4', 'bmw_x5']
new_cars = ['bmw_x6', 'bmw_x7', 'bmw_x8', 'bmw_x9', 'bmw_x5']
for new_cars in new_cars:
    if new_cars in old_cars:
        print(f"Sorry, this car, {new_cars}, already has in store!")
    else:
        print(f"This car, {new_cars}, available for order!")
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for user_name, user_info in users.items():
#     print(f"\nUsername: {user_name}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")



# brothers = {
#     'isancho': {
#         'first': 'sancho',
#         'last': 'imankulov',
#         'location': 'bishkek',
#     },
#     'botyaim': {
#         'first': 'botya',
#         'last': 'imankulov',
#         'location': 'bishkek',
#     },
# }
# for user_name, user_info in brothers.items():
#     print(f"Username: {user_name}")
#     fullname = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {fullname.title()}")
#     print(f"\tLocation: {location.title()}")





cars = {
    'domestic': {
        'name': 'lada',
        'model': 'granta',
        'location': 'russia',
    },
    'foreign': {
        'name': 'dodge',
        'model': 'caliber',
        'location': 'usa',
    },
}
for manufacture, cars_info in cars.items():
    print(f"Manufacture: {manufacture.title()}")
    carsinformation = f"{cars_info['name']} {cars_info['model']}"
    carslocation = cars_info['location']
    print(f"\tFull name: {carsinformation.title()}")
    print(f"\tLocation: {carslocation.upper()}")




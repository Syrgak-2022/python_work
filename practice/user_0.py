# метод .items()

# user_0 = {
#     'username': 'simankulov',
#     'first_name': 'syrgak',
#     'lastname': 'imankulov',
#     }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")



# car = {
#     'model': 'bmw',
#     'year': 2022,
#     'paint': 'black',
#     'all_weels': 'full'
#     }
# for key, value in car.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")



# console = {
#     'name': 'xbox',
#     'year': 2023,
#     'paint': 'black',
#     'gamepass': '12 months',
#     'guarantee': 'full',
#     }
# for key, value in console.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")



# console = {
#     'name': 'xbox',
#     'year': 2023,
#     'paint': 'black',
#     'gamepass': '12 months',
#     'guarantee': 'full',
#     }
# for key in console.keys():
#     print(key)
#
# car = {
#     'model': 'bmw',
#     'year': 2022,
#     'paint': 'black',
#     'all_weels': 'full'
#     }
# for key in car.keys():
#     print(key)


# favourite_languages = {
#     'syrgak': 'python',
#     'botya': 'c++',
#     'sancho': 'java',
#     'eldo': 'c#',
#     'tima': 'dolphin'
#     }
# friends = ['syrgak', 'botya']
# for name in favourite_languages.keys():
#     print(name.title())
#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}")




# favourite_cars = {
#     'syrgak': 'dodge',
#     'botya': 'bmw',
#     'sancho': 'audi',
#     'eldo': 'kia',
#     'tima': 'haval',
#     }
# names = ['eldo', 'tima']
# for name in favourite_cars.keys():
#     print(name.title())
#     if name in names:
#         car = favourite_cars[name]
#         print(f"\t{name.title()}, I see you love {car}")



# favourite_paints = {
#     'syrgak': 'red',
#     'botya': 'blue',
#     'sancho': 'white',
#     'eldo': 'green',
#     'tima': 'black'
#     }
# names = ['sancho', 'tima']
# for name in favourite_paints.keys():
#     print(name.title())
#     if name in names:
#         paint = favourite_paints[name]
#         print(f"\t{name.title()} {paint}")


# favourite_paints = {
#     'syrgak': 'red',
#     'botya': 'blue',
#     'sancho': 'white',
#     'eldo': 'green',
#     'tima': 'black'
#     }
# for paint in favourite_paints.values():
#     print(paint)




# favourite_numbers = {
#     'syrgak': 8,
#     'botya': 6,
#     'sancho': 4,
#     'eldo': 2,
#     'sezima': 9,
#     'arushka': 7,
#     'aselya': 5,
#     'anara': 3,
#     'rysya': 1,
#     }
# # numbers = favourite_numbers['syrgak']
# # print(f"Syrgak's favourite number is: {numbers}")
# #
# # numbers = favourite_numbers['botya']
# # print(f"\nBotya's favourite number is: {numbers}")
# #
# # numbers = favourite_numbers['sancho']
# # print(f"\nSancho's favourite number is: {numbers}")
# #
# # numbers = favourite_numbers['eldo']
# # print(f"\nEldo's favourite number is: {numbers}")
#
# for name, numbers in favourite_numbers.items():
#     print(f"{name} {numbers}")


rivers = {
    'amazonka': 'south america',
    'nile': 'egypt',
    'yanzy': 'china',
    }
river = ['amazonka', 'nile', 'yanzy']
for name in rivers.keys():
    print(name.title())
    if name in river:
        country = rivers[name]
        print(f"\tThe {name.title()} through {country.title()}")
for river, country in rivers.items():
    print(river)
    print(country)
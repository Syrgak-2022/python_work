# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
#
# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")


# alien_0 = {'color': 'blue', 'points': '5', 'shape': 'circle', 'size': 'small'}
# alien_1 = {'color': 'green', 'points': '10', 'shape': 'oval', 'size': 'average'}
# alien_2 = {'color': 'red', 'point': '15', 'shape': 'square', 'size': 'big'}
#
# new_alien_0 = alien_0['color']
# new_alien_1 = alien_1['points']
# new_alien_2 = alien_2['shape']
#
# print(alien_0['color'])
# print(alien_1['shape'])
# print(alien_2['size'])
#
# print(f"You shoot down the {new_alien_0} alien!")
# print(f"Yoy've earned {new_alien_1} points!")
# print(f"You shoot down a {new_alien_2} spaceship!")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['shape'] = 'oval'
# alien_0['size'] = 'small'
# alien_0['body'] = 'thin'
# alien_0['mind'] = 'smart'
# alien_0['weapon'] = 'laser'
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# alien_0['size'] = 'small'
# alien_0['shape'] = 'oval'
# alien_0['body'] = 'thin'
# alien_0['color'] = 'red'
# alien_0['points'] = '10'
# alien_0['size'] = 'big'
# print(alien_0)


# Удаление пар "ключ-значение"
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# alien_0['size'] = 'small'
# alien_0['shape'] = 'oval'
# alien_0['body'] = 'thin'
# alien_0['color'] = 'red'
# alien_0['points'] = '10'
# alien_0['size'] = 'big'
# print(alien_0)
# del alien_0['body']
# print(alien_0)
# del alien_0['color']
# print(alien_0)
# body_value = alien_0.get('body', 'No body value assigned')
# print(body_value)




# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print(f"Original position {alien_0['x_position']}")
#
# # Пришелец перемещается вправо
# # Вычисляем величину смещения на основании текущей скорости
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3   # прищелец двигается быстро
#
# #Новая позиция равна сумме старой позиции и приращения
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")



# car = {'x_position': 0, 'y_position': 30, 'speed': 'fast'}
# print(f"Original position: {car['x_position']}.")
# if car['speed'] == 'slow':
#     x_increment = 1
# elif car['speed'] == 'fast':
#     x_increment = 3
# elif car['speed'] == 'very fast':
#     x_increment = 4
# else:
#     x_increment = 2
# car['x_position'] = car['x_position'] + x_increment
# print(f"New car's position: {car['x_position']}")



# plane = {'x_position': 0, 'y_position': 40, 'speed': 'very fast'}
# print(f"Original position: {plane['x_position']}")
#
# if plane['speed'] == 'slow':
#     x_increment = 10
# elif plane['speed'] == 'medium':
#     x_increment = 30
# elif plane['speed'] == 'very fast':
#     x_increment = 60
# else:
#     x_increment = 40
# plane['x_position'] = plane['x_position'] + x_increment
# print(f"New position: {plane['x_position']}")


# alien_0 = {'color': 'red', 'points': 5}
# alien_1 = {'color': 'blue', 'points': 10}
# alien_2 = {'color': 'green', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)


# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of aliens: {len(aliens)}")

#
# robots = []
# for robot_number in range(50):
#     new_robot = {'color': 'metallic', 'points': 10, 'speed': 'slow'}
#     robots.append(new_robot)
# for robot in robots[:10]:
#     print(robot)
# print("...")
# print(f"Total number of robots: {len(robots)}")


# zombies = []
# for zombie_number in range(100):
#     new_zombie = {'color': 'green', 'points': 10}
#     zombies.append(new_zombie)
# for zombie in zombies[:10]:
#     print(zombie)
# print("...")
# print(f"Total number of zombie: {len(zombies)}")


zombies = []
for zombie_number in range(0, 30):
    new_zombie = {'color': 'green', 'points': 5, 'speed': 'slow'}
    zombies.append(new_zombie)

for zombie in zombies[0:5]:
    if zombie['color'] == 'green':
        zombie['color'] = 'yellow'
        zombie['points'] = 10
        zombie['speed'] = 'medium'
    if zombie['color'] == 'yellow':
        zombie['color'] = 'red'
        zombie['points'] = 15
        zombie['speed'] = 'fast'
for zombie in zombies[0:10]:
    print(zombie)
print(f"Total number of zombies: {len(zombies)}")
bike = ['honda', 'java', 'bmw']
print(bike)
bike[0] = 'ducati'
print(bike)
bike.append('honda')
print(bike)
bike.insert(4, 'suzuki')
print(bike)
bike.insert(5, 'ural')
print(bike)
del bike[5]
print(bike)
bike.append('ural')
print(bike)
popped_bikes = bike.pop()
print(bike)
print(popped_bikes)
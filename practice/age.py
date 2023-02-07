age = 35
if age < 2:
    status = 'baby'
elif age >= 2 and age < 4:
    status = 'kid'
elif age >= 13 and age < 13:
    status = 'child'
elif age >= 13 and age < 20:
    status = 'tennager'
elif age >= 20 and age < 65:
    status = 'adult'
else:
    staus = 'old'
print(f"You are {status}")

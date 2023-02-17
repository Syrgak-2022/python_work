sandwich_orders = ['pastrami', 'fried', 'pastrami', 'cheese', 'chicken', 'pastrami', 'potato']
print("Pastrami absent today")
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Ordered sandwiches: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches: ")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches)
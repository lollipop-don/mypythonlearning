sandwitch_orders = ['tuna','meat','ham','cheese']
finished_sandwitches = []
while sandwitch_orders:
    sandwich = sandwitch_orders.pop()
    print(f'your {sandwich} sandwich is ready')
    finished_sandwitches.append(sandwich)
for value in finished_sandwitches:
    print(f'{value} sandwich was made')
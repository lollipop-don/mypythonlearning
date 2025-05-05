sandwitch_orders = ['tuna','pastrami','meat','pastrami','ham','pastrami','cheese']
print('the deli has run out of pastrami')
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')
finished_sandwitches = []
while sandwitch_orders:
    sandwich = sandwitch_orders.pop()
    print(f'your {sandwich} sandwich is ready')
    finished_sandwitches.append(sandwich)
for value in finished_sandwitches:
    print(f'{value} sandwich was made')
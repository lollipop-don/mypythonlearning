unconfirmed_users = ['alica','bob','candace']
confirmed_users = []


while unconfirmed_users:
    pop = unconfirmed_users.pop()
    print(f'processed element {pop.title()}')
    confirmed_users.append(pop)
print('now confirmed users are : ')
for value in confirmed_users:
    print(value.title())




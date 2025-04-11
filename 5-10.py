current_usernames = ['tiko','gigi','qEti','aleko','Natela','ketevani']

copy_of_current_usernames =[]
for value in current_usernames:
    copy_of_current_usernames.append(value.upper())

new_users = ['mariana','aleqsandra','TiKO','sofia','GigI']
for value in new_users:
    if value.upper() in copy_of_current_usernames:
        print(f'{value} you need to enter a new username')                      
    else:
        print(f'the username {value} is available')    


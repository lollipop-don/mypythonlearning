current_users = ['oNe', 'twO','three','FouR','fIve']
new_users = ['tets','two','fOUr','tiko','gigi']
copy_of_current_users = []
for value in current_users:
    copy_of_current_users.append(value.upper())
   
for value in new_users:
    if value.upper() in copy_of_current_users:
        print(f'{value}: this username is taken')
    else:
        print(f'{value} welcome to the website,you are a new user')
















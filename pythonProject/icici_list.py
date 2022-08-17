user_id = input('User Id- ')
pwd = input('Password- ')

ex_user_ids = ['jaya', 'jana', 'imai', 'yugi']
ex_pwds = ['jaya', 'jana', 'imai', 'yugi']

index_of_user_id = None

for i in range(len(ex_user_ids)):
    if ex_user_ids[i] == user_id:
        index_of_user_id = i

if index_of_user_id is None:
    print('invalid login, userid')

if ex_pwds[index_of_user_id] == pwd:
    print('login successful')
else:
    print('invalid login, password')

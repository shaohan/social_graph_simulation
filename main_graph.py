import final_project_as_1125

graph0 = final_project_as_1125.Graph(4)

for user in graph0.get_users():
    print('user ID: ', user.id)
    for friend in user.get_friends():
        print('-- ', friend.id)

print('=== circle_connect() ===')
graph0.circle_connect()

for user in graph0.get_users():
    print('user ID: ', user.id)
    for friend in user.get_friends():
        print('-- ', friend.id)


print('=== random_connections() ===')
graph0.random_connections(2)

for user in graph0.get_users():
    print('user ID: ', user.id)
    for friend in user.get_friends():
        print('-- ', friend.id)

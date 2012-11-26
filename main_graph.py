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

print('=== Create new Graph instance  ===')

graph1 = final_project_as_1125.Graph(4)
graph1.circle_connect()

for user in graph1.get_users():
    print('user ID: ', user.id)
    print('has_adopted: ', user.has_adopted())
    for friend in user.get_friends():
        print('-- ', friend.id)


print('=== has_adopted() ===')
for user in graph1.get_users():
    print('user ID: ', user.id)
    print('is_adopted:', user.has_adopted())

print('=== time_step() ===')
graph1.get_users()[0].set_adopted(True)
graph1.time_step(0.25)

for user in graph1.get_users():
    print('user ID: ', user.id)
    print('is_adopted:', user.has_adopted())

graph1.time_step(0.25)

for user in graph1.get_users():
    print('user ID: ', user.id)
    print('is_adopted:', user.has_adopted())

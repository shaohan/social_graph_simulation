import final_project_as_1125

user0 = final_project_as_1125.User()
user1 = final_project_as_1125.User()
user2 = final_project_as_1125.User()

print(user0)
print(user0.get_id())
print('user0: ', user0.has_adopted())

user0.set_adopted(True)
print('user0: ', user0.has_adopted())
print('user1: ', user1.has_adopted())

user0.set_adopted(False)
print('user0: ', user0.has_adopted())

user1.set_adopted(True)
print('user1: ', user1.has_adopted())

print(' === friend test ===')
print('user0 friend')
for friend in user0.get_friends():
    print('-- ', friend.id)

user0.add_friend(user2)
print('user0 friend')
for friend in user0.get_friends():
    print('-- ', friend.id)

user0.add_friend(user1)
print('user0 friend')
for friend in user0.get_friends():
    print('-- ', friend.id)

user0.add_friend(user0)
print('user0 friend')
for friend in user0.get_friends():
    print('-- ', friend.id)

user0.add_friend(user1)
print('user0 friend')
for friend in user0.get_friends():
    print('-- ', friend.id)

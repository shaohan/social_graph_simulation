import final_project_as_1125

POPULATION = 4
NUM_CONNECTIONS = 1
NUM_FIRST_ADOPTERS = 1

graph = final_project_as_1125.Graph(POPULATION)
graph.circle_connect()
graph.random_connections(NUM_CONNECTIONS)

analyzer = final_project_as_1125.GraphAnalyzer(graph)

for user in graph.get_users():
    print('user ID: ', user.id)
    for friend in user.get_friends():
        print('-- ', friend.id)

print("Population:               ", POPULATION)
print("Num_Connections:          ", NUM_CONNECTIONS)
print("Number of first adopters: ", NUM_FIRST_ADOPTERS)
analyzer.choose_users(NUM_FIRST_ADOPTERS)

import final_project_as_1125

POPULATION = 4
NUM_RANDOM_CONNECTIONS = 1
NUM_FIRST_ADOPTERS = 2

def print_users(graph):
    for user in graph.get_users():
        print('user ID:', user.id)
        for friend in user.get_friends():
            print('-- ', friend.id)

print("Start testing")
my_graph = final_project_as_1125.Graph(POPULATION)
my_graph.circle_connect()
my_graph.random_connections(NUM_RANDOM_CONNECTIONS)
my_analyzer = final_project_as_1125.GraphAnalyzer(my_graph)

print("=== get_users() test ===")
print_users(my_graph)
print_users(my_graph)

print("Population:               ", POPULATION)
print("Num_Random_Connections:   ", NUM_RANDOM_CONNECTIONS)
print("Number of first adopters: ", NUM_FIRST_ADOPTERS)

my_analyzer.choose_users(NUM_FIRST_ADOPTERS)
#my_graph.print_users()

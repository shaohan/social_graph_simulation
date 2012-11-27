import final_project_as_1125

def print_users(graph):
    for user in graph.get_users():
        print('user ID:', user.id)
        for friend in user.get_friends():
            print('-- ', friend.id)

print("Start testing")
my_graph = final_project_as_1125.Graph(5)
my_graph.circle_connect()
my_graph.random_connections(1)
my_analyzer = final_project_as_1125.GraphAnalyzer(my_graph)

print("=== get_users() test ===")
print_users(my_graph)
print_users(my_graph)
#my_analyzer.choose_users(20)
#my_graph.print_users()

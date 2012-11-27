import final_project_as_1125

POPULATION = 500
NUM_RANDOM_CONNECTIONS = 1000
NUM_FIRST_ADOPTERS = 4

def print_users(graph):
    for user in graph.get_users():
        print('user ID:', user.id)
        for friend in user.get_friends():
            print('-- ', friend.id)

def run_simulation():

    print("Start testing")
    my_graph = final_project_as_1125.Graph(POPULATION)
    my_graph.circle_connect()
    my_graph.random_connections(NUM_RANDOM_CONNECTIONS)
    my_analyzer = final_project_as_1125.GraphAnalyzer(my_graph)

    print("Population:               ", POPULATION)
    print("Num_Random_Connections:   ", NUM_RANDOM_CONNECTIONS)
    print("Number of first adopters: ", NUM_FIRST_ADOPTERS)

    my_analyzer.choose_users(NUM_FIRST_ADOPTERS)
#my_graph.print_users()

    time_step_count = 1
    while True:
    #print("Running time_step: ", time_step_count)
        time_step_count = time_step_count + 1
        if my_graph.time_step(0.25):
            print ("The graph is saturated")
            break
    print("Total time step used: ", time_step_count)

    adopted_count = 0
    not_adopted_count = 0
    for i in my_graph.get_users():
        if i.has_adopted:
            adopted_count = adopted_count + 1
        else:
            not_adopted_count = not_adopted_count + 1
            print("Total adopted count: ", adopted_count)
            print("Total not adopted count: ", not_adopted_count)
    return time_step_count

time_step_counts = []
for i in range(0, 100):
    time_step_counts.append(run_simulation())
    print('====================')

total_time_step_count = 0
for time_step_count in time_step_counts:
    total_time_step_count += time_step_count

print("Average time step counts: ", total_time_step_count / 100.0)

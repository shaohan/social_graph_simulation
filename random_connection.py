import random
import copy

connection_list = [ [0, 1], [1, 2], [2, 3], [3, 4], [4, 5] ]
original_list = copy.deepcopy(connection_list)

def connection_list_reverse(connection_list):
    reversed_connection_list = []
    for i in connection_list:
        i.reverse()
        reversed_connection_list.append(i)
    return(reversed_connection_list)

#print("reversed_conneciton_list = ", connection_list_reverse(connection_list))
#print("original_list = ", original_list)        
#connection_list_reverse(connection_list)

def random_connections(num_connections, population):

    random_list = []
    for i in range(0, num_connections):
        i = [random.randint(0, population), random.randint(0, population)]
        if i in original_list:
            print(i, "=> it's duplicated!")
        elif i in connection_list_reverse(connection_list):
            print(i, "=> it's duplicated!")
        elif i[0] == i[1]:
            print(i, "=> is not a conneciton")
        else:
            print(i)
            random_list.append(i)
            random_connections(num_connections - 1, population)
    return(random_list)

print("ramdon_list =",  random_connections(5, 10))






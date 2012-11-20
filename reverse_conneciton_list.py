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

random_list = []
for i in range(1, 10):
    i = [random.randint (0, 10), random.randint(0, 10)]
    if i in original_list:
        print("it's duplicated!")
    elif i in connection_list_reverse(connection_list):
        print("it's duplicated!")
    else:
        print(i)
        random_list.append(i)
    
print("ramdon_list =",  random_list)




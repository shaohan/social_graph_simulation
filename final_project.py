import random

class Graph(object):

    def __init__(self, population):
        """create a new graph with population users and no connections.
        no users in the new graph should have the new technology"""

        self.population = population
        user_all = []
        for i in range(0, population):
            i = [i]
            user_all.append(i)
        print(user_all)

        # input: an integer = population
        # output: user_all = [ [0], [1], [2], [3], [4],... [population - 1] ]
        

    def circle_connect(self):
        """connect each user i to user i+1, and connect the last user
        to user 0"""
        
        connection_list = []
        for i in range(0, population - 1):
            connection = [i, i + 1]
            connection_list.append(connection)        
        connection_list.append([ population - 1, 0 ])

        # input: an integer = population
        # output: [ [0, 1], [1, 2], [2, 3], [3, 4],... [population - 1, 0] ]
        
            
    def random_connections(self, num_connections):
        """add num_connections new connections randomly to the graph"""
        
        random_list = []
        for i in range(0, num_connections):
            i = [random.randint(0, population), random.randint(0, population)]
            random_list.append(i)
            




        # input: an integer = num_connections
        # output: num_connections lines of random connections 



    # connection (num_connections) lines of random connections
    # if the random connection already exist in connection_list:
    #       create another random line, until we have (num_connections)  






    def time_step(self, prob):
        """move the simulation forward by one time period.  For
        every user that has the new technology, the probability of
        passing it on to each friend is prob"""


        
    def get_users(self):
        """returns a list containing the users in the graph, in
        order of their IDs"""
        pass





class User(object):

    def __lt__(self, other):
        """this is a built in comparison function, so that
        user1 < user2 always returns False.  This is handy
        for sorting lists that contain users without throwing
        errors"""
        return False
    
    def get_friends(self):
        """returns a list of the user's friends,
        which are also users"""
        pass

    def is_friend(self, other):
        """returns True if this User and other are friends.
            returns False otherwise"""
        pass

    def get_id(self):
        """Returns this user's id"""
        pass



    def has_adopted(self):
        """Returns True if the user has adopted the new technology.
        Returns False otherwise"""
        pass

    def set_adopted(self, new_status):
        """If new_status is True, this user adopts the new technology.
        If new_status is False, this user becomes a non-adopter."""
        pass


class GraphAnalyzer(object):
    def __init__(self, graph):
        pass

    def choose_users(n):
        """returns a list of n users to serve as first-adopters,
        chosen so that the technology saturates the graph as quickly
        as possible"""
        pass

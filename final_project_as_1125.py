import random

class Graph(object):

    def __init__(self, population):
        """create a new graph with population sers and no connections.
        no users in the new graph should have the new technology"""

        self.population = population
        self.user_all = []
        for i in range(0, population):
            new_user = "User" + str(i)
            #new_user = User(i)
            self.user_all.append(new_user)
        print(self.user_all)


    def circle_connect(self):
        """connect each user i to user i+1, and connect the last user to user 0"""
        pass


    def random_connections(self, num_connections):
        """add num_connections(an assigned integer) new connections randomly to the graph"""
        pass
    

    def time_step(self, prob):
        """move the simulation forward by one time period. For every user that has the new technology, the probability of passing it on to each friend is prob"""
        pass

    
    def get_users(self):
        """returns a list containing the users in the graph, in order of their IDs"""
        pass



class User(object):
    def __init__(self, ID):
        self.ID = ID
        self.friends = []
   
     
    def __It__(self, other):
        """this is a built in comparison function, so that User1 < User2 always return False. This is handy for sorting lists that contain users without throwing errors"""
        return False
    

    def get_friedns(self):
        """return a list of the user's friends, which are also users"""
        return self.friends


    def is_friend(self, other):
        """return True if this User and other are friends. return False otherwise"""
        if other in self.friends:
            return True
        else:
            return False


    def add_friend(self, other):
        if other not in self.friends:
            self.friends.append(other)

        
    def get_id(self):
        """return this user's id"""
        return self.ID


    def has_adopted(self):
        """Returns True if the user has adopted the new technology. Returns False otherwise"""
        pass

    
    def set_adopted(self, new_status):
        """If new_status is True, this user adopts the new technology. If new_status is False, this user becomes a non-adopter."""
        pass


class GraphAnalyzer(object):
    def __init__(self, graph):
        pass

    def choose_users(n):
        """returns a list of n users to serve as first-adopters, chosen so that the technology saturates the graph as quickly as possible"""
        pass





inst1 = Graph(10)
#output => ['User0', 'User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9']

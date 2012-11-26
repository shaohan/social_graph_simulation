import random

class Graph(object):

    def __init__(self, population):
        """create a new graph with population sers and no connections.
        no users in the new graph should have the new technology"""

        self.population = population
        self.users = []
        for i in range(0, population):
            new_user = User()
            self.users.append(new_user)
#output: users = [User0, User1, User2, ..., User(population - 1)]

    def circle_connect(self):
        """connect each user i to user i+1, and connect the last user to user 0"""
        for i in range(0, self.population - 1):
            self.users[i].add_friend(self.users[i + 1])
        self.users[self.population - 1].add_friend(self.users[0])

#output: user0.friends = [user(population-1), user1],
#        user1.friends = [user0, user2],
#        user2.friends = [user1, user3],
#        ...user(population-1).friends = [user(population-2), user0]

    def random_connections(self, num_connections):
        """add num_connections(an assigned integer) new connections randomly to the graph"""
        add_connection = 0
        while add_connection < num_connections:
            user1 = random.choice(self.users)
            user2 = random.choice(self.users)
            if user1 is not user2:
                if user1.is_friend(user2):
                    continue
                user1.add_friend(user2)
                add_connection += 1

    def time_step(self, prob):
        """move the simulation forward by one time period. For every user that has the new technology, the probability of passing it on to each friend is prob"""
        pass

    def get_users(self):
        """returns a list containing the users in the graph, in order of their IDs"""
        return self.users


class User(object):

    def __init__(self):
        if not hasattr(self, 'next_id'):
            User.next_id = 0
        self.id = User.next_id
        User.next_id += 1
        self.is_adopted = False
        self.friends = []

    def __lt__(self, other):
        """this is a built in comparison function, so that User1 < User2 always return False. This is handy for sorting lists that contain users without throwing errors"""
        return self.id < other.id

    def get_friends(self):
        """return a list of the user's friends, which are also users"""
        return self.friends

    def is_friend(self, other):
        """return True if this User and other are friends. return False otherwise"""
        if other in self.friends:
            return True
        else:
            return False

    def add_friend(self, other):
        if self == other:
            return
        if other not in self.friends:
            self.friends.append(other)
            other.friends.append(self)

    def get_id(self):
        """return this user's id"""
        return self.id

    def has_adopted(self):
        """Returns True if the user has adopted the new technology. Returns False otherwise"""
        return self.is_adopted

    def set_adopted(self, new_status):
        """If new_status is True, this user adopts the new technology. If new_status is False, this user becomes a non-adopter."""
        self.is_adopted = new_status


class GraphAnalyzer(object):
    def __init__(self, graph):
        self.graph = graph

    def choose_users(self, n):
        """returns a list of n users to serve as first-adopters, chosen so that the technology saturates the graph as quickly as possible"""







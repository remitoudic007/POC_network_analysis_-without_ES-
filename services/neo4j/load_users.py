from dotenv import dotenv_values

from py2neo import Node, Relationship
from py2neo import Graph
from py2neo.bulk import create_nodes, create_relationships

import platform_users
users = platform_users.users
links = platform_users.links
links_bulk = platform_users.links_bulk


config = dotenv_values("../../.env")


class LoadUser:

    def __init__(self,  config_db):

        self.graph_data_storage = Graph(host=config_db["NEO_DB_HOST"],
                                        password=config_db["NEO_DB_PASS"],
                                        name=config_db["NEO_DB_NAME"])
        self.transactions = self.graph_data_storage.begin()
        self.graph_objects = ""

    def load_graph_data(self, user_data: dict, links_data: dict):
        """
        load data  in to  Node and  Relationship(links) objects
        """
        graph_obj = dict()
        for user in users:
            graph_obj[user["name"]] = Node("User",
                                           name=user["name"],
                                           email=user["email"],
                                           facebook=user["fb"],
                                           phone=user["phone"])
        for link in links:
            for link in links:
                link_obj = Relationship(graph_obj[link["src"]],
                                        link["link"],
                                        graph_obj[link["target"]])
                graph_obj[link["src"]+"-"+link["target"]] = link_obj

        self.graph_objects = graph_obj

    def write_graph_to_db(self):
        # users_graph construction
        for key in self.graph_objects.keys():
            self.transactions.create(self.graph_objects[key])

        self.graph_data_storage.commit(self.transactions)
        print("commit")

    def loadCreateBulkUser(self, user, label_string):
        # create users in  bulk
        create_nodes(self.graph_data_storage.auto(),
                     user,
                     labels={label_string})

    def creatRelationshipsBulk(self, data,):
        create_relationships(self.graph_data_storage.auto(),
                             data,
                             "ACTORS")
        print("created links ")


Network = LoadUser(config)


# Example of user :

# Option 1
# Network.load_graph_data(users,links)
# Network.write_graph_to_db()

# Option 2
# Network.loadCreateBulkUser(users, "platformUser")
# Network.creatRelationshipsBulk(links_bulk)

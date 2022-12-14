from py2neo import Node, Relationship
from py2neo import Graph

import platform_users
users = platform_users.users
links = platform_users.links


users_graph = Graph(password='neo4j')
# transactions
tx = users_graph.begin()


# users_graph design
nodes_box=dict()
for user in users:
    nodes_box[user["name"]] = Node("User",
                    name = user["name"],
                    email = user["email"],
                    facebook = user["fb"],
                    phone = user["phone"])

for link in  links:
     nodes_box[link["src"]+"-"+link["target"]] = Relationship( nodes_box[link["src"]],
                               link["link"],
                               nodes_box[link["target"]])


# users_graph construction
for key in nodes_box.keys():
    tx.create(nodes_box[key])

users_graph.commit(tx)

print('done')
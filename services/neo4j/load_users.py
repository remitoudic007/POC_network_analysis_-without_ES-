from py2neo import Node, Relationship
from py2neo import Graph

import platform_users
users = platform_users.users
links = platform_users.links



graph = Graph(password='neo4j')
# transactions
tx = graph.begin()

for user in users:
    new_node = Node("User",
                    name = user["name"],
                    email = user["email"],
                    facebook = user["fb"],
                    phone = user["phone"])


    tx.create(new_node)


# for link in  links:
#     new_relation=Relationship( source= link["src"],
#                                linked_by=link["target"],
#                                target=link["target"])



graph.commit(tx)

print('done')
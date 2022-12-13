from neo4j import GraphDatabase
import nxneo4j as nx

uri = "http://localhost:7474/browser/"  # in Neo4j Desktop
# custom URL for Sandbox or Aura
user = "neo4j"
# your user name
# default is always "neo4j"
# unless you have changed it.
password = "remitoudic"
driver = GraphDatabase.driver(uri="bolt://localhost", auth=(user, password))

G = nx.Graph(driver)

list_nodes = ["Actor1 ",
              "Actor2", ]

# G.add_nodes_from(list_nodes)
G.add_node("Betul", age=4, gender='F')

# list_edges = [
#     {"source": "Actor1",
#      "target": "Actor2"}, ]

# for dep in list_edges:
#     G.add_edge(dep["source"], dep["target"])

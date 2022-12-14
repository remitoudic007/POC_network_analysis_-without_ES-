# find all the actors

from py2neo import Graph
import json


graph_neo = Graph(password='neo4j')

def find_commom_attribues(graph)-> dict:

    common = dict()
    T= graph.run( " MATCH (n) RETURN n")
    T=T.data()

    E=[ elt["n"]["email"] for elt in T]
    P=[ elt["n"]["phone"] for elt in T]
    F=[ elt["n"]["facebook"] for elt in T]

    common["phone"] = dict((x,P.count(x)) for x in set(P) if P.count(x)>1)
    common["email"] = dict((x,E.count(x)) for x in set(E)if E.count(x)>1)
    common["facebook"] = dict((x,F.count(x)) for x in set(F)if F.count(x)>1)

    return  common


COMMON_attr=find_commom_attribues( graph_neo)

def find_actor(dict_common):
    """
    find user with common  attributes
    """
    actors= dict()
    counter_actor=0
    for email in  dict_common["email"]:

        via_email = graph_neo.nodes.match(email=email)
        actors["email"]=via_email.all()

    for phone in  dict_common["phone"]:
        via_phone= graph_neo.nodes.match(phone=phone)
        actors["phone"]=via_phone.all()

    for fb in  dict_common["facebook"]:
        via_facebook = graph_neo.nodes.match(facebook=fb)
        actors["facebook"]=via_facebook.all()

    print (json.dumps(actors, indent=1))

    return actors


test=find_actor(COMMON_attr)



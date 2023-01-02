# find all the actors

from py2neo import Graph
import json
import random

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

    number_of_actors=len(common["phone"])+ len(common["email"])+ len(common["facebook"])

    res = {  "common_attributes" : common,
             "number_of_actors" : number_of_actors}

    return res


COMMON_attr=find_commom_attribues( graph_neo)



def find_nodes_actors(dict_common):
    """
    find user with common  attributes
    """

    actors= { "names":[],
              "actors_details":[]}
    counter_actor=0


    for email in  dict_common["email"]:
        via_email = graph_neo.nodes.match(email=email)
        name= "actor"+str(random.randint(10,100))
        actors["names"].append(name)
        actors["actors_details"]. append({"name":name,
                                          "linked_by":"email",
                                          "users_member": via_email.all()})


    for phone in  dict_common["phone"]:
        via_phone= graph_neo.nodes.match(phone=phone)
        name= "actor"+str(random.randint(10,100))
        actors["names"].append(name)
        actors["actors_details"]. append({"name":name,
                                          "linked_by":"email",
                                          "users_member": via_phone.all()})

    for fb in  dict_common["facebook"]:
        via_facebook = graph_neo.nodes.match(facebook=fb)
        name= "actor"+str(random.randint(10,100))
        actors["names"].append(name)
        actors["actors_details"]. append({ "name":name,
                                          "linked_by":"email",
                                          "users_member": via_facebook.all()})

    return actors



# " main "

Actors= find_nodes_actors(COMMON_attr["common_attributes"])
n_actors= COMMON_attr["number_of_actors"]

print ( '\n',"Actors numbers :",n_actors,)
print (" details: ", json.dumps(Actors, indent=1))





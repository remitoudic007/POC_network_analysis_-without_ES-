from neo4j import GraphDatabase


class NetworkNeo:
    """
    Here only neo4j official library in purpose
    """

    def __init__(self, uri, DB_name, pwd, graph):
        self.driver = GraphDatabase.driver(uri,
                                           auth=(DB_name, pwd))
        self.graph = graph

    def close(self):
        self.driver.close()

    def write_to_DB(self, ):
        with self.driver.session() as session:
            session.execute_write(self.create_and_return)
            print("done")

    def create_and_return(self, tx):
        result = tx.run(self.graph)
        return result

    def find_direct_connection():
        ...

    def find_actors():
        ...

    def find_clusters():
        ...


if __name__ == "__main__":

    config = dict()


    config["graph"] = """
        CREATE (user1:User {name:"User1", email:'abc@gmail.com',fb:'F1', phone:453576})
        CREATE (user2:User {name:"User2", email:'abc@gmail.com',fb:'F2', phone:342156})
        CREATE (user3:User {name:"User3", email:'abc@gmail.com',fb:'F3', phone:123456})
        CREATE (user4:User {name:"User4", email:'efd@gmail.com',fb:'F3', phone:966642})
        CREATE (user99:User {name:"User99", email: 'xsz@gmail.com',fb:'F4', phone:123456})

        CREATE (user1)-[:EMAIL]->(user2)
        CREATE (user2)-[:EMAIL]->(user3)
        CREATE (user3)-[:EMAIL]->(user1)
        CREATE (user3)-[:FaceBook]->(user4)
        CREATE (user99)-[:phone]->(user3)

        CREATE (user1)-[:Actors { name:"actor1" , area:['ebay'], highrisk: 5}]->(user2)
        CREATE (user2)-[:Actors { name:"actor1" , area:['ebay'], highrisk: 3}]->(user3)
        CREATE (user3)-[:Actors { name:"actor2" , area:['ebay'], highrisk: 3}]->(user4)
        CREATE (user99)-[:Actors { name:"actor3" , area:['ebay'], highrisk: 3}]->(user3)
        """
    config["uri"] = "neo4j://localhost:7687"
    config["name"] = "neo4j"
    config["pwd"] = "neo4j"
    Network = NetworkNeo(config["uri"],
                         config["name"],
                         config["pwd"],
                         config["graph"])

    Network.write_to_DB()
    Network.close()

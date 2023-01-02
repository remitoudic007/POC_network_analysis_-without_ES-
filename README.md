# POC:  network analysis without ES

Code related to Jira'S ticket /BP-18177

## How to start the project ?

- Install docker compose
- run docker compose up --build  at the root level
- to reset neo4j docker-compose down --volumes

## Getting stated
    Backend :  http://0.0.0.0:8000/docs
    neo4j UI : http://0.0.0.0:7474/browser    (default user - pwd)
    frontend : http://0.0.0.0:8080

## About the  "User/Actor/Network study case".

Definitions:

    - Platform user: Always connected to a single item, this can be any item we
      have across the channels, listings, post,website.

    - Actor: these are grouped platform users, they have a direct connection(s) 
       to each other.

    - Network: Multiple actors who have a traversed connection to members of the actor

Tristan  PDF  for the study case
[PDF](https://drive.google.com/file/d/1YyBkmV_cKvXzEnV_IwWBNk8QItkS-lQ-/view?usp=sharing)


## Neo4j cheatsheet
    Delete all :                 MATCH (n) DETACH DELETE n
    Select all :                 MATCH (n) RETURN n
    Select all actors :      MATCH (n)-[r:Actors]->() RETURN n.name

## Some reading :
https://singerlinks.com/2020/10 should-i-use-py2neo-or-the-native-python-driver-to-access-neo4j/

https://github.com/neo4j-examples/movies-python-bolt

https://github.com/elena/py2neo-quickstart



MATCH (a:User), (b:User)
WHERE a.name = "User1"  AND  b.name = "User99"
CREATE (a)-[:Actors {area: ['ebay'], highrisk: 5}]->(b)
RETURN a,b


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




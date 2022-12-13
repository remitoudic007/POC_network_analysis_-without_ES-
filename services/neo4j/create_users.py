from neo4j import GraphDatabase
import platform_users

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "remitoudic"))
users = platform_users.users
relations = platform_users.relations


def create_user(tx, name, email, fb, phone):
    tx.run("CREATE (U:User {name: $name, email:$email, fb:$fb, phone:$phone})",
           name=name,
           email=email,
           fb=fb,
           phone=phone
           )


with driver.session() as session:

    for user in users:
        session.execute_write(create_user,
                              user["name"],
                              user["email"],
                              user["fb"],
                              user["phone"]
                              )

driver.close()
print("ok")

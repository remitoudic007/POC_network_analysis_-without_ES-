from dotenv import dotenv_values
from load_users import  LoadUser
import names
import random
config = dotenv_values("../../.env")
Network = LoadUser(config)


def  gen_email():
    email = ''
    for _ in range(7):
        letter = random.sample(letters,1)[0]
        email += letter
    email += '@gmail.com'
    return email

# create 10000 data users
data=[]
for i in range(10000):
        fake_user = {  
        "name": names.get_full_name(),
        "email": gen_email(),
        "fb": "F1",
        "phone": random.randrange(1000000, 9999999)},

Network.loadCreateBulkUser(users, "platformUser")

Network.creatRelationshipsBulk(links_bulk)
print("OK")




